#ifndef CANVAS_HPP
#define CANVAS_HPP

#include "pixels.hpp"

class Canvas {
protected:
  int width, height;
  PX_TYPE* layer;

  template<class C>
  constexpr void update(int x, int y, const C &c) noexcept {
    layer[y * width + x] = c.a;
  }

public:
  constexpr Canvas() : width{0}, height{0}, layer{} {}
  constexpr Canvas(PX_TYPE *inplace_arr, int dim1, int dim2) : width{dim1}, height{dim2}, layer{inplace_arr} {}
  virtual ~Canvas() = default;

  constexpr void stroke(int x, int y, const Colour& c) noexcept ;

  [[nodiscard]] constexpr bool in_bounds(int x, int y) const noexcept ;

  [[nodiscard]] constexpr int get_width() const noexcept { return width; }
  [[nodiscard]] constexpr int get_height() const noexcept { return height; }


  template<class C>
  [[nodiscard]] constexpr C get_px(int x, int y) const noexcept {
    return C(layer[y * width + x]);
  }

};

// ---------------- template declerations ---------------- //

// ---------------- constexpr definitions ---------------- //

constexpr void Canvas::stroke(int x, int y, const Colour& c) noexcept {
  /* bound safe stroke function */
  if (in_bounds(x, y)) {
    update<Colour>(x, y, c);
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
  return (bool) (1 - (x < 0) * (x >= width) * (y < 0) * (y >= height));
}



#endif
