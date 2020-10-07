%module(package="BRImage.clib") algorithms

%{
    #define SWIG_FILE_WITH_INIT
    #include "freqmod.hpp"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* input_arr, int input_dim)}
%apply (double* ARGOUT_ARRAY1, int DIM1) {(double* output_arr, int output_dim)}

%include "freqmod.hpp"

%pythoncode %{
def freqmod(arr, omega, max_phase):
    return freqmod_row(arr, len(arr), omega, max_phase)
%}
