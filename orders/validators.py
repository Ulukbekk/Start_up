def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls', '.cdr', '.zip', '.dir', 'txt', '.rar']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')