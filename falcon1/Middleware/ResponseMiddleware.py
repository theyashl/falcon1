class ResponseMiddleware:
    def process_response(self, req, resp, resource, req_succeded):
        if not hasattr(resp.context, 'result'):
            return
        resp.media = resp.context.result