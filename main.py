import sys
from argparse import ArgumentParser, Namespace
from DEFAULTS import BUCKET_NAME
from upload_to_s3 import upload_file_to_s3
from print_s3_buckets import list_s3_buckets

parser = ArgumentParser()
parser.add_argument('-l', '--list', help='Lists the buckets that exist in your AWS account.', action='store_true')

# parser.parse_known_args() returns a tuple - the first element [0] is a list of parsed arguments like -l and --list,
# the second is a list of unknown arguments like filepath and bucket name
# since I am using sys.argv, I do not need the second list at the moment

args: Namespace = parser.parse_known_args()[0]

def main():
    if args.list:
        list_s3_buckets()
        sys.exit()
    
    if not args.list and (len(sys.argv) < 2 or len(sys.argv) > 3):
        print("Usage: python3 upload_to_s3.py <path_to_file> <bucket_name>")
        sys.exit(1)
    
    local_path = sys.argv[1]
    bucket_name = sys.argv[2] if len(sys.argv) == 3 else BUCKET_NAME
    
    upload_file_to_s3(local_path, bucket_name, object_key=None)

main()