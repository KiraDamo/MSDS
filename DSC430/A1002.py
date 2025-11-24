#Written by Kira Damo
#I have not given or received any unauthorized assistance on this assignment
#June 14
#https://youtu.be/HhbSx_qz8Kc

import numpy as np
import matplotlib.pyplot as plt

def salt_and_pepper(img, p):
    'takes red channels of image and makes it gray. Still maintains dimensions'
    #if colored, change to gray, otherwise keep as is
    if img.ndim == 3:
        img_gray = img[:, :, 0]
    else:
        img_gray = img

    noise = img_gray.copy()
    #picks random pixel to salt or pepper
    rand=np.random.rand(*img_gray.shape)

    #salting
    noise[rand < (p/2)] = 0
    noise[rand > 1-(p/2)] = 1

    return noise

def median_filter(img, W):
    'border that uses the median filter everywhere including edges.'
    padded = np.pad(img, W//2) #floor of W/2

    new_img = np.zeros_like(img) #same dimension as photo but all white

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            #creates window centered at i,j with length and width of w
            window = padded[i:i+W, j:j+W]
            new_img[i, j] = np.median(window)
    return new_img
    
def main():
    'displays images'
    img = plt.imread('Depaul.jpg')
    noise_img = salt_and_pepper(img, 0.5)
    #when p is too high, the noise will be preserved 
    plt.figure(figsize=(12,4))
    #original
    plt.subplot(1,3,1)
    plt.imshow(img)
    #noise
    plt.subplot(1,3,2)
    plt.imshow(noise_img, cmap='gray')
    #clean
    plt.subplot(1,3,3)
    cleaned_img = median_filter(noise_img, 1)
    plt.imshow(cleaned_img, cmap='gray')
    plt.show()
