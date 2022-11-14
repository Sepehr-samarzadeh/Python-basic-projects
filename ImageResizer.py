# you need to pip install Pillow
#then you import your image and change the size 
#enjoy

from PIL import Image

image=Image.open('code.jpg') #you need to put your pic name 

print(f"current size: {image.size}")

resized_image=image.resize((600,600))
resized_image.save('resized-code-600.jpeg') #save your new image