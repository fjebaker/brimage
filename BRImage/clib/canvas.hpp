#ifndef CANVAS_HPP
#define CANVAS_HPP

typedef unsigned char PX_TYPE;


class Canvas {

protected:

  PX_TYPE* layer;
  int width;
  int height;

  PX_TYPE& index(int x, int y) noexcept ;

public:

  Canvas() = default;
  virtual ~Canvas() = default;

  void set_inplace_layer(PX_TYPE* inplace_arr, int dim1, int dim2) noexcept ;

  void stroke(int x, int y, PX_TYPE val) noexcept ;

  PX_TYPE get_px(int x, int y) const noexcept ;

  void subregion(Canvas& sub, int x0, int x1, int y0, int y1) const noexcept ;

  bool in_bounds(int x, int y) const noexcept ;

  int get_width() const noexcept ;
  int get_height() const noexcept ;

};

#endif
