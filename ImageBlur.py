__author__ = 'ManiKanta Kandagatla'


from PIL import Image
from PIL import ImageFilter

In = Image.open('C:/Users/ManiKanta Kandagatla/Desktop/a.jpg')
blur_img = In.copy()
i = 0
while i < 10:
    blur_img = blur_img.filter(ImageFilter.BLUR)
    i = i + 1
blur_img.save('C:/Users/ManiKanta Kandagatla/Desktop/out.jpg')