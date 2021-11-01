from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor

from essentials import read_env
from resources.twitter import post as postTwitter
from resources.instagram import post as postInsta
from resources.facebook import post as postFB


def upload(filename, env=read_env()):
    response = []
    upload_queue = []
    for portal,enable in env['platforms'].items():
        if enable:
            upload_queue.append((portal, filename, env['httpmethods'][portal]['post']))
        else:
            response.append(
                {
                    portal: 'Disabled'
                }
            )

    with ProcessPoolExecutor(max_workers=3) as executor:
        pool_dict = {
            executor.submit(
                upload_to_platform,
                item[0],
                item[1],
                item[2],
            ): item for item in upload_queue
        }
    for _future in as_completed(pool_dict):
        response.append(_future.result())

    return response


def upload_to_platform(portal, filecontent, method):
    if method and portal == 'twitter':
        post_info = postTwitter(filecontent)

        return {
            portal: {
                'msg': f'Posted Image.',
                'info': post_info,
            },
            'op_mode': 'original',
            'status_code': 200,
        }
    else:
        return {
            portal: f'[Mocked] Posted Image.',
            'op_mode': 'mock',
            'status_code': 200,
        }
