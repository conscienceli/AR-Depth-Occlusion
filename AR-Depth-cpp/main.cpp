#include "src/ARDepth.h"

int main() {
    std::string input_frames = "../data/frames";
    std::string input_colmap = "../data/reconstruction";
    bool resize = true;
    bool visualize = true;
    ARDepth ardepth(input_frames, input_colmap, resize, visualize);
    ardepth.run();

    return 0;
}