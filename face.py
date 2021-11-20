import csv
import boto3




photo = 'jana.jpg'

client = boto3.client('rekognition')

with open(photo,'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_faces(Image={'Bytes': source_bytes} , Attributes=['ALL'])
print(response)