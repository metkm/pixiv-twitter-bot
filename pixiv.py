import pixivpy3
import tweet
import time
import eimage

username = ''
password = ''

neededtags = ["女の子", "ツインテール", '女子高生', 'CU-NO', '白ビキニ', 'ストッキング', '猫耳', '猫と女の子', '白髪', 'オーバーウォッチ', '黒タイツ', '美脚']
posted = open('./posted.txt', 'r').readlines()
taglist = []


def download(totalbookmark, url, id):
    api.download(url, path='./Images/')
    imgformat = "".join((url).split('.')[-1:])
    time.sleep(10)
    eimage.circle(totalbookmark, "https://www.pixiv.net/en/artworks/{}".format(id), f"{id}_p0.{imgformat}", imgformat)


def isposted(illustid):
    with open('posted.txt', 'r+') as r:
        rr = r.readlines()

    if id not in rr:
        with open('posted.txt', 'a+') as f:
            f.write(str(illustid) + "\n")
            return True
    elif id in rr:
        return False


def illusttags(tags, bookmarkcount):
    if bookmarkcount > 1000:
        for i in tags:
            if i['name'] in neededtags:
                return True


while True:
    try:
        api = pixivpy3.AppPixivAPI()
        api.login(username, password)
        illust = api.illust_recommended(content_type='illust').illusts[0]
        if illusttags(illust['tags'], illust['total_bookmarks']) == True:
            if isposted(illust['id']):
                try:
                    print('posting')
                    download(illust['total_bookmarks'], illust['meta_single_page']['original_image_url'], illust.id)
                    time.sleep(3600)
                except:
                    download(illust['image_urls']['large'], illust.id)
                    time.sleep(3600)

    except:
        time.sleep(5)
