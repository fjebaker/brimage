#ifndef SUBCANVAS_HPP
#define SUBCANVAS_HPP

#include "canvas.hpp"
#include "../configs.hpp"


class SubCanvas : public Canvas {
private:
  PX_TYPE region[SQ_WIDTH * SQ_WIDTH];

public:

  SubCanvas() noexcept ;
  virtual ~SubCanvas() noexcept override = default ;

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
