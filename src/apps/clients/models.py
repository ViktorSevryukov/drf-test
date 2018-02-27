import os
import uuid
from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


def upload_photo(instance, filename):
    """
    Get path for load photo
    :param instance:
    :param filename:
    :return:
    """
    ext = filename.split(".")[-1]
    new_filename = '{name}.{ext}'.format(name=str(uuid.uuid4()), ext=ext)
    return os.path.join('clients', 'photo', new_filename)


class Client(TimeStampedModel):
    """
    Client info
    """
    MAX_RATING = 10

    first_name = models.CharField(_("first name"), default='', max_length=32)
    last_name = models.CharField(_("last name"), default='', max_length=32)
    birth_date = models.DateField(_("birth date"), default=None)
    photo = models.ImageField(_("photo"), upload_to=upload_photo, null=True,
                              blank=True)
    rating = models.PositiveSmallIntegerField(
        _("rating"),
        default=0,
        validators=[MaxValueValidator(MAX_RATING), MinValueValidator(0)]
    )

    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Get client's full name
        """
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def age(self):
        """
        Get client's age
        """
        today = date.today()
        years_diff = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years_diff -= 1
        return years_diff
