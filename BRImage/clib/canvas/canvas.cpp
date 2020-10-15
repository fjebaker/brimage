#include "canvas.hpp"
#include <iostream>
/*
template<>
void Canvas::update(int x, int y, const RGB &c) noexcept {
  std::cout << ".";
  int index = 3 * ( x + width * y) ;
  layer[index] = c.r;
  layer[index + 1] = c.g;
  layer[index + 2] = c.b;
}

template<>
RGB Canvas::get_px(int x, int y) const noexcept {
  int index = 3 * ( x + width * y) ;
  return RGB(
    layer[index],
    layer[index + 1],
    layer[index + 2]
  );
}


AIMING FOR 4320000

template<> void update(int x, int y, const RGB &c) noexcept {
  int index = 3 * ( x + width * y) ;
  layer[index] = c.r;
  layer[index + 1] = c.g;
  layer[index + 2] = c.b;
}


template<> RGB get_px(int x, int y) const noexcept {
  int index = 3 * ( x + width * y) ;
  return RGB(
    layer[index],
    layer[index + 1],
    layer[index + 2]
  );
}
*/
