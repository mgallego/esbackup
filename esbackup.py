#!venv/bin/python
import settings, requests, time, datetime, json

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

def create_snapshot():
    snapshot_name = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    snapshot_url = url + '/_snapshot/%s/%s?wait_for_completion=true' %(settings.repository_name, snapshot_name)
    payload = {"indices": ','.join(settings.indices)}
    r = requests.put(snapshot_url, data=json.dumps(payload))
    response = r.json()
    if (200 != r.status_code):
        print '%s returns %s' %(snaptshot_url, r.status_code)
        print response
        exit(1)
    print 'Created the new %s snaptshot' %(snapshot_name)

def get_snapshots():
    snaptshots_url = url + '/_snapshot/'+settings.repository_name+'/_all'
    r = requests.get(snaptshots_url)
    if (200 != r.status_code):
        print '%s returns %s' %(snaptshots_url, r.status_code)
        exit(1)
    return r.json()

def delete_snapshot(snapshot_name):
    snapshot_url = url + '/_snapshot/%s/%s?wait_for_completion=true' %(settings.repository_name, snapshot_name)
    print snapshot_url
    r = requests.delete(snapshot_url)
    response = r.json()
    if (200 != r.status_code):
        print '%s returns %s' %(snapshot_url, r.status_code)
        print response
        exit(1)
    print 'Delete the %s snaptshot' %(snapshot_name)

def clean_snaptshots():
    response = get_snapshots()
    while (len(response['snapshots']) > settings.snaptshops_to_store):
        delete_snapshot(response['snapshots'][0]['snapshot'])
        response = get_snapshots()

def main():
    check_connection()
    check_repository()
    create_snapshot()
    clean_snaptshots()

if __name__ == "__main__":
    main()
