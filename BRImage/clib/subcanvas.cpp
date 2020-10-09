#include "subcanvas.hpp"

#include <stdlib.h>

SubCanvas::SubCanvas(int width, int height) noexcept {
  this->width = width;
  this->height = height;
  layer = (PX_TYPE*) malloc(width * height * sizeof(PX_TYPE));
}

SubCanvas::~SubCanvas() noexcept {
  free(layer);
}
