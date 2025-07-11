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
    ListNatsAccountsRequestOrderBy,
    ListNatsCredentialsRequestOrderBy,
    ListSnsCredentialsRequestOrderBy,
    ListSqsCredentialsRequestOrderBy,
    SnsInfoStatus,
    SqsInfoStatus,
    File,
    ListNatsAccountsResponse,
    ListNatsCredentialsResponse,
    ListSnsCredentialsResponse,
    ListSqsCredentialsResponse,
    NatsAccount,
    NatsApiCreateNatsAccountRequest,
    NatsApiCreateNatsCredentialsRequest,
    NatsApiDeleteNatsAccountRequest,
    NatsApiDeleteNatsCredentialsRequest,
    NatsApiGetNatsAccountRequest,
    NatsApiGetNatsCredentialsRequest,
    NatsApiListNatsAccountsRequest,
    NatsApiListNatsCredentialsRequest,
    NatsApiUpdateNatsAccountRequest,
    NatsCredentials,
    SnsApiActivateSnsRequest,
    SnsApiCreateSnsCredentialsRequest,
    SnsApiDeactivateSnsRequest,
    SnsApiDeleteSnsCredentialsRequest,
    SnsApiGetSnsCredentialsRequest,
    SnsApiGetSnsInfoRequest,
    SnsApiListSnsCredentialsRequest,
    SnsApiUpdateSnsCredentialsRequest,
    SnsCredentials,
    SnsInfo,
    SnsPermissions,
    SqsApiActivateSqsRequest,
    SqsApiCreateSqsCredentialsRequest,
    SqsApiDeactivateSqsRequest,
    SqsApiDeleteSqsCredentialsRequest,
    SqsApiGetSqsCredentialsRequest,
    SqsApiGetSqsInfoRequest,
    SqsApiListSqsCredentialsRequest,
    SqsApiUpdateSqsCredentialsRequest,
    SqsCredentials,
    SqsInfo,
    SqsPermissions,
)
from .marshalling import (
    unmarshal_NatsAccount,
    unmarshal_NatsCredentials,
    unmarshal_SnsCredentials,
    unmarshal_SqsCredentials,
    unmarshal_ListNatsAccountsResponse,
    unmarshal_ListNatsCredentialsResponse,
    unmarshal_ListSnsCredentialsResponse,
    unmarshal_ListSqsCredentialsResponse,
    unmarshal_SnsInfo,
    unmarshal_SqsInfo,
    marshal_NatsApiCreateNatsAccountRequest,
    marshal_NatsApiCreateNatsCredentialsRequest,
    marshal_NatsApiUpdateNatsAccountRequest,
    marshal_SnsApiActivateSnsRequest,
    marshal_SnsApiCreateSnsCredentialsRequest,
    marshal_SnsApiDeactivateSnsRequest,
    marshal_SnsApiUpdateSnsCredentialsRequest,
    marshal_SqsApiActivateSqsRequest,
    marshal_SqsApiCreateSqsCredentialsRequest,
    marshal_SqsApiDeactivateSqsRequest,
    marshal_SqsApiUpdateSqsCredentialsRequest,
)

