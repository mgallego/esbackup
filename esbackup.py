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

def check_repository():
    repository_url = url + '/_snapshot/'+settings.repository_name
    r = requests.get(repository_url)
    if (200 != r.status_code):
        print '%s returns %s' %(repository_url, r.status_code)
        exit(1)

def clean_snaptshops():
    snapthost_url = url + '/_snapshot/'+settings.repository_name+'/_all'
    r = requests.get(snapthost_url)
    if (200 != r.status_code):
        print '%s returns %s' %(snapthost_url, r.status_code)
        exit(1)
    response = r.json()
    if (len(response['snapshots']) > settings.snaptshops_to_store):
        print 'Remove old snapshots'

def main():
    check_connection()
    check_repository()
    clean_snaptshops()


if __name__ == "__main__":
    main()

