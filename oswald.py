from PIL import Image
img=Image.open('oswald11.png').convert('LA')
rotate=img.rotate(270)
transposed=rotate.transpose(Image.FLIP_LEFT_RIGHT)
transposed.save('final.png')

