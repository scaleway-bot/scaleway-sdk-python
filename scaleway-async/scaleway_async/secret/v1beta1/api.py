# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages_async,
    validate_path_param,
)
from .types import (
    BrowseSecretsRequestOrderBy,
    ListSecretsRequestOrderBy,
    Product,
    SecretType,
    SecretVersionStatus,
    AccessSecretVersionResponse,
    BrowseSecretsResponse,
    EphemeralPolicy,
    EphemeralProperties,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    UpdateSecretRequest,
    AddSecretOwnerRequest,
    CreateSecretVersionRequest,
    UpdateSecretVersionRequest,
)
from .marshalling import (
    marshal_AddSecretOwnerRequest,
    marshal_CreateSecretRequest,
    marshal_CreateSecretVersionRequest,
    marshal_UpdateSecretRequest,
    marshal_UpdateSecretVersionRequest,
    unmarshal_Secret,
    unmarshal_SecretVersion,
    unmarshal_AccessSecretVersionResponse,
    unmarshal_BrowseSecretsResponse,
    unmarshal_ListSecretVersionsResponse,
    unmarshal_ListSecretsResponse,
)


class SecretV1Beta1API(API):
    """
    Secret Manager API.

    This API allows you to conveniently store, access and share sensitive data such as passwords, API keys and certificates.
    Secret Manager API.
    """

    async def create_secret(
        self,
        *,
        name: str,
        type_: SecretType,
        protected: bool,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
    ) -> Secret:
        """
        Create a secret.
        You must specify the `region` to create a secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the secret.
        :param name: Name of the secret.
        :param tags: List of the secret's tags.
        :param description: Description of the secret.
        :param type_: Type of the secret.
        (Optional.) See `Secret.Type` enum for description of values. If not specified, the type is `Opaque`.
        :param path: Path of the secret.
        (Optional.) Location of the secret in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: Ephemeral policy of the secret.
        (Optional.) Policy that defines whether/when a secret's versions expire. By default, the policy is applied to all the secret's versions.
        :param protected: Returns `true` if secret protection is enabled on a given secret.
        A protected secret cannot be deleted.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.create_secret(
                name="example",
                type_=unknown_type,
                protected=True,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets",
            body=marshal_CreateSecretRequest(
                CreateSecretRequest(
                    name=name,
                    type_=type_,
                    protected=protected,
                    region=region,
                    project_id=project_id,
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

    async def get_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Get metadata using the secret's ID.
        Retrieve the metadata of a secret specified by the `region` and `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.get_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def update_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral_policy: Optional[EphemeralPolicy] = None,
    ) -> Secret:
        """
        Update metadata of a secret.
        Edit a secret's metadata such as name, tag(s), description and ephemeral policy. The secret to update is specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param name: Secret's updated name (optional).
        :param tags: Secret's updated list of tags (optional).
        :param description: Description of the secret.
        :param path: Path of the folder.
        (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :param ephemeral_policy: Ephemeral policy of the secret.
        (Optional.) Policy that defines whether/when a secret's versions expire.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.update_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
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

    async def delete_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a secret.
        Delete a given secret specified by the `region` and `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.

        Usage:
        ::

            result = await api.delete_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return None

    async def list_secrets(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: ListSecretsRequestOrderBy = ListSecretsRequestOrderBy.NAME_ASC,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral: Optional[bool] = None,
    ) -> ListSecretsResponse:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
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
        :return: :class:`ListSecretsResponse <ListSecretsResponse>`

        Usage:
        ::

            result = await api.list_secrets()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets",
            params={
                "ephemeral": ephemeral,
                "name": name,
                "order_by": order_by,
                "organization_id": organization_id
                or self.client.default_organization_id,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "path": path,
                "project_id": project_id or self.client.default_project_id,
                "tags": tags,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretsResponse(res.json())

    async def list_secrets_all(
        self,
        *,
        region: Optional[Region] = None,
        organization_id: Optional[str] = None,
        project_id: Optional[str] = None,
        order_by: Optional[ListSecretsRequestOrderBy] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        name: Optional[str] = None,
        path: Optional[str] = None,
        ephemeral: Optional[bool] = None,
    ) -> List[Secret]:
        """
        List secrets.
        Retrieve the list of secrets created within an Organization and/or Project. You must specify either the `organization_id` or the `project_id` and the `region`.
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
        :return: :class:`List[ListSecretsResponse] <List[ListSecretsResponse]>`

        Usage:
        ::

            result = await api.list_secrets_all()
        """

        return await fetch_all_pages_async(
            type=ListSecretsResponse,
            key="secrets",
            fetcher=self.list_secrets,
            args={
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
            },
        )

    async def browse_secrets(
        self,
        *,
        order_by: BrowseSecretsRequestOrderBy,
        prefix: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> BrowseSecretsResponse:
        """
        Browse secrets.
        Retrieve the list of secrets and folders for the given prefix. You must specify either the `organization_id` or the `project_id` and the `region`.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param order_by:
        :param prefix: Filter secrets and folders for a given prefix (default /).
        :param page:
        :param page_size:
        :return: :class:`BrowseSecretsResponse <BrowseSecretsResponse>`

        Usage:
        ::

            result = await api.browse_secrets(
                order_by=name_asc,
                prefix="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/browse",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "prefix": prefix,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_BrowseSecretsResponse(res.json())

    async def protect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Enable secret protection.
        Enable secret protection for a given secret specified by the `secret_id` parameter. Enabling secret protection means that your secret can be read and modified, but it cannot be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret to enable secret protection for.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.protect_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/protect",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def unprotect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Disable secret protection.
        Disable secret protection for a given secret specified by the `secret_id` parameter. Disabling secret protection means that your secret can be read, modified and deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret to disable secret protection for.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = await api.unprotect_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/unprotect",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    async def add_secret_owner(
        self,
        *,
        secret_id: str,
        product: Product,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Allow a product to use the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param product: ID of the product to add.
        See `Product` enum for description of values.

        Usage:
        ::

            result = await api.add_secret_owner(
                secret_id="example",
                product=unknown_product,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/add-owner",
            body=marshal_AddSecretOwnerRequest(
                AddSecretOwnerRequest(
                    secret_id=secret_id,
                    product=product,
                    region=region,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    async def create_secret_version(
        self,
        *,
        secret_id: str,
        data: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        data_crc32: Optional[int] = None,
    ) -> SecretVersion:
        """
        Create a version.
        Create a version of a given secret specified by the `region` and `secret_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param data: The base64-encoded secret payload of the version.
        :param description: Description of the version.
        :param disable_previous: Disable the previous secret version.
        (Optional.) If there is no previous version or if the previous version was already disabled, does nothing.
        :param data_crc32: (Optional.) The CRC32 checksum of the data as a base-10 integer.
        If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.create_secret_version(
                secret_id="example",
                data="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
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

    async def get_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Get metadata of a secret's version using the secret's ID.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.get_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def update_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        ephemeral_properties: Optional[EphemeralProperties] = None,
    ) -> SecretVersion:
        """
        Update metadata of a version.
        Edit the metadata of a secret's given version, specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param description: Description of the version.
        :param ephemeral_properties: Ephemeral properties of the version.
        (Optional.) Properties that defines the version's expiration date, whether it expires after being accessed once, and the action to perform (disable or delete) once the version expires.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.update_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
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

    async def delete_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a version.
        Delete a secret's version and the sensitive data contained in it. Deleting a version is permanent and cannot be undone.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).

        Usage:
        ::

            result = await api.delete_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
        return None

    async def list_secret_versions(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`

        Usage:
        ::

            result = await api.list_secret_versions(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
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

    async def list_secret_versions_all(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's ID.
        Retrieve the list of a given secret's versions specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :return: :class:`List[ListSecretVersionsResponse] <List[ListSecretVersionsResponse]>`

        Usage:
        ::

            result = await api.list_secret_versions_all(secret_id="example")
        """

        return await fetch_all_pages_async(
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

    async def access_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's ID.
        Access sensitive data in a secret's version specified by the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`

        Usage:
        ::

            result = await api.access_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/access",
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())

    async def enable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Enable a version.
        Make a specific version accessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.enable_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/enable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    async def disable_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
        """
        Disable a version.
        Make a specific version inaccessible. You must specify the `region`, `secret_id` and `revision` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = await api.disable_secret_version(
                secret_id="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "POST",
            f"/secret-manager/v1beta1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/disable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())