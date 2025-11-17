#  Copyright (c) 2025 by the OpenSR team
#  Permissions are hereby granted under the terms of the Apache 2.0 License:
#  https://opensource.org/license/apache-2-0.

from typing import Annotated

from pydantic import Field

from procodile import JobContext, ProcessRegistry

registry = ProcessRegistry()


@registry.process(
    id="generate_sr_product",
    title="Generate OpenSR Product",
)
def generate_sr_product(
    _ctx: JobContext,
    included_bands: Annotated[
        str, Field(title="Included bands")
    ] = "B03, B04, B05, B08",
    bbox: Annotated[
        tuple[float, float, float, float],
        Field(title="Spatial coverage", json_schema_extra=dict(format="bbox")),
    ] = (0, 40, 20, 60),
    pyramid_levels: Annotated[int, Field(title="Number of pyramid-levels", ge=1)] = 8,
    output_format: Annotated[
        str,
        Field(
            title="Output format",
            json_schema_extra=dict(enum=["GeoTIFF/COG", "Zarr v2", "Zarr v3"]),
        ),
    ] = "Zarr v3",
) -> str:
    """
    Generate a 2.5m Super-Resolution Product from Sentinel-2 L2A data.
    """

    # TODO: call actual SR-implementation here

    # Return a dummy result so the process inputs are use in some way
    if output_format == "GeoTIFF/COG":
        ext = "tif"
    else:
        ext = f"{'levels' if pyramid_levels > 1 else 'zarr'}"
    return f"opensr-test-{bbox}-{included_bands}-{pyramid_levels}.{ext}"


__all__ = [
    "generate_sr_product",
    "registry",
]
