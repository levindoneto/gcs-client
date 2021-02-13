from google.cloud import storage

def get_buckets():
    storage_client = storage.Client.from_service_account_json('MyFirstProject-39fc0f84b82a.json')
    buckets = list(storage_client.list_buckets())
    
    return buckets

get_buckets()
upload_file('jobs-numen', )