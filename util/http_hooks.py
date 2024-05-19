from requests import Response


def raise_for_status_hook(response: Response, *args, **kwargs):
    response.raise_for_status()