from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image

def validate_image(image):
    file_size = image.file.size
    limit_kb = 10240  # Set the limit for file size (in KB)
    if file_size > limit_kb * 1024:
        raise ValidationError(_('Image file too large ( > %(limit_value)sKB )'), params={'limit_value': limit_kb})
    
    try:
        img = Image.open(image)
        img.verify()  # Verify that this is an image
    except (IOError, SyntaxError):
        raise ValidationError(_('Invalid image'))
    
    # Check for image formats
    valid_formats = ['JPEG', 'JPG', 'PNG', 'WEBP', "GIF", "SVG", "BMP", "ICO", "AVIF"] 
    if img.format not in valid_formats:
        raise ValidationError(_('Unsupported file extension. Allowed extensions are: %(valid_formats)s'), params={'valid_formats': ', '.join(valid_formats)})
