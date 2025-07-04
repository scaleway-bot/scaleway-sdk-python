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
    DnsRecordStatus,
    DnsRecordType,
    DnsRecordsStatus,
    DomainAction,
    DomainAvailabilityAction,
    DomainAvailabilityStatus,
    DomainDnsAction,
    DomainStatus,
    DomainZoneOwner,
    HostingStatus,
    ListDatabaseUsersRequestOrderBy,
    ListDatabasesRequestOrderBy,
    ListFtpAccountsRequestOrderBy,
    ListHostingsRequestOrderBy,
    ListMailAccountsRequestOrderBy,
    ListOffersRequestOrderBy,
    ListWebsitesRequestOrderBy,
    NameserverStatus,
    OfferOptionName,
    OfferOptionWarning,
    PlatformPlatformGroup,
    AutoConfigDomainDns,
    CheckUserOwnsDomainResponse,
    ControlPanel,
    ControlPanelApiListControlPanelsRequest,
    CreateDatabaseRequestUser,
    CreateHostingRequestDomainConfiguration,
    Database,
    DatabaseApiAssignDatabaseUserRequest,
    DatabaseApiChangeDatabaseUserPasswordRequest,
    DatabaseApiCreateDatabaseRequest,
    DatabaseApiCreateDatabaseUserRequest,
    DatabaseApiDeleteDatabaseRequest,
    DatabaseApiDeleteDatabaseUserRequest,
    DatabaseApiGetDatabaseRequest,
    DatabaseApiGetDatabaseUserRequest,
    DatabaseApiListDatabaseUsersRequest,
    DatabaseApiListDatabasesRequest,
    DatabaseApiUnassignDatabaseUserRequest,
    DatabaseUser,
    DnsApiCheckUserOwnsDomainRequest,
    DnsApiGetDomainDnsRecordsRequest,
    DnsApiGetDomainRequest,
    DnsApiSearchDomainsRequest,
    DnsApiSyncDomainDnsRecordsRequest,
    DnsRecord,
    DnsRecords,
    Domain,
    DomainAvailability,
    FtpAccount,
    FtpAccountApiChangeFtpAccountPasswordRequest,
    FtpAccountApiCreateFtpAccountRequest,
    FtpAccountApiListFtpAccountsRequest,
    FtpAccountApiRemoveFtpAccountRequest,
    Hosting,
    HostingApiCreateHostingRequest,
    HostingApiCreateSessionRequest,
    HostingApiDeleteHostingRequest,
    HostingApiGetHostingRequest,
    HostingApiGetResourceSummaryRequest,
    HostingApiListHostingsRequest,
    HostingApiResetHostingPasswordRequest,
    HostingApiUpdateHostingRequest,
    HostingSummary,
    HostingUser,
    ListControlPanelsResponse,
    ListDatabaseUsersResponse,
    ListDatabasesResponse,
    ListFtpAccountsResponse,
    ListHostingsResponse,
    ListMailAccountsResponse,
    ListOffersResponse,
    ListWebsitesResponse,
    MailAccount,
    MailAccountApiChangeMailAccountPasswordRequest,
    MailAccountApiCreateMailAccountRequest,
    MailAccountApiListMailAccountsRequest,
    MailAccountApiRemoveMailAccountRequest,
    Nameserver,
    Offer,
    OfferApiListOffersRequest,
    OfferOption,
    OfferOptionRequest,
    Platform,
    PlatformControlPanel,
    PlatformControlPanelUrls,
    ResetHostingPasswordResponse,
    ResourceSummary,
    SearchDomainsResponse,
    Session,
    SyncDomainDnsRecordsRequestRecord,
    Website,
    WebsiteApiListWebsitesRequest,
)
from .content import (
    DOMAIN_AVAILABILITY_TRANSIENT_STATUSES,
    DOMAIN_TRANSIENT_STATUSES,
    HOSTING_TRANSIENT_STATUSES,
)
from .marshalling import (
    unmarshal_DatabaseUser,
    unmarshal_Database,
    unmarshal_FtpAccount,
    unmarshal_MailAccount,
    unmarshal_CheckUserOwnsDomainResponse,
    unmarshal_DnsRecords,
    unmarshal_Domain,
    unmarshal_Hosting,
    unmarshal_ListControlPanelsResponse,
    unmarshal_ListDatabaseUsersResponse,
    unmarshal_ListDatabasesResponse,
    unmarshal_ListFtpAccountsResponse,
    unmarshal_ListHostingsResponse,
    unmarshal_ListMailAccountsResponse,
    unmarshal_ListOffersResponse,
    unmarshal_ListWebsitesResponse,
    unmarshal_ResetHostingPasswordResponse,
    unmarshal_ResourceSummary,
    unmarshal_SearchDomainsResponse,
    unmarshal_Session,
    marshal_DatabaseApiAssignDatabaseUserRequest,
    marshal_DatabaseApiChangeDatabaseUserPasswordRequest,
    marshal_DatabaseApiCreateDatabaseRequest,
    marshal_DatabaseApiCreateDatabaseUserRequest,
    marshal_DatabaseApiUnassignDatabaseUserRequest,
    marshal_DnsApiCheckUserOwnsDomainRequest,
    marshal_DnsApiSyncDomainDnsRecordsRequest,
    marshal_FtpAccountApiChangeFtpAccountPasswordRequest,
    marshal_FtpAccountApiCreateFtpAccountRequest,
    marshal_HostingApiCreateHostingRequest,
    marshal_HostingApiUpdateHostingRequest,
    marshal_MailAccountApiChangeMailAccountPasswordRequest,
    marshal_MailAccountApiCreateMailAccountRequest,
    marshal_MailAccountApiRemoveMailAccountRequest,
)
from ...std.types import (
    LanguageCode as StdLanguageCode,
)

