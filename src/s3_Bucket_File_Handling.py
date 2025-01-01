import boto3
from src.getCreds import getCreds

config = getCreds.get_creds()

# Creating Client
s3 = boto3.client('s3', region_name=config['creds']['region_name'],   
                  aws_access_key_id=config['creds']['aws_access_key_id'],   
                  aws_secret_access_key=config['creds']['aws_secret_access_key'])


#s3.upload_file()
s3.upload_file(Filename='gid_requests_2019_01_01.csv', 
               Bucket='gid-requests',   
               Key='gid_requests_2019_01_01.csv')



#s3.list_objects()
response = s3.list_objects(Bucket='gid-requests', 
                           MaxKeys=2,  
                           Prefix='gid_requests_2019_')
print(response)

#s3.head_object() --> object metadata
response = s3.head_object(  
    Bucket='gid-requests',   
    Key='gid_requests_2018_12_30.csv')
print(response)

#s3.download_file()
s3.download_file(  
    Filename='gid_requests_downed.csv',  
    Bucket='gid-requests',   
    Key='gid_requests_2018_12_30.csv')

#s3.delete_object()
s3.delete_object(  
    Bucket='gid-requests',   
    Key='gid_requests_2018_12_30.csv')

