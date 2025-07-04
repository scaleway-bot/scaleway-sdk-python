# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Any, Awaitable, Dict, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    marshal_Money,
    unmarshal_Money,
    marshal_ScwFile,
    unmarshal_ScwFile,
    unmarshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    WaitForOptions,
    project_or_organization_id,
    random_name,
    resolve_one_of,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    ListPublicCatalogProductsRequestProductType,
    PublicCatalogProductPropertiesHardwareCPUArch,
    PublicCatalogProductStatus,
    PublicCatalogProductUnitOfMeasureCountableUnit,
    ListPublicCatalogProductsResponse,
    PublicCatalogApiListPublicCatalogProductsRequest,
    PublicCatalogProduct,
    PublicCatalogProductEnvironmentalImpactEstimation,
    PublicCatalogProductLocality,
    PublicCatalogProductPrice,
    PublicCatalogProductProperties,
    PublicCatalogProductPropertiesAppleSilicon,
    PublicCatalogProductPropertiesDedibox,
    PublicCatalogProductPropertiesElasticMetal,
    PublicCatalogProductPropertiesHardware,
    PublicCatalogProductPropertiesHardwareCPU,
    PublicCatalogProductPropertiesHardwareCPUPhysical,
    PublicCatalogProductPropertiesHardwareCPUVirtual,
    PublicCatalogProductPropertiesHardwareGPU,
    PublicCatalogProductPropertiesHardwareNetwork,
    PublicCatalogProductPropertiesHardwareRAM,
    PublicCatalogProductPropertiesHardwareStorage,
    PublicCatalogProductPropertiesInstance,
    PublicCatalogProductUnitOfMeasure,
)
from .marshalling import (
    unmarshal_ListPublicCatalogProductsResponse,
)

class ProductCatalogV2Alpha1PublicCatalogAPI(API):
    """
    
    """
    def list_public_catalog_products(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        product_types: Optional[List[ListPublicCatalogProductsRequestProductType]] = None,
        global_: Optional[bool] = None,
        region: Optional[ScwRegion] = None,
        zone: Optional[ScwZone] = None,
        datacenter: Optional[str] = None,
    ) -> ListPublicCatalogProductsResponse:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :param product_types: The list of filtered product categories.
        :param global_: Filter global products.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param region: Filter products by region.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param zone: Filter products by zone.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param datacenter: Filter products by datacenter.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :return: :class:`ListPublicCatalogProductsResponse <ListPublicCatalogProductsResponse>`
        
        Usage:
        ::
        
            result = api.list_public_catalog_products()
        """
        
        
        res = self._request(
            "GET",
            f"/product-catalog/v2alpha1/public-catalog/products",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "product_types": product_types,
                **resolve_one_of([
                    OneOfPossibility("datacenter", datacenter),
                    OneOfPossibility("global_", global_),
                    OneOfPossibility("region", region),
                    OneOfPossibility("zone", zone),
                ]),
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPublicCatalogProductsResponse(res.json())
        
    def list_public_catalog_products_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        product_types: Optional[List[ListPublicCatalogProductsRequestProductType]] = None,
        global_: Optional[bool] = None,
        region: Optional[ScwRegion] = None,
        zone: Optional[ScwZone] = None,
        datacenter: Optional[str] = None,
    ) -> List[PublicCatalogProduct]:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :param product_types: The list of filtered product categories.
        :param global_: Filter global products.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param region: Filter products by region.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param zone: Filter products by zone.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :param datacenter: Filter products by datacenter.
        One-Of ('locality'): at most one of 'global_', 'region', 'zone', 'datacenter' could be set.
        :return: :class:`List[PublicCatalogProduct] <List[PublicCatalogProduct]>`
        
        Usage:
        ::
        
            result = api.list_public_catalog_products_all()
        """

        return  fetch_all_pages(
            type=ListPublicCatalogProductsResponse,
            key="products",
            fetcher=self.list_public_catalog_products,
            args={
                "page": page,
                "page_size": page_size,
                "product_types": product_types,
                "global_": global_,
                "region": region,
                "zone": zone,
                "datacenter": datacenter,
            },
        )
        
