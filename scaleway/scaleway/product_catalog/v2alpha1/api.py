# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.utils import (
    fetch_all_pages,
)
from .types import (
    ListPublicCatalogProductsRequestProductType,
    ListPublicCatalogProductsResponse,
    PublicCatalogProduct,
)
from .marshalling import (
    unmarshal_ListPublicCatalogProductsResponse,
)


class ProductCatalogV2Alpha1PublicCatalogAPI(API):
    """ """

    def list_public_catalog_products(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        product_types: Optional[
            List[ListPublicCatalogProductsRequestProductType]
        ] = None,
    ) -> ListPublicCatalogProductsResponse:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :param product_types: The list of filtered product categories.
        :return: :class:`ListPublicCatalogProductsResponse <ListPublicCatalogProductsResponse>`

        Usage:
        ::

            result = api.list_public_catalog_products()
        """

        res = self._request(
            "GET",
            "/product-catalog/v2alpha1/public-catalog/products",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "product_types": product_types,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPublicCatalogProductsResponse(res.json())

    def list_public_catalog_products_all(
        self,
        *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        product_types: Optional[
            List[ListPublicCatalogProductsRequestProductType]
        ] = None,
    ) -> List[PublicCatalogProduct]:
        """
        List all available products.
        List all available products in the Scaleway catalog. Returns a complete list of products with their corresponding description, locations, prices and properties. You can define the `page` number and `page_size` for your query in the request.
        :param page: Number of the page. Value must be greater or equal to 1.
        :param page_size: The number of products per page. Value must be greater or equal to 1.
        :param product_types: The list of filtered product categories.
        :return: :class:`List[PublicCatalogProduct] <List[PublicCatalogProduct]>`

        Usage:
        ::

            result = api.list_public_catalog_products_all()
        """

        return fetch_all_pages(
            type=ListPublicCatalogProductsResponse,
            key="products",
            fetcher=self.list_public_catalog_products,
            args={
                "page": page,
                "page_size": page_size,
                "product_types": product_types,
            },
        )
