class CustomResponse():

    @classmethod
    def default_response(cls, msg, status):
        if isinstance(msg, tuple):
            msg = msg[0]
        response_json = {
            "message": msg,
            "status": status
        }
        return response_json

    @staticmethod
    def data_response(data, status, msg):
        """

        :param data:
        :param status:
        :param msg:
        :return:
        """
        if isinstance(msg, tuple):
            msg = msg[0]
        response_json = {"data": data,
                         "message": msg,
                         "status": status
                         }
        return response_json