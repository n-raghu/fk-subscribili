from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor

from essentials import read_env
from resources.twitter import fetch as fetchTwitter


def fetch(env=read_env()):
    response = []
    fetch_queue = []
    for portal,enable in env['platforms'].items():
        if enable:
            fetch_queue.append((portal, env['httpmethods'][portal]['get']))
        else:
            response.append(
                {
                    portal: 'Disabled'
                }
            )
    with ProcessPoolExecutor(max_workers=3) as executor:
        pool_dict = {
            executor.submit(
                fetch_from_portal,
                item[0],
                item[1]
            ): item for item in fetch_queue
        }
    for _future in as_completed(pool_dict):
        response.append(_future.result())


def fetch_from_portal(portal, method):
    if method and portal == 'twitter':
        response = fetchTwitter()

    return {
        'body': f'[Mocked] Downloaded Image from {portal}',
        'op_mode': 'original' if method else 'mock',
        'status_code': 200,
    }
