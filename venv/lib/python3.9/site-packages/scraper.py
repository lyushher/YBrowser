import requests
import lxml.html

def request(headers=None, params=None, timeout=10):
    h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
    }
    h.update(headers or {})
    resp = requests.get(url,
            headers=h,
            params=params,
            timeout=timeout)
    resp.raise_for_status()
    return resp

def get_html(url, **kwargs):
    resp = request(url, **kwargs)
    return lxml.html.fromstring(resp.content.decode('utf8'))

def get_json(url, **kwargs):
    resp = request(url, **kwargs)
    return resp.json()

def download(url, path):
    fname = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return path