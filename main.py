from tkinter.filedialog import askopenfilename
from PIL import Image
import sys

dice = []
for x in range(0, 6):
    dice.append(Image.open(sys.path[0] + "/Images/dice" + str(x+1) + ".png"))


def assign_dice_to_color(grey_value):

    if grey_value < 42:
        return dice[5]
    elif grey_value < 84:
        return dice[4]
    elif grey_value < 126:
        return dice[3]
    elif grey_value < 168:
        return dice[2]
    elif grey_value < 210:
        return dice[1]
    else:
        return dice[0]


def get_color_brightness(c):

    # calculates perceived brightness of color by converting to greyscale, returns float from 0 - 1

    return (c[0] * 0.2989) + (c[1] * 0.5870) + (c[2] * 0.114) / 255


if __name__ == "__main__":

    filename = askopenfilename()
    print(filename)
