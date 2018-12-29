# drf-gitlab-webhook

drf-gitlab-webhook is a django app wich implements a webhook endpoint
for gitlab requests and send django signals for every hook event.

## Quick start

1. Add "drf_gitlab_webhook" to INSTALLED_APPS:

```
INSTALLED_APPS = {
  ...
  'drf_gitlab_webhook'
}
```

2. Include the drf_gitlab_webhook URLconf in urls.py:

```
url(r'^webhook/', include('drf_gitlab_webhook.urls'))
```

3. Then you have an endpoint called `webhook/event/`

_Dev notes:_
build package: python setup.py sdist
install: pip install --user drf-gitlab-webhook/dist/drf-gitlab-webhook-01.tar.gz
