import boto3
import sys
from DEFAULTS import BUCKET_NAME

from botocore.exceptions import NoCredentialsError, ClientError
from boto3.exceptions import S3UploadFailedError

def upload_file_to_s3(local_path, bucket_name=BUCKET_NAME, object_key=None):
    if object_key is None:
        # use the file name as the object key
        import os
        object_key = os.path.basename(local_path)

    s3_client = boto3.client("s3")

    try:
        s3_client.upload_file(local_path, bucket_name, object_key)
        print(f"Uploaded '{local_path}' to 's3://{bucket_name}/{object_key}'")
    except FileNotFoundError:
        print(f"Local file not found: {local_path}")
    except NoCredentialsError:
        print(f"Credentials required. Try 'aws configure'.")
    except ClientError as e:
        print(f"Failed to upload: {e}")
    except S3UploadFailedError:
        print("The bucket does not exist.")

if __name__=="__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 upload_to_s3.py <path_to_file> <bucket_name>")
        sys.exit(1)
        
    local_file_path = sys.argv[1]
    bucket_name = sys.argv[2] if len(sys.argv) == 3 else BUCKET_NAME
    upload_file_to_s3(local_file_path, bucket_name)