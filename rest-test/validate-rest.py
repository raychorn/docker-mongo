import os
import requests

def test_get1():
    url = 'http://169.254.17.208:9000/rest/services/4a1bf01e-0693-48c5-a52b-fc275205c1d8/__directory__/'

    resp = requests.get(url=url)
    data = resp.json()
    print(data)
    
def test_get2():
    url = 'http://10.0.0.84:9000/rest/services/4a1bf01e-0693-48c5-a52b-fc275205c1d8/__directory__/'

    resp = requests.get(url=url)
    data = resp.json()
    print(data)
    

if (__name__ == '__main__'):
    if (0):
        for k,v in os.environ.items():
            print('{} : {}'.format(k, v))
        
    test_get1()
