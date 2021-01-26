from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class Assignment(models.Model):
    description = models.CharField(_('Assignment description'), max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')


class Hint(models.Model):
    description = models.CharField(_('Hint description'), max_length=2000)
    assignment =  models.ForeignKey(Assignment, related_name='assignment_hints', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Hint')
        verbose_name_plural = _('Hints')
