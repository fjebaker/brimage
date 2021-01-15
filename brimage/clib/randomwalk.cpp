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
void random_walk(const Canvas &reference, Canvas &canvas, int x_init,
                 int y_init) noexcept {
  const int width = reference.get_width();
  const int height = reference.get_height();

  int sintab[_MAX_ANGLES_NO];
  int costab[_MAX_ANGLES_NO];
  for (int i = 0; i < _MAX_ANGLES_NO; i++) {
    const double angle = 2 * PI * i / (double)_MAX_ANGLES_NO;
    sintab[i] = _MAX_STROKE_LEN * sin(angle);
    costab[i] = _MAX_STROKE_LEN * cos(angle);
  }

  // current x and y values, corrected for the size of the region
  int currx = x_init;
  int curry = y_init;

  if (currx < MID_SQ_WIDTH || currx > width - MID_SQ_WIDTH) {
    currx = rand() % (width - SQ_WIDTH) +
            MID_SQ_WIDTH; // if outside of bounds, use random value
  }
  if (curry < MID_SQ_WIDTH || curry > height - MID_SQ_WIDTH) {
    curry = rand() % (height - SQ_WIDTH) + MID_SQ_WIDTH;
  }

  SubCanvas impart;
  SubCanvas rw_part;

  Line good_line(0, 0, 0, 0);

  int corx, cory;

  double localerr;

  int nx, ny, _nx, _ny;
  double currerr;
  T shade(reference.get_px<T>(currx, curry));

  for (int i = 0; i < _MAX_SEGMENT_NO; i++) {

    // x and y values ranging from 0 to the max respective minus size of the
    // square
    corx = currx - MID_SQ_WIDTH;
    cory = curry - MID_SQ_WIDTH;

    // segfault prevention clause; if outside of image, break
    // todo: have a better way of calculating regions near the boundary
    if (corx < 0 || cory < 0 || currx + MID_SQ_WIDTH > width ||
        curry + MID_SQ_WIDTH > height) {
      break;
    }

    // get subregions
    subregion<T>(impart, reference, corx, corx + SQ_WIDTH, cory,
                 cory + SQ_WIDTH);
    subregion<T>(rw_part, canvas, corx, corx + SQ_WIDTH, cory, cory + SQ_WIDTH);

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
        subregion<T>(rw_part, canvas, corx, corx + SQ_WIDTH, cory,
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
                          MonochomeCanvas &canvas, int x_init,
                          int y_init) noexcept {
  random_walk<Grey>(reference, canvas, x_init, y_init);
}

template <>
void random_walk_template(const RGBCanvas &reference, RGBCanvas &canvas,
                          int x_init, int y_init) noexcept {
  random_walk<RGB>(reference, canvas, x_init, y_init);
}
