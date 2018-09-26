#This program downloads an image from a web page

import random
import urllib.request


def download_img_url(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


download_img_url('https://static-global-s-msn-com.akamaized.net/img-resizer/tenant/amp/entityid/AAAGfwg.png')

