import json
import re
import requests

GITHUB_API = 'https://api.github.com/repos/ethereum/py-evm/pulls?state=closed'
URL_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:jpg)"

def get_five_recent_pictures():
    params = {}
    r = requests.get(GITHUB_API, params=params)
    pics = []
    for pr in r.json():
        pic_url = grab_picture_from_pr(pr)
        if pic_url is not None and len(pics) < 10:
            pics.append(pic_url)
    return pics

def grab_picture_from_pr(pr):
    body = pr['body']
    if body is None:
        return None
    img = extract_image_link(body)
    return img

def extract_image_link(url):
    url = re.search(URL_REGEX, url)
    if url is None:
        return None
    return url.group()


