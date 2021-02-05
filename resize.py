#This python program takes a .png file of an object and transforms it in to a 1:1 aspect ratio .png file
#without changing the form of the original image
#This can be further developed to have the functionality to convert orginal png, transform it and save as jpg file
#Also this can be modified to have the funtionality to batch process images within a certain directory

import os
from PIL import Image
image1 = Image.open("x.png") #opens original png and it puts it inside variable
width, height =image1.size #gets the height an width of the image
if width>height: 
    result = Image.new(image1.mode, (width, width), (255,255,255)) #a blank square image of length equal to width is created. Length of width is used because the image is oriented such that it's width is larger than length 
    result.paste(image1,(0,((width-height)//2))) #Pastes original image on the newly create image
else:
    result = Image.new(image1.mode, (height, height), (255, 255, 255))#a blank square image of length equal to height is created. Length of height is used because the image is oriented such that it's length is larger than width 
    result.paste(image1,(((height-width)//2),0)) #Pastes original image on the newly create image

print(width, height)#Displays width and height
result.save('y.png')#saves edited image  
result.show()#Opens the final image