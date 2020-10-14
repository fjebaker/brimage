#include "subcanvas.hpp"

#include <stdlib.h>

SubCanvas::SubCanvas() noexcept {
  width = SQ_WIDTH;
  height = SQ_WIDTH;
  layer = region;
}
