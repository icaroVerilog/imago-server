import json

from flask            import Request
from misc.status_code import StatusCode
from core.middlewares import EnsureAuthenticated
from core.services    import ComentPostService

class ComentPostController:
    def handle(self, request:Request):
        ensure_authenticated = EnsureAuthenticated()
        coment_post_service = ComentPostService()

        auth = ensure_authenticated.handle(
            request.headers["token"],
            request.headers["username"]
        )

        if (auth):
            request_parsed = request.get_json()

            response = coment_post_service.execute(
                username = request_parsed["username"], 
                post_id  = request_parsed["post_id"], 
                content  = request_parsed["comentary"]
            )

            if (response):
                return json.dumps({
                    "message": "success", "data": response, "status_code": StatusCode.OK
                }), StatusCode.OK
            else:
                return json.dumps({
                    "message": "failed", "data": "", "status_code": StatusCode.Error
                }), StatusCode.Error
        else:
            return json.dumps({
            "message": "unauthorized", "status_code": StatusCode.Unauthorized
        }), StatusCode.Unauthorized