class MnqV1Beta1NatsAPI(API):
    """
    This API allows you to manage Scaleway NATS accounts.
    """
    def create_nats_account(
        self,
        *,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        project_id: Optional[str] = None,
    ) -> NatsAccount:
        """
        Create a NATS account.
        Create a NATS account associated with a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: NATS account name.
        :param project_id: Project containing the NATS account.
        :return: :class:`NatsAccount <NatsAccount>`
        
        Usage:
        ::
        
            result = api.create_nats_account()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts",
            body=marshal_NatsApiCreateNatsAccountRequest(
                NatsApiCreateNatsAccountRequest(
                    region=region,
                    name=name or random_name(prefix="mnq"),
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())
        
    def delete_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a NATS account.
        Delete a NATS account, specified by its NATS account ID. Note that deleting a NATS account is irreversible, and any credentials, streams, consumer and stored messages belonging to this NATS account will also be deleted.
        :param nats_account_id: ID of the NATS account to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_nats_account(
                nats_account_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)
        
        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
        )

        self._throw_on_error(res)
    def update_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
    ) -> NatsAccount:
        """
        Update the name of a NATS account.
        Update the name of a NATS account, specified by its NATS account ID.
        :param nats_account_id: ID of the NATS account to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: NATS account name.
        :return: :class:`NatsAccount <NatsAccount>`
        
        Usage:
        ::
        
            result = api.update_nats_account(
                nats_account_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)
        
        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
            body=marshal_NatsApiUpdateNatsAccountRequest(
                NatsApiUpdateNatsAccountRequest(
                    nats_account_id=nats_account_id,
                    region=region,
                    name=name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())
        
    def get_nats_account(
        self,
        *,
        nats_account_id: str,
        region: Optional[ScwRegion] = None,
    ) -> NatsAccount:
        """
        Get a NATS account.
        Retrieve information about an existing NATS account identified by its NATS account ID. Its full details, including name and endpoint, are returned in the response.
        :param nats_account_id: ID of the NATS account to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`NatsAccount <NatsAccount>`
        
        Usage:
        ::
        
            result = api.get_nats_account(
                nats_account_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_nats_account_id = validate_path_param("nats_account_id", nats_account_id)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts/{param_nats_account_id}",
        )

        self._throw_on_error(res)
        return unmarshal_NatsAccount(res.json())
        
    def list_nats_accounts(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsAccountsRequestOrderBy] = None,
    ) -> ListNatsAccountsResponse:
        """
        List NATS accounts.
        List all NATS accounts in the specified region, for a Scaleway Organization or Project. By default, the NATS accounts returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of NATS accounts to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListNatsAccountsResponse <ListNatsAccountsResponse>`
        
        Usage:
        ::
        
            result = api.list_nats_accounts()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-accounts",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNatsAccountsResponse(res.json())
        
    def list_nats_accounts_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsAccountsRequestOrderBy] = None,
    ) -> List[NatsAccount]:
        """
        List NATS accounts.
        List all NATS accounts in the specified region, for a Scaleway Organization or Project. By default, the NATS accounts returned in the list are ordered by creation date in ascending order, though this can be modified via the `order_by` field.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of NATS accounts to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[NatsAccount] <List[NatsAccount]>`
        
        Usage:
        ::
        
            result = api.list_nats_accounts_all()
        """

        return  fetch_all_pages(
            type=ListNatsAccountsResponse,
            key="nats_accounts",
            fetcher=self.list_nats_accounts,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        
    def create_nats_credentials(
        self,
        *,
        nats_account_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
    ) -> NatsCredentials:
        """
        Create NATS credentials.
        Create a set of credentials for a NATS account, specified by its NATS account ID.
        :param nats_account_id: NATS account containing the credentials.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :return: :class:`NatsCredentials <NatsCredentials>`
        
        Usage:
        ::
        
            result = api.create_nats_credentials(
                nats_account_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials",
            body=marshal_NatsApiCreateNatsCredentialsRequest(
                NatsApiCreateNatsCredentialsRequest(
                    nats_account_id=nats_account_id,
                    region=region,
                    name=name or random_name(prefix="mnq"),
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_NatsCredentials(res.json())
        
    def delete_nats_credentials(
        self,
        *,
        nats_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete NATS credentials.
        Delete a set of credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can no longer be used to access the NATS account, and active connections using this credentials will be closed.
        :param nats_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_nats_credentials(
                nats_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_nats_credentials_id = validate_path_param("nats_credentials_id", nats_credentials_id)
        
        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials/{param_nats_credentials_id}",
        )

        self._throw_on_error(res)
    def get_nats_credentials(
        self,
        *,
        nats_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> NatsCredentials:
        """
        Get NATS credentials.
        Retrieve an existing set of credentials, identified by the `nats_credentials_id`. The credentials themselves are NOT returned, only their metadata (NATS account ID, credentials name, etc), are returned in the response.
        :param nats_credentials_id: ID of the credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`NatsCredentials <NatsCredentials>`
        
        Usage:
        ::
        
            result = api.get_nats_credentials(
                nats_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_nats_credentials_id = validate_path_param("nats_credentials_id", nats_credentials_id)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials/{param_nats_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_NatsCredentials(res.json())
        
    def list_nats_credentials(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        nats_account_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsCredentialsRequestOrderBy] = None,
    ) -> ListNatsCredentialsResponse:
        """
        List NATS credentials.
        List existing credentials in the specified NATS account. The response contains only the metadata for the credentials, not the credentials themselves, which are only returned after a **Create Credentials** call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param nats_account_id: Include only credentials for this NATS account.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListNatsCredentialsResponse <ListNatsCredentialsResponse>`
        
        Usage:
        ::
        
            result = api.list_nats_credentials()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/nats-credentials",
            params={
                "nats_account_id": nats_account_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListNatsCredentialsResponse(res.json())
        
    def list_nats_credentials_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        nats_account_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListNatsCredentialsRequestOrderBy] = None,
    ) -> List[NatsCredentials]:
        """
        List NATS credentials.
        List existing credentials in the specified NATS account. The response contains only the metadata for the credentials, not the credentials themselves, which are only returned after a **Create Credentials** call.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only NATS accounts in this Project.
        :param nats_account_id: Include only credentials for this NATS account.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[NatsCredentials] <List[NatsCredentials]>`
        
        Usage:
        ::
        
            result = api.list_nats_credentials_all()
        """

        return  fetch_all_pages(
            type=ListNatsCredentialsResponse,
            key="nats_credentials",
            fetcher=self.list_nats_credentials,
            args={
                "region": region,
                "project_id": project_id,
                "nats_account_id": nats_account_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        

class MnqV1Beta1SnsAPI(API):
    """
    This API allows you to manage your Scaleway Topics and Events.
    """
    def activate_sns(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Activate Topics and Events.
        Activate Topics and Events for the specified Project ID. Topics and Events must be activated before any usage. Activating Topics and Events does not trigger any billing, and you can deactivate at any time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to activate the Topics and Events service.
        :return: :class:`SnsInfo <SnsInfo>`
        
        Usage:
        ::
        
            result = api.activate_sns()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/activate-sns",
            body=marshal_SnsApiActivateSnsRequest(
                SnsApiActivateSnsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())
        
    def get_sns_info(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Get Topics and Events info.
        Retrieve the Topics and Events information of the specified Project ID. Informations include the activation status and the Topics and Events API endpoint URL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project to retrieve Topics and Events info from.
        :return: :class:`SnsInfo <SnsInfo>`
        
        Usage:
        ::
        
            result = api.get_sns_info()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-info",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())
        
    def deactivate_sns(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SnsInfo:
        """
        Deactivate Topics and Events.
        Deactivate Topics and Events for the specified Project ID. You must delete all topics and credentials before this call or you need to set the force_delete parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to deactivate the Topics and Events service.
        :return: :class:`SnsInfo <SnsInfo>`
        
        Usage:
        ::
        
            result = api.deactivate_sns()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/deactivate-sns",
            body=marshal_SnsApiDeactivateSnsRequest(
                SnsApiDeactivateSnsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsInfo(res.json())
        
    def create_sns_credentials(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        permissions: Optional[SnsPermissions] = None,
    ) -> SnsCredentials:
        """
        Create Topics and Events credentials.
        Create a set of credentials for Topics and Events, specified by a Project ID. Credentials give the bearer access to topics, and the level of permissions can be defined granularly.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project containing the Topics and Events credentials.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SnsCredentials <SnsCredentials>`
        
        Usage:
        ::
        
            result = api.create_sns_credentials()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials",
            body=marshal_SnsApiCreateSnsCredentialsRequest(
                SnsApiCreateSnsCredentialsRequest(
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="mnq_sns"),
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())
        
    def delete_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete Topics and Events credentials.
        Delete a set of Topics and Events credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can then no longer be used to access Topics and Events.
        :param sns_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_sns_credentials(
                sns_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sns_credentials_id = validate_path_param("sns_credentials_id", sns_credentials_id)
        
        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
        )

        self._throw_on_error(res)
    def update_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        permissions: Optional[SnsPermissions] = None,
    ) -> SnsCredentials:
        """
        Update Topics and Events credentials.
        Update a set of Topics and Events credentials. You can update the credentials' name, or their permissions.
        :param sns_credentials_id: ID of the Topics and Events credentials to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SnsCredentials <SnsCredentials>`
        
        Usage:
        ::
        
            result = api.update_sns_credentials(
                sns_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sns_credentials_id = validate_path_param("sns_credentials_id", sns_credentials_id)
        
        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
            body=marshal_SnsApiUpdateSnsCredentialsRequest(
                SnsApiUpdateSnsCredentialsRequest(
                    sns_credentials_id=sns_credentials_id,
                    region=region,
                    name=name,
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())
        
    def get_sns_credentials(
        self,
        *,
        sns_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> SnsCredentials:
        """
        Get Topics and Events credentials.
        Retrieve an existing set of credentials, identified by the `credentials_id`. The credentials themselves, as well as their metadata (name, project ID etc), are returned in the response.
        :param sns_credentials_id: ID of the Topics and Events credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SnsCredentials <SnsCredentials>`
        
        Usage:
        ::
        
            result = api.get_sns_credentials(
                sns_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sns_credentials_id = validate_path_param("sns_credentials_id", sns_credentials_id)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials/{param_sns_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SnsCredentials(res.json())
        
    def list_sns_credentials(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSnsCredentialsRequestOrderBy] = None,
    ) -> ListSnsCredentialsResponse:
        """
        List Topics and Events credentials.
        List existing Topics and Events credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only Topics and Events credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListSnsCredentialsResponse <ListSnsCredentialsResponse>`
        
        Usage:
        ::
        
            result = api.list_sns_credentials()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sns-credentials",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnsCredentialsResponse(res.json())
        
    def list_sns_credentials_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSnsCredentialsRequestOrderBy] = None,
    ) -> List[SnsCredentials]:
        """
        List Topics and Events credentials.
        List existing Topics and Events credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only Topics and Events credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[SnsCredentials] <List[SnsCredentials]>`
        
        Usage:
        ::
        
            result = api.list_sns_credentials_all()
        """

        return  fetch_all_pages(
            type=ListSnsCredentialsResponse,
            key="sns_credentials",
            fetcher=self.list_sns_credentials,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        

class MnqV1Beta1SqsAPI(API):
    """
    This API allows you to manage your Scaleway Queues.
    """
    def activate_sqs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Activate Queues.
        Activate Queues for the specified Project ID. Queues must be activated before any usage such as creating credentials and queues. Activating Queues does not trigger any billing, and you can deactivate at any time.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to activate the Queues service.
        :return: :class:`SqsInfo <SqsInfo>`
        
        Usage:
        ::
        
            result = api.activate_sqs()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/activate-sqs",
            body=marshal_SqsApiActivateSqsRequest(
                SqsApiActivateSqsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())
        
    def get_sqs_info(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Get Queues info.
        Retrieve the Queues information of the specified Project ID. Informations include the activation status and the Queues API endpoint URL.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project to retrieve Queues info from.
        :return: :class:`SqsInfo <SqsInfo>`
        
        Usage:
        ::
        
            result = api.get_sqs_info()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-info",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())
        
    def deactivate_sqs(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> SqsInfo:
        """
        Deactivate Queues.
        Deactivate Queues for the specified Project ID. You must delete all queues and credentials before this call or you need to set the force_delete parameter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project on which to deactivate the Queues service.
        :return: :class:`SqsInfo <SqsInfo>`
        
        Usage:
        ::
        
            result = api.deactivate_sqs()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/deactivate-sqs",
            body=marshal_SqsApiDeactivateSqsRequest(
                SqsApiDeactivateSqsRequest(
                    region=region,
                    project_id=project_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsInfo(res.json())
        
    def create_sqs_credentials(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        name: Optional[str] = None,
        permissions: Optional[SqsPermissions] = None,
    ) -> SqsCredentials:
        """
        Create Queues credentials.
        Create a set of credentials for Queues, specified by a Project ID. Credentials give the bearer access to queues, and the level of permissions can be defined granularly.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Project containing the Queues credentials.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SqsCredentials <SqsCredentials>`
        
        Usage:
        ::
        
            result = api.create_sqs_credentials()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials",
            body=marshal_SqsApiCreateSqsCredentialsRequest(
                SqsApiCreateSqsCredentialsRequest(
                    region=region,
                    project_id=project_id,
                    name=name or random_name(prefix="mnq_sqs"),
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())
        
    def delete_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete Queues credentials.
        Delete a set of Queues credentials, specified by their credentials ID. Deleting credentials is irreversible and cannot be undone. The credentials can then no longer be used to access Queues.
        :param sqs_credentials_id: ID of the credentials to delete.
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_sqs_credentials(
                sqs_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sqs_credentials_id = validate_path_param("sqs_credentials_id", sqs_credentials_id)
        
        res = self._request(
            "DELETE",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
        )

        self._throw_on_error(res)
    def update_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        permissions: Optional[SqsPermissions] = None,
    ) -> SqsCredentials:
        """
        Update Queues credentials.
        Update a set of Queues credentials. You can update the credentials' name, or their permissions.
        :param sqs_credentials_id: ID of the Queues credentials to update.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Name of the credentials.
        :param permissions: Permissions associated with these credentials.
        :return: :class:`SqsCredentials <SqsCredentials>`
        
        Usage:
        ::
        
            result = api.update_sqs_credentials(
                sqs_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sqs_credentials_id = validate_path_param("sqs_credentials_id", sqs_credentials_id)
        
        res = self._request(
            "PATCH",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
            body=marshal_SqsApiUpdateSqsCredentialsRequest(
                SqsApiUpdateSqsCredentialsRequest(
                    sqs_credentials_id=sqs_credentials_id,
                    region=region,
                    name=name,
                    permissions=permissions,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())
        
    def get_sqs_credentials(
        self,
        *,
        sqs_credentials_id: str,
        region: Optional[ScwRegion] = None,
    ) -> SqsCredentials:
        """
        Get Queues credentials.
        Retrieve an existing set of credentials, identified by the `credentials_id`. The credentials themselves, as well as their metadata (name, project ID etc), are returned in the response.
        :param sqs_credentials_id: ID of the Queues credentials to get.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SqsCredentials <SqsCredentials>`
        
        Usage:
        ::
        
            result = api.get_sqs_credentials(
                sqs_credentials_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_sqs_credentials_id = validate_path_param("sqs_credentials_id", sqs_credentials_id)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials/{param_sqs_credentials_id}",
        )

        self._throw_on_error(res)
        return unmarshal_SqsCredentials(res.json())
        
    def list_sqs_credentials(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSqsCredentialsRequestOrderBy] = None,
    ) -> ListSqsCredentialsResponse:
        """
        List Queues credentials.
        List existing Queues credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only Queues credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`ListSqsCredentialsResponse <ListSqsCredentialsResponse>`
        
        Usage:
        ::
        
            result = api.list_sqs_credentials()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/mnq/v1beta1/regions/{param_region}/sqs-credentials",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSqsCredentialsResponse(res.json())
        
    def list_sqs_credentials_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListSqsCredentialsRequestOrderBy] = None,
    ) -> List[SqsCredentials]:
        """
        List Queues credentials.
        List existing Queues credentials in the specified region. The response contains only the metadata for the credentials, not the credentials themselves.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Include only Queues credentials in this Project.
        :param page: Page number to return.
        :param page_size: Maximum number of credentials to return per page.
        :param order_by: Order in which to return results.
        :return: :class:`List[SqsCredentials] <List[SqsCredentials]>`
        
        Usage:
        ::
        
            result = api.list_sqs_credentials_all()
        """

        return  fetch_all_pages(
            type=ListSqsCredentialsResponse,
            key="sqs_credentials",
            fetcher=self.list_sqs_credentials,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )
        
