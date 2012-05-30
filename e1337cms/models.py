from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    title = models.CharField(_('title'), max_length=250)
    slug = models.SlugField(_('slug'), max_length=200)
    content = models.TextField(_('content'))
    published = models.BooleanField(_("is published"), blank=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                                related_name='children', db_index=True,
                                verbose_name=_('parent'))

    creation_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['creation_date']
        verbose_name = _('page')
        verbose_name_plural = _('pages')
