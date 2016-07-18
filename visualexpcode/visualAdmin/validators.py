import os
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_sound_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ogg','.oga', '.mp3', '.flac', '.aac', '.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError(excep_message(valid_extensions))

def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ogg','.ogv', '.mkv', '.mp4', '.flv', '.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError(excep_message(valid_extensions))

def excep_message(valid_extensions):
    msg = _('Format de fichier non supporté, veuillez utiliser un des formats suivants : ')
    for ext in valid_extensions:
        msg+= ext + ', '

    return msg[:-2] #remove last comma and space from string