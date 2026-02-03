# Cloud Bear ![Bear logo](images/bear_100x80.png)

A command line utility to work with AWS services via boto3.

## Motivation

The goal behind the project is to build a CLI-native local tool for common AWS use cases: file upload, resource management, basic infrastructure deployment.

The tool facilitates commonplace operations while providing a degree of convenience with extra CLI flags.

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

Add kwargs to use the script with arguments.

Ideas:

--list-buckets
--upload
--help
--bucket and --key as options.