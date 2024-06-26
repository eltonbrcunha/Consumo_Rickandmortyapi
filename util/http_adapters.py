from requests import PreparedRequest, Response
from requests.adapters import HTTPAdapter


DEFAULT_TIMEOUT = 5

class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs) -> None:
        self.timeout = DEFAULT_TIMEOUT

        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
            del kwargs['timeout']

        super().__init__(*args, **kwargs)

    def send(self, request: PreparedRequest, **kwargs) -> Response:
        timeout = kwargs.get('timeout')
        if timeout is None:
            kwargs['timeout'] = self.timeout

        return super().send(request, **kwargs)