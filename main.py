import sys
from DEFAULTS import BUCKET_NAME
from upload_to_s3 import upload_file_to_s3

def main():
    local_path = sys.argv[1]
    bucket_name = sys.argv[2] if len(sys.argv) == 3 else BUCKET_NAME
    upload_file_to_s3(local_path, bucket_name, object_key=None)

if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 upload_to_s3.py <path_to_file> <bucket_name>")
        sys.exit(1)

main()