#ifndef PIXELS_HPP
#define PIXELS_HPP

#include <cmath>
typedef unsigned char PX_TYPE;

struct Colour {
  constexpr Colour() noexcept
  : r{0}, g{0}, b{0}, a{0} {
  }

  constexpr Colour(PX_TYPE grey) noexcept
  : Colour{} {
    a = grey;
  }

  constexpr Colour(const Colour&) = default ;
  constexpr Colour(Colour&&) = default ;

  ~Colour() noexcept = default ;

  inline double diff(const Colour& c) noexcept {
    return (double)
        abs(this->r - c.r)
      + abs(this->g - c.g)
      + abs(this->b - c.b)
      + abs(this->a - c.a) ;
  }

  PX_TYPE r, g, b, a;
};

struct Grey : public Colour {
};
struct RGB : public Colour {
};

#endif
