from flask import jsonify, make_response


class Serializer:
    """ Contains method that serializes data """

    @classmethod
    def serialize(cls, response, status_code, message=200):
        """ Serializes output to json format """
        return make_response(jsonify({'status': status_code, 'data': response}), status_code)