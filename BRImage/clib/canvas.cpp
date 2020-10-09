#include "canvas.hpp"

void Canvas::set_inplace_layer(PX_TYPE* inplace_arr, int dim1, int dim2) noexcept {
  layer = inplace_arr;
  height = dim1;
  width = dim2;
}

void Canvas::subregion(Canvas& subreg, int x0, int x1, int y0, int y1) const noexcept {
  for (int y = y0; y < y1; y++) {
    for (int x = x0; x < x1; x++) {
      subreg.index(x - x0, y - y0) = get_px(x, y);
    }
  }
}

void Canvas::stroke(int x, int y, PX_TYPE val) noexcept {
  /* bound safe stroke function */
  if (in_bounds(x, y)) {
    index(x, y) = val;
  }
}

PX_TYPE Canvas::get_px(int x, int y) const noexcept {
  return layer[y * width + x];
}

int Canvas::get_width() const noexcept {
  return width;
}
int Canvas::get_height() const noexcept {
  return height;
}

bool Canvas::in_bounds(int x, int y) const noexcept {
  if (x < 0 || x >= width || y < 0 || y>= height) {
    return false;
  } else {
    return true;
  }
}

PX_TYPE& Canvas::index(int x, int y) noexcept {
    return layer[y * width + x];
}
