import uuid
from django.db import models

# Create your models here.


class StorageUnit(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    row_count = models.IntegerField()
    column_count = models.IntegerField()

    def __str__(self):
        return self.name


class StorageItem(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    row_index = models.IntegerField()
    column_index = models.IntegerField()

    storage_unit = models.ForeignKey(StorageUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
