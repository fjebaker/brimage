#ifndef CANVAS_HPP
#define CANVAS_HPP

typedef unsigned char PX_TYPE;


class Canvas {

protected:

  int width  = 0 ;
  int height = 0 ;

  PX_TYPE* layer;
  PX_TYPE& index(int x, int y) noexcept ;

public:

  Canvas() = default;
  virtual ~Canvas() = default;

  void set_inplace_layer(PX_TYPE* inplace_arr, int dim1, int dim2) noexcept ;

  void stroke(int x, int y, PX_TYPE val) noexcept ;

  PX_TYPE get_px(int x, int y) const noexcept ;

  bool in_bounds(int x, int y) const noexcept ;

  int get_width() const noexcept ;
  int get_height() const noexcept ;

};

inline PX_TYPE& Canvas::index(int x, int y) noexcept {
    return layer[y * width + x];
}

inline void Canvas::stroke(int x, int y, PX_TYPE val) noexcept {
  /* bound safe stroke function */
  if (in_bounds(x, y)) {
    index(x, y) = val;
  }
}

inline PX_TYPE Canvas::get_px(int x, int y) const noexcept {
  return layer[y * width + x];
}

inline bool Canvas::in_bounds(int x, int y) const noexcept {
  if (x < 0 || x >= width || y < 0 || y>= height) {
    return false;
  } else {
    return true;
  }
}

inline int Canvas::get_width() const noexcept {
  return width;
}
inline int Canvas::get_height() const noexcept {
  return height;
}



#endif
