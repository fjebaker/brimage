#include "randomwalk.hpp"

#include "shapes/shapes.hpp"

#include "configs.hpp"

#include <cmath>
#include <iostream>
#include <stdlib.h>

template <class T>
inline constexpr double calc_diff(const SubCanvas &reference,
                                  const SubCanvas &canvas) {
  double running_sum = 0;
  for (int i = 0; i < SQ_WIDTH; i++) {
    for (int j = 0; j < SQ_WIDTH; j++) {
      if (reference.in_bounds(i, j) && canvas.in_bounds(i, j)) {
        running_sum +=
            reference.get_px<RGB>(i, j).diff(canvas.get_px<RGB>(i, j));
      }
    }
  }
  return running_sum;
}

template <class T>
void random_walk(const Canvas &reference, Canvas &canvas) noexcept {
  const int width = reference.get_width();
  const int height = reference.get_height();

  int sintab[_MAX_ANGLES_NO];
  int costab[_MAX_ANGLES_NO];
  for (int i = 0; i < _MAX_ANGLES_NO; i++) {
    const double angle = 2 * PI * i / (double)_MAX_ANGLES_NO;
    sintab[i] = _MAX_STROKE_LEN * sin(angle);
    costab[i] = _MAX_STROKE_LEN * cos(angle);
  }

  int currx = rand() % (width - SQ_WIDTH) + MID_SQ_WIDTH;
  int curry = rand() % (height - SQ_WIDTH) + MID_SQ_WIDTH;

  SubCanvas impart;
  SubCanvas rw_part;

  Line good_line(0, 0, 0, 0);

  int corx, cory;

  double localerr;

  int nx, ny, _nx, _ny;
  double currerr;
  T shade(reference.get_px<T>(currx, curry));

  for (int i = 0; i < _MAX_SEGMENT_NO; i++) {

    corx = currx - MID_SQ_WIDTH;
    cory = curry - MID_SQ_WIDTH;

    // get subregions
    impart.subregion<T>(reference, corx, corx + SQ_WIDTH, cory,
                        cory + SQ_WIDTH);
    rw_part.subregion<T>(canvas, corx, corx + SQ_WIDTH, cory, cory + SQ_WIDTH);

    localerr = calc_diff<T>(impart, rw_part);

    bool saved = false;
    _nx = currx;
    _ny = curry;

    for (int a = 0; a < _MAX_ANGLES_NO; a++) {
      nx = currx + costab[a];
      ny = curry + sintab[a];

      if (canvas.in_bounds(nx, ny)) {
        // draw line
        Line l(MID_SQ_WIDTH, MID_SQ_WIDTH, costab[a] + MID_SQ_WIDTH,
               sintab[a] + MID_SQ_WIDTH);
        l.trace<T>(rw_part, shade);

        currerr = calc_diff<T>(impart, rw_part);

        if (currerr < localerr) {
          saved = true;
          good_line = l; // copy assignment
          _nx = nx;
          _ny = ny;
          localerr = currerr;
        }

        // reset rw_part region
        rw_part.subregion<T>(canvas, corx, corx + SQ_WIDTH, cory,
                             cory + SQ_WIDTH);
      }
    }

    if (saved) {
      // if new good_line, add to canvas and update endpoints
      good_line.p1.x += currx - MID_SQ_WIDTH;
      good_line.p2.x += currx - MID_SQ_WIDTH;
      good_line.p1.y += curry - MID_SQ_WIDTH;
      good_line.p2.y += curry - MID_SQ_WIDTH;
      good_line.trace<T>(canvas, shade);
      currx = _nx;
      curry = _ny;
    }
  }
}

template <>
void random_walk_template(const MonochomeCanvas &reference,
                          MonochomeCanvas &canvas) noexcept {
  random_walk<Grey>(reference, canvas);
}

template <>
void random_walk_template(const RGBCanvas &reference,
                          RGBCanvas &canvas) noexcept {
  random_walk<RGB>(reference, canvas);
}

template <>
void random_walk_template(const Canvas &reference, Canvas &canvas) noexcept {
  random_walk<Colour>(reference, canvas);
}
