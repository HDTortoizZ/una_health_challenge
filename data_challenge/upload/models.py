from django.db import models


class Upload(models.Model):
    # The media root should be set with an uploads directory that this type of model and save files to.
    # As I understand it, saving files to a directory rather than the database is standard because of performance
    # issues.
    file = models.FileField(upload_to='uploads/')
