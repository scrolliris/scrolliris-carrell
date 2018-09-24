import pyramid.httpexceptions as exc
from pyramid.response import Response
from pyramid.view import (
    view_config,
    notfound_view_config
)


def tpl(filepath):
    return './templates/{0:s}.pt'.format(filepath)


# -- view

@notfound_view_config(renderer=tpl('404'),
                      append_slash=exc.HTTPMovedPermanently)
def notfound(request):
    request.response.status = 404
    return {}


@view_config(context=exc.HTTPInternalServerError, renderer='string')
def internal_server_error(req):
    body = 'Cannot {} {}'.format(req.method, req.path)
    return Response(body, status='500 Internal Server Error')


@view_config(route_name='index', renderer=tpl('index'),
             request_method='GET')
def index(_req):
    return dict()


def includeme(_):
    pass
