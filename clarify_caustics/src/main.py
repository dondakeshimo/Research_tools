import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps


img_org = Image.open("data/image007.png")
img_np = np.array(img_org)
plt.imshow(img_np)
plt.show()

img = img_org.filter(ImageFilter.FIND_EDGES)
img_np = np.array(img)
plt.imshow(img_np)
plt.show()

img = img_org.point(lambda x: x * 2)
img_np = np.array(img)
plt.imshow(img_np)
plt.show()

img = img_org.convert("L")
img = img.point(lambda x: 0 if x < 20 else x)
img_np = np.array(img)
plt.imshow(img_np)
plt.show()

img = ImageOps.equalize(img_org)
img_np = np.array(img)
plt.imshow(img_np)
plt.show()

img_np.shape
