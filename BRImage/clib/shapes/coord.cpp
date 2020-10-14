#include "coord.hpp"

Coord::Coord() noexcept : x{0}, y{0} { /* default constructor */
}
Coord::Coord(double x, double y) noexcept : x{x}, y{y} {
  /* double constructor */
}
Coord::Coord(const Coord &c) noexcept : x{c.x}, y{c.y} {
  /* copy constructor */
}

Coord Coord::operator-(const Coord &c) const noexcept {
  Coord temp{*this};
  temp.x -= c.x;
  temp.y -= c.y;
  return temp;
}
Coord Coord::operator+(const Coord &c) const noexcept {
  Coord temp{*this};
  temp.x += c.x;
  temp.y += c.y;
  return temp;
}
Coord &Coord::operator=(const Coord &c) noexcept {
  x = c.x;
  y = c.y;
  return *this;
}
