from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_date = models.DateTimeField(db_index=True, default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TaggedObjectType(models.TextChoices):
    bookmark = 'bookmark', 'bookmark'
    note = 'note', 'note'


class TaggedItem(BaseModel):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    tagged_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag


class Bookmark(BaseModel):
    uri = models.URLField()
    tags = GenericRelation(TaggedItem, related_name='bookmark')

    def __str__(self):
        return self.uri


class Note(BaseModel):
    text = models.CharField(max_length=100)
    tags = GenericRelation(TaggedItem, related_name='note')

    def __str__(self):
        return self.text
