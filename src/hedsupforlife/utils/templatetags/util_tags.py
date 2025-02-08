from typing import Optional

from django import template
from django.db.models import Model
from django.http.request import QueryDict
from django.template.defaultfilters import slugify

register = template.Library()

MODE_ADD = "__add"
MODE_REMOVE = "__remove"
MODE_TOGGLE = "__toggle"


register = template.Library()


@register.simple_tag
def format_heading_id(text, id) -> str:
    """Generate Unique IDs for page headings"""
    # Get the first 8 characters of the ID
    truncated_id = id[:8]

    # Join slugified text and truncated ID
    formatted_text = f"{slugify(text)}-{truncated_id}"

    return formatted_text


# Table of contents
@register.filter(name="table_of_contents_array")
def table_of_contents_array(streamfield_content):
    h2_blocks = [
        (format_heading_id(block.value, block.id), block.value)
        for block in streamfield_content
        if block.block_type == "h2"
    ]

    return h2_blocks


@register.simple_tag(takes_context=True)
def querystring_modify(
    context, base=None, remove_blanks=False, remove_utm=True, **kwargs
):
    querydict = get_base_querydict(context, base)
    for key, value in kwargs.items():
        if isinstance(value, Model):
            value = str(value.pk)
        elif not hasattr(value, "__iter__"):
            value = str(value)

        if key.endswith(MODE_TOGGLE):
            key = key[: -len(MODE_TOGGLE)]
            values = set(querydict.getlist(key))  # type:ignore reportGeneralTypeIssues
            if value in values:
                values.remove(value)
            else:
                values.add(value)
                querydict.setlist(key, list(values))

        elif key.endswith(MODE_ADD):
            key = key[: -len(MODE_ADD)]
            values = set(querydict.getlist(key))  # type:ignore reportGeneralTypeIssues
            if value not in values:
                values.add(value)
                querydict.setlist(key, list(values))

        elif key.endswith(MODE_REMOVE):
            key = key[: -len(MODE_REMOVE)]
            values = set(querydict.getlist(key))  # type:ignore reportGeneralTypeIssues
            if value in values:
                values.remove(value)
                assert hasattr(querydict, "set_list")
                querydict.setlist(key, list(values))

        elif value is None:
            querydict.pop(key, None)
        else:
            if isinstance(value, (str, bytes)):
                querydict[key] = value
            elif hasattr(value, "__iter__") and hasattr(querydict, "setlist"):
                querydict.setlist(key, list(value))

    clean_querydict(querydict, remove_blanks, remove_utm)

    return f"?{querydict.urlencode()}"


def get_base_querydict(context, base):
    if base is None and "request" in context:
        return context["request"].GET.copy()
    if isinstance(base, QueryDict):
        return base.copy()
    if isinstance(base, dict):
        return QueryDict.fromkeys(base, mutable=True)
    if isinstance(base, str):
        return QueryDict(base, mutable=True)
    # request not present or base value unsupported
    return QueryDict("", mutable=True)


def clean_querydict(querydict, remove_blanks=False, remove_utm=True):
    remove_vals: set[Optional[str]] = {None}

    if remove_blanks:
        remove_vals.add("")

    if remove_utm:
        for key in querydict.keys():
            if key.lower().startswith("utm_"):
                querydict.pop(key)

    for key, values in querydict.lists():
        cleaned_values = [v for v in values if v not in remove_vals]
        if cleaned_values:
            querydict.setlist(key, cleaned_values)
        else:
            del querydict[key]
