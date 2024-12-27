'''AWS S3 bucket storage and the Boto3 client to manage files programmatically in the cloud. By leveraging IAM roles, the implementation ensures secure and controlled access to S3 resources, enabling robust file handling workflows.

Key Highlights:
S3 Bucket Setup:
Creation and configuration of S3 buckets for cloud storage.
Implementation of bucket policies and permissions to manage access.

IAM Role for Security:
Configuration of an IAM role with specific permissions for accessing S3 buckets.
Attaching the role to resources (e.g., EC2 instances) or using temporary credentials for enhanced security.

Boto3 S3 Client Methods:
File Uploads: upload_file() and put_object() for adding files to S3.
File Downloads: download_file() for retrieving files.
File Management: Listing files (list_objects_v2), deleting files (delete_object), and generating pre-signed URLs for secure temporary access.
Metadata Handling: Reading and writing object metadata using Boto3.

Automation with Python:
Writing Python scripts to automate file transfers and management tasks.
Error handling and logging to ensure resilience and traceability.

Outcome:
The project equips users with the skills to:
Securely manage files in AWS S3 using the Python Boto3 client.
Configure and utilize IAM roles for access control.
Implement efficient, automated workflows for cloud-based file storage and retrieval.'''

import boto3
import json


with open("../config.json",'r') as f:
    config = json.load(f)

print(config)
# Creating Client
s3 = boto3.client('s3', region_name=config['creds']['region_name'],   
                  aws_access_key_id=config['creds']['aws_access_key_id'],   
                  aws_secret_access_key=config['creds']['aws_secret_access_key'])


#s3.upload_file()
s3.upload_file(Filename='gid_requests_2019_01_01.csv', 
               Bucket='gid-requests',   
               Key='gid_requests_2019_01_01.csv')

#s3.list_objects()
#s3.head_object()
#s3.download_file()
#s3.delete_object()
