# Cloud Bear ![Bear logo](images/bear_100x80.png)

A command line utility to work with AWS services via boto3.

## Motivation

WIP

## Quick Start

WIP

## Usage

Upload a file to S3:

```
python3 upload_to_s3.py <filename> [bucket name]
```

If the bucket name is not provided, it is imported from DEFAULTS.py (BUCKET_NAME).

## Requirements

- Python 3.x
- boto3 (see requirements.txt)
- AWS CLI installed separately (e.g., via snap or package manager)

## Next Steps

Add a file with a function to list buckets:

// Print out bucket names
// for bucket in s3.buckets.all():
//    print(bucket.name)