from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor

from essentials import read_env
from resources.twitter import delete as delTwitter


def delete(env=read_env()):
    response = []
    delete_queue = []
    for portal,enable in env['platforms'].items():
        if enable:
            delete_queue.append((portal, env['httpmethods'][portal]['del']))
        else:
            response.append(
                {
                    portal: 'Disabled'
                }
            )
    with ProcessPoolExecutor(max_workers=3) as executor:
        pool_dict = {
            executor.submit(
                del_from_portal,
                item[0],
                item[1],
            ): item for item in delete_queue
        }
    for _future in as_completed(pool_dict):
        response.append(_future.result())

    return response


def del_from_portal(portal, method):
    if method and portal == 'twitter':
        idi = delTwitter()

        return {
            portal: f'Media ID deleted - {idi}',
            'status_code': 200
        }
    else:
        return {
            portal: f'[Mocked] Latest Image delete.',
            'status_code': 200,
        }
