class VersioningComonent:
    def process_request(self, req, resp):
        print(req.path)