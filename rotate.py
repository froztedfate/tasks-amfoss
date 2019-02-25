from PIL import Image
output=Image.open('greyscale1.png')
output.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
