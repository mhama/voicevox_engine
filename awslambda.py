import json
import urllib.request

def handler(event, context):
    url = 'http://127.0.0.1:50021/simple_synthesis'
    params = {
            'text': 'hello',
            }

    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
    except urllib.error.HTTPError as err:
         return {
                "statusCode": err.code,
                "body": "HTTP Error." + err
                }
    except urllib.error.URLError as err:
         return {
                "statusCode": err.code,
                "body": "URL Error." + err
                }
    return {
            "statusCode": res.getcode(),
            "headers": {
                "Content-Type": "audio/mpeg"
                },
            "body": body
            }


