#include "freqmod.hpp"

#include <cmath>

double remap(double x, double s1, double s2, double d1, double d2) {
  /* remaps x in range s1 to s2, into d1 to d2 */
  return (((x - s1) * (d2 - d1)) / (s2 - s1)) + d1;
}

void freqmod_row(double *input_arr, int input_dim, double *output_arr,
                 int output_dim, double omega, double max_phase) {

  double integral = 0, runningmod = 0, min_phase = -max_phase, x = 0, val;

  for (int i = 0; i < input_dim; i++) {
    x = input_arr[i];
    x = remap(x, 0, 255, min_phase, max_phase);
    integral += x;

    x = cos(((omega * i) + integral) * 0.5);

    val = fabs(x - runningmod);
    runningmod = x;

    val = remap(2 * (val - omega), min_phase, max_phase, 0, 255);
    output_arr[i] = val;
  }
}
