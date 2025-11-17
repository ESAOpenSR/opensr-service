from wraptile.services.local import LocalService

from .processes import registry

service = LocalService("OpenSR Service", process_registry=registry)

__all__ = ["service"]
