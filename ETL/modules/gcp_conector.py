from google.cloud import storage
from google.oauth2 import service_account
from io import StringIO


credentials = service_account.Credentials.from_service_account_file(r"D:\workspace\bike-factory-345816-a93afc80e64f.json")

   
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client(credentials=credentials)
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)







## Não utlizado ainda ----------------------------------------------------------------------
def download_blob_into_memory(bucket_name, blob_name):
    """Downloads a blob into memory."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The ID of your GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.get_blob(blob_name)
    download_file = blob.download_as_text(encoding="utf-8")

    # print(
    #     "Downloaded storage object {} from bucket {} as the following string: {}.".format(
    #         blob_name, bucket_name, contents
    #     )
    # )
    return download_file




# # The name for the new bucket
# bucket_name = "testannnnndddddoooooo"

# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

# print("Bucket {} created.".format(bucket.name))