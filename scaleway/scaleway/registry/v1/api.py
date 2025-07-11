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
    ImageStatus,
    ImageVisibility,
    ListImagesRequestOrderBy,
    ListNamespacesRequestOrderBy,
    ListTagsRequestOrderBy,
    NamespaceStatus,
    TagStatus,
    CreateNamespaceRequest,
    DeleteImageRequest,
    DeleteNamespaceRequest,
    DeleteTagRequest,
    GetImageRequest,
    GetNamespaceRequest,
    GetTagRequest,
    Image,
    ListImagesRequest,
    ListImagesResponse,
    ListNamespacesRequest,
    ListNamespacesResponse,
    ListTagsRequest,
    ListTagsResponse,
    Namespace,
    Tag,
    UpdateImageRequest,
    UpdateNamespaceRequest,
)
from .content import (
    IMAGE_TRANSIENT_STATUSES,
    NAMESPACE_TRANSIENT_STATUSES,
    TAG_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_Image,
    unmarshal_Namespace,
    unmarshal_Tag,
    unmarshal_ListImagesResponse,
    unmarshal_ListNamespacesResponse,
    unmarshal_ListTagsResponse,
    marshal_CreateNamespaceRequest,
    marshal_UpdateImageRequest,
    marshal_UpdateNamespaceRequest,
)

