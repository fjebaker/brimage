%module(package="brimage.clib") algorithms

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
%apply (unsigned char* INPLACE_ARRAY2, int DIM1, int DIM2) {(PX_TYPE* inplace_arr, int dim1, int dim2)};
%apply (unsigned char* INPLACE_ARRAY3, int DIM1, int DIM2, int DIM3) {(PX_TYPE* inplace_img, int dim1, int dim2, int dim3)};

%exception RGBCanvas {
  try {
    $action
  } catch (std::runtime_error &e) {
    PyErr_SetString(PyExc_RuntimeError, const_cast<char*>(e.what()));
    SWIG_fail;
  }
}

%include "freqmod.hpp"
%include "randomwalk.hpp"

%inline %{
#include <iostream>
void test(PX_TYPE* inplace_img, int dim1, int dim2, int dim3) {
  for(int y = 0; y < dim1; y++) {
    for (int x = 0; x < dim2; x++) {
      for (int z = 0; z < dim3; z++) {
        int index = 3 * (x + y * dim2) + z;
        std::cout << (int) inplace_img[index] << " ";
      }
    }
  }
  std::cout << std::endl;
}

%}

class RGBCanvas {
public:
  RGBCanvas() = default;
  ~RGBCanvas() = default;
  RGBCanvas(PX_TYPE* inplace_img, int dim1, int dim2, int dim3) ;
};

class MonochomeCanvas {
public:
  MonochomeCanvas() = default;
  ~MonochomeCanvas() = default;
  MonochomeCanvas(PX_TYPE* inplace_arr, int dim1, int dim2) ;
};

%template(random_walk_monochrome) random_walk_template<MonochomeCanvas>;
%template(random_walk_rgb) random_walk_template<RGBCanvas>;

%pythoncode %{
def freqmod(arr, omega, max_phase):
    return freqmod_row(arr, len(arr), omega, max_phase)
%}
