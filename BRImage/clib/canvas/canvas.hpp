#ifndef CANVAS_HPP
#define CANVAS_HPP

typedef unsigned char PX_TYPE;

class Canvas {

protected:
  int width = 0;
  int height = 0;

  PX_TYPE *layer;
  constexpr PX_TYPE &index(int x, int y) noexcept {
    return layer[y * width + x];
  }

public:
  Canvas() = default;
  virtual ~Canvas() = default;

  void set_inplace_layer(PX_TYPE *inplace_arr, int dim1, int dim2) noexcept;

  constexpr void stroke(int x, int y, PX_TYPE val) noexcept {
    /* bound safe stroke function */
    if (in_bounds(x, y)) {
      index(x, y) = val;
    }
  }

  [[nodiscard]] constexpr PX_TYPE get_px(int x, int y) const noexcept {
    return layer[y * width + x];
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
