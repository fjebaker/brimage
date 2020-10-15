%module(package="BRImage.clib") algorithms

%{
    #define SWIG_FILE_WITH_INIT
    #include "freqmod.hpp"
    #include "canvas/canvas.hpp"
    #include "randomwalk.hpp"
    #include "canvas/pixels.hpp"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* input_arr, int input_dim)}
%apply (double* ARGOUT_ARRAY1, int DIM1) {(double* output_arr, int output_dim)}
%apply (unsigned char* INPLACE_ARRAY2, int DIM1, int DIM2) {(PX_TYPE* inplace_arr2, int dim1, int dim2)};
%apply (unsigned char* INPLACE_ARRAY3, int DIM1, int DIM2, int DIM3) {(PX_TYPE* inplace_arr3, int dim1, int dim2, int dim3)};

%exception GreyCanvas {
  try {
    $action
  } catch (std::runtime_error &e) {
    PyErr_SetString(PyExc_RuntimeError, const_cast<char*>(e.what()));
    SWIG_fail;
  }
}

%include "freqmod.hpp"
%include "randomwalk.hpp"


class Canvas {
public:
  Canvas() = default;
  virtual ~Canvas() = default;
  Canvas(PX_TYPE* inplace_arr2, int dim1, int dim2) ;
};

%pythoncode %{
def freqmod(arr, omega, max_phase):
    return freqmod_row(arr, len(arr), omega, max_phase)
%}
