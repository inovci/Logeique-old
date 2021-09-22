import os
from django.core.files.storage import FileSystemStorage
import base64
from django.conf import settings

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"


def save_temp_profile_image_from_base64String(imageString, user):
    INCORRECT_PADDING_EXCEPTION = "Incorrect padding"
    try:
        if not os.path.exists(settings.MEDIA_ROOT):
            os.mkdir(settings.MEDIA_ROOT)
        if not os.path.exists(f"{settings.MEDIA_ROOT}/{user.id}"):
            os.mkdir(f"{settings.MEDIA_ROOT}/{user.id}")
        url = os.path.join(
            f"{settings.MEDIA_ROOT}/{user.id}", TEMP_PROFILE_IMAGE_NAME)
        storage = FileSystemStorage(location=url)
        image = base64.b64decode(imageString)
        with storage.open('', 'wb+') as destination:
            destination.write(image)
            destination.close()
        return url
    except Exception as e:
        if str(e) == INCORRECT_PADDING_EXCEPTION:
            imageString += "=" * ((4 - len(imageString) % 4) % 4)
            return save_temp_profile_image_from_base64String(imageString, user)
    return None
