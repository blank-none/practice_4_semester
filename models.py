class User:
    def __init__(self, login, secret):
        self.login = login
        self.secret = secret

class Session:
    def __init__(self, session_id, user_id, method_id, data_in, params, data_out, status, start_time, end_time):
        self.session_id = session_id
        self.user_id = user_id
        self.method_id = method_id
        self.data_in = data_in
        self.params = params
        self.data_out = data_out
        self.status = status
        self.created_at = start_time
        self.time_op = end_time - start_time

    def to_dict(self):
        return {
            'session_id': self.session_id,
            'user_id': self.user_id,
            'method_id': self.method_id,
            'data_in': self.data_in,
            'params': self.params,
            'data_out': self.data_out,
            'status': self.status,
            'created_at': self.created_at,
            'time_op': self.time_op
        }
