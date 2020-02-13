import cv2
from PIL import Image, ImageFont, ImageDraw
import tweet

alpha = 0.2


def circle(totalbookmark, link, imgname, imgformat):
    normalimglocation = f"Images/{imgname}"
    img = Image.open(normalimglocation)
    cvimg = cv2.imread(normalimglocation, 1)
    imgcopy = cvimg.copy()

    width, height = img.size
    centerimage = round(int(width / 2))
    circle = round(int(ratio(100, height)))

    cv2.circle(cvimg, (centerimage, height), circle, (0, 0, 0), -1)  # width, height
    transparentimg = cv2.addWeighted(imgcopy, alpha, cvimg, 1 - alpha, 0)

    cv2.imwrite(f"withcount/{imgname}", transparentimg)
    text(f"withcount/{imgname}", totalbookmark, link)


def text(filelocation, totalbookmark, link):
    img = Image.open(filelocation)
    width, height = img.size
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Fonts/Bebas-Regular.ttf', ratio2(height=height))

    textwidth, textheight = font.getsize(str(totalbookmark))
    halftextwidth = textwidth / 2

    draw.text(((width / 2) - halftextwidth, height - textheight), str(totalbookmark), fill=(255, 255, 255), font=font)

    img.save(filelocation, 'PNG')
    print(filelocation)

    tweet.post(link, filelocation)


def ratio(num1, height):
    return round(int((height / 120) * 10))


def ratio2(height):
    return round(int((height / 100) * 7))
