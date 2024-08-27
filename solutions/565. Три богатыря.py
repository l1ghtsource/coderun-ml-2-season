import numpy as np
from scipy.interpolate import LinearNDInterpolator

with open('/kaggle/input/coderun-bogatiry/data.npy', 'rb') as file:
    images = np.load(file)


def restore_image(image):
    h, w, c = image.shape
    mask = image == 0
    restored = np.copy(image)

    for ch in range(c):
        channel = image[:, :, ch]
        mask_channel = mask[:, :, ch]

        known_y, known_x = np.where(~mask_channel)
        unknown_y, unknown_x = np.where(mask_channel)

        if len(known_y) == 0:
            return image

        known_coords = np.array(list(zip(known_y, known_x)))
        known_values = channel[~mask_channel]

        interpolator = LinearNDInterpolator(known_coords, known_values)

        unknown_coords = np.array(list(zip(unknown_y, unknown_x)))
        restored_channel = interpolator(unknown_coords)

        restored[unknown_y, unknown_x, ch] = restored_channel

    return restored


restored_images = np.zeros_like(images, dtype=np.float32)

for i in range(images.shape[0]):
    restored_images[i] = restore_image(images[i])

with open('answers.npy', 'wb') as file:
    np.save(file, restored_images.astype(np.uint8), allow_pickle=False, fix_imports=False)
