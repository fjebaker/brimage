#include "canvas.hpp"

template<>
void Canvas::update(int x, int y, const RGB &c) noexcept {
  const int CARRY = width * height;
  layer[y * width + x] = c.r;
  layer[y * width + x + CARRY] = c.g;
  layer[y * width + x + CARRY + CARRY] = c.b;
}

template<>
RGB Canvas::get_px(int x, int y) const noexcept {
  const int CARRY = width * height;
  return RGB(
    layer[y * width + x],
    layer[y * width + x + CARRY],
    layer[y * width + x + CARRY + CARRY]
  );
}
