from PIL import Image
img = Image.open('oswald11.png').convert('LA')
img.save('greyscale.png')


