from flask import Flask
from flask_restful import Api

from essentials import read_env
from handlers.api_disparate_platforms import DisparatePlatformImages

env = read_env()
app = Flask(__name__)

api = Api(app)

api.add_resource(DisparatePlatformImages, env['endpoints']['images'])
#api.add_resource(DisparatePlatformImages, env['endpoints']['about'])


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )
