from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for {{cookiecutter.project_name}}."""

    first_name = CharField("Имя", max_length=45, null=True, blank=True)
    last_name = CharField("Фамилия", max_length=100, null=True, blank=True)
    middle_name = CharField("Отчество", max_length=100, null=True, blank=True)
    location = CharField("Адрес проживания", max_length=150, null=True, blank=True)
    date_birthday = DateTimeField("Дата рождения", null=True, blank=True)
    city = CharField("Город", max_length=100, null=True, blank=True)
    country = CharField("Страна", max_length=100, null=True, blank=True)

    avatar = ImageField("Изображение профиля", upload_to="upload/images/", null=True, blank=True)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
