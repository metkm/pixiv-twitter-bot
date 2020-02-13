import tweepy
from PIL import Image

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def getsize(image):
    image_file = Image.open(image)
    return int(len(image_file.fp.read()))


def reducesave(image):
    image_file = Image.open(image)
    width, height = image_file.size

    newwidth = round((width / 100) * 20)
    newheight = round((height / 100) * 20)

    xwidth = width - newwidth
    xheight = height - newheight

    img = image_file.resize((int(xwidth), int(xheight)), Image.ANTIALIAS)
    img.save(image, optimize=True, quality=50)


def post(text, image):
    if getsize(image) < 3000000:
        tweet = text
        image = image
        api.update_with_media(image, tweet)
    else:
        while True:
            reducesave(image)
            if getsize(image) < 3000000:
                tweet = text
                image = image
                api.update_with_media(image, tweet)
                return True
