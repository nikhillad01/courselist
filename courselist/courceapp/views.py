import logging
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer
from .utils import upload_to_s3, validate_image

# instance of a logger
logger = logging.getLogger(__name__)


class CoursesViewset(ModelViewSet):
    """
       Modelviewset to perform all CRUD operations on Course model
    """
    http_method_names = ['head', 'options', 'get', 'post', 'patch', 'delete']
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer

    def get_queryset(self):
        try:
            return Course.objects.filter(is_deleted=False)
        except (ValueError, AttributeError):
            return Response({'message': 'Courses not found'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            logger.exception('Object not exists', ObjectDoesNotExist)
            return Response({'message': 'No courses exists for this id.'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        img = request.FILES.get("img", None)

        if validate_image(img):
            img_src = upload_to_s3(settings.S3_BUCKET_NAME, img, img.name)
            request.data['image_src'] = img_src
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Please provide image'
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Handles Patch request
        Uploads image to s3 and replaces s3 image url if image provided
        """
        try:
            course_instance = Course.objects.get(id=self.kwargs.get('pk', 0))
        except ObjectDoesNotExist:
            return Response({'message': 'No record found for this id.'}, status=status.HTTP_400_BAD_REQUEST)

        request_data = self.request.data

        if hasattr(request_data, '_mutable'):  # makes QueryDict mutable
            request_data._mutable = True

        request_data['updated_at'] = datetime.now(tz=timezone.utc)
        img = request.FILES.get("img", None)

        if img and validate_image(img):
            img_src = upload_to_s3(settings.S3_BUCKET_NAME, img, img.name)
            request_data['image_src'] = img_src

        serializer = CourseSerializer(instance=course_instance, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        Soft delete method , makes  Flag is_delete = True instead of deleting the object
        Args:
            **kwargs: Id of object

        Returns: Empty response with Status 204

        """
        try:
            course_instance = Course.objects.get(id=self.kwargs.get('pk', 0))
            if not course_instance.is_deleted:
                course_instance.is_deleted = True
                course_instance.deleted_at = datetime.now(tz=timezone.utc)
                course_instance.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'Already Deleted'}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            logger.exception('Object not exists', ObjectDoesNotExist)
            return Response({'message': 'No record found of this id.'}, status=status.HTTP_400_BAD_REQUEST)
