# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from datetime import datetime
from typing import List, Optional

from scaleway_core.api import API
from scaleway_core.bridge import (
    Region,
)
from scaleway_core.utils import (
    fetch_all_pages,
    validate_path_param,
)
from .types import (
    ListFoldersRequestOrderBy,
    ListSecretsRequestOrderBy,
    Product,
    SecretEphemeralAction,
    SecretType,
    SecretVersionStatus,
    AccessSecretVersionResponse,
    Folder,
    ListFoldersResponse,
    ListSecretVersionsResponse,
    ListSecretsResponse,
    ListTagsResponse,
    PasswordGenerationParams,
    Secret,
    SecretVersion,
    CreateSecretRequest,
    CreateFolderRequest,
    UpdateSecretRequest,
    AddSecretOwnerRequest,
    CreateSecretVersionRequest,
    GeneratePasswordRequest,
    UpdateSecretVersionRequest,
)
from .marshalling import (
    marshal_AddSecretOwnerRequest,
    marshal_CreateFolderRequest,
    marshal_CreateSecretRequest,
    marshal_CreateSecretVersionRequest,
    marshal_GeneratePasswordRequest,
    marshal_UpdateSecretRequest,
    marshal_UpdateSecretVersionRequest,
    unmarshal_Folder,
    unmarshal_Secret,
    unmarshal_SecretVersion,
    unmarshal_AccessSecretVersionResponse,
    unmarshal_ListFoldersResponse,
    unmarshal_ListSecretVersionsResponse,
    unmarshal_ListSecretsResponse,
    unmarshal_ListTagsResponse,
)


