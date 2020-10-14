#include "canvas.hpp"

void Canvas::set_inplace_layer(PX_TYPE *inplace_arr, int dim1,
                               int dim2) noexcept {
  layer = inplace_arr;
  height = dim1;
  width = dim2;
}
