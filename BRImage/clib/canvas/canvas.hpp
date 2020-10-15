#ifndef CANVAS_HPP
#define CANVAS_HPP

#include "pixels.hpp"
#include <stdexcept>

class Canvas {
protected:
  int width, height;
  PX_TYPE *layer;

  template <class C> void update(int x, int y, const C &c) noexcept {
    layer[y * width + x] = c.a;
  }
  template <> void update(int x, int y, const RGB &c) noexcept {
    int index = 3 * (x + width * y);
    layer[index] = c.r;
    layer[index + 1] = c.g;
    layer[index + 2] = c.b;
  }

public:
  constexpr Canvas() : width{0}, height{0}, layer{} {}
  virtual ~Canvas() = default;

  template <class C> constexpr void stroke(int x, int y, const C &c) noexcept;

  [[nodiscard]] constexpr bool in_bounds(int x, int y) const noexcept;

  [[nodiscard]] constexpr int get_width() const noexcept { return width; }
  [[nodiscard]] constexpr int get_height() const noexcept { return height; }

  template <class C>[[nodiscard]] C get_px(int x, int y) const noexcept {
    return C(layer[y * width + x]);
  }
  template <> RGB get_px(int x, int y) const noexcept {
    int index = 3 * (x + width * y);
    return RGB(layer[index], layer[index + 1], layer[index + 2]);
  }
};

class MonochomeCanvas : public Canvas {
public:
  MonochomeCanvas() = default;
  ~MonochomeCanvas() = default;
  constexpr MonochomeCanvas(PX_TYPE *inplace_arr, int dim1, int dim2)
      : Canvas{} {
    width = dim1;
    height = dim2;
    layer = inplace_arr;
  }
};

class RGBCanvas : public Canvas {
public:
  RGBCanvas() = default;
  ~RGBCanvas() = default;
  constexpr RGBCanvas(PX_TYPE *inplace_img, int dim1, int dim2, int dim3)
      : Canvas{} {
    if (dim3 != 3) {
      throw std::runtime_error(
          "RGB Canvas requires array with shape (y, x, 3).");
    }
    width = dim1;
    height = dim2;
    layer = inplace_img;
  }
};

// ---------------- template declerations ---------------- //

// ---------------- constexpr definitions ---------------- //

template <class C>
constexpr void Canvas::stroke(int x, int y, const C &c) noexcept {
  /* bound safe stroke function */
  if (in_bounds(x, y)) {
    update<C>(x, y, c);
  }
}

constexpr bool Canvas::in_bounds(int x, int y) const noexcept {
  /* branchless version of
      if (x < 0 || x >= width || y < 0 || y >= height) {
        return false;
      } else {
        return true;
      }
  */
  return (bool)(1 - (x < 0) * (x >= width) * (y < 0) * (y >= height));
}

#endif
