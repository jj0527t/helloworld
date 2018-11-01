# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:54:59 2018

@author: test
"""

#%%
from PIL import Image
import scipy.fftpack
import numpy 

image_name = 'C:/xampp/htdocs/images/a0.jpg'
image = Image.open(image_name)
# RGB
print(image.mode)
image = image.resize( (512, 512), 1 )
# get pixel
print(image.getpixel((0,0)))
image_gray = image.convert("L")
# Y = 0.299 R + 0.587 G + 0.114 B
print(image_gray.getpixel((0,0)))
# 512x52
dctSize = image_gray.size[0]
# PIL: getdata -> pixel 
pixels = numpy.array(image_gray.getdata(), dtype=numpy.float).reshape((dctSize, dctSize))
all_subdct = numpy.empty((dctSize, dctSize))
x = 0
for i in range (0, len(pixels[0]), 8):
    x+=1
    for j in range(0, len(pixels[0]), 8):
        subpixels = pixels[i:i+8, j:j+8]
        # .T: xy change
        subdct = scipy.fftpack.dct(scipy.fftpack.dct(subpixels.T, norm="ortho").T, norm="ortho")
        all_subdct[i:i+8, j:j+8] = subdct
        
# normalization
all_subdct2 = all_subdct.clip(0, 255)
# float to int
all_subdct2 = all_subdct2.astype("uint8")
# transform
all_subdct_img = Image.fromarray(all_subdct2)
all_subdct_img.save("/python/helloworld/after_dct_div8.png")
# perform 2-dimensional DCT (discrete cosine transform):
dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels.T, norm="ortho").T, norm="ortho")
dct2 = dct.clip(0, 255)
dct2 = dct2.astype("uint8")
dct_img = Image.fromarray(dct2)
dct_img.save("/python/helloworld/after_dct.png") 

all_subidct = numpy.empty((dctSize, dctSize))
for i in range (0, len(pixels[0]), 8):
    for j in range (0, len(pixels[0]), 8):
        subidct = scipy.fftpack.idct(scipy.fftpack.idct(all_subdct[i:i+8, j:j+8].T, norm="ortho").T, norm="ortho")
        all_subidct[i:i+8, j:j+8] = subidct

all_subidct2 = all_subidct.clip(0, 255)
all_subidct2 = all_subidct2.astype("uint8")
all_subidct_img = Image.fromarray(all_subidct2)
all_subidct_img.save("/python/helloworld/after_idct_div8.png")




#%%