class RegistryV1API(API):
    """
    This API allows you to manage your Container Registry resources.
    """
    def list_namespaces(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListNamespacesResponse:
        """
        List namespaces.
        List all namespaces in a specified region. By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `instance_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :param name: Filter by the namespace name (exact match).
        :return: :class:`ListNamespacesResponse <ListNamespacesResponse>`
        
        Usage:
        ::
        
            result = api.list_namespaces()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/namespaces",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNamespacesResponse(res.json())
        
    def list_namespaces_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNamespacesRequestOrderBy] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Namespace]:
        """
        List namespaces.
        List all namespaces in a specified region. By default, the namespaces listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `instance_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering namespace listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :param name: Filter by the namespace name (exact match).
        :return: :class:`List[Namespace] <List[Namespace]>`
        
        Usage:
        ::
        
            result = api.list_namespaces_all()
        """

        return  fetch_all_pages(
            type=ListNamespacesResponse,
            key="namespaces",
            fetcher=self.list_namespaces,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name,
            },
        )
        
    def get_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Namespace:
        """
        Get a namespace.
        Retrieve information about a given namespace, specified by its `namespace_id` and region. Full details about the namespace, such as `description`, `project_id`, `status`, `endpoint`, `is_public`, `size`, and `image_count` are returned in the response.
        :param namespace_id: UUID of the namespace.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`
        
        Usage:
        ::
        
            result = api.get_namespace(
                namespace_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_namespace_id = validate_path_param("namespace_id", namespace_id)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())
        
    def wait_for_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Namespace, bool]] = None,
    ) -> Namespace:
        """
        Get a namespace.
        Retrieve information about a given namespace, specified by its `namespace_id` and region. Full details about the namespace, such as `description`, `project_id`, `status`, `endpoint`, `is_public`, `size`, and `image_count` are returned in the response.
        :param namespace_id: UUID of the namespace.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`
        
        Usage:
        ::
        
            result = api.get_namespace(
                namespace_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in NAMESPACE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_namespace,
            options=options,
            args={
                "namespace_id": namespace_id,
                "region": region,
            },
        )
        
    def create_namespace(
        self,
        *,
        description: str,
        is_public: bool,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> Namespace:
        """
        Create a namespace.
        Create a new Container Registry namespace. You must specify the namespace name and region in which you want it to be created. Optionally, you can specify the `project_id` and `is_public` in the request payload.
        :param description: Description of the namespace.
        :param is_public: Defines whether or not namespace is public.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the namespace.
        :param organization_id: Namespace owner (deprecated).
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :param project_id: Project ID on which the namespace will be created.
        One-Of ('project_identifier'): at most one of 'project_id', 'organization_id' could be set.
        :return: :class:`Namespace <Namespace>`
        
        Usage:
        ::
        
            result = api.create_namespace(
                description="example",
                is_public=False,
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/registry/v1/regions/{param_region}/namespaces",
            body=marshal_CreateNamespaceRequest(
                CreateNamespaceRequest(
                    description=description,
                    is_public=is_public,
                    region=region,
                    name=name or random_name(prefix="ns"),
                    project_id=project_id,
                    organization_id=organization_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())
        
    def update_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        is_public: Optional[bool] = None,
    ) -> Namespace:
        """
        Update a namespace.
        Update the parameters of a given namespace, specified by its `namespace_id` and `region`. You can update the `description` and `is_public` parameters.
        :param namespace_id: ID of the namespace to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Namespace description.
        :param is_public: Defines whether or not the namespace is public.
        :return: :class:`Namespace <Namespace>`
        
        Usage:
        ::
        
            result = api.update_namespace(
                namespace_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_namespace_id = validate_path_param("namespace_id", namespace_id)
        
        res = self._request(
            "PATCH",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
            body=marshal_UpdateNamespaceRequest(
                UpdateNamespaceRequest(
                    namespace_id=namespace_id,
                    region=region,
                    description=description,
                    is_public=is_public,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())
        
    def delete_namespace(
        self,
        *,
        namespace_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Namespace:
        """
        Delete a namespace.
        Delete a given namespace. You must specify, in the endpoint, the `region` and `namespace_id` parameters of the namespace you want to delete.
        :param namespace_id: UUID of the namespace.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Namespace <Namespace>`
        
        Usage:
        ::
        
            result = api.delete_namespace(
                namespace_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_namespace_id = validate_path_param("namespace_id", namespace_id)
        
        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/namespaces/{param_namespace_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Namespace(res.json())
        
    def list_images(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListImagesRequestOrderBy] = None,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListImagesResponse:
        """
        List images.
        List all images in a specified region. By default, the images listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `namespace_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param namespace_id: Filter by the namespace ID.
        :param name: Filter by the image name (exact match).
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :return: :class:`ListImagesResponse <ListImagesResponse>`
        
        Usage:
        ::
        
            result = api.list_images()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images",
            params={
                "name": name,
                "namespace_id": namespace_id,
                "order_by": order_by,
                "organization_id": organization_id or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListImagesResponse(res.json())
        
    def list_images_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListImagesRequestOrderBy] = None,
        namespace_id: Optional[str] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[Image]:
        """
        List images.
        List all images in a specified region. By default, the images listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `namespace_id` and `project_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering image listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param namespace_id: Filter by the namespace ID.
        :param name: Filter by the image name (exact match).
        :param organization_id: Filter by Organization ID.
        :param project_id: Filter by Project ID.
        :return: :class:`List[Image] <List[Image]>`
        
        Usage:
        ::
        
            result = api.list_images_all()
        """

        return  fetch_all_pages(
            type=ListImagesResponse,
            key="images",
            fetcher=self.list_images,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "namespace_id": namespace_id,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )
        
    def get_image(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Image:
        """
        Get an image.
        Retrieve information about a given container image, specified by its `image_id` and region. Full details about the image, such as `name`, `namespace_id`, `status`, `visibility`, and `size` are returned in the response.
        :param image_id: UUID of the image.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Image <Image>`
        
        Usage:
        ::
        
            result = api.get_image(
                image_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_image_id = validate_path_param("image_id", image_id)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())
        
    def wait_for_image(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Image, bool]] = None,
    ) -> Image:
        """
        Get an image.
        Retrieve information about a given container image, specified by its `image_id` and region. Full details about the image, such as `name`, `namespace_id`, `status`, `visibility`, and `size` are returned in the response.
        :param image_id: UUID of the image.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Image <Image>`
        
        Usage:
        ::
        
            result = api.get_image(
                image_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in IMAGE_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_image,
            options=options,
            args={
                "image_id": image_id,
                "region": region,
            },
        )
        
    def update_image(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
        visibility: Optional[ImageVisibility] = None,
    ) -> Image:
        """
        Update an image.
        Update the parameters of a given image, specified by its `image_id` and `region`. You can update the `visibility` parameter.
        :param image_id: ID of the image to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param visibility: Set to `public` to allow the image to be pulled without authentication. Else, set to  `private`. Set to `inherit` to keep the same visibility configuration as the namespace.
        :return: :class:`Image <Image>`
        
        Usage:
        ::
        
            result = api.update_image(
                image_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_image_id = validate_path_param("image_id", image_id)
        
        res = self._request(
            "PATCH",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
            body=marshal_UpdateImageRequest(
                UpdateImageRequest(
                    image_id=image_id,
                    region=region,
                    visibility=visibility,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())
        
    def delete_image(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Image:
        """
        Delete an image.
        Delete a given image. You must specify, in the endpoint, the `region` and `image_id` parameters of the image you want to delete.
        :param image_id: UUID of the image.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Image <Image>`
        
        Usage:
        ::
        
            result = api.delete_image(
                image_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_image_id = validate_path_param("image_id", image_id)
        
        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Image(res.json())
        
    def list_tags(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTagsRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> ListTagsResponse:
        """
        List tags.
        List all tags for a given image, specified by region. By default, the tags listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `name`.
        :param image_id: UUID of the image.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param name: Filter by the tag name (exact match).
        :return: :class:`ListTagsResponse <ListTagsResponse>`
        
        Usage:
        ::
        
            result = api.list_tags(
                image_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_image_id = validate_path_param("image_id", image_id)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/images/{param_image_id}/tags",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTagsResponse(res.json())
        
    def list_tags_all(
        self,
        *,
        image_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListTagsRequestOrderBy] = None,
        name: Optional[str] = None,
    ) -> List[Tag]:
        """
        List tags.
        List all tags for a given image, specified by region. By default, the tags listed are ordered by creation date in ascending order. This can be modified via the order_by field. You can also define additional parameters for your query, such as the `name`.
        :param image_id: UUID of the image.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: A positive integer to choose the page to display.
        :param page_size: A positive integer lower or equal to 100 to select the number of items to display.
        :param order_by: Criteria to use when ordering tag listings. Possible values are `created_at_asc`, `created_at_desc`, `name_asc`, `name_desc`, `region`, `status_asc` and `status_desc`. The default value is `created_at_asc`.
        :param name: Filter by the tag name (exact match).
        :return: :class:`List[Tag] <List[Tag]>`
        
        Usage:
        ::
        
            result = api.list_tags_all(
                image_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListTagsResponse,
            key="tags",
            fetcher=self.list_tags,
            args={
                "image_id": image_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "name": name,
            },
        )
        
    def get_tag(
        self,
        *,
        tag_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Tag:
        """
        Get a tag.
        Retrieve information about a given image tag, specified by its `tag_id` and region. Full details about the tag, such as `name`, `image_id`, `status`, and `digest` are returned in the response.
        :param tag_id: UUID of the tag.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Tag <Tag>`
        
        Usage:
        ::
        
            result = api.get_tag(
                tag_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_tag_id = validate_path_param("tag_id", tag_id)
        
        res = self._request(
            "GET",
            f"/registry/v1/regions/{param_region}/tags/{param_tag_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Tag(res.json())
        
    def wait_for_tag(
        self,
        *,
        tag_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Tag, bool]] = None,
    ) -> Tag:
        """
        Get a tag.
        Retrieve information about a given image tag, specified by its `tag_id` and region. Full details about the tag, such as `name`, `image_id`, `status`, and `digest` are returned in the response.
        :param tag_id: UUID of the tag.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Tag <Tag>`
        
        Usage:
        ::
        
            result = api.get_tag(
                tag_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in TAG_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_tag,
            options=options,
            args={
                "tag_id": tag_id,
                "region": region,
            },
        )
        
    def delete_tag(
        self,
        *,
        tag_id: str,
        region: Optional[ScwRegion] = None,
        force: Optional[bool] = None,
    ) -> Tag:
        """
        Delete a tag.
        Delete a given image tag. You must specify, in the endpoint, the `region` and `tag_id` parameters of the tag you want to delete.
        :param tag_id: UUID of the tag.
        :param region: Region to target. If none is passed will use default region from the config.
        :param force: If two tags share the same digest the deletion will fail unless this parameter is set to true (deprecated).
        :return: :class:`Tag <Tag>`
        
        Usage:
        ::
        
            result = api.delete_tag(
                tag_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_tag_id = validate_path_param("tag_id", tag_id)
        
        res = self._request(
            "DELETE",
            f"/registry/v1/regions/{param_region}/tags/{param_tag_id}",
            params={
                "force": force,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Tag(res.json())
        
