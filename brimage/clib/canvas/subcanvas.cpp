#include "subcanvas.hpp"
/*
template <>
void subregion<Grey>(SubCanvas& subcanv, const Canvas &supercanv, int x0, int
x1, int y0, int y1) noexcept {
  // copy in row by row
  for (int y = y0; y < y1; y++) {
    memcpy(subcanv.layer + (y - y0) * subcanv.width,
           supercanv.layer + (y * supercanv.width) + x0,
           sizeof(PX_TYPE) * (x1 - x0));
  }
}

*/
