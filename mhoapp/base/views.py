import os

from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    # Creates a URL for receiving images throught a POST request when using the TinyMCE Wysiwyg editor.
    # Docs: https://www.fatalerrors.org/a/0Nh20A.html
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({
                'message': 'Wrong file format',
                'error': True,
            })

        AWS_S3_ENDPOINT_URL = os.environ['AWS_S3_ENDPOINT_URL']
        MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/media/'    

        upload_time = timezone.now()
        path = os.path.join(
            MEDIA_URL,
            'tinymce',
            str(upload_time.year),
            str(upload_time.month),
            str(upload_time.day)
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, file_obj.name)

        file_url = f'{settings.MEDIA_URL}tinymce/{upload_time.year}/{upload_time.month}/{upload_time.day}/{file_obj.name}'

        if os.path.exists(file_path):
            return JsonResponse({
                'message': 'File already exist',
                'location': file_url,
                'error': True,
            })

        if file_obj.size > 1000001:
            return JsonResponse({
                'message': 'File size must be lower than 1MB',
                'location': file_url,
                'error': True,
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url,
            'error': False,
        })
    return JsonResponse({'detail': "Wrong request"})