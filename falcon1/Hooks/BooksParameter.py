import falcon


class ValidateParameters:
    def validate_params(self, req, resp, resource, params):
        if req.params:
            limit = req.get_param_as_int('limit') or 0
            if limit>10:
                raise falcon.HTTPBadRequest(title="Wrong Limit Parameter",
                description="Please Provide Valid Limit")
