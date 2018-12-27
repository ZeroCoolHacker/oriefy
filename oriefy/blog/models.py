from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Blog(models.Model):

    title   = models.CharField(_("Title"), max_length=70)
    text    = models.CharField(_("Text"), max_length=5000)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
