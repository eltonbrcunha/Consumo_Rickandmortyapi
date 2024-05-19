import requests
from util.http_adapters import TimeoutHTTPAdapter
from urllib3.util.retry import Retry
from util.http_hooks import raise_for_status_hook


retry_policy = Retry(
    total=4,
    backoff_factor=1,
    status_forcelist=[429,500,502,503,504],
    allowed_methods= ["GET", "HEAD", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"],
)

adapter = TimeoutHTTPAdapter(max_retries= retry_policy)

http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)
http.hooks["response"] = [raise_for_status_hook]