# pylint: disable=C0103
from django.dispatch import Signal

push_hook = Signal(providing_args=['payload'])
tag_push_hook = Signal(providing_args=['payload'])
issue_hook = Signal(providing_args=['payload'])
note_hook = Signal(providing_args=['payload'])
merge_request_hook = Signal(providing_args=['payload'])
wiki_page_hook = Signal(providing_args=['payload'])
pipeline_hook = Signal(providing_args=['payload'])
build_hook = Signal(providing_args=['payload'])
