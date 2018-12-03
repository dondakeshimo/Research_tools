from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2


image = Image.open("black_double_parafin_2.tiff")
np_image = np.asarray(image)
plt.imshow(np_image)
np_image.shape
plt.show()
