import base64
from io import BytesIO
from datetime import datetime as dtm

import wget
import tweepy
from cryptography.fernet import Fernet

from essentials import read_env

cfg = read_env()


def create_auth_ins(cfg=cfg):
    key = cfg['key'] + '='
    key_secret = cfg['twitter']['key_secret']
    F = Fernet(key.encode())
    key_secret = F.decrypt(key_secret.encode())
    key_id = 'BP' + cfg['twitter']['key_id'] + 'LdL'
    auth = tweepy.OAuthHandler(, key_secret.decode())

    token = cfg['twitter']['token']
    secret = cfg['twitter']['secret_1'] + cfg['twitter']['secret_2']
    token_ = F.decrypt(token.encode())
    secret_ = F.decrypt(secret.encode())

    auth.set_access_token(token_, secret_)
    return tweepy.API(auth)


def queryUserTimeLine(last_id=0, uid='n14raghu'):
    api = create_auth_ins()
    if last_id > 0:
        return api.user_timeline(
            screen_name=uid,
            count=100,
            include_rts=False,
            exclude_replies=True,
            max_id=last_id-1
        )

    return api.user_timeline(
        screen_name=uid,
        count=100,
        include_rts=False,
        exclude_replies=True,
    )


def findMediaFromTweets(tweets):
    for tweet in tweets:
        media = tweet.entities.get('media', [])
        if media:
            return {
                'tweet': tweet.id,
                'media': media
            }
            return media

    return False


def fetchLatestMedia():
    last_id = 0
    while True:
        tweets = queryUserTimeLine(last_id)
        media = findMediaFromTweets(tweets)
        if media:
            break
        last_id = tweets[-1].id-1

    return media


def post_file(file_):
    api = create_auth_ins()
    media = api.simple_upload(file_)
    tweet = f'Honey Bee post from Tweepy at {dtm.utcnow()}'
    res = api.update_status(status=tweet, media_ids=[media.media_id])

    return {
        "twitter": res.id,
    }


def post_content(content):
    api = create_auth_ins()
    file_obj = BytesIO(base64.b64decode(content.encode()))
    media = api.simple_upload(filename='filename', file=file_obj)
    tweet = f'Honey Bee post from Tweepy at {dtm.utcnow()}'
    res = api.update_status(status=tweet, media_ids=[media.media_id])

    return {
        "twitter": res.id,
    }


def post(bodyParams):
    content = bodyParams.get('img_txt', False)
    file_ = bodyParams.get('filename', False)
    if file_:
        return post_file(file_)
    if content:
        return post_content(content)
    else:
        return {
            "status_code": 400,
            'err': "Missing required params"
        }


def fetch():
    media = fetchLatestMedia()
    uri = media['media'][0]['media_url']
    wget.download(uri, out='output/flask_twitter.PNG')


def delete():
    print('DELETING')
    api = create_auth_ins()
    media = fetchLatestMedia()
    idi = media['tweet']
    api.destroy_status(idi)
    return idi
