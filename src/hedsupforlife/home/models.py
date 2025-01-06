from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page


class HomePage(Page):
    welcome = models.CharField(
        verbose_name="welcome",
        max_length=100,
    )

    content_panels = Page.content_panels + [
        FieldPanel("welcome"),
    ]
