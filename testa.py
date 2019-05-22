import requests
import json

r=requests.post(
    url="http://127.0.0.1:8000/test/?key=46fdfe5b9809c2313caee5d393ecb127&ctime=1558447785.4032075",
    data=json.dumps({'k1':'v1'}).encode('utf-8'),
    headers={'Content-Type':'application/json'}
)
print(r.text)