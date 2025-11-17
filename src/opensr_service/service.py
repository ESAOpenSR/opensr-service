#  Copyright (c) 2025 by the OpenSR team
#  Permissions are hereby granted under the terms of the Apache 2.0 License:
#  https://opensource.org/license/apache-2-0.

from wraptile.services.local import LocalService

from .processes import registry

service = LocalService("OpenSR Service", process_registry=registry)

__all__ = ["service"]
