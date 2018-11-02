# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:26:02 2018

@author: test
"""

#%%
from PIL import Image
import numpy
import math
import matplotlib.pyplot as plt
import cv2

image_name = '/python/a0.jpg'
watermark_name = '/python/image_with_watermark.jpg'

image = cv2.imread(image_name)
image = image.astype('float')
watermark = cv2.imread(watermark_name)
watermark = watermark.astype('float')
(b, g, r) = cv2.split(image)
(b1, g1, r1) = cv2.split(watermark)

B = b - b1
G = g - g1
R = r - r1

width = image.shape[0]
height = image.shape[1]


mser = R*R
mseg = G*G
mseb = B*B

SUM = mser.sum() + mseg.sum() + mseb.sum()

MSE = SUM / (height * width * 3)
PSNR = 10*math.log ( (255.0*255.0/(MSE)) ,10)

print ('PSNR:', PSNR)
im = numpy.array (Image.open (image_name))
im2 = numpy.array (Image.open (watermark_name))
plt.subplot (121)
plt.title('origin image')
plt.imshow(im,plt.cm.gray)
plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.title('rebuilt image')
plt.imshow(im2,plt.cm.gray)
plt.xticks([]), plt.yticks([])
plt.show()