class SecretV1Alpha1API(API):
    """
    Secret Manager API.

    Secret Manager API.
    This API allows you to conveniently store, access and share sensitive data.
    """

    def create_secret(
        self,
        *,
        name: str,
        type_: SecretType,
        ephemeral_action: SecretEphemeralAction,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
        expires_at: Optional[datetime] = None,
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
        :param expires_at: Expiration date of the secret.
        (Optional.) Date on which the secret will be deleted or deactivated.
        :param ephemeral_action: Action to be taken when the secret expires.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = api.create_secret(
                name="example",
                type_=unknown_secret_type,
                ephemeral_action=unknown_ephemeral_action,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets",
            body=marshal_CreateSecretRequest(
                CreateSecretRequest(
                    name=name,
                    type_=type_,
                    ephemeral_action=ephemeral_action,
                    region=region,
                    project_id=project_id,
                    tags=tags,
                    description=description,
                    path=path,
                    expires_at=expires_at,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def create_folder(
        self,
        *,
        name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Folder:
        """
        Create folder.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project containing the folder.
        :param name: Name of the folder.
        :param path: Path of the folder.
        (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :return: :class:`Folder <Folder>`

        Usage:
        ::

            result = api.create_folder(name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders",
            body=marshal_CreateFolderRequest(
                CreateFolderRequest(
                    name=name,
                    region=region,
                    project_id=project_id,
                    path=path,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Folder(res.json())

    def get_secret(
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

            result = api.get_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def get_secret_by_name(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> Secret:
        """
        Get metadata using the secret's name.
        Retrieve the metadata of a secret specified by the `region` and `secret_name` parameters.

        GetSecretByName usage is now deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`Secret <Secret>`
        :deprecated

        Usage:
        ::

            result = api.get_secret_by_name(secret_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def update_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
    ) -> Secret:
        """
        Update metadata of a secret.
        Edit a secret's metadata such as name, tag(s) and description. The secret to update is specified by the `secret_id` and `region` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param name: Secret's updated name (optional).
        :param tags: Secret's updated list of tags (optional).
        :param description: Description of the secret.
        :param path: Path of the folder.
        (Optional.) Location of the folder in the directory structure. If not specified, the path is `/`.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = api.update_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "PATCH",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
            body=marshal_UpdateSecretRequest(
                UpdateSecretRequest(
                    secret_id=secret_id,
                    region=region,
                    name=name,
                    tags=tags,
                    description=description,
                    path=path,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def list_secrets(
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
        is_managed: Optional[bool] = None,
        path: Optional[str] = None,
        is_ephemeral: Optional[bool] = None,
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
        :param is_managed: Filter by managed / not managed (optional).
        :param path: Filter by path (optional).
        :param is_ephemeral: Filter by ephemeral / not ephemeral (optional).
        :return: :class:`ListSecretsResponse <ListSecretsResponse>`

        Usage:
        ::

            result = api.list_secrets()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets",
            params={
                "is_ephemeral": is_ephemeral,
                "is_managed": is_managed,
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

    def list_secrets_all(
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
        is_managed: Optional[bool] = None,
        path: Optional[str] = None,
        is_ephemeral: Optional[bool] = None,
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
        :param is_managed: Filter by managed / not managed (optional).
        :param path: Filter by path (optional).
        :param is_ephemeral: Filter by ephemeral / not ephemeral (optional).
        :return: :class:`List[ListSecretsResponse] <List[ListSecretsResponse]>`

        Usage:
        ::

            result = api.list_secrets_all()
        """

        return fetch_all_pages(
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
                "is_managed": is_managed,
                "path": path,
                "is_ephemeral": is_ephemeral,
            },
        )

    def list_folders(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: ListFoldersRequestOrderBy = ListFoldersRequestOrderBy.CREATED_AT_ASC,
    ) -> ListFoldersResponse:
        """
        List folders.
        Retrieve the list of folders created within a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param path: Filter by path (optional).
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`ListFoldersResponse <ListFoldersResponse>`

        Usage:
        ::

            result = api.list_folders()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders",
            params={
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "path": path,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListFoldersResponse(res.json())

    def list_folders_all(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        path: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        order_by: Optional[ListFoldersRequestOrderBy] = None,
    ) -> List[Folder]:
        """
        List folders.
        Retrieve the list of folders created within a Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: Filter by Project ID (optional).
        :param path: Filter by path (optional).
        :param page:
        :param page_size:
        :param order_by:
        :return: :class:`List[ListFoldersResponse] <List[ListFoldersResponse]>`

        Usage:
        ::

            result = api.list_folders_all()
        """

        return fetch_all_pages(
            type=ListFoldersResponse,
            key="folders",
            fetcher=self.list_folders,
            args={
                "region": region,
                "project_id": project_id,
                "path": path,
                "page": page,
                "page_size": page_size,
                "order_by": order_by,
            },
        )

    def delete_secret(
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

            result = api.delete_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}",
        )

        self._throw_on_error(res)
        return None

    def delete_folder(
        self,
        *,
        folder_id: str,
        region: Optional[Region] = None,
    ) -> Optional[None]:
        """
        Delete a given folder specified by the `region` and `folder_id` parameters.
        :param region: Region to target. If none is passed will use default region from the config.
        :param folder_id: ID of the folder.

        Usage:
        ::

            result = api.delete_folder(folder_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_folder_id = validate_path_param("folder_id", folder_id)

        res = self._request(
            "DELETE",
            f"/secret-manager/v1alpha1/regions/{param_region}/folders/{param_folder_id}",
        )

        self._throw_on_error(res)
        return None

    def protect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Protect a secret.
        Protect a given secret specified by the `secret_id` parameter. A protected secret can be read and modified but cannot be deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret to protect.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = api.protect_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/protect",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def unprotect_secret(
        self,
        *,
        secret_id: str,
        region: Optional[Region] = None,
    ) -> Secret:
        """
        Unprotect a secret.
        Unprotect a given secret specified by the `secret_id` parameter. An unprotected secret can be read, modified and deleted.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret to unprotect.
        :return: :class:`Secret <Secret>`

        Usage:
        ::

            result = api.unprotect_secret(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/unprotect",
        )

        self._throw_on_error(res)
        return unmarshal_Secret(res.json())

    def add_secret_owner(
        self,
        *,
        secret_id: str,
        product: Product,
        region: Optional[Region] = None,
        product_name: Optional[str] = None,
    ) -> Optional[None]:
        """
        Allow a product to use the secret.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param product_name: (Deprecated: use `product` field) Name of the product to add.
        :param product: ID of the product to add.
        See `Product` enum for description of values.

        Usage:
        ::

            result = api.add_secret_owner(
                secret_id="example",
                product=unknown,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/add-owner",
            body=marshal_AddSecretOwnerRequest(
                AddSecretOwnerRequest(
                    secret_id=secret_id,
                    product=product,
                    region=region,
                    product_name=product_name,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return None

    def create_secret_version(
        self,
        *,
        secret_id: str,
        data: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        password_generation: Optional[PasswordGenerationParams] = None,
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
        :param password_generation: Options to generate a password.
        (Optional.) If specified, a random password will be generated. The `data` and `data_crc32` fields must be empty. By default, the generator will use upper and lower case letters, and digits. This behavior can be tuned using the generation parameters.

        One-of ('_password_generation'): at most one of 'password_generation' could be set.
        :param data_crc32: (Optional.) The CRC32 checksum of the data as a base-10 integer.
        If specified, Secret Manager will verify the integrity of the data received against the given CRC32 checksum. An error is returned if the CRC32 does not match. If, however, the CRC32 matches, it will be stored and returned along with the SecretVersion on future access requests.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = api.create_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions",
            body=marshal_CreateSecretVersionRequest(
                CreateSecretVersionRequest(
                    secret_id=secret_id,
                    data=data,
                    region=region,
                    description=description,
                    disable_previous=disable_previous,
                    password_generation=password_generation,
                    data_crc32=data_crc32,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def generate_password(
        self,
        *,
        secret_id: str,
        length: int,
        region: Optional[Region] = None,
        description: Optional[str] = None,
        disable_previous: Optional[bool] = None,
        no_lowercase_letters: Optional[bool] = None,
        no_uppercase_letters: Optional[bool] = None,
        no_digits: Optional[bool] = None,
        additional_chars: Optional[str] = None,
    ) -> SecretVersion:
        """
        Generate a password in a new version.
        Generate a password for the given secret specified by the `region` and `secret_id` parameters. This will also create a new version of the secret that will store the password.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_id: ID of the secret.
        :param description: Description of the version.
        :param disable_previous: (Optional.) Disable the previous secret version.
        This has no effect if there is no previous version or if the previous version was already disabled.
        :param length: Length of the password to generate (between 1 and 1024 characters).
        :param no_lowercase_letters: (Optional.) Exclude lower case letters by default in the password character set.
        :param no_uppercase_letters: (Optional.) Exclude upper case letters by default in the password character set.
        :param no_digits: (Optional.) Exclude digits by default in the password character set.
        :param additional_chars: (Optional.) Additional ASCII characters to be included in the password character set.
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = api.generate_password(
                secret_id="example",
                length=1,
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "POST",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/generate-password",
            body=marshal_GeneratePasswordRequest(
                GeneratePasswordRequest(
                    secret_id=secret_id,
                    length=length,
                    region=region,
                    description=description,
                    disable_previous=disable_previous,
                    no_lowercase_letters=no_lowercase_letters,
                    no_uppercase_letters=no_uppercase_letters,
                    no_digits=no_digits,
                    additional_chars=additional_chars,
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

            result = api.get_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def get_secret_version_by_name(
        self,
        *,
        secret_name: str,
        revision: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> SecretVersion:
        """
        Get metadata of a secret's version using the secret's name.
        Retrieve the metadata of a secret's given version specified by the `region`, `secret_name`, `revision` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `GetSecretVersion` request.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
        :return: :class:`SecretVersion <SecretVersion>`
        :deprecated

        Usage:
        ::

            result = api.get_secret_version_by_name(
                secret_name="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions/{param_revision}",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def update_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
        description: Optional[str] = None,
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
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = api.update_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}",
            body=marshal_UpdateSecretVersionRequest(
                UpdateSecretVersionRequest(
                    secret_id=secret_id,
                    revision=revision,
                    region=region,
                    description=description,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def list_secret_versions(
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

            result = api.list_secret_versions(secret_id="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_id = validate_path_param("secret_id", secret_id)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions",
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

            result = api.list_secret_versions_all(secret_id="example")
        """

        return fetch_all_pages(
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

    def list_secret_versions_by_name(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
        project_id: Optional[str] = None,
    ) -> ListSecretVersionsResponse:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name`,`region` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `ListSecretVersions` request.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`ListSecretVersionsResponse <ListSecretVersionsResponse>`
        :deprecated

        Usage:
        ::

            result = api.list_secret_versions_by_name(secret_name="example")
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "status": status,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSecretVersionsResponse(res.json())

    def list_secret_versions_by_name_all(
        self,
        *,
        secret_name: str,
        region: Optional[Region] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        status: Optional[List[SecretVersionStatus]] = None,
        project_id: Optional[str] = None,
    ) -> List[SecretVersion]:
        """
        List versions of a secret using the secret's name.
        Retrieve the list of a given secret's versions specified by the `secret_name`,`region` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `ListSecretVersions` request.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param page:
        :param page_size:
        :param status: Filter results by status.
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for the secret in all Projects.
        :return: :class:`List[ListSecretVersionsResponse] <List[ListSecretVersionsResponse]>`
        :deprecated

        Usage:
        ::

            result = api.list_secret_versions_by_name_all(secret_name="example")
        """

        return fetch_all_pages(
            type=ListSecretVersionsResponse,
            key="versions",
            fetcher=self.list_secret_versions_by_name,
            args={
                "secret_name": secret_name,
                "region": region,
                "page": page,
                "page_size": page_size,
                "status": status,
                "project_id": project_id,
            },
        )

    def enable_secret_version(
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

            result = api.enable_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/enable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def disable_secret_version(
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

            result = api.disable_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/disable",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def access_secret_version(
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

            result = api.access_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/access",
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())

    def access_secret_version_by_name(
        self,
        *,
        secret_name: str,
        revision: str,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
    ) -> AccessSecretVersionResponse:
        """
        Access a secret's version using the secret's name.
        Access sensitive data in a secret's version specified by the `region`, `secret_name`, `revision` and `project_id` parameters.

        This method is deprecated.

        Scaleway recommends that you use the `ListSecrets` request with the `name` filter to specify the secret version desired, then use the `AccessSecretVersion` request.
        :param region: Region to target. If none is passed will use default region from the config.
        :param secret_name: Name of the secret.
        :param revision: Version number.
        The first version of the secret is numbered 1, and all subsequent revisions augment by 1. Value can be either:
        - a number (the revision number)
        - "latest" (the latest revision)
        - "latest_enabled" (the latest enabled revision).
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for the secret version in all Projects.
        :return: :class:`AccessSecretVersionResponse <AccessSecretVersionResponse>`
        :deprecated

        Usage:
        ::

            result = api.access_secret_version_by_name(
                secret_name="example",
                revision="example",
            )
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )
        param_secret_name = validate_path_param("secret_name", secret_name)
        param_revision = validate_path_param("revision", revision)

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets-by-name/{param_secret_name}/versions/{param_revision}/access",
            params={
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_AccessSecretVersionResponse(res.json())

    def destroy_secret_version(
        self,
        *,
        secret_id: str,
        revision: str,
        region: Optional[Region] = None,
    ) -> SecretVersion:
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
        :return: :class:`SecretVersion <SecretVersion>`

        Usage:
        ::

            result = api.destroy_secret_version(
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
            f"/secret-manager/v1alpha1/regions/{param_region}/secrets/{param_secret_id}/versions/{param_revision}/destroy",
        )

        self._throw_on_error(res)
        return unmarshal_SecretVersion(res.json())

    def list_tags(
        self,
        *,
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListTagsResponse:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for tags in all Projects.
        :param page:
        :param page_size:
        :return: :class:`ListTagsResponse <ListTagsResponse>`

        Usage:
        ::

            result = api.list_tags()
        """

        param_region = validate_path_param(
            "region", region or self.client.default_region
        )

        res = self._request(
            "GET",
            f"/secret-manager/v1alpha1/regions/{param_region}/tags",
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
        region: Optional[Region] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[str]:
        """
        List tags.
        List all tags associated with secrets within a given Project.
        :param region: Region to target. If none is passed will use default region from the config.
        :param project_id: ID of the Project to target.
        (Optional.) If not specified, Secret Manager will look for tags in all Projects.
        :param page:
        :param page_size:
        :return: :class:`List[ListTagsResponse] <List[ListTagsResponse]>`

        Usage:
        ::

            result = api.list_tags_all()
        """

        return fetch_all_pages(
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
