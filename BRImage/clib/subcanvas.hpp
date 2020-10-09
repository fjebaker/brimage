#ifndef SUBCANVAS_HPP
#define SUBCANVAS_HPP

#include "canvas.hpp"


class SubCanvas : public Canvas {

public:

  SubCanvas() = delete ;
  virtual ~SubCanvas() noexcept override ;

  SubCanvas(int width, int height) noexcept ;

};

#endif
