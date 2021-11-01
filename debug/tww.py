import sys
from datetime import datetime as dtm

import wget
import tweepy
from bson.objectid import ObjectId
from cryptography.fernet import Fernet

sys.path.append('..')
from essentials import read_env

cfg = read_env()
fnm = 'honey_bee.PNG'
status = f'Image uploaded from Tweepy({str(ObjectId())})'


def create_auth_ins(cfg=cfg):
    key = cfg['key']
    key_secret = cfg['twitter']['key_secret']
    F = Fernet(key.encode())
    key_secret = F.decrypt(key_secret.encode())
    auth = tweepy.OAuthHandler(cfg['twitter']['key_id'], key_secret.decode())

    token = cfg['twitter']['token']
    secret = cfg['twitter']['secret']
    token_ = F.decrypt(token.encode())
    secret_ = F.decrypt(secret.encode())

    auth.set_access_token(token_, secret_)
    return tweepy.API(auth)


def post(file_=fnm):
    api = create_auth_ins()
    media = api.simple_upload(fnm)
    tweet = f'Honey Bee post from Tweepy at {dtm.utcnow()}'

    return api.update_status(status=tweet, media_ids=[media.media_id])


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


def downloadLatestMedia():
    media = fetchLatestMedia()
    uri = media['media'][0]['media_url']
    return wget.download(uri)


def deleteLatestMedia():
    api = create_auth_ins()
    media = fetchLatestMedia()
    idi = media['tweet']
    return api.destroy_status(idi)
