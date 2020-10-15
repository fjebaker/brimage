#ifndef SUBCANVAS_HPP
#define SUBCANVAS_HPP

#include "../configs.hpp"
#include "canvas.hpp"

#include <iostream>

class SubCanvas : public Canvas {
private:
  PX_TYPE region[SQ_WIDTH * SQ_WIDTH * 3]; // factor 3 required for RGB

public:
  SubCanvas() noexcept {
    width = SQ_WIDTH;
    height = SQ_WIDTH;
    layer = region;
  }
  SubCanvas(const SubCanvas &) = delete;
  SubCanvas(SubCanvas &&) = delete;

  virtual ~SubCanvas() noexcept override = default;

  template <class C>
  friend constexpr void subregion(SubCanvas &subcanv, const Canvas &supercanv,
                                  int x0, int x1, int y0, int y1) noexcept;
};

template <class C>
constexpr void subregion(SubCanvas &subcanv, const Canvas &supercanv, int x0,
                         int x1, int y0, int y1) noexcept {
  for (int y = y0; y < y1; y++) {
    for (int x = x0; x < x1; x++) {
      subcanv.update<C>(x - x0, y - y0, supercanv.get_px<C>(x, y));
    }
  }
}

/*
template <>
constexpr void subregion<Grey>(SubCanvas& subcanv, const Canvas &supercanv, int
x0, int x1, int y0, int y1) noexcept {
    // copy in row by row
    for (int y = y0; y < y1; y++) {
      memcpy(subcanv.layer + (y - y0) * subcanv.width,
             supercanv.layer + (y * supercanv.width) + x0,
             sizeof(PX_TYPE) * (x1 - x0));
    }
  }
*/

#endif
