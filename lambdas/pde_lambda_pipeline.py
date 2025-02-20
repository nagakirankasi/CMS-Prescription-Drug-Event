import boto3
import pandas as pd
import json
import os
import logging

# Initialize AWS clients
s3 = boto3.client('s3')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables
SCHEMA_BUCKET = os.environ['SCHEMA_BUCKET']
SCHEMA_KEY = os.environ['SCHEMA_KEY']
OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

# Load schema from S3
def load_schema():
    try:
        response = s3.get_object(Bucket=SCHEMA_BUCKET, Key=SCHEMA_KEY)
        schema = json.loads(response['Body'].read().decode('utf-8'))
        return schema['fields']
    except Exception as e:
        logger.error(f"Failed to load schema: {str(e)}")
        raise

# Process PDE file
def process_pde_file(bucket, key):
    try:
        # Download file from S3
        s3.download_file(bucket, key, '/tmp/input_pde.txt')
        schema = load_schema()
        column_names = [field['name'] for field in schema]
        dtypes = {field['name']: field['type'] for field in schema}

        # Read file using schema
        df = pd.read_csv('/tmp/input_pde.txt', sep='|', names=column_names, dtype=str)

        # Data transformations
        if 'Claim_Amount' in df.columns:
            df['Claim_Amount'] = pd.to_numeric(df['Claim_Amount'], errors='coerce')

        # Save processed file to Parquet
        output_key = key.replace('raw/', 'processed/').replace('.txt', '.parquet')
        output_path = f'/tmp/{output_key.split("/")[-1]}'
        df.to_parquet(output_path, index=False)

        # Upload to S3
        s3.upload_file(output_path, OUTPUT_BUCKET, output_key)
        logger.info(f"Successfully processed and uploaded: {output_key}")

    except Exception as e:
        logger.error(f"Failed to process PDE file {key}: {str(e)}")
        raise

# Lambda handler
def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        logger.info(f"Processing file: {key} from bucket: {bucket}")
        process_pde_file(bucket, key)

    return {'statusCode': 200, 'body': 'PDE processing complete.'}
