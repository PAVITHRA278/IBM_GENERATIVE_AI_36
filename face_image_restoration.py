
import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('inputs/cropped_faces/Adele_crop.png')
img2 = imread('inputs/cropped_faces/Julia_Roberts_crop.png')
img3 = imread('inputs/cropped_faces/Justin_Timberlake_crop.png')
img4 = imread('inputs/cropped_faces/Paris_Hilton_crop.png')

# show images
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(1, 4, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(1, 4, 2)
ax2.imshow(img2)
ax2.axis('off')
ax3 = fig.add_subplot(1, 4, 3)
ax3.imshow(img3)
ax3.axis('off')
ax4 = fig.add_subplot(1, 4, 4)
ax4.imshow(img4)
ax4.axis('off')

!rm -rf results
!python inference_gfpgan.py -i inputs/cropped_faces -o results -v 1 -s 2 --aligned

!ls results

import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('results/cmp/Adele_crop_00.png')
img2 = imread('results/cmp/Julia_Roberts_crop_00.png')
img3 = imread('results/cmp/Justin_Timberlake_crop_00.png')
img4 = imread('results/cmp/Paris_Hilton_crop_00.png')

# show images
fig = plt.figure(figsize=(15, 30))
ax1 = fig.add_subplot(4, 1, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(4, 1, 2)
ax2.imshow(img2)
ax2.axis('off')
ax3 = fig.add_subplot(4, 1, 3)
ax3.imshow(img3)
ax3.axis('off')
ax4 = fig.add_subplot(4, 1, 4)
ax4.imshow(img4)
ax4.axis('off')

"""We can see that:
Not only the **facial details**, but also the **colors** are enhanced by the GFPGAN model.
"""

# Visualize input images to be resotred
import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('inputs/whole_imgs/00.jpg')
img2 = imread('inputs/whole_imgs/10045.png')

# show images
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img2)
ax2.axis('off')

!python inference_gfpgan.py -i inputs/whole_imgs -o results -v 1 -s 2 --bg_upsampler realesrgan

import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('results/cmp/00_00.png')
img2 = imread('results/cmp/00_01.png')
img3 = imread('results/cmp/10045_02.png')
img4 = imread('results/cmp/10045_01.png')

# show images
fig = plt.figure(figsize=(15, 30))
ax1 = fig.add_subplot(4, 1, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(4, 1, 2)
ax2.imshow(img2)
ax2.axis('off')
ax3 = fig.add_subplot(4, 1, 3)
ax3.imshow(img3)
ax3.axis('off')
ax4 = fig.add_subplot(4, 1, 4)
ax4.imshow(img4)
ax4.axis('off')

# Visualize the whole images
# However, due to the color and detail inconsistency, the results may look unnatural.

import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('results/restored_imgs/00.jpg')
img2 = imread('results/restored_imgs/10045.png')

# show images
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(1, 2, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(1, 2, 2)
ax2.imshow(img2)
ax2.axis('off')



"""## 2. Inference"""



"""## 3. Visualize"""

# Visualize the results
# The left are the inputs images; the right are the results of GFPGAN
import cv2
import matplotlib.pyplot as plt

def imread(img_path):
  img = cv2.imread(img_path)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  return img

# read images
img1 = imread('results/cmp/008_Benedict_Cumberbatch_01.png')
img2 = imread('results/cmp/008_Benedict_Cumberbatch_00.png')


# show images
fig = plt.figure(figsize=(15, 15))
ax1 = fig.add_subplot(2, 1, 1)
ax1.imshow(img1)
ax1.axis('off')
ax2 = fig.add_subplot(2, 1, 2)
ax2.imshow(img2)
ax2.axis('off')

"""## 4. Download results"""

# download the result
!ls results
print('Download results')
os.system('zip -r download.zip results')
files.download("download.zip")