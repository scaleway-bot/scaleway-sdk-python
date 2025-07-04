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
    BrowseSecretsRequestOrderBy,
    EphemeralPolicyAction,
    ListSecretsRequestOrderBy,
    Product,
    SecretStatus,
    SecretType,
    SecretVersionStatus,
    AccessSecretVersionByPathRequest,
    AccessSecretVersionRequest,
    AccessSecretVersionResponse,
    AddSecretOwnerRequest,
    BasicCredentials,
    BrowseSecretsRequest,
    BrowseSecretsResponse,
    BrowseSecretsResponseItem,
    BrowseSecretsResponseItemFolderDetails,
    BrowseSecretsResponseItemSecretDetails,
    CreateSecretRequest,
    CreateSecretVersionRequest,
    DatabaseCredentials,
    DeleteSecretRequest,
    DeleteSecretVersionRequest,
    DisableSecretVersionRequest,
    EnableSecretVersionRequest,
    EphemeralPolicy,
    EphemeralProperties,
    GetSecretRequest,
    GetSecretVersionRequest,
    ListSecretTypesRequest,
    ListSecretTypesResponse,
    ListSecretVersionsRequest,
    ListSecretVersionsResponse,
    ListSecretsRequest,
    ListSecretsResponse,
    ListTagsRequest,
    ListTagsResponse,
    ProtectSecretRequest,
    RestoreSecretRequest,
    RestoreSecretVersionRequest,
    SSHKey,
    Secret,
    SecretVersion,
    UnprotectSecretRequest,
    UpdateSecretRequest,
    UpdateSecretVersionRequest,
)
from .marshalling import (
    unmarshal_SecretVersion,
    unmarshal_Secret,
    unmarshal_AccessSecretVersionResponse,
    unmarshal_BrowseSecretsResponse,
    unmarshal_ListSecretTypesResponse,
    unmarshal_ListSecretVersionsResponse,
    unmarshal_ListSecretsResponse,
    unmarshal_ListTagsResponse,
    marshal_AddSecretOwnerRequest,
    marshal_CreateSecretRequest,
    marshal_CreateSecretVersionRequest,
    marshal_UpdateSecretRequest,
    marshal_UpdateSecretVersionRequest,
)

