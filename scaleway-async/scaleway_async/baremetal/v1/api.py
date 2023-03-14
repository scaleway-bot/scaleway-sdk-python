# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import Awaitable, List, Optional, Union

from scaleway_core.api import API
from scaleway_core.bridge import (
    Zone,
)
from scaleway_core.utils import (
    WaitForOptions,
    fetch_all_pages_async,
    validate_path_param,
    wait_for_resource_async,
)
from .types import (
    ListServerEventsRequestOrderBy,
    ListServerPrivateNetworksRequestOrderBy,
    ListServersRequestOrderBy,
    ListSettingsRequestOrderBy,
    OfferSubscriptionPeriod,
    ServerBootType,
    BMCAccess,
    CreateServerRequestInstall,
    GetServerMetricsResponse,
    IP,
    ListOSResponse,
    ListOffersResponse,
    ListOptionsResponse,
    ListServerEventsResponse,
    ListServerPrivateNetworksResponse,
    ListServersResponse,
    ListSettingsResponse,
    OS,
    Offer,
    Option,
    Server,
    ServerEvent,
    ServerPrivateNetwork,
    SetServerPrivateNetworksResponse,
    Setting,
    CreateServerRequest,
    UpdateServerRequest,
    InstallServerRequest,
    RebootServerRequest,
    StartServerRequest,
    StartBMCAccessRequest,
    UpdateIPRequest,
    AddOptionServerRequest,
    UpdateSettingRequest,
    PrivateNetworkApiAddServerPrivateNetworkRequest,
    PrivateNetworkApiSetServerPrivateNetworksRequest,
)
from .content import (
    SERVER_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_AddOptionServerRequest,
    marshal_CreateServerRequest,
    marshal_InstallServerRequest,
    marshal_PrivateNetworkApiAddServerPrivateNetworkRequest,
    marshal_PrivateNetworkApiSetServerPrivateNetworksRequest,
    marshal_RebootServerRequest,
    marshal_StartBMCAccessRequest,
    marshal_StartServerRequest,
    marshal_UpdateIPRequest,
    marshal_UpdateServerRequest,
    marshal_UpdateSettingRequest,
    unmarshal_IP,
    unmarshal_OS,
    unmarshal_Offer,
    unmarshal_Option,
    unmarshal_Server,
    unmarshal_ServerPrivateNetwork,
    unmarshal_Setting,
    unmarshal_BMCAccess,
    unmarshal_GetServerMetricsResponse,
    unmarshal_ListOSResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListOptionsResponse,
    unmarshal_ListServerEventsResponse,
    unmarshal_ListServerPrivateNetworksResponse,
    unmarshal_ListServersResponse,
    unmarshal_ListSettingsResponse,
    unmarshal_SetServerPrivateNetworksResponse,
)


