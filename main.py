from tkinter.filedialog import askopenfilename
from PIL import Image
import sys
import numpy as np

NEW_IMG_HEIGHT = 100

dice = []
for x in range(0, 6):
    dice.append(Image.open(sys.path[0] + "/Images/dice" + str(x+1) + ".png").resize((32, 32)))

def convert_to_dice_image(filename):
    img = Image.open(filename)
    gray_image = img.convert('L')
    width, height = img.size
    relative_size = width / height
    small_img = gray_image.resize((int(NEW_IMG_HEIGHT * relative_size), NEW_IMG_HEIGHT))

    pixel_matrix = np.array(small_img)
    dice_img = Image.new('L', (int(NEW_IMG_HEIGHT*relative_size*32)-32, NEW_IMG_HEIGHT*32), color = 'white')

    for row in range(0, NEW_IMG_HEIGHT):
        for column in range(0, int(NEW_IMG_HEIGHT * relative_size)):
            greyval = pixel_matrix[row][column]
            die_face = assign_dice_to_color(greyval)
            dice_img.paste(die_face, (column*32, row*32))

    dice_img.save('DiceImage.jpg', quality = 100)
    print("Done!")
    print("In real life this image would measure:"
          f" {int((1.6*NEW_IMG_HEIGHT*relative_size)/10)}cm x {int((1.6*NEW_IMG_HEIGHT/10))}cm.")


def assign_dice_to_color(grey_value):
    if grey_value < 45:
        return dice[5]
    elif grey_value < 90:
        return dice[4]
    elif grey_value < 135:
        return dice[3]
    elif grey_value < 180:
        return dice[2]
    elif grey_value < 225:
        return dice[1]
    else:
        return dice[0]


def get_color_brightness(c):

    # calculates perceived brightness of color by converting to greyscale, returns float from 0 - 1

    return (c[0] * 0.2989) + (c[1] * 0.5870) + (c[2] * 0.114) / 255


if __name__ == "__main__":

    filename = askopenfilename()
    print(filename)
    convert_to_dice_image(filename)
