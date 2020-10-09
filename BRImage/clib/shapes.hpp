#ifndef SHAPES_HPP
#define SHAPES_HPP

#include "coord.hpp"
#include "canvas.hpp"

class Shape {

public:

  Shape() = default ;
  virtual ~Shape() = default ;

  Shape(const Shape& s) = default ;
  // delete move constructor
  Shape(Shape&&) = delete;

  // pure virtual function
  virtual void trace(Canvas&) const noexcept = 0;

};

class Line : public Shape {

public:

  Coord p1;
  Coord p2;

  Line() noexcept ;
  ~Line() override = default ;

  Line(double x1, double y1, double x2, double y2) noexcept ;
  Line(const Coord& p1, const Coord& p2) noexcept ;

  Line& operator=(const Line& line) noexcept ;

  Line& operator=(Line&&) = delete ;

  void trace(Canvas& canvas) const noexcept override ;
  void trace(Canvas& canvas, unsigned char shade) const noexcept ;

};

#endif
