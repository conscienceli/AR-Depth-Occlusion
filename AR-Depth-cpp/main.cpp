#include "src/ARDepth.h"

int main() {
    std::string input_frames = "./666/frames";
    std::string input_colmap = "./666/reconstruction";
    bool resize = true;
    bool visualize = true;
    ARDepth ardepth(input_frames, input_colmap, resize, visualize);
    ardepth.run();

    return 0;
}