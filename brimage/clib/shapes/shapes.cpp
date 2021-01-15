#include "shapes.hpp"

Shape::Shape() noexcept {}

Line::~Line() noexcept {}

Line::Line(double x1, double y1, double x2, double y2) noexcept
    : p1{x1, y1}, p2{x2, y2} {
  /* double constructor */
}

Line &Line::operator=(const Line &line) noexcept {
  p1 = line.p1;
  p2 = line.p2;
  return *this;
}
