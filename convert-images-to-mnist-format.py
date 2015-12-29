#resize script converts images to 28x28 px pngs
#this python script for converting 28x28 pixel pngs to MNIST format

from PIL import Image
import os
from array import *

def average(pixel):
  return (pixel[0] + pixel[1] + pixel[2])/3

folders = ['./training-images', './test-images']

for folder in folders:
  #reinit data
  data_image = array('B')
  data_label = array('B')

  #TODO get this into a sub-routine
  #set headers one byte at a time
  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x08)
  data_image.append(0x03) # magic number for training images

  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x02) # two images, TODO replace with variable

  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x1C) # number of rows 28

  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x00)
  data_image.append(0x1C) # number of columnns 28

  #TODO get this into a sub-routine
  data_label.append(0x00)
  data_label.append(0x00)
  data_label.append(0x08)
  data_label.append(0x01) # magic number for training images

  data_label.append(0x00)
  data_label.append(0x00)
  data_label.append(0x00)
  data_label.append(0x02) # two images, TODO replace with variable

  for dirname, dirnames, filenames in os.walk(folder):
    for filename in filenames:
      if filename.endswith('.png'):

        im = Image.open(os.path.join(dirname, filename))
        pix = im.load()
        #print(os.path.join(dirname, filename))

        #store the class name from look at path
        class_name = int(os.path.join(dirname).split('/')[-1])
        #print class_name

        ###############################
        #        MNIST Fork           #
        #getting image into byte array#
        ###############################

        #append image
        for x in range(0,28):
          for y in range(0,28):
            print average(pix[x,y])
            data_image.append(average(pix[x,y]))

        #append label
        data_label.append(class_name) # labels start (one unsigned byte each)

  #####################
  #write all to binary#
  #####################

  #TODO make sure to convert if else into string replace for neatness
  # folders = ['./training-images', './test-images']
  if folder==folders[0]:
    output_file = open('train-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()

    output_file = open('train-labels-idx1-ubyte', 'wb')
    data_label.tofile(output_file)
    output_file.close()
  elif folder==folders[1]:
    output_file = open('test-images-idx3-ubyte', 'wb')
    data_image.tofile(output_file)
    output_file.close()

    output_file = open('test-labels-idx1-ubyte', 'wb')
    data_label.tofile(output_file)
    output_file.close()


