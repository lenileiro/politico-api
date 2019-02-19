from flask import jsonify, make_response


class Serializer:
    
    @classmethod
    def serialize_error(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'message': response}
            ), status_code)

    @classmethod
    def serialize_msg(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'data': {'message': response}}
            ), status_code)

    @classmethod
    def serialize_object_list(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'data': [response]}
            ), status_code)

    @classmethod
    def serialize_object_dict(cls, response, status_code=200):
        return make_response(jsonify(
            {'status': status_code, 'data': response}), status_code)
