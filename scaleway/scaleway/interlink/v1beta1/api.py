# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region as ScwRegion,
)
from scaleway_core.utils import (
    WaitForOptions,
    validate_path_param,
    fetch_all_pages,
    wait_for_resource,
)
from .types import (
    BgpStatus,
    DedicatedConnectionStatus,
    LinkKind,
    LinkStatus,
    ListDedicatedConnectionsRequestOrderBy,
    ListLinksRequestOrderBy,
    ListPartnersRequestOrderBy,
    ListPopsRequestOrderBy,
    ListRoutingPoliciesRequestOrderBy,
    AttachRoutingPolicyRequest,
    AttachVpcRequest,
    CreateLinkRequest,
    CreateRoutingPolicyRequest,
    DedicatedConnection,
    Link,
    ListDedicatedConnectionsResponse,
    ListLinksResponse,
    ListPartnersResponse,
    ListPopsResponse,
    ListRoutingPoliciesResponse,
    Partner,
    Pop,
    RoutingPolicy,
    UpdateLinkRequest,
    UpdateRoutingPolicyRequest,
)
from .content import (
    DEDICATED_CONNECTION_TRANSIENT_STATUSES,
    LINK_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_DedicatedConnection,
    unmarshal_Link,
    unmarshal_Partner,
    unmarshal_Pop,
    unmarshal_RoutingPolicy,
    unmarshal_ListDedicatedConnectionsResponse,
    unmarshal_ListLinksResponse,
    unmarshal_ListPartnersResponse,
    unmarshal_ListPopsResponse,
    unmarshal_ListRoutingPoliciesResponse,
    marshal_AttachRoutingPolicyRequest,
    marshal_AttachVpcRequest,
    marshal_CreateLinkRequest,
    marshal_CreateRoutingPolicyRequest,
    marshal_UpdateLinkRequest,
    marshal_UpdateRoutingPolicyRequest,
)


