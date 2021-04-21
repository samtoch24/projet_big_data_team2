import traceback
import sys
from flask import jsonify


class CustomError:
    local = True

    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def throw(self):
        if self.local:
            etype, value, tb = sys.exc_info()
            tracelist = traceback.format_tb(tb, 2000)
        else:
            tracelist = []
        return jsonify({'message': self.message, 'traces': tracelist}), self.status_code
