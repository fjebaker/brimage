#ifndef SHAPES_HPP
#define SHAPES_HPP

#include "../canvas/canvas.hpp"
#include "coord.hpp"

#include <cmath>

class Shape {

public:
  Shape() noexcept;
  virtual ~Shape() = default;

  Shape(const Shape &s) = default;
  // delete move constructor
  Shape(Shape &&) = delete;

  // pure virtual function
  virtual void trace(Canvas<Grey> &) const noexcept = 0;
};

class Line : public Shape {

public:
  Coord p1;
  Coord p2;

  Line() = default;
  ~Line() noexcept override;

  Line(double x1, double y1, double x2, double y2) noexcept;
  Line(const Coord &p1, const Coord &p2) noexcept;

  Line &operator=(const Line &line) noexcept;

  Line &operator=(Line &&) = delete;

  void trace(Canvas<Grey> &canvas) const noexcept;

  template <class C>
  void trace(Canvas<C> &canvas, const C &shade) const noexcept;
};

inline void Line::trace(Canvas<Grey> &canvas) const noexcept {
  trace<Grey>(canvas, 0);
}

template <class C>
inline void Line::trace(Canvas<C> &canvas, const C &colour) const noexcept {
  // Bresenham's Line Algorithm
  int x0 = (int)p1.x;
  int x1 = (int)p2.x;
  int y0 = (int)p1.y;
  int y1 = (int)p2.y;
  int dx = abs(x1 - x0);
  int dy = -1 * abs(y1 - y0);
  int sx = x0 < x1 ? 1 : -1;
  int sy = y0 < y1 ? 1 : -1;
  int err = dx + dy;

  while (x0 != x1 && y0 != y1) {
    canvas.stroke(x0, y0, colour);
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

#endif
