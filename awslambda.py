import time
import json
import urllib.request
import requests
from base64 import b64encode,b64decode

# wait until the server starts.
def wait_till_ready(port, timeoutsec):
    interval = 0.5
    for i in range(round(timeoutsec/interval)):
        try:
            requests.get("http://127.0.0.1:" + str(port))
            return
        except requests.exceptions.ConnectionError:
            time.sleep(interval)

    raise Exception("failed to connect to the server")

# handler for non-proxy ingegration
def handler(event, context):
    print(event)
    wait_till_ready(50021, 30)
    url = 'http://127.0.0.1:50021/simple_synthesis'
    params = {
            'text': event.get('text', 'hello'),
            'speaker': event.get('speaker', '10'),
            }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
    except urllib.error.HTTPError as err:
         return {
                "statusCode": err.code,
                "body": f"HTTP Error. {err=} {err.read()}"
                }
    except urllib.error.URLError as err:
         return {
                "statusCode": 400,
                "body": f"URL Error. {err=}"
                }
    # for API Gateway non-proxy integration
    return b64encode(body).decode('utf-8')

    # for Api Gateway proxy integration
    #return {
    #        "statusCode": 200,
    #        "headers": { "Content-Type": "audio/mpeg" },
    #        "body": b64encode(body).decode('utf-8'),
    #        'isBase64Encoded': True
    #        }


