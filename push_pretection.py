import boto3

# Hardcoded AWS credentials (vulnerable practice)
aws_access_key_id = "AKIAEXAMPLEACCESSKEY"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Create an S3 client using the hardcoded credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# List buckets as an example action
buckets = s3_client.list_buckets()
print("Buckets:", [bucket['Name'] for bucket in buckets['Buckets']])

