import os
import time
import shutil
import zipfile

from flask import jsonify, request, send_file
from flask_restful import Resource

from resources.postmedia import upload
from resources.fetchmedia import fetch
from resources.delmedia import delete


class DisparatePlatformImages(Resource):
    def get(self):
        response = fetch()
        zipname = f'download_{int(time.time())}'
        shutil.make_archive(zipname, 'zip', 'output/')
        return send_file(
            f'{zipname}.zip',
            mimetype='zip',
            attachment_filename=f'{zipname}.zip',
            as_attachment=True
        )

    def post(self):
        bodyParams = request.get_json()
        return jsonify(upload(bodyParams))

    def delete(self):
        response = delete()
        return jsonify(response)