class BaremetalV1API(API):
    """
    Elastic Metal API.

    This API allows to manage your Elastic Metal server.
    """

    async def list_servers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListServersRequestOrderBy = ListServersRequestOrderBy.CREATED_AT_ASC,
        tags: Optional[List[str]] = None,
        status: Optional[List[str]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        option_id: Optional[str] = None,
    ) -> ListServersResponse:
        """
        List Elastic Metal servers for a specific organization.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of servers per page.
        :param order_by: Order of the servers.
        :param tags: Tags to filter for.
        :param status: Status to filter for.
        :param name: Names to filter for.
        :param organization_id: Organization ID to filter for.
        :param project_id: Project ID to filter for.
        :param option_id: Option ID to filter for.
        :return: :class:`ListServersResponse <ListServersResponse>`

        Usage:
        ::

            result = await api.list_servers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers",
            params={
                "name": name,
                "option_id": option_id,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServersResponse(res.json())

    async def list_servers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServersRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        status: Optional[List[str]] = None,
        name: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        option_id: Optional[str] = None,
    ) -> List[Server]:
        """
        List Elastic Metal servers for a specific organization.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of servers per page.
        :param order_by: Order of the servers.
        :param tags: Tags to filter for.
        :param status: Status to filter for.
        :param name: Names to filter for.
        :param organization_id: Organization ID to filter for.
        :param project_id: Project ID to filter for.
        :param option_id: Option ID to filter for.
        :return: :class:`List[ListServersResponse] <List[ListServersResponse]>`

        Usage:
        ::

            result = await api.list_servers_all()
        """

        return await fetch_all_pages_async(
            type=ListServersResponse,
            key="servers",
            fetcher=self.list_servers,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "tags": tags,
                "status": status,
                "name": name,
                "organization_id": organization_id,
                "project_id": project_id,
                "option_id": option_id,
            },
        )

    async def get_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Get full details of an existing Elastic Metal server associated with the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.get_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def wait_for_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Server, Union[bool, Awaitable[bool]]]] = None,
    ) -> Server:
        """
        Waits for :class:`Server <Server>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :param options: The options for the waiter
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = api.wait_for_server(server_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SERVER_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_server,
            options=options,
            args={
                "server_id": server_id,
                "zone": zone,
            },
        )

    async def create_server(
        self,
        *,
        offer_id: str,
        name: str,
        description: str,
        zone: Optional[Zone] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        install: Optional[CreateServerRequestInstall] = None,
        option_ids: Optional[List[str]] = None,
    ) -> Server:
        """
        Create a new Elastic Metal server. Once the server is created, proceed with the [installation of an OS](#post-3e949e).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param offer_id: Offer ID of the new server.
        :param organization_id: Organization ID with which the server will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param project_id: Project ID with which the server will be created.

        One-of ('project_identifier'): at most one of 'organization_id', 'project_id' could be set.
        :param name: Name of the server (≠hostname).
        :param description: Description associated with the server, max 255 characters.
        :param tags: Tags to associate to the server.
        :param install: Object describing the configuration details of the OS installation on the server.
        :param option_ids: IDs of options to enable on server.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.create_server(
                offer_id="example",
                name="example",
                description="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers",
            body=marshal_CreateServerRequest(
                CreateServerRequest(
                    offer_id=offer_id,
                    name=name,
                    description=description,
                    zone=zone,
                    organization_id=organization_id,
                    project_id=project_id,
                    tags=tags,
                    install=install,
                    option_ids=option_ids,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def update_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Server:
        """
        Update the server associated with the ID. You can update parameters such as the server's name, tags and description. Any parameters left null in the request body are not updated.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server to update.
        :param name: Name of the server (≠hostname), not updated if null.
        :param description: Description associated with the server, max 255 characters, not updated if null.
        :param tags: Tags associated with the server, not updated if null.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.update_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
            body=marshal_UpdateServerRequest(
                UpdateServerRequest(
                    server_id=server_id,
                    zone=zone,
                    name=name,
                    description=description,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def install_server(
        self,
        *,
        server_id: str,
        os_id: str,
        hostname: str,
        ssh_key_ids: List[str],
        zone: Optional[Zone] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        service_user: Optional[str] = None,
        service_password: Optional[str] = None,
    ) -> Server:
        """
        Install an Operating System (OS) on the Elastic Metal server with a specific ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: Server ID to install.
        :param os_id: ID of the OS to installation on the server.
        :param hostname: Hostname of the server.
        :param ssh_key_ids: SSH key IDs authorized on the server.
        :param user: User used for the installation.
        :param password: Password used for the installation.
        :param service_user: User used for the service to install.
        :param service_password: Password used for the service to install.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.install_server(
                server_id="example",
                os_id="example",
                hostname="example",
                ssh_key_ids=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/install",
            body=marshal_InstallServerRequest(
                InstallServerRequest(
                    server_id=server_id,
                    os_id=os_id,
                    hostname=hostname,
                    ssh_key_ids=ssh_key_ids,
                    zone=zone,
                    user=user,
                    password=password,
                    service_user=service_user,
                    service_password=service_password,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def get_server_metrics(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> GetServerMetricsResponse:
        """
        Get the ping status of the server associated with the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: Server ID to get the metrics.
        :return: :class:`GetServerMetricsResponse <GetServerMetricsResponse>`

        Usage:
        ::

            result = await api.get_server_metrics(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/metrics",
        )

        self._throw_on_error(res)
        return unmarshal_GetServerMetricsResponse(res.json())

    async def delete_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Delete the server associated with the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server to delete.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.delete_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def reboot_server(
        self,
        *,
        server_id: str,
        boot_type: ServerBootType,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Reboot the Elastic Metal server associated with the ID, use the `boot_type` `rescue` to reboot the server in rescue mode.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server to reboot.
        :param boot_type: The type of boot.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.reboot_server(
                server_id="example",
                boot_type=unknown_boot_type,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/reboot",
            body=marshal_RebootServerRequest(
                RebootServerRequest(
                    server_id=server_id,
                    boot_type=boot_type,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def start_server(
        self,
        *,
        server_id: str,
        boot_type: ServerBootType,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Start the server associated with the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server to start.
        :param boot_type: The type of boot.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.start_server(
                server_id="example",
                boot_type=unknown_boot_type,
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/start",
            body=marshal_StartServerRequest(
                StartServerRequest(
                    server_id=server_id,
                    boot_type=boot_type,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def stop_server(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Stop the server associated with the ID. The server remains allocated to your account and all data remains on the local storage of the server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server to stop.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.stop_server(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/stop",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def list_server_events(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListServerEventsRequestOrderBy = ListServerEventsRequestOrderBy.CREATED_AT_ASC,
    ) -> ListServerEventsResponse:
        """
        List event (i.e. start/stop/reboot) associated to the server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server events searched.
        :param page: Page number.
        :param page_size: Number of server events per page.
        :param order_by: Order of the server events.
        :return: :class:`ListServerEventsResponse <ListServerEventsResponse>`

        Usage:
        ::

            result = await api.list_server_events(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/events",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerEventsResponse(res.json())

    async def list_server_events_all(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListServerEventsRequestOrderBy] = None,
    ) -> List[ServerEvent]:
        """
        List event (i.e. start/stop/reboot) associated to the server ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server events searched.
        :param page: Page number.
        :param page_size: Number of server events per page.
        :param order_by: Order of the server events.
        :return: :class:`List[ListServerEventsResponse] <List[ListServerEventsResponse]>`

        Usage:
        ::

            result = await api.list_server_events_all(server_id="example")
        """

        return await fetch_all_pages_async(
            type=ListServerEventsResponse,
            key="events",
            fetcher=self.list_server_events,
            args={
                "server_id": server_id,
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    async def start_bmc_access(
        self,
        *,
        server_id: str,
        ip: str,
        zone: Optional[Zone] = None,
    ) -> BMCAccess:
        """
        Start BMC (Baseboard Management Controller) access associated with the ID.
        The BMC (Baseboard Management Controller) access is available one hour after the installation of the server.
        You need first to create an option Remote Access. You will find the ID and the price with a call to listOffers (https://developers.scaleway.com/en/products/baremetal/api/#get-78db92). Then add the option https://developers.scaleway.com/en/products/baremetal/api/#post-b14abd.
        After adding the BMC option, you need to Get Remote Access to get the login/password https://developers.scaleway.com/en/products/baremetal/api/#get-cefc0f. Do not forget to delete the Option after use.

        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :param ip: The IP authorized to connect to the server.
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = await api.start_bmc_access(
                server_id="example",
                ip="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
            body=marshal_StartBMCAccessRequest(
                StartBMCAccessRequest(
                    server_id=server_id,
                    ip=ip,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_BMCAccess(res.json())

    async def get_bmc_access(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> BMCAccess:
        """
        Get the BMC (Baseboard Management Controller) access associated with the ID, including the URL and login information needed to connect.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :return: :class:`BMCAccess <BMCAccess>`

        Usage:
        ::

            result = await api.get_bmc_access(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)
        return unmarshal_BMCAccess(res.json())

    async def stop_bmc_access(
        self,
        *,
        server_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Stop BMC (Baseboard Management Controller) access associated with the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.

        Usage:
        ::

            result = await api.stop_bmc_access(server_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/bmc-access",
        )

        self._throw_on_error(res)
        return None

    async def update_ip(
        self,
        *,
        server_id: str,
        ip_id: str,
        zone: Optional[Zone] = None,
        reverse: Optional[str] = None,
    ) -> IP:
        """
        Configure the IP address associated with the server ID and IP ID. You can use this method to set a reverse DNS for an IP address.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :param ip_id: ID of the IP to update.
        :param reverse: New reverse IP to update, not updated if null.
        :return: :class:`IP <IP>`

        Usage:
        ::

            result = await api.update_ip(
                server_id="example",
                ip_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_ip_id = validate_path_param("ip_id", ip_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/ips/{param_ip_id}",
            body=marshal_UpdateIPRequest(
                UpdateIPRequest(
                    server_id=server_id,
                    ip_id=ip_id,
                    zone=zone,
                    reverse=reverse,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_IP(res.json())

    async def add_option_server(
        self,
        *,
        server_id: str,
        option_id: str,
        zone: Optional[Zone] = None,
        expires_at: Optional[datetime] = None,
    ) -> Server:
        """
        Add an option, such as Private Networks, to a specific server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :param option_id: ID of the option to add.
        :param expires_at: Auto expire the option after this date.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.add_option_server(
                server_id="example",
                option_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/options/{param_option_id}",
            body=marshal_AddOptionServerRequest(
                AddOptionServerRequest(
                    server_id=server_id,
                    option_id=option_id,
                    zone=zone,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def delete_option_server(
        self,
        *,
        server_id: str,
        option_id: str,
        zone: Optional[Zone] = None,
    ) -> Server:
        """
        Delete an option from a specific server.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: ID of the server.
        :param option_id: ID of the option to delete.
        :return: :class:`Server <Server>`

        Usage:
        ::

            result = await api.delete_option_server(
                server_id="example",
                option_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/options/{param_option_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Server(res.json())

    async def list_offers(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        subscription_period: OfferSubscriptionPeriod = OfferSubscriptionPeriod.UNKNOWN_SUBSCRIPTION_PERIOD,
    ) -> ListOffersResponse:
        """
        List all available Elastic Metal server configurations.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of offers per page.
        :param subscription_period: Subscription period type to filter offers by.
        :return: :class:`ListOffersResponse <ListOffersResponse>`

        Usage:
        ::

            result = await api.list_offers()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/offers",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "subscription_period": subscription_period,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())

    async def list_offers_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        subscription_period: Optional[OfferSubscriptionPeriod] = None,
    ) -> List[Offer]:
        """
        List all available Elastic Metal server configurations.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of offers per page.
        :param subscription_period: Subscription period type to filter offers by.
        :return: :class:`List[ListOffersResponse] <List[ListOffersResponse]>`

        Usage:
        ::

            result = await api.list_offers_all()
        """

        return await fetch_all_pages_async(
            type=ListOffersResponse,
            key="offers",
            fetcher=self.list_offers,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "subscription_period": subscription_period,
            },
        )

    async def get_offer(
        self,
        *,
        offer_id: str,
        zone: Optional[Zone] = None,
    ) -> Offer:
        """
        Get details of an offer identified by its offer ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param offer_id: ID of the researched Offer.
        :return: :class:`Offer <Offer>`

        Usage:
        ::

            result = await api.get_offer(offer_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_offer_id = validate_path_param("offer_id", offer_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/offers/{param_offer_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Offer(res.json())

    async def get_option(
        self,
        *,
        option_id: str,
        zone: Optional[Zone] = None,
    ) -> Option:
        """
        Return specific option for the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param option_id: ID of the option.
        :return: :class:`Option <Option>`

        Usage:
        ::

            result = await api.get_option(option_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_option_id = validate_path_param("option_id", option_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/options/{param_option_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Option(res.json())

    async def list_options(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListOptionsResponse:
        """
        List all options matching with filters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of options per page.
        :param offer_id: Offer ID to filter options for.
        :param name: Name to filter options for.
        :return: :class:`ListOptionsResponse <ListOptionsResponse>`

        Usage:
        ::

            result = await api.list_options()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/options",
            params={
                "name": name,
                "offer_id": offer_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOptionsResponse(res.json())

    async def list_options_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[Option]:
        """
        List all options matching with filters.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of options per page.
        :param offer_id: Offer ID to filter options for.
        :param name: Name to filter options for.
        :return: :class:`List[ListOptionsResponse] <List[ListOptionsResponse]>`

        Usage:
        ::

            result = await api.list_options_all()
        """

        return await fetch_all_pages_async(
            type=ListOptionsResponse,
            key="options",
            fetcher=self.list_options,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "offer_id": offer_id,
                "name": name,
            },
        )

    async def list_settings(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListSettingsRequestOrderBy = ListSettingsRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
    ) -> ListSettingsResponse:
        """
        Return all settings for a project ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Set the maximum list size.
        :param order_by: Sort order for items in the response.
        :param project_id: ID of the project.
        :return: :class:`ListSettingsResponse <ListSettingsResponse>`

        Usage:
        ::

            result = await api.list_settings()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/settings",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSettingsResponse(res.json())

    async def list_settings_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSettingsRequestOrderBy] = None,
        project_id: Optional[str] = None,
    ) -> List[Setting]:
        """
        Return all settings for a project ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Set the maximum list size.
        :param order_by: Sort order for items in the response.
        :param project_id: ID of the project.
        :return: :class:`List[ListSettingsResponse] <List[ListSettingsResponse]>`

        Usage:
        ::

            result = await api.list_settings_all()
        """

        return await fetch_all_pages_async(
            type=ListSettingsResponse,
            key="settings",
            fetcher=self.list_settings,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "project_id": project_id,
            },
        )

    async def update_setting(
        self,
        *,
        setting_id: str,
        zone: Optional[Zone] = None,
        enabled: Optional[bool] = None,
    ) -> Setting:
        """
        Update a setting for a project ID (enable or disable).
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param setting_id: ID of the setting.
        :param enabled: Defines whether the setting is enabled.
        :return: :class:`Setting <Setting>`

        Usage:
        ::

            result = await api.update_setting(setting_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_setting_id = validate_path_param("setting_id", setting_id)

        res = self._request(
            "PATCH",
            f"/baremetal/v1/zones/{param_zone}/settings/{param_setting_id}",
            body=marshal_UpdateSettingRequest(
                UpdateSettingRequest(
                    setting_id=setting_id,
                    zone=zone,
                    enabled=enabled,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Setting(res.json())

    async def list_os(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
    ) -> ListOSResponse:
        """
        List all OSes that are available for installation on Elastic Metal servers.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :param offer_id: Offer IDs to filter OSes for.
        :return: :class:`ListOSResponse <ListOSResponse>`

        Usage:
        ::

            result = await api.list_os()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/os",
            params={
                "offer_id": offer_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOSResponse(res.json())

    async def list_os_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        offer_id: Optional[str] = None,
    ) -> List[OS]:
        """
        List all OSes that are available for installation on Elastic Metal servers.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Page number.
        :param page_size: Number of OS per page.
        :param offer_id: Offer IDs to filter OSes for.
        :return: :class:`List[ListOSResponse] <List[ListOSResponse]>`

        Usage:
        ::

            result = await api.list_os_all()
        """

        return await fetch_all_pages_async(
            type=ListOSResponse,
            key="os",
            fetcher=self.list_os,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
                "offer_id": offer_id,
            },
        )

    async def get_os(
        self,
        *,
        os_id: str,
        zone: Optional[Zone] = None,
    ) -> OS:
        """
        Return specific OS for the ID.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param os_id: ID of the OS.
        :return: :class:`OS <OS>`

        Usage:
        ::

            result = await api.get_os(os_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_os_id = validate_path_param("os_id", os_id)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/os/{param_os_id}",
        )

        self._throw_on_error(res)
        return unmarshal_OS(res.json())


class BaremetalPrivateNetworkV1API(API):
    """
    Elastic Metal Private Network API.
    """

    async def add_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> ServerPrivateNetwork:
        """
        Add a server to a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: The ID of the server.
        :param private_network_id: The ID of the Private Network.
        :return: :class:`ServerPrivateNetwork <ServerPrivateNetwork>`

        Usage:
        ::

            result = await api.add_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "POST",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiAddServerPrivateNetworkRequest(
                PrivateNetworkApiAddServerPrivateNetworkRequest(
                    server_id=server_id,
                    private_network_id=private_network_id,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_ServerPrivateNetwork(res.json())

    async def set_server_private_networks(
        self,
        *,
        server_id: str,
        private_network_ids: List[str],
        zone: Optional[Zone] = None,
    ) -> SetServerPrivateNetworksResponse:
        """
        Set multiple Private Networks on a server
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: The ID of the server.
        :param private_network_ids: The IDs of the Private Networks.
        :return: :class:`SetServerPrivateNetworksResponse <SetServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.set_server_private_networks(
                server_id="example",
                private_network_ids=["example"],
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)

        res = self._request(
            "PUT",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks",
            body=marshal_PrivateNetworkApiSetServerPrivateNetworksRequest(
                PrivateNetworkApiSetServerPrivateNetworksRequest(
                    server_id=server_id,
                    private_network_ids=private_network_ids,
                    zone=zone,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SetServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListServerPrivateNetworksRequestOrderBy = ListServerPrivateNetworksRequestOrderBy.CREATED_AT_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> ListServerPrivateNetworksResponse:
        """
        List the Private Networks of a server
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: The sort order for the returned Private Networks.
        :param page: The page number for the returned Private Networks.
        :param page_size: The maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server ID.
        :param private_network_id: Filter Private Networks by Private Network ID.
        :param organization_id: Filter Private Networks by Organization ID.
        :param project_id: Filter Private Networks by Project ID.
        :return: :class:`ListServerPrivateNetworksResponse <ListServerPrivateNetworksResponse>`

        Usage:
        ::

            result = await api.list_server_private_networks()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/baremetal/v1/zones/{param_zone}/server-private-networks",
            params={
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "private_network_id": private_network_id,
                "project_id": project_id or self.client.default_project_id,
                "server_id": server_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListServerPrivateNetworksResponse(res.json())

    async def list_server_private_networks_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListServerPrivateNetworksRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        server_id: Optional[str] = None,
        private_network_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> List[ServerPrivateNetwork]:
        """
        List the Private Networks of a server
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: The sort order for the returned Private Networks.
        :param page: The page number for the returned Private Networks.
        :param page_size: The maximum number of Private Networks per page.
        :param server_id: Filter Private Networks by server ID.
        :param private_network_id: Filter Private Networks by Private Network ID.
        :param organization_id: Filter Private Networks by Organization ID.
        :param project_id: Filter Private Networks by Project ID.
        :return: :class:`List[ListServerPrivateNetworksResponse] <List[ListServerPrivateNetworksResponse]>`

        Usage:
        ::

            result = await api.list_server_private_networks_all()
        """

        return await fetch_all_pages_async(
            type=ListServerPrivateNetworksResponse,
            key="server_private_networks",
            fetcher=self.list_server_private_networks,
            args={
                "zone": zone,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "server_id": server_id,
                "private_network_id": private_network_id,
                "organization_id": organization_id,
                "project_id": project_id,
            },
        )

    async def delete_server_private_network(
        self,
        *,
        server_id: str,
        private_network_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a Private Network
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param server_id: The ID of the server.
        :param private_network_id: The ID of the Private Network.

        Usage:
        ::

            result = await api.delete_server_private_network(
                server_id="example",
                private_network_id="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_server_id = validate_path_param("server_id", server_id)
        param_private_network_id = validate_path_param(
            "private_network_id", private_network_id
        )

        res = self._request(
            "DELETE",
            f"/baremetal/v1/zones/{param_zone}/servers/{param_server_id}/private-networks/{param_private_network_id}",
        )

        self._throw_on_error(res)
        return None
