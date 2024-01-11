from uuid import uuid4
import threading
from falcon1 import clickhouse_conn
from datetime import datetime


class _Context:
    def __init__(self) -> None:
        self._thread_local = threading.local()

    @property
    def request_id(self):
        return getattr(self._thread_local, "request_id", None)
    
    @request_id.setter
    def request_id(self, value):
        self._thread_local.request_id = value

ctx = _Context()


class RequestIDMiddleware:
    def process_request(self, req, resp):
        request_id = uuid4()
        external_request_id = req.get_header("X-Request-ID", None)
        request_start_time = datetime.now()

        req.context.request_id = request_id
        req.context.external_request_id = external_request_id
        req.context.start_time = request_start_time

    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('X-Request-ID', req.context.request_id)
        request_end_time = datetime.now()
        path = req.path

        data = [
            req.context.request_id, req.context.external_request_id, req.method,
            path, req.context.start_time, request_end_time, resp.status
        ]
        clickhouse_conn.insert("transactions", [data], column_names=[
            'request_id', 'external_request_id', 'http_method', 'path',
            'start_time', 'end_time', 'http_status'
        ])
