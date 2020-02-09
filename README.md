
Main Steps:

1. Prepare video file "video.MOV" and extract the frames.
```bash
mkdir  ./AR-Depth-cpp/data/frames
ffmpeg -i video.MOV -vf "scale=480:270,fps=20" ./AR-Depth-cpp/data/frames/%06d.png
```
2. Get the reconstruction files with [colmap](https://colmap.github.io/install.html).
```bash
colmap automatic_reconstructor --workspace_path ./AR-Depth-cpp/data --image_path ./AR-Depth-cpp/data/frames --camera_model=PINHOLE --single_camera=1 --data_type=video  --use_gpu=false
```

3. Convert the reconstruction files to TXT format.
```bash
mkdir ./AR-Depth-cpp/data/reconstruction
colmap model_converter  --input_path ./AR-Depth-cpp/data/sparse/0 --output_path ./AR-Depth-cpp/data/reconstruction --output_type TXT
```

4. Remove all the comments lines in TXT files.

5. Build AR-Depth-cpp according to `./AR-Depth-cpp/README.md`. Then
    
```bash
cd AR_DEPTH
./AR_DEPTH
cd ..
```
