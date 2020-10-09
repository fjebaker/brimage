#include "shapes.hpp"

#include <cmath>

Line::Line() noexcept
  : p1{0, 0}, p2{1, 1} {
  /* default constructor */
}
Line::Line(double x1, double y1, double x2, double y2) noexcept
  : p1{x1, y1}, p2{x2, y2} {
  /* double constructor */
}
Line::Line(const Coord& p1, const Coord& p2) noexcept
  : p1{p1}, p2{p2} {
  /* Coord constructor */
}

Line& Line::operator=(const Line& line) noexcept {
  p1 = line.p1;
  p2 = line.p2;
  return *this;
}

void Line::trace(Canvas& canvas) const noexcept {
  trace(canvas, 0);
}
void Line::trace(Canvas& canvas, unsigned char shade) const noexcept {
  // Bresenham's Line Algorithm
  int x0 = (int) p1.x;
  int x1 = (int) p2.x;
  int y0 = (int) p1.y;
  int y1 = (int) p2.y;
  int dx = abs(x1 - x0);
  int dy = -1 * abs(y1 - y0);
  int sx = x0 < x1 ? 1 : -1;
  int sy = y0 < y1 ? 1 : -1;
  int err = dx + dy;

  while( x0 != x1 && y0 != y1) {
    canvas.stroke(x0, y0, shade);
    int e2 = 2 * err;
    if (e2 >= dy) {
      err += dy;
      x0 += sx;
    }
    if (e2 <= dx) {
      err += dx;
      y0 += sy;
    }
  }
}
