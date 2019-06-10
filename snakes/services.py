import json
import re
import requests
import os
from eth_utils import to_tuple


CAP_REPOS = [
    'https://api.github.com/repos/ethereum/py-evm/pulls?state=closed',
    'https://api.github.com/repos/ethereum/trinity/pulls?state=closed',
    'https://api.github.com/repos/ethereum/web3.py/pulls?state=closed',
    'https://api.github.com/repos/ethpm/py-ethpm/pulls?state=closed',
    'https://api.github.com/repos/ethereum/eth-utils/pulls?state=closed',
]

JPG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:jpg)"
JPEG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:jpeg)"
PNG_REGEX = "(http(s?):)([/|.|\w|\s|-])*\.(?:png)"


def get_recent_caps():
    ten_pics = [get_two_recent_caps(repo) for repo in CAP_REPOS]
    flattened = [item for sublist in ten_pics for item in sublist]
    return flattened


@to_tuple
def get_two_recent_caps(repo):
    params = {'access_token': os.environ['GITHUB']}
    r = requests.get(repo, params=params)
    counter = 0
    for pr in r.json():
        pic_url = grab_picture_from_pr(pr)
        if pic_url and counter <= 1:
            yield pic_url, pr['html_url']
            counter += 1


def grab_picture_from_pr(pr):
    body = pr['body']
    if body:
        return extract_image_link(body)
    return None


def extract_image_link(body):
    jpg = re.search(JPG_REGEX, body)
    if validate_img(jpg):
        return jpg.group()

    jpeg = re.search(JPEG_REGEX, body)
    if validate_img(jpeg):
        return jpeg.group()

    png = re.search(PNG_REGEX, body)
    if validate_img(png):
        return png.group()

    return None


def validate_img(search):
    # images from reddit api are not supported b/c of url format / regex search conflict
    if search and 'redd' not in search.group():
        return True
    return False
