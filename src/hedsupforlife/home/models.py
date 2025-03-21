from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.search import index

from hedsupforlife.utils.blocks import InternalLinkBlock, StoryBlock
from hedsupforlife.utils.models import BasePage


class HomePage(BasePage):
    template = "pages/home_page.html"
    introduction = models.TextField(blank=True)
    hero_cta = StreamField(
        [("link", InternalLinkBlock())],
        blank=True,
        min_num=0,
        max_num=1,
        use_json_field=True,
    )
    body = StreamField(StoryBlock(), use_json_field=True)
    search_fields = BasePage.search_fields + [index.SearchField("introduction")]

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("hero_cta"),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                InlinePanel(
                    "page_related_pages",
                    label="Pages",
                    max_num=12,
                ),
            ],
        ),
    ]
