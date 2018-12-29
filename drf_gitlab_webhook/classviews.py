from rest_framework.views import APIView
from rest_framework.response import Response
from . import signals

EVENTS = {
    'Push Hook': signals.push_hook,
    'Tag Push Hook': signals.tag_push_hook,
    'Issue Hook': signals.issue_hook,
    'Note Hook': signals.note_hook,
    'Merge Request Hook': signals.merge_request_hook,
    'Wiki Page Hook': signals.wiki_page_hook,
    'Pipeline Hook': signals.pipeline_hook,
    'Build Hook': signals.build_hook,
}


def get_event_header(request):
    return request.META.get('HTTP_X_GITLAB_EVENT', b'')


class HookEvent(APIView):
    queryset = None
    permission_classes = ()

    def send_signals(self, request, _format=None):
        event = get_event_header(request)
        if event not in EVENTS:
            return Response({}, 404)
        EVENTS[event].send(sender=None, payload=request.data)
        return Response({}, 200)

    def get(self, request, _format=None):
        return self.send_signals(request, _format)

    def post(self, request, _format=None):
        return self.send_signals(request, _format)
