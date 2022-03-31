from google.cloud import storage
import os
from google.oauth2 import service_account

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



# def download_public_file(bucket_name, source_blob_name, destination_file_name):
#     """Downloads a public blob from the bucket."""
#     bucket_name = "bike-factory-datalake"
#     source_blob_name = "bike-factory-datalake/01.RAW"
#     # destination_file_name = "local/path/to/file"

#     storage_client = storage.Client.create_anonymous_client()

#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)
#     blob.download_to_filename(destination_file_name)

#     print(
#         "Downloaded public blob {} from bucket {} to {}.".format(
#             source_blob_name, bucket.name, destination_file_name
#         )
#     )



# # The name for the new bucket
# bucket_name = "testannnnndddddoooooo"

# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

# print("Bucket {} created.".format(bucket.name))