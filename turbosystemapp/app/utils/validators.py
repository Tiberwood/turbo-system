import os

def validate_file_extension(value):
  ext = os.path.splitext(value)[1]
  valid_extensions = ['.pdf','.doc','.docx']
  if not ext in valid_extensions:
    raise ValidationError(u'Unsupported file extension.')
  return True