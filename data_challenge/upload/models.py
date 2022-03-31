from django.db import models


class Upload(models.Model):
    # The media root should be set with an uploads directory that this type of model and save files to.
    # As I understand it, saving files to a directory rather than the database is standard because of performance
    # issues.
    file = models.FileField(upload_to='uploads/')


class GlucoseLevels(models.Model):
    user_id = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    glucose_value_history = models.IntegerField()
    glucose_levels = models.IntegerField()
