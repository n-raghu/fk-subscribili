import time
import base64
import requests

api = f'http://172.99.5.16:5000/subscribili/v1/images'


def create_post_dat(filename):
    with open(filename, 'rb') as fnm:
        dat_ = base64.b64encode(fnm.read())
    return {
        'img_txt': dat_.decode()
    }


def del_image():
    response = requests.delete(api)
    return response.text


def post_image(filename):
    dat = create_post_dat(filename)
    response = requests.post(url=api, json=dat)
    return response.text


def download_image():
    response = requests.get(api)
    file_ = f'download_{int(time.time())}.zip'
    with open(file_, 'wb') as ofile:
        ofile.write(response.content)
    return response


if __name__ == '__main__':
    print('Would like to Post/Download/Delete Image: ', end='')
    usr_action = input()

    if usr_action.lower() == 'delete':
        print(del_image())

    if usr_action.lower() == 'download':
        print(download_image())

    if usr_action.lower() == 'post':
        print('Enter filename with path: ', end='')
        filename = input()
        print(post_image(filename))
