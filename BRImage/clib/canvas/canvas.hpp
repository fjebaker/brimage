#ifndef CANVAS_HPP
#define CANVAS_HPP

#include "pixels.hpp"

template <class C> class Canvas {

protected:
  int width = 0;
  int height = 0;

  PX_TYPE *layer;

  constexpr void update(int x, int y, const C &c) noexcept {
    layer[y * width + x] = c.val;
  }

public:
  Canvas() = default;
  virtual ~Canvas() = default;

  constexpr void set_inplace_layer(PX_TYPE *inplace_arr, int dim1,
                                   int dim2) noexcept {
    layer = inplace_arr;
    height = dim1;
    width = dim2;
  }

  constexpr void stroke(int x, int y, const C &c) noexcept {
    /* bound safe stroke function */
    if (in_bounds(x, y)) {
      update(x, y, c);
    }
  }

  [[nodiscard]] constexpr C get_px(int x, int y) const noexcept {
    return C(layer[y * width + x]);
  }

  constexpr bool in_bounds(int x, int y) const noexcept {
    if (x < 0 || x >= width || y < 0 || y >= height) {
      return false;
    } else {
      return true;
    }
  }

  [[nodiscard]] constexpr int get_width() const noexcept { return width; }
  [[nodiscard]] constexpr int get_height() const noexcept { return height; }
};

#endif
