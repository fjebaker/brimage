#ifndef PIXELS_HPP
#define PIXELS_HPP

#include <cmath>
typedef unsigned char PX_TYPE;

struct Grey {
  PX_TYPE val;
  constexpr Grey(PX_TYPE val) noexcept : val{val} {};
  constexpr Grey(const Grey &c) noexcept = default;
  constexpr Grey(Grey &&c) noexcept = default;
  ~Grey() noexcept = default;

  double diff(const Grey &c1) const noexcept { return abs(this->val - c1.val); }
};

struct RGB {
  PX_TYPE r, g, b;
  constexpr RGB(PX_TYPE r, PX_TYPE g, PX_TYPE b) noexcept : r{r}, g{g}, b{b} {};
  constexpr RGB(const RGB &c) noexcept = default;
  constexpr RGB(RGB &&c) noexcept = default;
  ~RGB() noexcept = default;

  double diff(const RGB &c1) const noexcept {
    return (double)abs(this->r - c1.r) + abs(this->g - c1.g) +
           abs(this->b - c1.b);
  }
};

#endif
