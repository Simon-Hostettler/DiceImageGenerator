from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np
import sys

NEW_IMG_HEIGHT = 100
NEW_IMG_NAME = "DiceImage.jpg"

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
    new_size = (int(NEW_IMG_HEIGHT * relative_size * 32) - 32, NEW_IMG_HEIGHT * 32)
    dice_img = Image.new('L', new_size, color='white')

    with open("DiceArrangement.txt", "w") as f:
        for row in range(0, NEW_IMG_HEIGHT):
            line = ""
            for column in range(0, int(NEW_IMG_HEIGHT * relative_size)):
                grey_val = pixel_matrix[row][column]
                dice_number = assign_dice_to_color(grey_val)
                dice_img.paste(dice[dice_number], (column*32, row*32))
                line += str(f"{dice_number + 1}, ")
            f.write(line[:-2] + "\n")

    dice_img.save(NEW_IMG_NAME, quality=100)
    print("Done!")
    print("In real life this image would measure:"
          f" {int((1.6*NEW_IMG_HEIGHT*relative_size))}cm x {int((1.6*NEW_IMG_HEIGHT))}cm.")


def assign_dice_to_color(grey_value):
    return 5-int(grey_value/45)


if __name__ == "__main__":
    image_name = askopenfilename()
    convert_to_dice_image(image_name)
