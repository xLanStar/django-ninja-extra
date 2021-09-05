from typing import Any, cast
from django.apps import apps
from injector import Injector

__all__ = ['resolve_container_services']


def resolve_container_services(*services):
    assert services, 'Service can not be empty'

    injector: Injector = Injector()
    app = cast(Any, apps.get_app_config('django_injector'))
    if app and app.injector:
        injector = app.injector

    if len(services) > 1:
        services_resolved = []
        for service in services:
            services_resolved.append(injector.get(service))
        return tuple(services_resolved)
    return injector.get(services[0])