class WebhostingV1ControlPanelAPI(API):
    """
    This API allows you to manage your Web Hosting services.
    """
    def list_control_panels(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListControlPanelsResponse:
        """
        "List the control panels type: cpanel or plesk.".
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of control panels to return (must be a positive integer lower or equal to 100).
        :return: :class:`ListControlPanelsResponse <ListControlPanelsResponse>`
        
        Usage:
        ::
        
            result = api.list_control_panels()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/control-panels",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListControlPanelsResponse(res.json())
        
    def list_control_panels_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ControlPanel]:
        """
        "List the control panels type: cpanel or plesk.".
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of control panels to return (must be a positive integer lower or equal to 100).
        :return: :class:`List[ControlPanel] <List[ControlPanel]>`
        
        Usage:
        ::
        
            result = api.list_control_panels_all()
        """

        return  fetch_all_pages(
            type=ListControlPanelsResponse,
            key="control_panels",
            fetcher=self.list_control_panels,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
            },
        )
        

class WebhostingV1DatabaseAPI(API):
    """
    This API allows you to manage your databases and database users for your Web Hosting services.
    """
    def create_database(
        self,
        *,
        hosting_id: str,
        database_name: str,
        region: Optional[ScwRegion] = None,
        new_user: Optional[CreateDatabaseRequestUser] = None,
        existing_username: Optional[str] = None,
    ) -> Database:
        """
        "Create a new database within your hosting plan".
        :param hosting_id: UUID of the hosting plan where the database will be created.
        :param database_name: Name of the database to be created.
        :param region: Region to target. If none is passed will use default region from the config.
        :param new_user: (Optional) Username and password to create a user and link to the database.
        One-Of ('user'): at most one of 'new_user', 'existing_username' could be set.
        :param existing_username: (Optional) Username to link an existing user to the database.
        One-Of ('user'): at most one of 'new_user', 'existing_username' could be set.
        :return: :class:`Database <Database>`
        
        Usage:
        ::
        
            result = api.create_database(
                hosting_id="example",
                database_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases",
            body=marshal_DatabaseApiCreateDatabaseRequest(
                DatabaseApiCreateDatabaseRequest(
                    hosting_id=hosting_id,
                    database_name=database_name,
                    region=region,
                    new_user=new_user,
                    existing_username=existing_username,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())
        
    def list_databases(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
    ) -> ListDatabasesResponse:
        """
        "List all databases within your hosting plan".
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of databases to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of databases in the response.
        :return: :class:`ListDatabasesResponse <ListDatabasesResponse>`
        
        Usage:
        ::
        
            result = api.list_databases(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabasesResponse(res.json())
        
    def list_databases_all(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabasesRequestOrderBy] = None,
    ) -> List[Database]:
        """
        "List all databases within your hosting plan".
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of databases to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of databases in the response.
        :return: :class:`List[Database] <List[Database]>`
        
        Usage:
        ::
        
            result = api.list_databases_all(
                hosting_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListDatabasesResponse,
            key="databases",
            fetcher=self.list_databases,
            args={
                "hosting_id": hosting_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        
    def get_database(
        self,
        *,
        hosting_id: str,
        database_name: str,
        region: Optional[ScwRegion] = None,
    ) -> Database:
        """
        "Get details of a database within your hosting plan".
        :param hosting_id: UUID of the hosting plan.
        :param database_name: Name of the database.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`
        
        Usage:
        ::
        
            result = api.get_database(
                hosting_id="example",
                database_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_database_name = validate_path_param("database_name", database_name)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases/{param_database_name}",
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())
        
    def delete_database(
        self,
        *,
        hosting_id: str,
        database_name: str,
        region: Optional[ScwRegion] = None,
    ) -> Database:
        """
        "Delete a database within your hosting plan".
        :param hosting_id: UUID of the hosting plan.
        :param database_name: Name of the database to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Database <Database>`
        
        Usage:
        ::
        
            result = api.delete_database(
                hosting_id="example",
                database_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_database_name = validate_path_param("database_name", database_name)
        
        res = self._request(
            "DELETE",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases/{param_database_name}",
        )

        self._throw_on_error(res)
        return unmarshal_Database(res.json())
        
    def create_database_user(
        self,
        *,
        hosting_id: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Create a new database user".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the user to create.
        :param password: Password of the user to create.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.create_database_user(
                hosting_id="example",
                username="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases-users",
            body=marshal_DatabaseApiCreateDatabaseUserRequest(
                DatabaseApiCreateDatabaseUserRequest(
                    hosting_id=hosting_id,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        
    def list_database_users(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabaseUsersRequestOrderBy] = None,
    ) -> ListDatabaseUsersResponse:
        """
        "List all database users".
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of database users to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of database users in the response.
        :return: :class:`ListDatabaseUsersResponse <ListDatabaseUsersResponse>`
        
        Usage:
        ::
        
            result = api.list_database_users(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/database-users",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListDatabaseUsersResponse(res.json())
        
    def list_database_users_all(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListDatabaseUsersRequestOrderBy] = None,
    ) -> List[DatabaseUser]:
        """
        "List all database users".
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of database users to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of database users in the response.
        :return: :class:`List[DatabaseUser] <List[DatabaseUser]>`
        
        Usage:
        ::
        
            result = api.list_database_users_all(
                hosting_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListDatabaseUsersResponse,
            key="users",
            fetcher=self.list_database_users,
            args={
                "hosting_id": hosting_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        
    def get_database_user(
        self,
        *,
        hosting_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Get details of a database user".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the database user to retrieve details.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.get_database_user(
                hosting_id="example",
                username="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_username = validate_path_param("username", username)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases-users/{param_username}",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        
    def delete_database_user(
        self,
        *,
        hosting_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Delete a database user".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the database user to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.delete_database_user(
                hosting_id="example",
                username="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_username = validate_path_param("username", username)
        
        res = self._request(
            "DELETE",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/database-users/{param_username}",
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        
    def change_database_user_password(
        self,
        *,
        hosting_id: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Change the password of a database user".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the user to update.
        :param password: New password.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.change_database_user_password(
                hosting_id="example",
                username="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_username = validate_path_param("username", username)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases-users/{param_username}/change-password",
            body=marshal_DatabaseApiChangeDatabaseUserPasswordRequest(
                DatabaseApiChangeDatabaseUserPasswordRequest(
                    hosting_id=hosting_id,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        
    def assign_database_user(
        self,
        *,
        hosting_id: str,
        username: str,
        database_name: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Assign a database user to a database".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the user to assign.
        :param database_name: Name of the database to be assigned.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.assign_database_user(
                hosting_id="example",
                username="example",
                database_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_database_name = validate_path_param("database_name", database_name)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases/{param_database_name}/assign-user",
            body=marshal_DatabaseApiAssignDatabaseUserRequest(
                DatabaseApiAssignDatabaseUserRequest(
                    hosting_id=hosting_id,
                    username=username,
                    database_name=database_name,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        
    def unassign_database_user(
        self,
        *,
        hosting_id: str,
        username: str,
        database_name: str,
        region: Optional[ScwRegion] = None,
    ) -> DatabaseUser:
        """
        "Unassign a database user from a database".
        :param hosting_id: UUID of the hosting plan.
        :param username: Name of the user to unassign.
        :param database_name: Name of the database to be unassigned.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DatabaseUser <DatabaseUser>`
        
        Usage:
        ::
        
            result = api.unassign_database_user(
                hosting_id="example",
                username="example",
                database_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_database_name = validate_path_param("database_name", database_name)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/databases/{param_database_name}/unassign-user",
            body=marshal_DatabaseApiUnassignDatabaseUserRequest(
                DatabaseApiUnassignDatabaseUserRequest(
                    hosting_id=hosting_id,
                    username=username,
                    database_name=database_name,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DatabaseUser(res.json())
        

class WebhostingV1DnsAPI(API):
    """
    This API allows you to manage your Web Hosting services.
    """
    def get_domain_dns_records(
        self,
        *,
        domain: str,
        region: Optional[ScwRegion] = None,
    ) -> DnsRecords:
        """
        Get DNS records.
        Get the set of DNS records of a specified domain associated with a Web Hosting plan's domain.
        :param domain: Domain associated with the DNS records.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`DnsRecords <DnsRecords>`
        
        Usage:
        ::
        
            result = api.get_domain_dns_records(
                domain="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_domain = validate_path_param("domain", domain)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/domains/{param_domain}/dns-records",
        )

        self._throw_on_error(res)
        return unmarshal_DnsRecords(res.json())
        
    def check_user_owns_domain(
        self,
        *,
        domain: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> CheckUserOwnsDomainResponse:
        """
        Check whether you own this domain or not.
        :param domain: Domain for which ownership is to be verified.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the project currently in use.
        :return: :class:`CheckUserOwnsDomainResponse <CheckUserOwnsDomainResponse>`
        
        Usage:
        ::
        
            result = api.check_user_owns_domain(
                domain="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_domain = validate_path_param("domain", domain)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/domains/{param_domain}/check-ownership",
            body=marshal_DnsApiCheckUserOwnsDomainRequest(
                DnsApiCheckUserOwnsDomainRequest(
                    domain=domain,
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_CheckUserOwnsDomainResponse(res.json())
        
    def sync_domain_dns_records(
        self,
        *,
        domain: str,
        region: Optional[ScwRegion] = None,
        update_web_records: Optional[bool] = None,
        update_mail_records: Optional[bool] = None,
        update_all_records: Optional[bool] = None,
        update_nameservers: Optional[bool] = None,
        custom_records: Optional[List[SyncDomainDnsRecordsRequestRecord]] = None,
        auto_config_domain_dns: Optional[AutoConfigDomainDns] = None,
    ) -> DnsRecords:
        """
        Synchronize your DNS records on the Elements Console and on cPanel.
        :param domain: Domain for which the DNS records will be synchronized.
        :param region: Region to target. If none is passed will use default region from the config.
        :param update_web_records: Whether or not to synchronize the web records (deprecated, use auto_config_domain_dns).
        :param update_mail_records: Whether or not to synchronize the mail records (deprecated, use auto_config_domain_dns).
        :param update_all_records: Whether or not to synchronize all types of records. This one has priority (deprecated, use auto_config_domain_dns).
        :param update_nameservers: Whether or not to synchronize domain nameservers (deprecated, use auto_config_domain_dns).
        :param custom_records: Custom records to synchronize.
        :param auto_config_domain_dns: Whether or not to synchronize each types of records.
        :return: :class:`DnsRecords <DnsRecords>`
        
        Usage:
        ::
        
            result = api.sync_domain_dns_records(
                domain="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_domain = validate_path_param("domain", domain)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/domains/{param_domain}/sync-domain-dns-records",
            body=marshal_DnsApiSyncDomainDnsRecordsRequest(
                DnsApiSyncDomainDnsRecordsRequest(
                    domain=domain,
                    region=region,
                    update_web_records=update_web_records,
                    update_mail_records=update_mail_records,
                    update_all_records=update_all_records,
                    update_nameservers=update_nameservers,
                    custom_records=custom_records,
                    auto_config_domain_dns=auto_config_domain_dns,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_DnsRecords(res.json())
        
    def search_domains(
        self,
        *,
        domain_name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SearchDomainsResponse:
        """
        Search for available domains based on domain name.
        :param domain_name: Domain name to search.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Scaleway Project in which to search the domain to create the Web Hosting plan.
        :return: :class:`SearchDomainsResponse <SearchDomainsResponse>`
        
        Usage:
        ::
        
            result = api.search_domains(
                domain_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/search-domains",
            params={
                "domain_name": domain_name,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SearchDomainsResponse(res.json())
        
    def get_domain(
        self,
        *,
        domain_name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> Domain:
        """
        Retrieve detailed information about a specific domain, including its status, DNS configuration, and ownership.
        :param domain_name: Domain name to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Scaleway Project in which to get the domain to create the Web Hosting plan.
        :return: :class:`Domain <Domain>`
        
        Usage:
        ::
        
            result = api.get_domain(
                domain_name="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_domain_name = validate_path_param("domain_name", domain_name)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/domains/{param_domain_name}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Domain(res.json())
        
    def wait_for_domain(
        self,
        *,
        domain_name: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        options: Optional[WaitForOptions[Domain, bool]] = None,
    ) -> Domain:
        """
        Retrieve detailed information about a specific domain, including its status, DNS configuration, and ownership.
        :param domain_name: Domain name to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Scaleway Project in which to get the domain to create the Web Hosting plan.
        :return: :class:`Domain <Domain>`
        
        Usage:
        ::
        
            result = api.get_domain(
                domain_name="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in DOMAIN_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_domain,
            options=options,
            args={
                "domain_name": domain_name,
                "region": region,
                "project_id": project_id,
            },
        )
        

class WebhostingV1OfferAPI(API):
    """
    This API allows you to manage your offer for your Web Hosting services.
    """
    def list_offers(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOffersRequestOrderBy] = None,
        hosting_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> ListOffersResponse:
        """
        List all available hosting offers along with their specific options.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of websites to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting offers in the response.
        :param hosting_id: UUID of the hosting plan.
        :param control_panels: Name of the control panel(s) to filter for.
        :return: :class:`ListOffersResponse <ListOffersResponse>`
        
        Usage:
        ::
        
            result = api.list_offers()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/offers",
            params={
                "control_panels": control_panels,
                "hosting_id": hosting_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListOffersResponse(res.json())
        
    def list_offers_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListOffersRequestOrderBy] = None,
        hosting_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> List[Offer]:
        """
        List all available hosting offers along with their specific options.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of websites to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting offers in the response.
        :param hosting_id: UUID of the hosting plan.
        :param control_panels: Name of the control panel(s) to filter for.
        :return: :class:`List[Offer] <List[Offer]>`
        
        Usage:
        ::
        
            result = api.list_offers_all()
        """

        return  fetch_all_pages(
            type=ListOffersResponse,
            key="offers",
            fetcher=self.list_offers,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "hosting_id": hosting_id,
                "control_panels": control_panels,
            },
        )
        

class WebhostingV1HostingAPI(API):
    """
    This API allows you to manage your Web Hosting services.
    """
    def create_hosting(
        self,
        *,
        offer_id: str,
        email: str,
        domain: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        offer_options: Optional[List[OfferOptionRequest]] = None,
        language: Optional[StdLanguageCode] = None,
        domain_configuration: Optional[CreateHostingRequestDomainConfiguration] = None,
        skip_welcome_email: Optional[bool] = None,
        auto_config_domain_dns: Optional[AutoConfigDomainDns] = None,
    ) -> Hosting:
        """
        Order a Web Hosting plan.
        Order a Web Hosting plan, specifying the offer type required via the `offer_id` parameter.
        :param offer_id: ID of the selected offer for the Web Hosting plan.
        :param email: Contact email for the Web Hosting client.
        :param domain: Domain name to link to the Web Hosting plan. You must already own this domain name, and have completed the DNS validation process beforehand.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Scaleway Project in which to create the Web Hosting plan.
        :param tags: List of tags for the Web Hosting plan.
        :param offer_options: List of the Web Hosting plan options IDs with their quantities.
        :param language: Default language for the control panel interface.
        :param domain_configuration: Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_config_domain_dns instead).
        :param skip_welcome_email: Indicates whether to skip a welcome email to the contact email containing hosting info.
        :param auto_config_domain_dns: Indicates whether to update hosting domain name servers and DNS records for domains managed by Scaleway Elements (deprecated, use auto_update_* fields instead).
        :return: :class:`Hosting <Hosting>`
        
        Usage:
        ::
        
            result = api.create_hosting(
                offer_id="example",
                email="example",
                domain="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings",
            body=marshal_HostingApiCreateHostingRequest(
                HostingApiCreateHostingRequest(
                    offer_id=offer_id,
                    email=email,
                    domain=domain,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    offer_options=offer_options,
                    language=language,
                    domain_configuration=domain_configuration,
                    skip_welcome_email=skip_welcome_email,
                    auto_config_domain_dns=auto_config_domain_dns,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())
        
    def list_hostings(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHostingsRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        statuses: Optional[List[HostingStatus]] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> ListHostingsResponse:
        """
        List all Web Hosting plans.
        List all of your existing Web Hosting plans. Various filters are available to limit the results, including filtering by domain, status, tag and Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting plans in the response.
        :param tags: Tags to filter for, only Web Hosting plans with matching tags will be returned.
        :param statuses: Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
        :param domain: Domain to filter for, only Web Hosting plans associated with this domain will be returned.
        :param project_id: Project ID to filter for, only Web Hosting plans from this Project will be returned.
        :param organization_id: Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
        :param control_panels: Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
        :return: :class:`ListHostingsResponse <ListHostingsResponse>`
        
        Usage:
        ::
        
            result = api.list_hostings()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings",
            params={
                "control_panels": control_panels,
                "domain": domain,
                "order_by": order_by,
                "organization_id": organization_id or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "statuses": statuses,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListHostingsResponse(res.json())
        
    def list_hostings_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListHostingsRequestOrderBy] = None,
        tags: Optional[List[str]] = None,
        statuses: Optional[List[HostingStatus]] = None,
        domain: Optional[str] = None,
        project_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        control_panels: Optional[List[str]] = None,
    ) -> List[HostingSummary]:
        """
        List all Web Hosting plans.
        List all of your existing Web Hosting plans. Various filters are available to limit the results, including filtering by domain, status, tag and Project ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number to return, from the paginated results (must be a positive integer).
        :param page_size: Number of Web Hosting plans to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting plans in the response.
        :param tags: Tags to filter for, only Web Hosting plans with matching tags will be returned.
        :param statuses: Statuses to filter for, only Web Hosting plans with matching statuses will be returned.
        :param domain: Domain to filter for, only Web Hosting plans associated with this domain will be returned.
        :param project_id: Project ID to filter for, only Web Hosting plans from this Project will be returned.
        :param organization_id: Organization ID to filter for, only Web Hosting plans from this Organization will be returned.
        :param control_panels: Name of the control panel to filter for, only Web Hosting plans from this control panel will be returned.
        :return: :class:`List[HostingSummary] <List[HostingSummary]>`
        
        Usage:
        ::
        
            result = api.list_hostings_all()
        """

        return  fetch_all_pages(
            type=ListHostingsResponse,
            key="hostings",
            fetcher=self.list_hostings,
            args={
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "tags": tags,
                "statuses": statuses,
                "domain": domain,
                "project_id": project_id,
                "organization_id": organization_id,
                "control_panels": control_panels,
            },
        )
        
    def get_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Hosting:
        """
        Get a Web Hosting plan.
        Get the details of one of your existing Web Hosting plans, specified by its `hosting_id`.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`
        
        Usage:
        ::
        
            result = api.get_hosting(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())
        
    def wait_for_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        options: Optional[WaitForOptions[Hosting, bool]] = None,
    ) -> Hosting:
        """
        Get a Web Hosting plan.
        Get the details of one of your existing Web Hosting plans, specified by its `hosting_id`.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`
        
        Usage:
        ::
        
            result = api.get_hosting(
                hosting_id="example",
            )
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in HOSTING_TRANSIENT_STATUSES

        return wait_for_resource(
            fetcher=self.get_hosting,
            options=options,
            args={
                "hosting_id": hosting_id,
                "region": region,
            },
        )
        
    def update_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        email: Optional[str] = None,
        tags: Optional[List[str]] = None,
        offer_options: Optional[List[OfferOptionRequest]] = None,
        offer_id: Optional[str] = None,
        protected: Optional[bool] = None,
    ) -> Hosting:
        """
        Update a Web Hosting plan.
        Update the details of one of your existing Web Hosting plans, specified by its `hosting_id`. You can update parameters including the contact email address, tags, options and offer.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :param email: New contact email for the Web Hosting plan.
        :param tags: New tags for the Web Hosting plan.
        :param offer_options: List of the Web Hosting plan options IDs with their quantities.
        :param offer_id: ID of the new offer for the Web Hosting plan.
        :param protected: Whether the hosting is protected or not.
        :return: :class:`Hosting <Hosting>`
        
        Usage:
        ::
        
            result = api.update_hosting(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "PATCH",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}",
            body=marshal_HostingApiUpdateHostingRequest(
                HostingApiUpdateHostingRequest(
                    hosting_id=hosting_id,
                    region=region,
                    email=email,
                    tags=tags,
                    offer_options=offer_options,
                    offer_id=offer_id,
                    protected=protected,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())
        
    def delete_hosting(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Hosting:
        """
        Delete a Web Hosting plan.
        Delete a Web Hosting plan, specified by its `hosting_id`. Note that deletion is not immediate: it will take place at the end of the calendar month, after which time your Web Hosting plan and all its data (files and emails) will be irreversibly lost.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Hosting <Hosting>`
        
        Usage:
        ::
        
            result = api.delete_hosting(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "DELETE",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Hosting(res.json())
        
    def create_session(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Session:
        """
        Create a user session.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Session <Session>`
        
        Usage:
        ::
        
            result = api.create_session(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/sessions",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Session(res.json())
        
    def reset_hosting_password(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ResetHostingPasswordResponse:
        """
        Reset a Web Hosting plan password.
        :param hosting_id: UUID of the hosting.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ResetHostingPasswordResponse <ResetHostingPasswordResponse>`
        
        Usage:
        ::
        
            result = api.reset_hosting_password(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/reset-password",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_ResetHostingPasswordResponse(res.json())
        
    def get_resource_summary(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
    ) -> ResourceSummary:
        """
        Get the total counts of websites, databases, email accounts, and FTP accounts of a Web Hosting plan.
        :param hosting_id: Hosting ID.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`ResourceSummary <ResourceSummary>`
        
        Usage:
        ::
        
            result = api.get_resource_summary(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/resource-summary",
        )

        self._throw_on_error(res)
        return unmarshal_ResourceSummary(res.json())
        

class WebhostingV1FtpAccountAPI(API):
    """
    This API allows you to manage your FTP accounts for your Web Hosting services.
    """
    def create_ftp_account(
        self,
        *,
        hosting_id: str,
        username: str,
        path: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> FtpAccount:
        """
        Create a new FTP account within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param username: Username for the new FTP account.
        :param path: Path for the new FTP account.
        :param password: Password for the new FTP account.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`FtpAccount <FtpAccount>`
        
        Usage:
        ::
        
            result = api.create_ftp_account(
                hosting_id="example",
                username="example",
                path="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/ftp-accounts",
            body=marshal_FtpAccountApiCreateFtpAccountRequest(
                FtpAccountApiCreateFtpAccountRequest(
                    hosting_id=hosting_id,
                    username=username,
                    path=path,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FtpAccount(res.json())
        
    def list_ftp_accounts(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFtpAccountsRequestOrderBy] = None,
        domain: Optional[str] = None,
    ) -> ListFtpAccountsResponse:
        """
        List all FTP accounts within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of FTP accounts to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of FTP accounts in the response.
        :param domain: Domain to filter the FTP accounts.
        :return: :class:`ListFtpAccountsResponse <ListFtpAccountsResponse>`
        
        Usage:
        ::
        
            result = api.list_ftp_accounts(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/ftp-accounts",
            params={
                "domain": domain,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFtpAccountsResponse(res.json())
        
    def list_ftp_accounts_all(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFtpAccountsRequestOrderBy] = None,
        domain: Optional[str] = None,
    ) -> List[FtpAccount]:
        """
        List all FTP accounts within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of FTP accounts to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of FTP accounts in the response.
        :param domain: Domain to filter the FTP accounts.
        :return: :class:`List[FtpAccount] <List[FtpAccount]>`
        
        Usage:
        ::
        
            result = api.list_ftp_accounts_all(
                hosting_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListFtpAccountsResponse,
            key="ftp_accounts",
            fetcher=self.list_ftp_accounts,
            args={
                "hosting_id": hosting_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "domain": domain,
            },
        )
        
    def remove_ftp_account(
        self,
        *,
        hosting_id: str,
        username: str,
        region: Optional[ScwRegion] = None,
    ) -> FtpAccount:
        """
        Delete a specific FTP account within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param username: Username of the FTP account to be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`FtpAccount <FtpAccount>`
        
        Usage:
        ::
        
            result = api.remove_ftp_account(
                hosting_id="example",
                username="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_username = validate_path_param("username", username)
        
        res = self._request(
            "DELETE",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/ftp-accounts/{param_username}",
        )

        self._throw_on_error(res)
        return unmarshal_FtpAccount(res.json())
        
    def change_ftp_account_password(
        self,
        *,
        hosting_id: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> FtpAccount:
        """
        :param hosting_id: UUID of the hosting plan.
        :param username: Username of the FTP account.
        :param password: New password for the FTP account.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`FtpAccount <FtpAccount>`
        
        Usage:
        ::
        
            result = api.change_ftp_account_password(
                hosting_id="example",
                username="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        param_username = validate_path_param("username", username)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/ftp-accounts/{param_username}/change-password",
            body=marshal_FtpAccountApiChangeFtpAccountPasswordRequest(
                FtpAccountApiChangeFtpAccountPasswordRequest(
                    hosting_id=hosting_id,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_FtpAccount(res.json())
        

class WebhostingV1MailAccountAPI(API):
    """
    This API allows you to manage your mail accounts for your Web Hosting services.
    """
    def create_mail_account(
        self,
        *,
        hosting_id: str,
        domain: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> MailAccount:
        """
        Create a new mail account within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param domain: Domain part of the mail account address.
        :param username: Username part address of the mail account address.
        :param password: Password for the new mail account.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`MailAccount <MailAccount>`
        
        Usage:
        ::
        
            result = api.create_mail_account(
                hosting_id="example",
                domain="example",
                username="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/mail-accounts",
            body=marshal_MailAccountApiCreateMailAccountRequest(
                MailAccountApiCreateMailAccountRequest(
                    hosting_id=hosting_id,
                    domain=domain,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_MailAccount(res.json())
        
    def list_mail_accounts(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListMailAccountsRequestOrderBy] = None,
        domain: Optional[str] = None,
    ) -> ListMailAccountsResponse:
        """
        List all mail accounts within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of mail accounts to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of mail accounts in the response.
        :param domain: Domain to filter the mail accounts.
        :return: :class:`ListMailAccountsResponse <ListMailAccountsResponse>`
        
        Usage:
        ::
        
            result = api.list_mail_accounts(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/mail-accounts",
            params={
                "domain": domain,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListMailAccountsResponse(res.json())
        
    def list_mail_accounts_all(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListMailAccountsRequestOrderBy] = None,
        domain: Optional[str] = None,
    ) -> List[MailAccount]:
        """
        List all mail accounts within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of mail accounts to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order of mail accounts in the response.
        :param domain: Domain to filter the mail accounts.
        :return: :class:`List[MailAccount] <List[MailAccount]>`
        
        Usage:
        ::
        
            result = api.list_mail_accounts_all(
                hosting_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListMailAccountsResponse,
            key="mail_accounts",
            fetcher=self.list_mail_accounts,
            args={
                "hosting_id": hosting_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
                "domain": domain,
            },
        )
        
    def remove_mail_account(
        self,
        *,
        hosting_id: str,
        domain: str,
        username: str,
        region: Optional[ScwRegion] = None,
    ) -> MailAccount:
        """
        Delete a mail account within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param domain: Domain part of the mail account address.
        :param username: Username part of the mail account address.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`MailAccount <MailAccount>`
        
        Usage:
        ::
        
            result = api.remove_mail_account(
                hosting_id="example",
                domain="example",
                username="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/remove-mail-account",
            body=marshal_MailAccountApiRemoveMailAccountRequest(
                MailAccountApiRemoveMailAccountRequest(
                    hosting_id=hosting_id,
                    domain=domain,
                    username=username,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_MailAccount(res.json())
        
    def change_mail_account_password(
        self,
        *,
        hosting_id: str,
        domain: str,
        username: str,
        password: str,
        region: Optional[ScwRegion] = None,
    ) -> MailAccount:
        """
        Update the password of a mail account within your hosting plan.
        :param hosting_id: UUID of the hosting plan.
        :param domain: Domain part of the mail account address.
        :param username: Username part of the mail account address.
        :param password: New password for the mail account.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`MailAccount <MailAccount>`
        
        Usage:
        ::
        
            result = api.change_mail_account_password(
                hosting_id="example",
                domain="example",
                username="example",
                password="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "POST",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/change-mail-password",
            body=marshal_MailAccountApiChangeMailAccountPasswordRequest(
                MailAccountApiChangeMailAccountPasswordRequest(
                    hosting_id=hosting_id,
                    domain=domain,
                    username=username,
                    password=password,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_MailAccount(res.json())
        

class WebhostingV1WebsiteAPI(API):
    """
    This API allows you to manage your websites for your Web Hosting services.
    """
    def list_websites(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWebsitesRequestOrderBy] = None,
    ) -> ListWebsitesResponse:
        """
        List all websites for a specific hosting.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of websites to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting websites in the response.
        :return: :class:`ListWebsitesResponse <ListWebsitesResponse>`
        
        Usage:
        ::
        
            result = api.list_websites(
                hosting_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_hosting_id = validate_path_param("hosting_id", hosting_id)
        
        res = self._request(
            "GET",
            f"/webhosting/v1/regions/{param_region}/hostings/{param_hosting_id}/websites",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListWebsitesResponse(res.json())
        
    def list_websites_all(
        self,
        *,
        hosting_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListWebsitesRequestOrderBy] = None,
    ) -> List[Website]:
        """
        List all websites for a specific hosting.
        :param hosting_id: UUID of the hosting plan.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: Page number (must be a positive integer).
        :param page_size: Number of websites to return (must be a positive integer lower or equal to 100).
        :param order_by: Sort order for Web Hosting websites in the response.
        :return: :class:`List[Website] <List[Website]>`
        
        Usage:
        ::
        
            result = api.list_websites_all(
                hosting_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListWebsitesResponse,
            key="websites",
            fetcher=self.list_websites,
            args={
                "hosting_id": hosting_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        
