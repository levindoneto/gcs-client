from google.cloud import storage

def upload_file(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))

def get_buckets():
    storage_client = storage.Client.from_service_account_json('MyFirstProject-39fc0f84b82a.json')
    buckets = list(storage_client.list_buckets())
    
    return buckets
# print(get_buckets())
upload_file('bucket-name', 'install_deps.sh', 'subfolder/install_deps.sh')