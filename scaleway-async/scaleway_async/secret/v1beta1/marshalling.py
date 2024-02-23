# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from typing import Any, Dict

from scaleway_core.profile import ProfileDefaults
from dateutil import parser
from .types import (
    EphemeralPolicyAction,
    Product,
    SecretType,
    AccessSecretVersionResponse,
    BrowseSecretsResponse,
    BrowseSecretsResponseItem,
    BrowseSecretsResponseItemFolderDetails,
    BrowseSecretsResponseItemSecretDetails,
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


def unmarshal_EphemeralPolicy(data: Any) -> EphemeralPolicy:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EphemeralPolicy' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("expires_once_accessed", None)
    args["expires_once_accessed"] = field

    field = data.get("time_to_live", None)
    args["time_to_live"] = field

    return EphemeralPolicy(**args)


def unmarshal_BrowseSecretsResponseItemFolderDetails(
    data: Any,
) -> BrowseSecretsResponseItemFolderDetails:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BrowseSecretsResponseItemFolderDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    return BrowseSecretsResponseItemFolderDetails(**args)


def unmarshal_BrowseSecretsResponseItemSecretDetails(
    data: Any,
) -> BrowseSecretsResponseItemSecretDetails:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BrowseSecretsResponseItemSecretDetails' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ephemeral_policy", None)
    args["ephemeral_policy"] = (
        unmarshal_EphemeralPolicy(field) if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("protected", None)
    args["protected"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("version_count", None)
    args["version_count"] = field

    return BrowseSecretsResponseItemSecretDetails(**args)


def unmarshal_EphemeralProperties(data: Any) -> EphemeralProperties:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'EphemeralProperties' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("action", None)
    args["action"] = field

    field = data.get("expires_at", None)
    args["expires_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("expires_once_accessed", None)
    args["expires_once_accessed"] = field

    return EphemeralProperties(**args)


def unmarshal_BrowseSecretsResponseItem(data: Any) -> BrowseSecretsResponseItem:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BrowseSecretsResponseItem' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("folder", None)
    args["folder"] = (
        unmarshal_BrowseSecretsResponseItemFolderDetails(field)
        if field is not None
        else None
    )

    field = data.get("name", None)
    args["name"] = field

    field = data.get("secret", None)
    args["secret"] = (
        unmarshal_BrowseSecretsResponseItemSecretDetails(field)
        if field is not None
        else None
    )

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return BrowseSecretsResponseItem(**args)


def unmarshal_Secret(data: Any) -> Secret:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'Secret' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("ephemeral_policy", None)
    args["ephemeral_policy"] = (
        unmarshal_EphemeralPolicy(field) if field is not None else None
    )

    field = data.get("id", None)
    args["id"] = field

    field = data.get("managed", None)
    args["managed"] = field

    field = data.get("name", None)
    args["name"] = field

    field = data.get("path", None)
    args["path"] = field

    field = data.get("project_id", None)
    args["project_id"] = field

    field = data.get("protected", None)
    args["protected"] = field

    field = data.get("region", None)
    args["region"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("tags", None)
    args["tags"] = field

    field = data.get("type", None)
    args["type_"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("version_count", None)
    args["version_count"] = field

    return Secret(**args)


def unmarshal_SecretVersion(data: Any) -> SecretVersion:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'SecretVersion' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("created_at", None)
    args["created_at"] = parser.isoparse(field) if type(field) is str else field

    field = data.get("description", None)
    args["description"] = field

    field = data.get("ephemeral_properties", None)
    args["ephemeral_properties"] = (
        unmarshal_EphemeralProperties(field) if field is not None else None
    )

    field = data.get("latest", None)
    args["latest"] = field

    field = data.get("revision", None)
    args["revision"] = field

    field = data.get("secret_id", None)
    args["secret_id"] = field

    field = data.get("status", None)
    args["status"] = field

    field = data.get("updated_at", None)
    args["updated_at"] = parser.isoparse(field) if type(field) is str else field

    return SecretVersion(**args)


def unmarshal_AccessSecretVersionResponse(data: Any) -> AccessSecretVersionResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'AccessSecretVersionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("data", None)
    args["data"] = field

    field = data.get("data_crc32", None)
    args["data_crc32"] = field

    field = data.get("revision", None)
    args["revision"] = field

    field = data.get("secret_id", None)
    args["secret_id"] = field

    return AccessSecretVersionResponse(**args)


def unmarshal_BrowseSecretsResponse(data: Any) -> BrowseSecretsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'BrowseSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("current_path", None)
    args["current_path"] = field

    field = data.get("items", None)
    args["items"] = (
        [unmarshal_BrowseSecretsResponseItem(v) for v in field]
        if field is not None
        else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return BrowseSecretsResponse(**args)


def unmarshal_ListSecretVersionsResponse(data: Any) -> ListSecretVersionsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretVersionsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", None)
    args["total_count"] = field

    field = data.get("versions", None)
    args["versions"] = (
        [unmarshal_SecretVersion(v) for v in field] if field is not None else None
    )

    return ListSecretVersionsResponse(**args)


def unmarshal_ListSecretsResponse(data: Any) -> ListSecretsResponse:
    if type(data) is not dict:
        raise TypeError(
            f"Unmarshalling the type 'ListSecretsResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("secrets", None)
    args["secrets"] = (
        [unmarshal_Secret(v) for v in field] if field is not None else None
    )

    field = data.get("total_count", None)
    args["total_count"] = field

    return ListSecretsResponse(**args)


def marshal_EphemeralPolicy(
    request: EphemeralPolicy,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = EphemeralPolicyAction(request.action)

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    if request.time_to_live is not None:
        output["time_to_live"] = request.time_to_live

    return output


def marshal_EphemeralProperties(
    request: EphemeralProperties,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.action is not None:
        output["action"] = EphemeralPolicyAction(request.action)

    if request.expires_at is not None:
        output["expires_at"] = request.expires_at.astimezone().isoformat()

    if request.expires_once_accessed is not None:
        output["expires_once_accessed"] = request.expires_once_accessed

    return output


def marshal_AddSecretOwnerRequest(
    request: AddSecretOwnerRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.product is not None:
        output["product"] = Product(request.product)

    return output


def marshal_CreateSecretRequest(
    request: CreateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(
            request.ephemeral_policy, defaults
        )

    if request.name is not None:
        output["name"] = request.name

    if request.path is not None:
        output["path"] = request.path

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id

    if request.protected is not None:
        output["protected"] = request.protected

    if request.tags is not None:
        output["tags"] = request.tags

    if request.type_ is not None:
        output["type"] = SecretType(request.type_)

    return output


def marshal_CreateSecretVersionRequest(
    request: CreateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.data is not None:
        output["data"] = request.data

    if request.data_crc32 is not None:
        output["data_crc32"] = request.data_crc32

    if request.description is not None:
        output["description"] = request.description

    if request.disable_previous is not None:
        output["disable_previous"] = request.disable_previous

    return output


def marshal_UpdateSecretRequest(
    request: UpdateSecretRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.ephemeral_policy is not None:
        output["ephemeral_policy"] = marshal_EphemeralPolicy(
            request.ephemeral_policy, defaults
        )

    if request.name is not None:
        output["name"] = request.name

    if request.path is not None:
        output["path"] = request.path

    if request.tags is not None:
        output["tags"] = request.tags

    return output


def marshal_UpdateSecretVersionRequest(
    request: UpdateSecretVersionRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.description is not None:
        output["description"] = request.description

    if request.ephemeral_properties is not None:
        output["ephemeral_properties"] = marshal_EphemeralProperties(
            request.ephemeral_properties, defaults
        )

    return output