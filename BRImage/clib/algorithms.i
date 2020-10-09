%module(package="BRImage.clib") algorithms

%{
    #define SWIG_FILE_WITH_INIT
    #include "freqmod.hpp"
    #include "canvas.hpp"
    #include "randomwalk.hpp"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* input_arr, int input_dim)}
%apply (double* ARGOUT_ARRAY1, int DIM1) {(double* output_arr, int output_dim)}
%apply (unsigned char* INPLACE_ARRAY2, int DIM1, int DIM2) {(PX_TYPE* inplace_arr, int dim1, int dim2)};

%include "freqmod.hpp"
%include "randomwalk.hpp"

class Canvas {
public:
  Canvas() = default;
  virtual ~Canvas() = default;
  void set_inplace_layer(PX_TYPE* inplace_arr, int dim1, int dim2) noexcept ;
};

%pythoncode %{
def freqmod(arr, omega, max_phase):
    return freqmod_row(arr, len(arr), omega, max_phase)
%}