class InterlinkV1Beta1API(API):
    """
    This API allows you to manage your Scaleway InterLink, to connect your on-premises infrastructure with your Scaleway VPC.
    """

    def list_dedicated_connections(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListDedicatedConnectionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        status: Optional[DedicatedConnectionStatus] = None,
        bandwidth_mbps: Optional[int] = None,
        pop_id: Optional[str] = None,
    ) -> ListDedicatedConnectionsResponse:
        """
        List dedicated connections.
        For self-hosted users, list their dedicated physical connections in a given region. By default, the connections returned in the list are ordered by name in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of connections to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Link name to filter for.
        :param tags: Tags to filter for.
        :param status: Connection status to filter for.
        :param bandwidth_mbps: Filter for dedicated connections with this bandwidth size.
        :param pop_id: Filter for dedicated connections present in this PoP.
        :return: :class:`ListDedicatedConnectionsResponse <ListDedicatedConnectionsResponse>`

        Usage:
        ::

            result = api.list_dedicated_connections()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/dedicated-connections",
            params={
                "bandwidth_mbps": bandwidth_mbps,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pop_id": pop_id,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDedicatedConnectionsResponse(res.json())

    def list_dedicated_connections_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListDedicatedConnectionsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        status: Optional[DedicatedConnectionStatus] = None,
        bandwidth_mbps: Optional[int] = None,
        pop_id: Optional[str] = None,
    ) -> List[DedicatedConnection]:
        """
        List dedicated connections.
        For self-hosted users, list their dedicated physical connections in a given region. By default, the connections returned in the list are ordered by name in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of connections to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Link name to filter for.
        :param tags: Tags to filter for.
        :param status: Connection status to filter for.
        :param bandwidth_mbps: Filter for dedicated connections with this bandwidth size.
        :param pop_id: Filter for dedicated connections present in this PoP.
        :return: :class:`List[DedicatedConnection] <List[DedicatedConnection]>`

        Usage:
        ::

            result = api.list_dedicated_connections_all()
        """

        return fetch_all_pages(
            type=ListDedicatedConnectionsResponse,
            key="connections",
            fetcher=self.list_dedicated_connections,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
                "tags": tags,
                "status": status,
                "bandwidth_mbps": bandwidth_mbps,
                "pop_id": pop_id,
            },
        )

    def get_dedicated_connection(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
    ) -> DedicatedConnection:
        """
        Get a dedicated connection.
        For self-hosted users, get a dedicated physical connection corresponding to the given ID. The response object includes information such as the connection's name, status and total bandwidth.
        :param connection_id: ID of connection to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DedicatedConnection <DedicatedConnection>`

        Usage:
        ::

            result = api.get_dedicated_connection(
                connection_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_connection_id = validate_path_param("connection_id", connection_id)

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/dedicated-connections/{param_connection_id}",
        )

        self._throw_on_error(res)
        return unmarshal_DedicatedConnection(res.json())

    def wait_for_dedicated_connection(
        self,
        *,
        connection_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[DedicatedConnection, bool]] = None,
    ) -> DedicatedConnection:
        """
        Get a dedicated connection.
        For self-hosted users, get a dedicated physical connection corresponding to the given ID. The response object includes information such as the connection's name, status and total bandwidth.
        :param connection_id: ID of connection to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DedicatedConnection <DedicatedConnection>`

        Usage:
        ::

            result = api.get_dedicated_connection(
                connection_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = (
                lambda res: res.status not in DEDICATED_CONNECTION_TRANSIENT_STATUSES
            )

        return wait_for_resource(
            fetcher=self.get_dedicated_connection,
            options=options,
            args={
                "connection_id": connection_id,
                "region": region,
            },
        )

    def list_partners(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPartnersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pop_ids: Optional[List[str]] = None,
    ) -> ListPartnersResponse:
        """
        List available partners.
        List all available partners. By default, the partners returned in the list are ordered by name in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of partners to return per page.
        :param pop_ids: Filter for partners present (offering a connection) in one of these PoPs.
        :return: :class:`ListPartnersResponse <ListPartnersResponse>`

        Usage:
        ::

            result = api.list_partners()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/partners",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pop_ids": pop_ids,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPartnersResponse(res.json())

    def list_partners_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPartnersRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        pop_ids: Optional[List[str]] = None,
    ) -> List[Partner]:
        """
        List available partners.
        List all available partners. By default, the partners returned in the list are ordered by name in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of partners to return per page.
        :param pop_ids: Filter for partners present (offering a connection) in one of these PoPs.
        :return: :class:`List[Partner] <List[Partner]>`

        Usage:
        ::

            result = api.list_partners_all()
        """

        return fetch_all_pages(
            type=ListPartnersResponse,
            key="partners",
            fetcher=self.list_partners,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "pop_ids": pop_ids,
            },
        )

    def get_partner(
        self,
        *,
        partner_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Partner:
        """
        Get a partner.
        Get a partner for the given partner IP. The response object includes information such as the partner's name, email address and portal URL.
        :param partner_id: ID of partner to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Partner <Partner>`

        Usage:
        ::

            result = api.get_partner(
                partner_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_partner_id = validate_path_param("partner_id", partner_id)

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/partners/{param_partner_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Partner(res.json())

    def list_pops(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPopsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        hosting_provider_name: Optional[str] = None,
        partner_id: Optional[str] = None,
        link_bandwidth_mbps: Optional[int] = None,
        dedicated_available: Optional[bool] = None,
    ) -> ListPopsResponse:
        """
        List PoPs.
        List all available PoPs (locations) for a given region. By default, the results are returned in ascending alphabetical order by name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of PoPs to return per page.
        :param name: PoP name to filter for.
        :param hosting_provider_name: Hosting provider name to filter for.
        :param partner_id: Filter for PoPs hosting an available shared connection from this partner.
        :param link_bandwidth_mbps: Filter for PoPs with a shared connection allowing this bandwidth size. Note that we cannot guarantee that PoPs returned will have available capacity.
        :param dedicated_available: Filter for PoPs with a dedicated connection available for self-hosted links.
        :return: :class:`ListPopsResponse <ListPopsResponse>`

        Usage:
        ::

            result = api.list_pops()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/pops",
            params={
                "dedicated_available": dedicated_available,
                "hosting_provider_name": hosting_provider_name,
                "link_bandwidth_mbps": link_bandwidth_mbps,
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "partner_id": partner_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListPopsResponse(res.json())

    def list_pops_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListPopsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        hosting_provider_name: Optional[str] = None,
        partner_id: Optional[str] = None,
        link_bandwidth_mbps: Optional[int] = None,
        dedicated_available: Optional[bool] = None,
    ) -> List[Pop]:
        """
        List PoPs.
        List all available PoPs (locations) for a given region. By default, the results are returned in ascending alphabetical order by name.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of PoPs to return per page.
        :param name: PoP name to filter for.
        :param hosting_provider_name: Hosting provider name to filter for.
        :param partner_id: Filter for PoPs hosting an available shared connection from this partner.
        :param link_bandwidth_mbps: Filter for PoPs with a shared connection allowing this bandwidth size. Note that we cannot guarantee that PoPs returned will have available capacity.
        :param dedicated_available: Filter for PoPs with a dedicated connection available for self-hosted links.
        :return: :class:`List[Pop] <List[Pop]>`

        Usage:
        ::

            result = api.list_pops_all()
        """

        return fetch_all_pages(
            type=ListPopsResponse,
            key="pops",
            fetcher=self.list_pops,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "name": name,
                "hosting_provider_name": hosting_provider_name,
                "partner_id": partner_id,
                "link_bandwidth_mbps": link_bandwidth_mbps,
                "dedicated_available": dedicated_available,
            },
        )

    def get_pop(
        self,
        *,
        pop_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Pop:
        """
        Get a PoP.
        Get a PoP for the given PoP ID. The response object includes the PoP's name and information about its physical location.
        :param pop_id: ID of PoP to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Pop <Pop>`

        Usage:
        ::

            result = api.get_pop(
                pop_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_pop_id = validate_path_param("pop_id", pop_id)

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/pops/{param_pop_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Pop(res.json())

    def list_links(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListLinksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        status: Optional[LinkStatus] = None,
        bgp_v4_status: Optional[BgpStatus] = None,
        bgp_v6_status: Optional[BgpStatus] = None,
        pop_id: Optional[str] = None,
        bandwidth_mbps: Optional[int] = None,
        partner_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        routing_policy_id: Optional[str] = None,
        pairing_key: Optional[str] = None,
        kind: Optional[LinkKind] = None,
        connection_id: Optional[str] = None,
    ) -> ListLinksResponse:
        """
        List links.
        List all your links (InterLink connections). A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of links to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Link name to filter for.
        :param tags: Tags to filter for.
        :param status: Link status to filter for.
        :param bgp_v4_status: BGP IPv4 status to filter for.
        :param bgp_v6_status: BGP IPv6 status to filter for.
        :param pop_id: Filter for links attached to this PoP (via connections).
        :param bandwidth_mbps: Filter for link bandwidth (in Mbps).
        :param partner_id: Filter for links hosted by this partner.
        :param vpc_id: Filter for links attached to this VPC.
        :param routing_policy_id: Filter for links using this routing policy.
        :param pairing_key: Filter for the link with this pairing_key.
        :param kind: Filter for hosted or self-hosted links.
        :param connection_id: Filter for links self-hosted on this connection.
        :return: :class:`ListLinksResponse <ListLinksResponse>`

        Usage:
        ::

            result = api.list_links()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/links",
            params={
                "bandwidth_mbps": bandwidth_mbps,
                "bgp_v4_status": bgp_v4_status,
                "bgp_v6_status": bgp_v6_status,
                "connection_id": connection_id,
                "kind": kind,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "pairing_key": pairing_key,
                "partner_id": partner_id,
                "pop_id": pop_id,
                "project_id": project_id or self.client.default_project_id,
                "routing_policy_id": routing_policy_id,
                "status": status,
                "tags": tags,
                "vpc_id": vpc_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListLinksResponse(res.json())

    def list_links_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListLinksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        status: Optional[LinkStatus] = None,
        bgp_v4_status: Optional[BgpStatus] = None,
        bgp_v6_status: Optional[BgpStatus] = None,
        pop_id: Optional[str] = None,
        bandwidth_mbps: Optional[int] = None,
        partner_id: Optional[str] = None,
        vpc_id: Optional[str] = None,
        routing_policy_id: Optional[str] = None,
        pairing_key: Optional[str] = None,
        kind: Optional[LinkKind] = None,
        connection_id: Optional[str] = None,
    ) -> List[Link]:
        """
        List links.
        List all your links (InterLink connections). A number of filters are available, including Project ID, name, tags and status.
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of links to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Link name to filter for.
        :param tags: Tags to filter for.
        :param status: Link status to filter for.
        :param bgp_v4_status: BGP IPv4 status to filter for.
        :param bgp_v6_status: BGP IPv6 status to filter for.
        :param pop_id: Filter for links attached to this PoP (via connections).
        :param bandwidth_mbps: Filter for link bandwidth (in Mbps).
        :param partner_id: Filter for links hosted by this partner.
        :param vpc_id: Filter for links attached to this VPC.
        :param routing_policy_id: Filter for links using this routing policy.
        :param pairing_key: Filter for the link with this pairing_key.
        :param kind: Filter for hosted or self-hosted links.
        :param connection_id: Filter for links self-hosted on this connection.
        :return: :class:`List[Link] <List[Link]>`

        Usage:
        ::

            result = api.list_links_all()
        """

        return fetch_all_pages(
            type=ListLinksResponse,
            key="links",
            fetcher=self.list_links,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
                "tags": tags,
                "status": status,
                "bgp_v4_status": bgp_v4_status,
                "bgp_v6_status": bgp_v6_status,
                "pop_id": pop_id,
                "bandwidth_mbps": bandwidth_mbps,
                "partner_id": partner_id,
                "vpc_id": vpc_id,
                "routing_policy_id": routing_policy_id,
                "pairing_key": pairing_key,
                "kind": kind,
                "connection_id": connection_id,
            },
        )

    def get_link(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Get a link.
        Get a link (InterLink session / logical InterLink resource) for the given link ID. The response object includes information about the link's various configuration details.
        :param link_id: ID of the link to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.get_link(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def wait_for_link(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Link, bool]] = None,
    ) -> Link:
        """
        Get a link.
        Get a link (InterLink session / logical InterLink resource) for the given link ID. The response object includes information about the link's various configuration details.
        :param link_id: ID of the link to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.get_link(
                link_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in LINK_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_link,
            options=options,
            args={
                "link_id": link_id,
                "region": region,
            },
        )

    def create_link(
        self,
        *,
        name: str,
        pop_id: str,
        bandwidth_mbps: int,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        connection_id: Optional[str] = None,
        partner_id: Optional[str] = None,
    ) -> Link:
        """
        Create a link.
        Create a link (InterLink session / logical InterLink resource) in a given PoP, specifying its various configuration details. Links can either be hosted (faciliated by partners' shared physical connections) or self-hosted (for users who have purchased a dedicated physical connection).
        :param name: Name of the link.
        :param pop_id: PoP (location) where the link will be created.
        :param bandwidth_mbps: Desired bandwidth for the link. Must be compatible with available link bandwidths and remaining bandwidth capacity of the connection.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the link in.
        :param tags: List of tags to apply to the link.
        :param connection_id: If set, creates a self-hosted link using this dedicated physical connection. As the customer, specify the ID of the physical connection you already have for this link.
        One-Of ('host'): at most one of 'connection_id', 'partner_id' could be set.
        :param partner_id: If set, creates a hosted link on a partner's connection. Specify the ID of the chosen partner, who already has a shared connection with available bandwidth.
        One-Of ('host'): at most one of 'connection_id', 'partner_id' could be set.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.create_link(
                name="example",
                pop_id="example",
                bandwidth_mbps=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links",
            body=marshal_CreateLinkRequest(
                CreateLinkRequest(
                    name=name,
                    pop_id=pop_id,
                    bandwidth_mbps=bandwidth_mbps,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    connection_id=connection_id,
                    partner_id=partner_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def update_link(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Link:
        """
        Update a link.
        Update an existing link, specified by its link ID. Only its name and tags can be updated.
        :param link_id: ID of the link to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the link.
        :param tags: List of tags to apply to the link.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.update_link(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "PATCH",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}",
            body=marshal_UpdateLinkRequest(
                UpdateLinkRequest(
                    link_id=link_id,
                    region=region,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def delete_link(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Delete a link.
        Delete an existing link, specified by its link ID. Note that as well as deleting the link here on the Scaleway side, it is also necessary to request deletion from the partner on their side. Only when this action has been carried out on both sides will the resource be completely deleted.
        :param link_id: ID of the link to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.delete_link(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "DELETE",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def attach_vpc(
        self,
        *,
        link_id: str,
        vpc_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Attach a VPC.
        Attach a VPC to an existing link. This facilitates communication between the resources in your Scaleway VPC, and your on-premises infrastructure.
        :param link_id: ID of the link to attach VPC to.
        :param vpc_id: ID of the VPC to attach.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.attach_vpc(
                link_id="example",
                vpc_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/attach-vpc",
            body=marshal_AttachVpcRequest(
                AttachVpcRequest(
                    link_id=link_id,
                    vpc_id=vpc_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def detach_vpc(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Detach a VPC.
        Detach a VPC from an existing link.
        :param link_id: ID of the link to detach the VPC from.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.detach_vpc(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/detach-vpc",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def attach_routing_policy(
        self,
        *,
        link_id: str,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Attach a routing policy.
        Attach a routing policy to an existing link. As all routes across the link are blocked by default, you must attach a routing policy to set IP prefix filters for allowed routes, facilitating traffic flow.
        :param link_id: ID of the link to attach a routing policy to.
        :param routing_policy_id: ID of the routing policy to be attached.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.attach_routing_policy(
                link_id="example",
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/attach-routing-policy",
            body=marshal_AttachRoutingPolicyRequest(
                AttachRoutingPolicyRequest(
                    link_id=link_id,
                    routing_policy_id=routing_policy_id,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def detach_routing_policy(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Detach a routing policy.
        Detach a routing policy from an existing link. Without a routing policy, all routes across the link are blocked by default.
        :param link_id: ID of the link to detach a routing policy from.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.detach_routing_policy(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/detach-routing-policy",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def enable_route_propagation(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Enable route propagation.
        Enable all allowed prefixes (defined in a routing policy) to be announced in the BGP session. This allows traffic to flow between the attached VPC and the on-premises infrastructure along the announced routes. Note that by default, even when route propagation is enabled, all routes are blocked. It is essential to attach a routing policy to define the ranges of routes to announce.
        :param link_id: ID of the link on which to enable route propagation.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.enable_route_propagation(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/enable-route-propagation",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def disable_route_propagation(
        self,
        *,
        link_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Link:
        """
        Disable route propagation.
        Prevent any prefixes from being announced in the BGP session. Traffic will not be able to flow over the InterLink until route propagation is re-enabled.
        :param link_id: ID of the link on which to disable route propagation.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Link <Link>`

        Usage:
        ::

            result = api.disable_route_propagation(
                link_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_link_id = validate_path_param("link_id", link_id)

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/links/{param_link_id}/disable-route-propagation",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Link(res.json())

    def list_routing_policies(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListRoutingPoliciesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> ListRoutingPoliciesResponse:
        """
        List routing policies.
        List all routing policies in a given region. A routing policy can be attached to one or multiple links (InterLink connections).
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of routing policies to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Routing policy name to filter for.
        :param tags: Tags to filter for.
        :return: :class:`ListRoutingPoliciesResponse <ListRoutingPoliciesResponse>`

        Usage:
        ::

            result = api.list_routing_policies()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/routing-policies",
            params={
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListRoutingPoliciesResponse(res.json())

    def list_routing_policies_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        order_by: Optional[ListRoutingPoliciesRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> List[RoutingPolicy]:
        """
        List routing policies.
        List all routing policies in a given region. A routing policy can be attached to one or multiple links (InterLink connections).
        :param region: Region to target. If none is passed will use default region from the config.
        :param order_by: Order in which to return results.
        :param page: Page number to return.
        :param page_size: Maximum number of routing policies to return per page.
        :param project_id: Project ID to filter for.
        :param organization_id: Organization ID to filter for.
        :param name: Routing policy name to filter for.
        :param tags: Tags to filter for.
        :return: :class:`List[RoutingPolicy] <List[RoutingPolicy]>`

        Usage:
        ::

            result = api.list_routing_policies_all()
        """

        return fetch_all_pages(
            type=ListRoutingPoliciesResponse,
            key="routing_policies",
            fetcher=self.list_routing_policies,
            args={
                "region": region,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "project_id": project_id,
                "organization_id": organization_id,
                "name": name,
                "tags": tags,
            },
        )

    def get_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
    ) -> RoutingPolicy:
        """
        Get routing policy.
        Get a routing policy for the given routing policy ID. The response object gives information including the policy's name, tags and prefix filters.
        :param routing_policy_id: ID of the routing policy to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = api.get_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "GET",
            f"/interlink/v1beta1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    def create_routing_policy(
        self,
        *,
        name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        prefix_filter_in: Optional[List[str]] = None,
        prefix_filter_out: Optional[List[str]] = None,
    ) -> RoutingPolicy:
        """
        Create a routing policy.
        Create a routing policy. Routing policies allow you to set IP prefix filters to define the incoming route announcements to accept from the peer, and the outgoing routes to announce to the peer.
        :param name: Name of the routing policy.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to create the routing policy in.
        :param tags: List of tags to apply to the routing policy.
        :param prefix_filter_in: IP prefixes to accept from the peer (ranges of route announcements to accept).
        :param prefix_filter_out: IP prefix filters to advertise to the peer (ranges of routes to advertise).
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = api.create_routing_policy(
                name="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/interlink/v1beta1/regions/{param_region}/routing-policies",
            body=marshal_CreateRoutingPolicyRequest(
                CreateRoutingPolicyRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    prefix_filter_in=prefix_filter_in,
                    prefix_filter_out=prefix_filter_out,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    def update_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        prefix_filter_in: Optional[List[str]] = None,
        prefix_filter_out: Optional[List[str]] = None,
    ) -> RoutingPolicy:
        """
        Update a routing policy.
        Update an existing routing policy, specified by its routing policy ID. Its name, tags and incoming/outgoing prefix filters can be updated.
        :param routing_policy_id: ID of the routing policy to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the routing policy.
        :param tags: List of tags to apply to the routing policy.
        :param prefix_filter_in: IP prefixes to accept from the peer (ranges of route announcements to accept).
        :param prefix_filter_out: IP prefix filters for routes to advertise to the peer (ranges of routes to advertise).
        :return: :class:`RoutingPolicy <RoutingPolicy>`

        Usage:
        ::

            result = api.update_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "PATCH",
            f"/interlink/v1beta1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
            body=marshal_UpdateRoutingPolicyRequest(
                UpdateRoutingPolicyRequest(
                    routing_policy_id=routing_policy_id,
                    region=region,
                    name=name,
                    tags=tags,
                    prefix_filter_in=prefix_filter_in,
                    prefix_filter_out=prefix_filter_out,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_RoutingPolicy(res.json())

    def delete_routing_policy(
        self,
        *,
        routing_policy_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a routing policy.
        Delete an existing routing policy, specified by its routing policy ID.
        :param routing_policy_id: ID of the routing policy to delete.
        :param region: Region to target. If none is passed will use default region from the config.

        Usage:
        ::

            result = api.delete_routing_policy(
                routing_policy_id="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_routing_policy_id = validate_path_param(
            "routing_policy_id", routing_policy_id
        )

        res = self._request(
            "DELETE",
            f"/interlink/v1beta1/regions/{param_region}/routing-policies/{param_routing_policy_id}",
        )

        self._throw_on_error(res)
