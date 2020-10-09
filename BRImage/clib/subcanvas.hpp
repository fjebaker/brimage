#ifndef SUBCANVAS_HPP
#define SUBCANVAS_HPP

#include "canvas.hpp"


class SubCanvas : public Canvas {

public:

  SubCanvas() = delete ;
  virtual ~SubCanvas() noexcept override ;

  SubCanvas(int width, int height) noexcept ;
  void subregion(const Canvas& supercanv, int x0, int x1, int y0, int y1) noexcept ;

};

inline void SubCanvas::subregion(const Canvas& supercanv, int x0, int x1, int y0, int y1) noexcept {
  for (int y = y0; y < y1; y++) {
    for (int x = x0; x < x1; x++) {
      index(x - x0, y - y0) = supercanv.get_px(x, y);
    }
  }
}

#endif
