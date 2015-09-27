#!venv/bin/python

import settings, requests

url = settings.server + ':' + str(settings.port)

def check_connection():
    r = requests.get(url)
    response = r.json()
    if (200 != response['status']):
        print 'The server returns %s' %(response['status'])
        exit(1)
    if (response['version']['number'] < 1.0):
        print 'Your Elasticsearch version (%s) is not compatible with snaptshots' %(response['version']['number'])
        exit(1)

def get_snaptshops():
    pass

def main():
    check_connection()
    get_snaptshops()


if __name__ == "__main__":
    main()

