#ifndef RANDOMWALK_HPP
#define RANDOMWALK_HPP

#include "canvas/subcanvas.hpp"

template <class T>
void random_walk_template(const T &reference, T &canvas) noexcept {}

template <>
void random_walk_template(const Canvas &reference, Canvas &canvas) noexcept;

template <>
void random_walk_template(const MonochomeCanvas &reference,
                          MonochomeCanvas &canvas) noexcept;

template <>
void random_walk_template(const RGBCanvas &reference,
                          RGBCanvas &canvas) noexcept;

#endif
