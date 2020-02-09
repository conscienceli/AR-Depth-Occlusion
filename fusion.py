import os
import os.path
from PIL import Image
import numpy as np
import cv2

file_dir = '../AR-Depth-cpp/output'
file_list = sorted(os.listdir(file_dir))
depth_folder = './depth'

os.makedirs(depth_folder, exist_ok=True)

for file_name in file_list:
    image = Image.open(f'{file_dir}/{file_name}')
    image_array = np.array(image)

    final_image_array = np.zeros(image_array.shape, dtype=np.uint8)
    for row_id, row in enumerate(image_array):
        for col_id, elem in enumerate(row):
            if elem < 100:
                final_image_array[row_id, col_id] = elem * 255 / 100 * 20
            else:
                final_image_array[row_id, col_id] = 0
    
    final_image = Image.fromarray(final_image_array, 'L')
    final_image.save(f'{depth_folder}/{file_name}')
    # final_image.show()
    img = cv2.imread(f'{depth_folder}/{file_name}',0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()