class LogAdminMiddleware:

    def process_response(self, request, response):
        print dir(response)
        print response.headers
        return None
