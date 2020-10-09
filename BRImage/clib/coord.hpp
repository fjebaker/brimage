#ifndef COORD_HPP
#define COORD_HPP

class Coord {

public:

  double x ;
  double y ;

  Coord() noexcept ;
  virtual ~Coord() = default ;

  Coord(double x, double y) noexcept ;
  Coord(const Coord& c) noexcept ;

  Coord operator-(const Coord& c) const noexcept ;
  Coord operator+(const Coord& c) const noexcept ;
  Coord& operator=(const Coord& c) noexcept ;

  Coord& operator=(Coord&&) = delete;

};

#endif