class SecretV1Beta1API(API):
    """
    This API allows you to manage your Secret Manager services, for storing, accessing and sharing sensitive data such as passwords, API keys and certificates.
    """
    def create_secret(
        self,
        *,
        name: str,
        protected: bool,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        type_: Optional[SecretType] = None,
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
        key_id: Optional[str] = None,
    ) -> Secret:
        """
        Create a secret.
        Create a secret in a given region specified by the `region` parameter.
        :param name: Name of the secret.
        :param protected: A protected secret cannot be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the secret.
        :param tags: List of the secret's tags.
        :param description: Description of the secret.
        :param type_: (Optional.) See the `Secret.Type` enum for a description of values. If not specified, the type is `Opaque`.
        :param path: (Optional.) Location of the secret in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
        :param key_id: (Optional.) The Scaleway Key Manager key ID will be used to encrypt and decrypt secret versions. If not specified, Secret Manager will use a Key Manager internal key.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.create_secret(
                name="example",
                protected=False,
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets",
            body=marshal_CreateSecretRequest(
                CreateSecretRequest(
                    name=name,
                    protected=protected,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    description=description,
                    type_=type_,
                    path=path,
                    ephemeral_policy=ephemeral_policy,
                    key_id=key_id,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
    def get_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Secret:
        """
        Get metadata using the secret's ID.
        Retrieve the metadata of a secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.get_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
    def update_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
    ) -> Secret:
        """
        Update metadata of a secret.
        Edit a secret's metadata such as name, tag(s), description and ephemeral policy. The secret to update is specified by the `secret_id` and `region` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param name: Secret's updated name (optional).
        :param tags: Secret's updated list of tags (optional).
        :param description: Description of the secret.
        :param path: (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: (Optional.) Policy that defines whether/when a secret's versions expire.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.update_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "PATCH",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}",
            body=marshal_UpdateSecretRequest(
                UpdateSecretRequest(
                    secret_id=secret_id,
                    region=region,
                    name=name,
                    tags=tags,
                    description=description,
                    path=path,
                    ephemeral_policy=ephemeral_policy,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
    def delete_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a secret.
        Delete a given secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "DELETE",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
    def list_secrets(
        self,
        *,
        scheduled_for_deletion: bool,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral: Optional[bool] = None,
        type_: Optional[SecretType] = None,
    ) -> ListSecretsResponse:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param scheduled_for_deletion: Filter by whether the secret was scheduled for deletion / not scheduled for deletion. By default, it will display only not scheduled for deletion secrets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param order_by: 
        :param page: 
        :param page_size: 
        :param tags: List of tags to filter on (optional).
        :param name: Filter by secret name (optional).
        :param path: Filter by exact path (optional).
        :param ephemeral: Filter by ephemeral / not ephemeral (optional).
        :param type_: Filter by secret type (optional).
        :return: :class:`ListSecretsResponse <ListSecretsResponse>`
        
        Usage:
        ::
        
            result = api.list_secrets(
                scheduled_for_deletion=False,
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets",
            params={
                "ephemeral": ephemeral,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "path": path,
                "project_id": project_id or self.client.default_project_id,
                "scheduled_for_deletion": scheduled_for_deletion,
                "tags": tags,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretsResponse(res.json())
        
    def list_secrets_all(
        self,
        *,
        scheduled_for_deletion: bool,
        region: Optional[ScwRegion] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral: Optional[bool] = None,
        type_: Optional[SecretType] = None,
    ) -> List[Secret]:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param scheduled_for_deletion: Filter by whether the secret was scheduled for deletion / not scheduled for deletion. By default, it will display only not scheduled for deletion secrets.
        :param region: Region to target. If none is passed will use default region from the config.
        :param organization_id: Filter by Organization ID (optional).
        :param project_id: Filter by Project ID (optional).
        :param order_by: 
        :param page: 
        :param page_size: 
        :param tags: List of tags to filter on (optional).
        :param name: Filter by secret name (optional).
        :param path: Filter by exact path (optional).
        :param ephemeral: Filter by ephemeral / not ephemeral (optional).
        :param type_: Filter by secret type (optional).
        :return: :class:`List[Secret] <List[Secret]>`
        
        Usage:
        ::
        
            result = api.list_secrets_all(
                scheduled_for_deletion=False,
            )
        """

        return  fetch_all_pages(
            type=ListSecretsResponse,
            key="secrets",
            fetcher=self.list_secrets,
            args={
                "scheduled_for_deletion": scheduled_for_deletion,
                "region": region,
                "organization_id": organization_id,
                "project_id": project_id,
                "order_by": order_by,
                "page": page,
                "page_size": page_size,
                "tags": tags,
                "name": name,
                "path": path,
                "ephemeral": ephemeral,
                "type_": type_,
            },
        )
        
    def browse_secrets(
        self,
        *,
        prefix: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        order_by: Optional[BrowseSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        type_: Optional[SecretType] = None,
    ) -> BrowseSecretsResponse:
        """
        Browse secrets.
        Retrieve the list of secrets and folders for the given prefix. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param prefix: Filter secrets and folders for a given prefix (default /).
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param order_by: 
        :param page: 
        :param page_size: 
        :param tags: Filter secrets by tags.
        :param type_: Filter by secret type (optional).
        :return: :class:`BrowseSecretsResponse <BrowseSecretsResponse>`
        
        Usage:
        ::
        
            result = api.browse_secrets(
                prefix="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/browse",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "prefix": prefix,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
                "type": type_,
            },
        )

        self._throw_on_error(res)
        return unmarshal_BrowseSecretsResponse(res.json())
        
    def protect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Secret:
        """
        Enable secret protection.
        Enable secret protection for a given secret specified by the `secret_id` parameter. Enabling secret protection means that your secret can be read and modified, but it cannot be deleted.
        :param secret_id: ID of the secret to enable secret protection for.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.protect_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/protect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
    def unprotect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Secret:
        """
        Disable secret protection.
        Disable secret protection for a given secret specified by the `secret_id` parameter. Disabling secret protection means that your secret can be read, modified and deleted.
        :param secret_id: ID of the secret to disable secret protection for.
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.unprotect_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/unprotect",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
    def add_secret_owner(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
        product: Optional[Product] = None,
    ) -> None:
        """
        Allow a product to use the secret.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param product: See `Product` enum for description of values.
        
        Usage:
        ::
        
            result = api.add_secret_owner(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/add-owner",
            body=marshal_AddSecretOwnerRequest(
                AddSecretOwnerRequest(
                    secret_id=secret_id,
                    region=region,
                    product=product,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
    def create_secret_version(
        self,
        *,
        secret_id: str,
        data: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        data_crc32: Optional[int] = None,
    ) -> SecretVersion:
        """
        Create a version.
        Create a version of a given secret specified by the `region` and `secret_id` parameters.
        :param secret_id: ID of the secret.
        :param data: The base64-encoded secret payload of the version.
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the version.
        :param disable_previous: (Optional.) If there is no previous version or if the previous version was already disabled, does nothing.
        :param data_crc32: If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.create_secret_version(
                secret_id="example",
                data="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions",
            body=marshal_CreateSecretVersionRequest(
                CreateSecretVersionRequest(
                    secret_id=secret_id,
                    data=data,
                    region=region,
                    description=description,
                    disable_previous=disable_previous,
                    data_crc32=data_crc32,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def get_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> SecretVersion:
        """
        Get metadata of a secret's version using the secret's ID.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.get_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def update_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
        description: Optional[str] = None,
        ephemeral_properties: Optional[EphemeralProperties] = None,
    ) -> SecretVersion:
        """
        Update metadata of a version.
        Edit the metadata of a secret's given version, specified by the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :param description: Description of the version.
        :param ephemeral_properties: (Optional.) Properties that defines the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.update_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "PATCH",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
            body=marshal_UpdateSecretVersionRequest(
                UpdateSecretVersionRequest(
                    secret_id=secret_id,
                    revision=revision,
                    region=region,
                    description=description,
                    ephemeral_properties=ephemeral_properties,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def delete_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> None:
        """
        Delete a version.
        Delete a secret's version and the sensitive data contained in it. Deleting a version is permanent and cannot be undone.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        
        Usage:
        ::
        
            result = api.delete_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "DELETE",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
    def list_secret_versions(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: 
        :param page_size: 
        :param status: Filter results by status.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`
        
        Usage:
        ::
        
            result = api.list_secret_versions(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretVersionsResponse(res.json())
        
    def list_secret_versions_all(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param secret_id: ID of the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param page: 
        :param page_size: 
        :param status: Filter results by status.
        :return: :class:`List[SecretVersion] <List[SecretVersion]>`
        
        Usage:
        ::
        
            result = api.list_secret_versions_all(
                secret_id="example",
            )
        """

        return  fetch_all_pages(
            type=ListSecretVersionsResponse,
            key="versions",
            fetcher=self.list_secret_versions,
            args={
                "secret_id": secret_id,
                "region": region,
                "page": page,
                "page_size": page_size,
                "status": status,
            },
        )
        
    def access_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's ID.
        Access sensitive data in a secret's version specified by the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`
        
        Usage:
        ::
        
            result = api.access_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/access",
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())
        
    def access_secret_version_by_path(
        self,
        *,
        secret_path: str,
        secret_name: str,
        revision: str,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's name and path.
        Access sensitive data in a secret's version specified by the `region`, `secret_name`, `secret_path` and `revision` parameters.
        :param secret_path: Secret's path.
        :param secret_name: Secret's name.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - an integer (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`
        
        Usage:
        ::
        
            result = api.access_secret_version_by_path(
                secret_path="example",
                secret_name="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets-by-path/versions/{param_revision}/access",
            params={
                "project_id": project_id or self.client.default_project_id,
                "secret_name": secret_name,
                "secret_path": secret_path,
            },
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())
        
    def enable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> SecretVersion:
        """
        Enable a version.
        Make a specific version accessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.enable_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/enable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def disable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> SecretVersion:
        """
        Disable a version.
        Make a specific version inaccessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param secret_id: ID of the secret.
        :param revision: The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.disable_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/disable",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def list_tags(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListTagsResponse:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        :param page: 
        :param page_size: 
        :return: :class:`ListTagsResponse <ListTagsResponse>`
        
        Usage:
        ::
        
            result = api.list_tags()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/tags",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListTagsResponse(res.json())
        
    def list_tags_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[str]:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        :param page: 
        :param page_size: 
        :return: :class:`List[str] <List[str]>`
        
        Usage:
        ::
        
            result = api.list_tags_all()
        """

        return  fetch_all_pages(
            type=ListTagsResponse,
            key="tags",
            fetcher=self.list_tags,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )
        
    def list_secret_types(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListSecretTypesResponse:
        """
        List secret types.
        List all secret types created within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        :param page: 
        :param page_size: 
        :return: :class:`ListSecretTypesResponse <ListSecretTypesResponse>`
        
        Usage:
        ::
        
            result = api.list_secret_types()
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        
        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secret-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretTypesResponse(res.json())
        
    def list_secret_types_all(
        self,
        *,
        region: Optional[ScwRegion] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SecretType]:
        """
        List secret types.
        List all secret types created within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        :param page: 
        :param page_size: 
        :return: :class:`List[SecretType] <List[SecretType]>`
        
        Usage:
        ::
        
            result = api.list_secret_types_all()
        """

        return  fetch_all_pages(
            type=ListSecretTypesResponse,
            key="types",
            fetcher=self.list_secret_types,
            args={
                "region": region,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
            },
        )
        
    def restore_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[ScwRegion] = None,
    ) -> SecretVersion:
        """
        Restore a version.
        Restore a secret's version specified by the `region`, `secret_id` and `revision` parameters.
        :param secret_id: 
        :param revision: 
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`SecretVersion <SecretVersion>`
        
        Usage:
        ::
        
            result = api.restore_secret_version(
                secret_id="example",
                revision="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())
        
    def restore_secret(
        self,
        *,
        secret_id: str,
        region: Optional[ScwRegion] = None,
    ) -> Secret:
        """
        Restore a secret.
        Restore a secret and all its versions scheduled for deletion specified by the `region` and `secret_id` parameters.
        :param secret_id: 
        :param region: Region to target. If none is passed will use default region from the config.
        :return: :class:`Secret <Secret>`
        
        Usage:
        ::
        
            result = api.restore_secret(
                secret_id="example",
            )
        """
        
        param_region = validate_path_param("region", region or self.client.default_region)
        param_secret_id = validate_path_param("secret_id", secret_id)
        
        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/restore",
            body={},
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())
        
