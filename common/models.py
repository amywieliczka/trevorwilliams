from django.db import models
from autoslug import AutoSlugField
from positions.fields import PositionField
# Create your models here.

FORMAT_CHOICES = (
    ('html', 'html'), 
    ('markdown', 'markdown')
)

TARGET_CHOICES = (
    ('_blank', '_blank'),
    ('_self', '_self'), 
    ('_top', '_top'), 
    ('_parent', '_parent')
)

class Navigation(models.Model):
    title = models.CharField(max_length=255, help_text='Navigation and default page title')
    slug = AutoSlugField(blank=True, editable=True, populate_from='title')
    order = PositionField()
    url = models.CharField(max_length=255, blank=True, default='', help_text='eg. link somewhere else http://life.com or /life/page/')
    target = models.CharField(max_length=255, blank=True, default='', help_text='eg. open link in "_blank" window', choices=TARGET_CHOICES)
    page_title = models.CharField(max_length=255, blank=True, default='', help_text='Optional html title')
    text = models.TextField(blank=True, default='')
    format = models.CharField(max_length=255, blank=True, default='', choices=FORMAT_CHOICES)
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Navigation'
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if self.url:
            return self.url
        return mark_safe('/%s/' % slug)