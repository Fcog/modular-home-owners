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

        upload_time = timezone.now()

        path = os.path.join(
            settings.MEDIA_ROOT if settings.DEVELOPMENT_MODE is True else settings.MEDIA_URL,
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

        if settings.DEVELOPMENT_MODE is True:
            with open(file_path, 'wb+') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
        else:            
            from custom_storages import MediaStorage
            media_storage = MediaStorage()
            if not media_storage.exists(file_path): # avoid overwriting existing file
                media_storage.save(file_path, file_obj)
                file_url = media_storage.url(file_path)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url,
            'error': False,
        })
    return JsonResponse({'detail': "Wrong request"})