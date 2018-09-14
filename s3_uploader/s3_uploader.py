import json
import logging
import boto3
import os
import base64
from requests_toolbelt.multipart import decoder
import settings
import utils
import uuid


def lambda_handler(event, context):
    event_keys = event.keys()

    if 'body-json' in event_keys and 'params' in event_keys:
        body_data = event['body-json']
        params = event['params']
    else:
        return {
            "message": "Body content is not in format."
        }

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(settings.BUCKET_NAME)

    multipart_string = base64.b64decode(body_data)
    content_type = params['header']['content-type']
    decoded_parts = decoder.MultipartDecoder(multipart_string, content_type)
    for part in decoded_parts.parts:
        filename = utils.get_filename(part.headers)
        filename, file_extension = os.path.splitext(filename)
        key = settings.FOLDER + '/' + filename + '-' + \
            str(uuid.uuid4()) + file_extension
        bucket.put_object(Key=key, Body=part.content)

    return {
        "message": "Success!"
    }
