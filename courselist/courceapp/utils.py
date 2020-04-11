import logging

import boto3
from django.conf import settings
from rest_framework import serializers

logger = logging.getLogger(__name__)
valid_image_formats = ['image/jpeg', 'image/jpg', 'image/png']


def validate_image(image):
    """
    Validates Image , checks format and Size
    Size should be less than 5 MB
    Args:
        image:  Image to validate
    Returns: Boolean

    """
    if not image:
        raise serializers.ValidationError({'message': 'Image not found'})

    if not image.size < 5000000:
        raise serializers.ValidationError({'message': 'File Size should less than 5 MB'})
    if image.content_type not in valid_image_formats:
        raise serializers.ValidationError({'message': 'File should be jpg , jpeg or png only'})

    return True


def upload_to_s3(bucketname, file, filename):
    """
       Upload any file to s3 bucket
       :param bucketname: Bucket to upload the file
       :param file: file to be upload
       :param filename: Name of the file to be stored on S3.
       :return: Uploaded file URL
       """

    try:
        s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        bucket = s3.Bucket(bucketname)
        bucket.put_object(Key=filename, Body=file)
        return "https://" + bucketname + ".s3.amazonaws.com/" + filename


    except Exception as error:
        logger.exception(error)
        raise serializers.ValidationError({'message': 'Something bad happened'})
