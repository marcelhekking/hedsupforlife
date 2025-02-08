from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    hoofd_pagina_afbeelding = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hoofdpagina_welkom_tekst = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("hoofd_pagina_afbeelding"),
        FieldPanel("hoofdpagina_welkom_tekst"),
    ]
