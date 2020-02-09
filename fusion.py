import os
from PIL import Image
import numpy as np
import cv2

range_factor = 40

file_dir = './AR-Depth-cpp/build/output'
file_list = sorted(os.listdir(file_dir))
depth_folder = './depth'
final_folder = './final'
raw_folder = './AR-Depth-cpp/data/frames'

os.makedirs(depth_folder, exist_ok=True)
os.makedirs(final_folder, exist_ok=True)
os.makedirs('./temp/', exist_ok=True)

stikers_path =['./pics/stiker1.png', './pics/stiker2.png', './pics/stiker3.png']
stikers = [np.array(Image.open(s), dtype=np.uint8) for s in stikers_path]
stikers_loc = [150, 70, 30]

for file_name in file_list:
    image = Image.open(f'{file_dir}/{file_name}')
    image_array = np.array(image)

    depth_image_array = np.zeros(image_array.shape, dtype=np.uint8)
    for row_id, row in enumerate(image_array):
        for col_id, elem in enumerate(row):
            if elem < 100:
                depth_image_array[row_id, col_id] = elem * 255 / 100 * range_factor
            else:
                depth_image_array[row_id, col_id] = 0
    
    depth_image = Image.fromarray(depth_image_array, 'L')
    depth_image.save(f'{depth_folder}/{file_name}')

    raw_image_array = np.array(Image.open(f'{raw_folder}/{file_name}'), dtype=np.uint8)
    final_image_array = np.zeros((image_array.shape[0], image_array.shape[1], 3), dtype=np.uint8)
    for stiker_id, stiker in enumerate(stikers):
        for row_id, row in enumerate(stiker):
            for col_id, elem in enumerate(row):
                if elem[3] == 0 or depth_image_array[row_id, col_id] < stikers_loc[stiker_id]:
                    if sum(final_image_array[row_id, col_id]) == 0:
                        final_image_array[row_id, col_id] = raw_image_array[row_id, col_id] 
                else:
                    final_image_array[row_id, col_id] = elem[:3]
    final_image = Image.fromarray(final_image_array, 'RGB')
    final_image.save(f'{final_folder}/{file_name}')

    depth = cv2.imread(f'{depth_folder}/{file_name}',0)
    depth_3_channel = cv2.cvtColor(depth, cv2.COLOR_GRAY2BGR)
    raw = cv2.imread(f'{raw_folder}/{file_name}', 1)
    final = cv2.imread(f'{final_folder}/{file_name}', 1)
    numpy_horizontal = np.hstack((raw, depth_3_channel, final))
    cv2.namedWindow('all', cv2.WINDOW_NORMAL)
    cv2.imshow('all', numpy_horizontal)

    cv2.imwrite(f'./temp/{file_name}', numpy_horizontal)
    
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

finals = [Image.open('./temp/'+s) for s in sorted(os.listdir('./temp'))]
finals[0].save('pics/sample.gif', save_all=True, append_images=finals[1:], optimize=True, duration=40, loop=0)