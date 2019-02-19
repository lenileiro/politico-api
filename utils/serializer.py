from flask import jsonify, make_response


class Serializer:
    
    @classmethod
    def error(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'message': response}
            ), status_code)

    @classmethod
    def slist(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'data': [response]}
            ), status_code)

    @classmethod
    def sdict(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'data': response}), status_code)
