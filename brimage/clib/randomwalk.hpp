#ifndef RANDOMWALK_HPP
#define RANDOMWALK_HPP

#include "canvas/subcanvas.hpp"

template <class T>
void random_walk_template(const T &reference, T &canvas, int x_init,
                          int y_init) noexcept {}

template <>
void random_walk_template(const MonochomeCanvas &reference,
                          MonochomeCanvas &canvas, int x_init,
                          int y_init) noexcept;

template <>
void random_walk_template(const RGBCanvas &reference, RGBCanvas &canvas,
                          int x_init, int y_init) noexcept;

#endif
