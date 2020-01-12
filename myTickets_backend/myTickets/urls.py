from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

from myTickets.views import *

schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version='v1'
    ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country/list', country_list),
    path('country/create', country_create),
    path('country/delete', country_delete),
    path('company/list', company_list),
    path('company/create', company_create),
    path('company/delete', company_delete),
    path('person/list', person_list),
    path('person/create', person_create),
    path('person/delete', person_delete),
    path('ticket/list', ticket_list),
    path('ticket/create', ticket_create),
    path('ticket/delete', ticket_delete),

    path('person/<int:pk>/get', person_get),
    path('person/<int:pk>/update', person_update),
    path('person/<int:pk>/delete', person_delete),
    path('ticket/<int:pk>/get', ticket_get),
    path('ticket/<int:pk>/update', ticket_update),
    path('ticket/<int:pk>/delete', ticket_delete),

    path('personvalidation/<slug:firstname>/<slug:lastname>', personal_validate),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^api-token-auth/', obtain_jwt_token),
]