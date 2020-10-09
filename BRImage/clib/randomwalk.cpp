#include "randomwalk.hpp"

#include "subcanvas.hpp"
#include "shapes.hpp"

#include <cmath>
#include <stdlib.h>

#define ANGLES_NO 5
#define SEGMENT_NO 500
#define STROKE_LEN 13
#define PI 3.141592653589793238463

inline double calc_diff(const Canvas& reference, const Canvas& canvas, int width, int height) {
  double running_sum = 0;

  for (int i = 0; i < width; i++) {
    for (int j = 0; j < height; j++) {
      if (reference.in_bounds(i, j)) {
        running_sum += abs(
          (int) reference.get_px(i, j) - (int) canvas.get_px(i, j)
        );
      }
    }
  }
  return running_sum;
}

void random_walk(const Canvas& reference, Canvas& canvas) {
  int width = reference.get_width();
  int height = reference.get_height();

  int sintab[ANGLES_NO];
  int costab[ANGLES_NO];
  for (int i = 0; i < ANGLES_NO; i++) {
    double angle = 2 * PI * i / (double) ANGLES_NO;
    sintab[i] = STROKE_LEN * sin(angle);
    costab[i] = STROKE_LEN * cos(angle);
  }

  int sqwidth = STROKE_LEN * 2 + 4;
  int mid_sqwidth = STROKE_LEN + 2;

  int currx = rand() % (width-sqwidth) + mid_sqwidth;
  int curry = rand() % (height-sqwidth) + mid_sqwidth;

  SubCanvas impart(sqwidth, sqwidth);
  SubCanvas rw_part(sqwidth, sqwidth);

  Line good_line(0,0,0,0);

  int corx, cory;

  double localerr;

  int nx, ny, _nx, _ny;
  double currerr;
  unsigned char shade = reference.get_px(currx, curry);

  for (int i = 0; i < SEGMENT_NO; i++) {

    corx = currx - mid_sqwidth;
    cory = curry - mid_sqwidth;

    // get subregions
    impart.subregion(reference,
      corx, corx+sqwidth, cory, cory+sqwidth
    );
    rw_part.subregion(canvas,
      corx, corx+sqwidth, cory, cory+sqwidth
    );

    localerr = calc_diff(impart, rw_part, sqwidth, sqwidth);

    bool saved = false;
    _nx = currx;
    _ny = curry;

    for (int a = 0; a < ANGLES_NO; a++) {
      nx = currx + costab[a];
      ny = curry + sintab[a];

      if (canvas.in_bounds(nx, ny)) {
        // draw line
        Line l(mid_sqwidth, mid_sqwidth, costab[a] + mid_sqwidth, sintab[a] + mid_sqwidth);
        l.trace(rw_part, shade);

        currerr = calc_diff(impart, rw_part, sqwidth, sqwidth);

        if (currerr < localerr) {
          saved = true;
          good_line = l; // copy assignment
          _nx = nx;
          _ny = ny;
          localerr = currerr;
        }

        // reset rw_part region
        rw_part.subregion(canvas,
          corx, corx+sqwidth, cory, cory+sqwidth
        );
      }
    }

    if (saved) {
      // if new good_line, add to canvas and update endpoints
      good_line.p1.x += currx - mid_sqwidth;
      good_line.p2.x += currx - mid_sqwidth;
      good_line.p1.y += curry - mid_sqwidth;
      good_line.p2.y += curry - mid_sqwidth;
      good_line.trace(canvas, shade);
      currx = _nx;
      curry = _ny;
    }

  }

}
