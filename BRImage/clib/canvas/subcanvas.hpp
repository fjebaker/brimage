#ifndef SUBCANVAS_HPP
#define SUBCANVAS_HPP

#include "../configs.hpp"
#include "canvas.hpp"

template <class C> class SubCanvas : public Canvas<C> {
private:
  PX_TYPE region[SQ_WIDTH * SQ_WIDTH];

public:
  SubCanvas() noexcept {
    this->width = SQ_WIDTH;
    this->height = SQ_WIDTH;
    this->layer = region;
  }
  virtual ~SubCanvas() noexcept override = default;

  constexpr void subregion(const Canvas<C> &supercanv, int x0, int x1, int y0,
                           int y1) noexcept {
    for (int y = y0; y < y1; y++) {
      for (int x = x0; x < x1; x++) {
        this->update(x - x0, y - y0, supercanv.get_px(x, y));
      }
    }
  }
};

#endif
