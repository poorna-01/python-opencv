import csv
import boto3




photo = 'image.jpg'

client = boto3.client('rekognition')

with open(photo,'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes': source_bytes})
print(response)