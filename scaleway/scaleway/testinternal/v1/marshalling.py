# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

from decimal import Decimal
from datetime import datetime
from typing import Any, Dict, List, Optional
from dateutil import parser

from scaleway_core.profile import ProfileDefaults
from scaleway_core.bridge import (
    Money,
    Region as ScwRegion,
    ScwFile,
    ServiceInfo,
    TimeSeries,
    TimeSeriesPoint,
    Zone as ScwZone,
    unmarshal_Money,
    marshal_Money,
    marshal_ScwFile,
    marshal_ServiceInfo,
    marshal_TimeSeries,
    unmarshal_TimeSeries,
)
from scaleway_core.utils import (
    OneOfPossibility,
    resolve_one_of,
)
from .types_private import (
    _GetRegionResponse,
)
from .types import (
    ComplexTestEnum,
    ListCharactersRequestOrderBy,
    MapEnum,
    PostAllOptionalMessageNestedEnum,
    PostAllTypesMessageNestedEnum,
    TransientStatus,
    Type,
    PostAllTypesMessageNestedMessage,
    PostAllTypesMessage,
    PostBodyAndPathSimpleMessage,
    EchoMessage,
    GetEnumMessage,
    GetZoneResponse,
    ListCharactersResponse,
    MetadataResponse,
    PatchEnumMessage,
    PostAllMapTypesMessage,
    PostAllOptionalMessageNestedMessage,
    PostAllOptionalMessageNestedMessageWithOptional,
    PostAllOptionalMessage,
    PostBodyAndPathAndQueryMessage,
    PostBodyAndPathComplexMessage,
    PostBodyAndPathSimple2Message,
    ComplexValidateMsg,
    PostComplexValidateMessage,
    PostDeprecatedOrganizationMessage,
    PostDeprecatedProjectMessage,
    PostEchoTimeSeriesMessage,
    PostEnumMessage,
    PostIPMessage,
    PostOneOfMessage,
    PostOrganizationIdMessage,
    PostProjectIdMessage,
    PostScalarTypesMessage,
    PostTagsMessage,
    Transient,
    PatchEnumRequest,
    PostAllMapTypesRequest,
    PostAllOptionalRequest,
    PostAllTypesRequest,
    PostBodyAndPathAndQueryRequest,
    PostBodyAndPathComplexRequest,
    PostBodyAndPathSimple2Request,
    PostBodyAndPathSimpleRequest,
    PostComplexValidateRequest,
    PostDeprecatedOrganizationRequest,
    PostDeprecatedProjectRequest,
    PostEchoRequest,
    PostEchoTimeSeriesRequest,
    PostEnumRequest,
    PostIPRequest,
    PostOneOfRequest,
    PostOrganizationIdRequest,
    PostProjectIdRequest,
    PostScalarTypesRequest,
    PostTagsRequest,
    PostWaitRequest,
    RegionalApiPostEchoRequest,
    ZoneApiPostEchoRequest,
)

def unmarshal_PostAllTypesMessageNestedMessage(data: Any) -> PostAllTypesMessageNestedMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllTypesMessageNestedMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bb", str())
    args["bb"] = field

    return PostAllTypesMessageNestedMessage(**args)

def unmarshal_PostAllTypesMessage(data: Any) -> PostAllTypesMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllTypesMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("singular_int32", 0)
    args["singular_int32"] = field

    field = data.get("singular_int64", 0)
    args["singular_int64"] = field

    field = data.get("singular_uint32", 0)
    args["singular_uint32"] = field

    field = data.get("singular_uint64", 0)
    args["singular_uint64"] = field

    field = data.get("singular_sint32", 0)
    args["singular_sint32"] = field

    field = data.get("singular_sint64", 0)
    args["singular_sint64"] = field

    field = data.get("singular_fixed32", 0)
    args["singular_fixed32"] = field

    field = data.get("singular_fixed64", 0)
    args["singular_fixed64"] = field

    field = data.get("singular_sfixed32", 0)
    args["singular_sfixed32"] = field

    field = data.get("singular_sfixed64", 0)
    args["singular_sfixed64"] = field

    field = data.get("singular_float", 0.0)
    args["singular_float"] = field

    field = data.get("singular_double", 0.0)
    args["singular_double"] = field

    field = data.get("singular_bool", False)
    args["singular_bool"] = field

    field = data.get("singular_string", str())
    args["singular_string"] = field

    field = data.get("singular_bytes", str())
    args["singular_bytes"] = field

    field = data.get("singular_nested_message", None)
    args["singular_nested_message"] = unmarshal_PostAllTypesMessageNestedMessage(field) if field is not None else None

    field = data.get("singular_nested_enum", getattr(PostAllTypesMessageNestedEnum, "ZERO"))
    args["singular_nested_enum"] = field

    field = data.get("repeated_int32", [])
    args["repeated_int32"] = field

    field = data.get("repeated_int64", [])
    args["repeated_int64"] = field

    field = data.get("repeated_uint32", [])
    args["repeated_uint32"] = field

    field = data.get("repeated_uint64", [])
    args["repeated_uint64"] = field

    field = data.get("repeated_sint32", [])
    args["repeated_sint32"] = field

    field = data.get("repeated_sint64", [])
    args["repeated_sint64"] = field

    field = data.get("repeated_fixed32", [])
    args["repeated_fixed32"] = field

    field = data.get("repeated_fixed64", [])
    args["repeated_fixed64"] = field

    field = data.get("repeated_sfixed32", [])
    args["repeated_sfixed32"] = field

    field = data.get("repeated_sfixed64", [])
    args["repeated_sfixed64"] = field

    field = data.get("repeated_float", [])
    args["repeated_float"] = field

    field = data.get("repeated_double", [])
    args["repeated_double"] = field

    field = data.get("repeated_bool", [])
    args["repeated_bool"] = field

    field = data.get("repeated_string", [])
    args["repeated_string"] = field

    field = data.get("repeated_bytes", [])
    args["repeated_bytes"] = field

    field = data.get("repeated_nested_message", [])
    args["repeated_nested_message"] = [unmarshal_PostAllTypesMessageNestedMessage(v) for v in field] if field is not None else None

    field = data.get("repeated_nested_enum", [])
    args["repeated_nested_enum"] = [PostAllTypesMessageNestedEnum(v) for v in field] if field is not None else None

    field = data.get("oneof_uint32", None)
    args["oneof_uint32"] = field

    field = data.get("oneof_nested_message", None)
    args["oneof_nested_message"] = unmarshal_PostAllTypesMessageNestedMessage(field) if field is not None else None

    field = data.get("oneof_string", None)
    args["oneof_string"] = field

    field = data.get("oneof_bytes", None)
    args["oneof_bytes"] = field

    field = data.get("singular_double_value", None)
    args["singular_double_value"] = field

    field = data.get("singular_float_value", None)
    args["singular_float_value"] = field

    field = data.get("singular_int64_value", None)
    args["singular_int64_value"] = field

    field = data.get("singular_uint64_value", None)
    args["singular_uint64_value"] = field

    field = data.get("singular_int32_value", None)
    args["singular_int32_value"] = field

    field = data.get("singular_uint32_value", None)
    args["singular_uint32_value"] = field

    field = data.get("singular_bool_value", None)
    args["singular_bool_value"] = field

    field = data.get("singular_string_value", None)
    args["singular_string_value"] = field

    field = data.get("singular_bytes_value", None)
    args["singular_bytes_value"] = field

    field = data.get("singular_timestamp", None)
    args["singular_timestamp"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("singular_any", None)
    args["singular_any"] = field

    field = data.get("singular_struct", None)
    args["singular_struct"] = field

    field = data.get("singular_money", None)
    args["singular_money"] = unmarshal_Money(field) if field is not None else None

    field = data.get("singular_strings_value", None)
    args["singular_strings_value"] = field

    field = data.get("singular_duration", None)
    args["singular_duration"] = field

    field = data.get("singular_ip", None)
    args["singular_ip"] = field

    field = data.get("singular_string_ip", str())
    args["singular_string_ip"] = field

    field = data.get("singular_string_ipv4", str())
    args["singular_string_ipv4"] = field

    field = data.get("singular_string_ipv6", str())
    args["singular_string_ipv6"] = field

    field = data.get("singular_string_value_ip", None)
    args["singular_string_value_ip"] = field

    field = data.get("singular_ipv4", None)
    args["singular_ipv4"] = field

    field = data.get("singular_string_value_ipv4", None)
    args["singular_string_value_ipv4"] = field

    field = data.get("singular_ipv6", None)
    args["singular_ipv6"] = field

    field = data.get("singular_string_value_ipv6", None)
    args["singular_string_value_ipv6"] = field

    field = data.get("singular_std_duration", None)
    args["singular_std_duration"] = field

    field = data.get("singular_std_long_duration", None)
    args["singular_std_long_duration"] = field

    field = data.get("singular_size", None)
    args["singular_size"] = field

    field = data.get("singular_uint64_size", 0)
    args["singular_uint64_size"] = field

    field = data.get("singular_string_ipnet", str())
    args["singular_string_ipnet"] = field

    field = data.get("repeated_double_value", [])
    args["repeated_double_value"] = field

    field = data.get("repeated_float_value", [])
    args["repeated_float_value"] = field

    field = data.get("repeated_int64_value", [])
    args["repeated_int64_value"] = field

    field = data.get("repeated_uint64_value", [])
    args["repeated_uint64_value"] = field

    field = data.get("repeated_int32_value", [])
    args["repeated_int32_value"] = field

    field = data.get("repeated_uint32_value", [])
    args["repeated_uint32_value"] = field

    field = data.get("singular_uint64value_size", None)
    args["singular_uint64value_size"] = field

    field = data.get("singular_string_value_ipnet", None)
    args["singular_string_value_ipnet"] = field

    field = data.get("repeated_bool_value", [])
    args["repeated_bool_value"] = field

    field = data.get("repeated_string_value", [])
    args["repeated_string_value"] = field

    field = data.get("repeated_bytes_value", [])
    args["repeated_bytes_value"] = field

    field = data.get("repeated_timestamp", [])
    args["repeated_timestamp"] = field

    field = data.get("repeated_any", [])
    args["repeated_any"] = field

    field = data.get("repeated_struct", [])
    args["repeated_struct"] = field

    field = data.get("repeated_money", [])
    args["repeated_money"] = [unmarshal_Money(v) for v in field] if field is not None else None

    field = data.get("repeated_strings_value", [])
    args["repeated_strings_value"] = field

    field = data.get("repeated_duration", [])
    args["repeated_duration"] = field

    field = data.get("repeated_ip", [])
    args["repeated_ip"] = field

    field = data.get("repeated_string_ip", [])
    args["repeated_string_ip"] = field

    field = data.get("repeated_string_value_ip", [])
    args["repeated_string_value_ip"] = field

    field = data.get("repeated_ipv4", [])
    args["repeated_ipv4"] = field

    field = data.get("repeated_string_ipv4", [])
    args["repeated_string_ipv4"] = field

    field = data.get("repeated_string_value_ipv4", [])
    args["repeated_string_value_ipv4"] = field

    field = data.get("repeated_ipv6", [])
    args["repeated_ipv6"] = field

    field = data.get("repeated_string_ipv6", [])
    args["repeated_string_ipv6"] = field

    field = data.get("repeated_string_value_ipv6", [])
    args["repeated_string_value_ipv6"] = field

    field = data.get("repeated_std_duration", [])
    args["repeated_std_duration"] = field

    field = data.get("repeated_std_long_duration", [])
    args["repeated_std_long_duration"] = field

    field = data.get("repeated_size", [])
    args["repeated_size"] = field

    field = data.get("repeated_uint64_size", [])
    args["repeated_uint64_size"] = field

    field = data.get("repeated_uint64value_size", [])
    args["repeated_uint64value_size"] = field

    field = data.get("repeated_string_ipnet", [])
    args["repeated_string_ipnet"] = field

    field = data.get("repeated_string_value_ipnet", [])
    args["repeated_string_value_ipnet"] = field

    return PostAllTypesMessage(**args)

def unmarshal_PostBodyAndPathSimpleMessage(data: Any) -> PostBodyAndPathSimpleMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostBodyAndPathSimpleMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    field = data.get("body", str())
    args["body"] = field

    return PostBodyAndPathSimpleMessage(**args)

def unmarshal_EchoMessage(data: Any) -> EchoMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'EchoMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("str", str())
    args["str_"] = field

    field = data.get("strs", str())
    args["strs"] = field

    return EchoMessage(**args)

def unmarshal_GetEnumMessage(data: Any) -> GetEnumMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetEnumMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    return GetEnumMessage(**args)

def unmarshal_GetZoneResponse(data: Any) -> GetZoneResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'GetZoneResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("zone", str())
    args["zone"] = field

    return GetZoneResponse(**args)

def unmarshal_ListCharactersResponse(data: Any) -> ListCharactersResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ListCharactersResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("total_count", str())
    args["total_count"] = field

    field = data.get("characters", str())
    args["characters"] = field

    return ListCharactersResponse(**args)

def unmarshal_MetadataResponse(data: Any) -> MetadataResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'MetadataResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metadata", str())
    args["metadata"] = field

    return MetadataResponse(**args)

def unmarshal_PatchEnumMessage(data: Any) -> PatchEnumMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PatchEnumMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", str())
    args["type_"] = field

    return PatchEnumMessage(**args)

def unmarshal_PostAllMapTypesMessage(data: Any) -> PostAllMapTypesMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllMapTypesMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("map_int32_int32", str())
    args["map_int32_int32"] = field

    field = data.get("map_int64_int64", str())
    args["map_int64_int64"] = field

    field = data.get("map_uint32_uint32", str())
    args["map_uint32_uint32"] = field

    field = data.get("map_uint64_uint64", str())
    args["map_uint64_uint64"] = field

    field = data.get("map_sint32_sint32", str())
    args["map_sint32_sint32"] = field

    field = data.get("map_sint64_sint64", str())
    args["map_sint64_sint64"] = field

    field = data.get("map_fixed32_fixed32", str())
    args["map_fixed32_fixed32"] = field

    field = data.get("map_fixed64_fixed64", str())
    args["map_fixed64_fixed64"] = field

    field = data.get("map_sfixed32_sfixed32", str())
    args["map_sfixed32_sfixed32"] = field

    field = data.get("map_sfixed64_sfixed64", str())
    args["map_sfixed64_sfixed64"] = field

    field = data.get("map_int32_float", str())
    args["map_int32_float"] = field

    field = data.get("map_int32_double", str())
    args["map_int32_double"] = field

    field = data.get("map_string_string", str())
    args["map_string_string"] = field

    field = data.get("map_int32_bytes", str())
    args["map_int32_bytes"] = field

    field = data.get("map_int32_enum", str())
    args["map_int32_enum"] = {key: MapEnum(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("map_int32_all_types", str())
    args["map_int32_all_types"] = {key: unmarshal_PostAllTypesMessage(value)for key, value in field.items()
    } if field is not None else None

    field = data.get("map_int32_ip", str())
    args["map_int32_ip"] = field

    field = data.get("map_int32_std_duration", str())
    args["map_int32_std_duration"] = field

    field = data.get("map_int32_std_long_duration", str())
    args["map_int32_std_long_duration"] = field

    field = data.get("map_int32_size", str())
    args["map_int32_size"] = field

    field = data.get("map_int32_uint64_size", str())
    args["map_int32_uint64_size"] = field

    field = data.get("map_int32_uint64value_size", str())
    args["map_int32_uint64value_size"] = field

    field = data.get("map_int32_string_ip", str())
    args["map_int32_string_ip"] = field

    field = data.get("map_int32_string_value_ip", str())
    args["map_int32_string_value_ip"] = field

    field = data.get("map_int32_ipv4", str())
    args["map_int32_ipv4"] = field

    field = data.get("map_int32_string_ipv4", str())
    args["map_int32_string_ipv4"] = field

    field = data.get("map_int32_string_value_ipv4", str())
    args["map_int32_string_value_ipv4"] = field

    field = data.get("map_int32_ipv6", str())
    args["map_int32_ipv6"] = field

    field = data.get("map_int32_string_ipv6", str())
    args["map_int32_string_ipv6"] = field

    field = data.get("map_int32_string_value_ipv6", str())
    args["map_int32_string_value_ipv6"] = field

    field = data.get("map_int32_strings_value", str())
    args["map_int32_strings_value"] = field

    field = data.get("map_int32_duration", str())
    args["map_int32_duration"] = field

    return PostAllMapTypesMessage(**args)

def unmarshal_PostAllOptionalMessageNestedMessage(data: Any) -> PostAllOptionalMessageNestedMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllOptionalMessageNestedMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("s", str())
    args["s"] = field

    return PostAllOptionalMessageNestedMessage(**args)

def unmarshal_PostAllOptionalMessageNestedMessageWithOptional(data: Any) -> PostAllOptionalMessageNestedMessageWithOptional:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllOptionalMessageNestedMessageWithOptional' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("bb", None)
    args["bb"] = field

    return PostAllOptionalMessageNestedMessageWithOptional(**args)

def unmarshal_PostAllOptionalMessage(data: Any) -> PostAllOptionalMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostAllOptionalMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("optional_int32", None)
    args["optional_int32"] = field

    field = data.get("optional_int64", None)
    args["optional_int64"] = field

    field = data.get("optional_uint32", None)
    args["optional_uint32"] = field

    field = data.get("optional_uint64", None)
    args["optional_uint64"] = field

    field = data.get("optional_sint32", None)
    args["optional_sint32"] = field

    field = data.get("optional_sint64", None)
    args["optional_sint64"] = field

    field = data.get("optional_fixed32", None)
    args["optional_fixed32"] = field

    field = data.get("optional_fixed64", None)
    args["optional_fixed64"] = field

    field = data.get("optional_sfixed32", None)
    args["optional_sfixed32"] = field

    field = data.get("optional_sfixed64", None)
    args["optional_sfixed64"] = field

    field = data.get("optional_float", None)
    args["optional_float"] = field

    field = data.get("optional_double", None)
    args["optional_double"] = field

    field = data.get("optional_bool", None)
    args["optional_bool"] = field

    field = data.get("optional_string", None)
    args["optional_string"] = field

    field = data.get("optional_bytes", None)
    args["optional_bytes"] = field

    field = data.get("optional_cord", None)
    args["optional_cord"] = field

    field = data.get("optional_nested_message_with_optional", None)
    args["optional_nested_message_with_optional"] = unmarshal_PostAllOptionalMessageNestedMessageWithOptional(field) if field is not None else None

    field = data.get("lazy_nested_message_with_optional", None)
    args["lazy_nested_message_with_optional"] = unmarshal_PostAllOptionalMessageNestedMessageWithOptional(field) if field is not None else None

    field = data.get("optional_nested_enum", None)
    args["optional_nested_enum"] = field

    field = data.get("optional_nested_message", None)
    args["optional_nested_message"] = unmarshal_PostAllOptionalMessageNestedMessage(field) if field is not None else None

    field = data.get("singular_int32", str())
    args["singular_int32"] = field

    field = data.get("singular_int64", str())
    args["singular_int64"] = field

    field = data.get("nested_message", None)
    args["nested_message"] = unmarshal_PostAllOptionalMessageNestedMessage(field) if field is not None else None

    field = data.get("singular_double_value", None)
    args["singular_double_value"] = field

    field = data.get("singular_float_value", None)
    args["singular_float_value"] = field

    field = data.get("singular_int64_value", None)
    args["singular_int64_value"] = field

    field = data.get("singular_uint64_value", None)
    args["singular_uint64_value"] = field

    field = data.get("singular_int32_value", None)
    args["singular_int32_value"] = field

    field = data.get("singular_uint32_value", None)
    args["singular_uint32_value"] = field

    field = data.get("singular_bool_value", None)
    args["singular_bool_value"] = field

    field = data.get("singular_string_value", None)
    args["singular_string_value"] = field

    field = data.get("singular_bytes_value", None)
    args["singular_bytes_value"] = field

    field = data.get("singular_timestamp", None)
    args["singular_timestamp"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("singular_any", None)
    args["singular_any"] = field

    field = data.get("singular_struct", None)
    args["singular_struct"] = field

    field = data.get("singular_money", None)
    args["singular_money"] = unmarshal_Money(field) if field is not None else None

    field = data.get("singular_strings_value", None)
    args["singular_strings_value"] = field

    field = data.get("singular_duration", None)
    args["singular_duration"] = field

    field = data.get("map_string_string", None)
    args["map_string_string"] = field

    field = data.get("timeseries", None)
    args["timeseries"] = unmarshal_TimeSeries(field) if field is not None else None

    return PostAllOptionalMessage(**args)

def unmarshal_PostBodyAndPathAndQueryMessage(data: Any) -> PostBodyAndPathAndQueryMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostBodyAndPathAndQueryMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    field = data.get("query", str())
    args["query"] = field

    field = data.get("body", None)
    args["body"] = unmarshal_PostBodyAndPathSimpleMessage(field) if field is not None else None

    return PostBodyAndPathAndQueryMessage(**args)

def unmarshal_PostBodyAndPathComplexMessage(data: Any) -> PostBodyAndPathComplexMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostBodyAndPathComplexMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    field = data.get("body", None)
    args["body"] = unmarshal_PostBodyAndPathSimpleMessage(field) if field is not None else None

    return PostBodyAndPathComplexMessage(**args)

def unmarshal_PostBodyAndPathSimple2Message(data: Any) -> PostBodyAndPathSimple2Message:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostBodyAndPathSimple2Message' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("path", str())
    args["path"] = field

    field = data.get("body", str())
    args["body"] = field

    return PostBodyAndPathSimple2Message(**args)

def unmarshal_ComplexValidateMsg(data: Any) -> ComplexValidateMsg:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'ComplexValidateMsg' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("const", str())
    args["const"] = field

    field = data.get("int_const", str())
    args["int_const"] = field

    field = data.get("bool_const", str())
    args["bool_const"] = field

    field = data.get("float_const", str())
    args["float_const"] = field

    field = data.get("double_in", str())
    args["double_in"] = field

    field = data.get("enum_const", str())
    args["enum_const"] = field

    field = data.get("nested", None)
    args["nested"] = unmarshal_ComplexValidateMsg(field) if field is not None else None

    field = data.get("float_val", None)
    args["float_val"] = field

    field = data.get("dur_val", None)
    args["dur_val"] = field

    field = data.get("ts_val", None)
    args["ts_val"] = parser.isoparse(field) if isinstance(field, str) else field

    field = data.get("another", None)
    args["another"] = unmarshal_ComplexValidateMsg(field) if field is not None else None

    field = data.get("any_val", None)
    args["any_val"] = field

    field = data.get("rep_ts_val", str())
    args["rep_ts_val"] = field

    field = data.get("map_val", str())
    args["map_val"] = field

    field = data.get("bytes_val", str())
    args["bytes_val"] = field

    field = data.get("x", None)
    args["x"] = field

    field = data.get("y", None)
    args["y"] = field

    return ComplexValidateMsg(**args)

def unmarshal_PostComplexValidateMessage(data: Any) -> PostComplexValidateMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostComplexValidateMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("val", None)
    args["val"] = unmarshal_ComplexValidateMsg(field) if field is not None else None

    return PostComplexValidateMessage(**args)

def unmarshal_PostDeprecatedOrganizationMessage(data: Any) -> PostDeprecatedOrganizationMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostDeprecatedOrganizationMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("organization", None)
    args["organization"] = field

    return PostDeprecatedOrganizationMessage(**args)

def unmarshal_PostDeprecatedProjectMessage(data: Any) -> PostDeprecatedProjectMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostDeprecatedProjectMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project", None)
    args["project"] = field

    return PostDeprecatedProjectMessage(**args)

def unmarshal_PostEchoTimeSeriesMessage(data: Any) -> PostEchoTimeSeriesMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostEchoTimeSeriesMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("metrics", None)
    args["metrics"] = unmarshal_TimeSeries(field) if field is not None else None

    return PostEchoTimeSeriesMessage(**args)

def unmarshal_PostEnumMessage(data: Any) -> PostEnumMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostEnumMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("type", getattr(Type, "UNKNOWN"))
    args["type_"] = field

    field = data.get("type2", None)
    args["type2"] = field

    field = data.get("type3", str())
    args["type3"] = field

    return PostEnumMessage(**args)

def unmarshal_PostIPMessage(data: Any) -> PostIPMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostIPMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("ip_v4", None)
    args["ip_v4"] = field

    field = data.get("ip_v6", None)
    args["ip_v6"] = field

    field = data.get("ip", None)
    args["ip"] = field

    return PostIPMessage(**args)

def unmarshal_PostOneOfMessage(data: Any) -> PostOneOfMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostOneOfMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("test", None)
    args["test"] = field

    field = data.get("test2", None)
    args["test2"] = field

    field = data.get("test_nested", None)
    args["test_nested"] = unmarshal_EchoMessage(field) if field is not None else None

    field = data.get("test3", None)
    args["test3"] = field

    return PostOneOfMessage(**args)

def unmarshal_PostOrganizationIdMessage(data: Any) -> PostOrganizationIdMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostOrganizationIdMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("organization_id", str())
    args["organization_id"] = field

    return PostOrganizationIdMessage(**args)

def unmarshal_PostProjectIdMessage(data: Any) -> PostProjectIdMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostProjectIdMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("project_id", str())
    args["project_id"] = field

    return PostProjectIdMessage(**args)

def unmarshal_PostScalarTypesMessage(data: Any) -> PostScalarTypesMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostScalarTypesMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("double_field", str())
    args["double_field"] = field

    field = data.get("float_field", str())
    args["float_field"] = field

    field = data.get("int32_field", str())
    args["int32_field"] = field

    field = data.get("int64_field", str())
    args["int64_field"] = field

    field = data.get("uint32_field", str())
    args["uint32_field"] = field

    field = data.get("uint64_field", str())
    args["uint64_field"] = field

    field = data.get("bool_field", str())
    args["bool_field"] = field

    field = data.get("string_field", str())
    args["string_field"] = field

    return PostScalarTypesMessage(**args)

def unmarshal_PostTagsMessage(data: Any) -> PostTagsMessage:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'PostTagsMessage' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("tags", None)
    args["tags"] = field

    return PostTagsMessage(**args)

def unmarshal_Transient(data: Any) -> Transient:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type 'Transient' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("status", str())
    args["status"] = field

    return Transient(**args)

def unmarshal__GetRegionResponse(data: Any) -> _GetRegionResponse:
    if not isinstance(data, dict):
        raise TypeError(
            "Unmarshalling the type '_GetRegionResponse' failed as data isn't a dictionary."
        )

    args: Dict[str, Any] = {}

    field = data.get("region", str())
    args["region"] = field

    return _GetRegionResponse(**args)

def marshal_PatchEnumRequest(
    request: PatchEnumRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None


    return output

def marshal_PostAllTypesMessageNestedMessage(
    request: PostAllTypesMessageNestedMessage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bb is not None:
        output["bb"] = request.bb
    else:
        output["bb"] = str()


    return output

def marshal_PostAllTypesMessage(
    request: PostAllTypesMessage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="oneof_uint32", value=request.oneof_uint32,marshal_func=None
            ),
            OneOfPossibility(param="oneof_nested_message", value=request.oneof_nested_message,marshal_func=marshal_PostAllTypesMessageNestedMessage
            ),
            OneOfPossibility(param="oneof_string", value=request.oneof_string,marshal_func=None
            ),
            OneOfPossibility(param="oneof_bytes", value=request.oneof_bytes,marshal_func=None
            ),
        ]),
    )

    if request.singular_int32 is not None:
        output["singular_int32"] = request.singular_int32
    else:
        output["singular_int32"] = 0

    if request.singular_int64 is not None:
        output["singular_int64"] = request.singular_int64
    else:
        output["singular_int64"] = 0

    if request.singular_uint32 is not None:
        output["singular_uint32"] = request.singular_uint32
    else:
        output["singular_uint32"] = 0

    if request.singular_uint64 is not None:
        output["singular_uint64"] = request.singular_uint64
    else:
        output["singular_uint64"] = 0

    if request.singular_sint32 is not None:
        output["singular_sint32"] = request.singular_sint32
    else:
        output["singular_sint32"] = 0

    if request.singular_sint64 is not None:
        output["singular_sint64"] = request.singular_sint64
    else:
        output["singular_sint64"] = 0

    if request.singular_fixed32 is not None:
        output["singular_fixed32"] = request.singular_fixed32
    else:
        output["singular_fixed32"] = 0

    if request.singular_fixed64 is not None:
        output["singular_fixed64"] = request.singular_fixed64
    else:
        output["singular_fixed64"] = 0

    if request.singular_sfixed32 is not None:
        output["singular_sfixed32"] = request.singular_sfixed32
    else:
        output["singular_sfixed32"] = 0

    if request.singular_sfixed64 is not None:
        output["singular_sfixed64"] = request.singular_sfixed64
    else:
        output["singular_sfixed64"] = 0

    if request.singular_float is not None:
        output["singular_float"] = request.singular_float
    else:
        output["singular_float"] = 0.0

    if request.singular_double is not None:
        output["singular_double"] = request.singular_double
    else:
        output["singular_double"] = 0.0

    if request.singular_bool is not None:
        output["singular_bool"] = request.singular_bool
    else:
        output["singular_bool"] = False

    if request.singular_string is not None:
        output["singular_string"] = request.singular_string
    else:
        output["singular_string"] = str()

    if request.singular_bytes is not None:
        output["singular_bytes"] = request.singular_bytes
    else:
        output["singular_bytes"] = str()

    if request.singular_nested_enum is not None:
        output["singular_nested_enum"] = str(request.singular_nested_enum)
    else:
        output["singular_nested_enum"] = getattr(PostAllTypesMessageNestedEnum, "ZERO")

    if request.repeated_int32 is not None:
        output["repeated_int32"] = request.repeated_int32
    else:
        output["repeated_int32"] = []

    if request.repeated_int64 is not None:
        output["repeated_int64"] = request.repeated_int64
    else:
        output["repeated_int64"] = []

    if request.repeated_uint32 is not None:
        output["repeated_uint32"] = request.repeated_uint32
    else:
        output["repeated_uint32"] = []

    if request.repeated_uint64 is not None:
        output["repeated_uint64"] = request.repeated_uint64
    else:
        output["repeated_uint64"] = []

    if request.singular_nested_message is not None:
        output["singular_nested_message"] = marshal_PostAllTypesMessageNestedMessage(request.singular_nested_message, defaults)
    else:
        output["singular_nested_message"] = None

    if request.repeated_sint32 is not None:
        output["repeated_sint32"] = request.repeated_sint32
    else:
        output["repeated_sint32"] = []

    if request.repeated_sint64 is not None:
        output["repeated_sint64"] = request.repeated_sint64
    else:
        output["repeated_sint64"] = []

    if request.repeated_fixed32 is not None:
        output["repeated_fixed32"] = request.repeated_fixed32
    else:
        output["repeated_fixed32"] = []

    if request.repeated_fixed64 is not None:
        output["repeated_fixed64"] = request.repeated_fixed64
    else:
        output["repeated_fixed64"] = []

    if request.repeated_sfixed32 is not None:
        output["repeated_sfixed32"] = request.repeated_sfixed32
    else:
        output["repeated_sfixed32"] = []

    if request.repeated_sfixed64 is not None:
        output["repeated_sfixed64"] = request.repeated_sfixed64
    else:
        output["repeated_sfixed64"] = []

    if request.repeated_float is not None:
        output["repeated_float"] = request.repeated_float
    else:
        output["repeated_float"] = []

    if request.repeated_double is not None:
        output["repeated_double"] = request.repeated_double
    else:
        output["repeated_double"] = []

    if request.repeated_bool is not None:
        output["repeated_bool"] = request.repeated_bool
    else:
        output["repeated_bool"] = []

    if request.repeated_string is not None:
        output["repeated_string"] = request.repeated_string
    else:
        output["repeated_string"] = []

    if request.repeated_bytes is not None:
        output["repeated_bytes"] = request.repeated_bytes
    else:
        output["repeated_bytes"] = []

    if request.repeated_nested_message is not None:
        output["repeated_nested_message"] = [marshal_PostAllTypesMessageNestedMessage(item, defaults) for item in request.repeated_nested_message]
    else:
        output["repeated_nested_message"] = []

    if request.repeated_nested_enum is not None:
        output["repeated_nested_enum"] = [str(item) for item in request.repeated_nested_enum]
    else:
        output["repeated_nested_enum"] = []

    if request.singular_string_ip is not None:
        output["singular_string_ip"] = request.singular_string_ip
    else:
        output["singular_string_ip"] = str()

    if request.singular_string_ipv4 is not None:
        output["singular_string_ipv4"] = request.singular_string_ipv4
    else:
        output["singular_string_ipv4"] = str()

    if request.singular_double_value is not None:
        output["singular_double_value"] = request.singular_double_value
    else:
        output["singular_double_value"] = None

    if request.singular_float_value is not None:
        output["singular_float_value"] = request.singular_float_value
    else:
        output["singular_float_value"] = None

    if request.singular_int64_value is not None:
        output["singular_int64_value"] = request.singular_int64_value
    else:
        output["singular_int64_value"] = None

    if request.singular_uint64_value is not None:
        output["singular_uint64_value"] = request.singular_uint64_value
    else:
        output["singular_uint64_value"] = None

    if request.singular_int32_value is not None:
        output["singular_int32_value"] = request.singular_int32_value
    else:
        output["singular_int32_value"] = None

    if request.singular_uint32_value is not None:
        output["singular_uint32_value"] = request.singular_uint32_value
    else:
        output["singular_uint32_value"] = None

    if request.singular_bool_value is not None:
        output["singular_bool_value"] = request.singular_bool_value
    else:
        output["singular_bool_value"] = None

    if request.singular_string_value is not None:
        output["singular_string_value"] = request.singular_string_value
    else:
        output["singular_string_value"] = None

    if request.singular_bytes_value is not None:
        output["singular_bytes_value"] = request.singular_bytes_value
    else:
        output["singular_bytes_value"] = None

    if request.singular_timestamp is not None:
        output["singular_timestamp"] = request.singular_timestamp.isoformat()
    else:
        output["singular_timestamp"] = None

    if request.singular_any is not None:
        output["singular_any"] = request.singular_any
    else:
        output["singular_any"] = None

    if request.singular_struct is not None:
        output["singular_struct"] = request.singular_struct
    else:
        output["singular_struct"] = None

    if request.singular_money is not None:
        output["singular_money"] = marshal_Money(request.singular_money, defaults)
    else:
        output["singular_money"] = None

    if request.singular_strings_value is not None:
        output["singular_strings_value"] = request.singular_strings_value
    else:
        output["singular_strings_value"] = None

    if request.singular_duration is not None:
        output["singular_duration"] = request.singular_duration
    else:
        output["singular_duration"] = None

    if request.singular_ip is not None:
        output["singular_ip"] = request.singular_ip
    else:
        output["singular_ip"] = None

    if request.singular_string_value_ip is not None:
        output["singular_string_value_ip"] = request.singular_string_value_ip
    else:
        output["singular_string_value_ip"] = None

    if request.singular_ipv4 is not None:
        output["singular_ipv4"] = request.singular_ipv4
    else:
        output["singular_ipv4"] = None

    if request.singular_string_value_ipv4 is not None:
        output["singular_string_value_ipv4"] = request.singular_string_value_ipv4
    else:
        output["singular_string_value_ipv4"] = None

    if request.singular_ipv6 is not None:
        output["singular_ipv6"] = request.singular_ipv6
    else:
        output["singular_ipv6"] = None

    if request.singular_string_ipv6 is not None:
        output["singular_string_ipv6"] = request.singular_string_ipv6
    else:
        output["singular_string_ipv6"] = str()

    if request.singular_uint64_size is not None:
        output["singular_uint64_size"] = request.singular_uint64_size
    else:
        output["singular_uint64_size"] = 0

    if request.singular_string_ipnet is not None:
        output["singular_string_ipnet"] = request.singular_string_ipnet
    else:
        output["singular_string_ipnet"] = str()

    if request.repeated_double_value is not None:
        output["repeated_double_value"] = request.repeated_double_value
    else:
        output["repeated_double_value"] = []

    if request.singular_string_value_ipv6 is not None:
        output["singular_string_value_ipv6"] = request.singular_string_value_ipv6
    else:
        output["singular_string_value_ipv6"] = None

    if request.singular_std_duration is not None:
        output["singular_std_duration"] = request.singular_std_duration
    else:
        output["singular_std_duration"] = None

    if request.singular_std_long_duration is not None:
        output["singular_std_long_duration"] = request.singular_std_long_duration
    else:
        output["singular_std_long_duration"] = None

    if request.singular_size is not None:
        output["singular_size"] = request.singular_size
    else:
        output["singular_size"] = None

    if request.singular_uint64value_size is not None:
        output["singular_uint64value_size"] = request.singular_uint64value_size
    else:
        output["singular_uint64value_size"] = None

    if request.singular_string_value_ipnet is not None:
        output["singular_string_value_ipnet"] = request.singular_string_value_ipnet
    else:
        output["singular_string_value_ipnet"] = None

    if request.repeated_float_value is not None:
        output["repeated_float_value"] = request.repeated_float_value
    else:
        output["repeated_float_value"] = []

    if request.repeated_int64_value is not None:
        output["repeated_int64_value"] = request.repeated_int64_value
    else:
        output["repeated_int64_value"] = []

    if request.repeated_uint64_value is not None:
        output["repeated_uint64_value"] = request.repeated_uint64_value
    else:
        output["repeated_uint64_value"] = []

    if request.repeated_int32_value is not None:
        output["repeated_int32_value"] = request.repeated_int32_value
    else:
        output["repeated_int32_value"] = []

    if request.repeated_uint32_value is not None:
        output["repeated_uint32_value"] = request.repeated_uint32_value
    else:
        output["repeated_uint32_value"] = []

    if request.repeated_bool_value is not None:
        output["repeated_bool_value"] = request.repeated_bool_value
    else:
        output["repeated_bool_value"] = []

    if request.repeated_string_value is not None:
        output["repeated_string_value"] = request.repeated_string_value
    else:
        output["repeated_string_value"] = []

    if request.repeated_bytes_value is not None:
        output["repeated_bytes_value"] = request.repeated_bytes_value
    else:
        output["repeated_bytes_value"] = []

    if request.repeated_timestamp is not None:
        output["repeated_timestamp"] = request.repeated_timestamp
    else:
        output["repeated_timestamp"] = []

    if request.repeated_any is not None:
        output["repeated_any"] = request.repeated_any
    else:
        output["repeated_any"] = []

    if request.repeated_struct is not None:
        output["repeated_struct"] = request.repeated_struct
    else:
        output["repeated_struct"] = []

    if request.repeated_money is not None:
        output["repeated_money"] = [marshal_Money(item, defaults) for item in request.repeated_money]
    else:
        output["repeated_money"] = []

    if request.repeated_strings_value is not None:
        output["repeated_strings_value"] = request.repeated_strings_value
    else:
        output["repeated_strings_value"] = []

    if request.repeated_duration is not None:
        output["repeated_duration"] = request.repeated_duration
    else:
        output["repeated_duration"] = []

    if request.repeated_ip is not None:
        output["repeated_ip"] = request.repeated_ip
    else:
        output["repeated_ip"] = []

    if request.repeated_string_ip is not None:
        output["repeated_string_ip"] = request.repeated_string_ip
    else:
        output["repeated_string_ip"] = []

    if request.repeated_string_value_ip is not None:
        output["repeated_string_value_ip"] = request.repeated_string_value_ip
    else:
        output["repeated_string_value_ip"] = []

    if request.repeated_ipv4 is not None:
        output["repeated_ipv4"] = request.repeated_ipv4
    else:
        output["repeated_ipv4"] = []

    if request.repeated_string_ipv4 is not None:
        output["repeated_string_ipv4"] = request.repeated_string_ipv4
    else:
        output["repeated_string_ipv4"] = []

    if request.repeated_string_value_ipv4 is not None:
        output["repeated_string_value_ipv4"] = request.repeated_string_value_ipv4
    else:
        output["repeated_string_value_ipv4"] = []

    if request.repeated_ipv6 is not None:
        output["repeated_ipv6"] = request.repeated_ipv6
    else:
        output["repeated_ipv6"] = []

    if request.repeated_string_ipv6 is not None:
        output["repeated_string_ipv6"] = request.repeated_string_ipv6
    else:
        output["repeated_string_ipv6"] = []

    if request.repeated_string_value_ipv6 is not None:
        output["repeated_string_value_ipv6"] = request.repeated_string_value_ipv6
    else:
        output["repeated_string_value_ipv6"] = []

    if request.repeated_std_duration is not None:
        output["repeated_std_duration"] = request.repeated_std_duration
    else:
        output["repeated_std_duration"] = []

    if request.repeated_std_long_duration is not None:
        output["repeated_std_long_duration"] = request.repeated_std_long_duration
    else:
        output["repeated_std_long_duration"] = []

    if request.repeated_size is not None:
        output["repeated_size"] = request.repeated_size
    else:
        output["repeated_size"] = []

    if request.repeated_uint64_size is not None:
        output["repeated_uint64_size"] = request.repeated_uint64_size
    else:
        output["repeated_uint64_size"] = []

    if request.repeated_uint64value_size is not None:
        output["repeated_uint64value_size"] = request.repeated_uint64value_size
    else:
        output["repeated_uint64value_size"] = []

    if request.repeated_string_ipnet is not None:
        output["repeated_string_ipnet"] = request.repeated_string_ipnet
    else:
        output["repeated_string_ipnet"] = []

    if request.repeated_string_value_ipnet is not None:
        output["repeated_string_value_ipnet"] = request.repeated_string_value_ipnet
    else:
        output["repeated_string_value_ipnet"] = []


    return output

def marshal_PostAllMapTypesRequest(
    request: PostAllMapTypesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.map_int32_int32 is not None:
        output["map_int32_int32"] = {
            key: value
            for key, value in request.map_int32_int32.items()
        }
    else:
        output["map_int32_int32"] = None

    if request.map_int64_int64 is not None:
        output["map_int64_int64"] = {
            key: value
            for key, value in request.map_int64_int64.items()
        }
    else:
        output["map_int64_int64"] = None

    if request.map_uint32_uint32 is not None:
        output["map_uint32_uint32"] = {
            key: value
            for key, value in request.map_uint32_uint32.items()
        }
    else:
        output["map_uint32_uint32"] = None

    if request.map_uint64_uint64 is not None:
        output["map_uint64_uint64"] = {
            key: value
            for key, value in request.map_uint64_uint64.items()
        }
    else:
        output["map_uint64_uint64"] = None

    if request.map_sint32_sint32 is not None:
        output["map_sint32_sint32"] = {
            key: value
            for key, value in request.map_sint32_sint32.items()
        }
    else:
        output["map_sint32_sint32"] = None

    if request.map_sint64_sint64 is not None:
        output["map_sint64_sint64"] = {
            key: value
            for key, value in request.map_sint64_sint64.items()
        }
    else:
        output["map_sint64_sint64"] = None

    if request.map_fixed32_fixed32 is not None:
        output["map_fixed32_fixed32"] = {
            key: value
            for key, value in request.map_fixed32_fixed32.items()
        }
    else:
        output["map_fixed32_fixed32"] = None

    if request.map_fixed64_fixed64 is not None:
        output["map_fixed64_fixed64"] = {
            key: value
            for key, value in request.map_fixed64_fixed64.items()
        }
    else:
        output["map_fixed64_fixed64"] = None

    if request.map_sfixed32_sfixed32 is not None:
        output["map_sfixed32_sfixed32"] = {
            key: value
            for key, value in request.map_sfixed32_sfixed32.items()
        }
    else:
        output["map_sfixed32_sfixed32"] = None

    if request.map_sfixed64_sfixed64 is not None:
        output["map_sfixed64_sfixed64"] = {
            key: value
            for key, value in request.map_sfixed64_sfixed64.items()
        }
    else:
        output["map_sfixed64_sfixed64"] = None

    if request.map_int32_float is not None:
        output["map_int32_float"] = {
            key: value
            for key, value in request.map_int32_float.items()
        }
    else:
        output["map_int32_float"] = None

    if request.map_int32_double is not None:
        output["map_int32_double"] = {
            key: value
            for key, value in request.map_int32_double.items()
        }
    else:
        output["map_int32_double"] = None

    if request.map_string_string is not None:
        output["map_string_string"] = {
            key: value
            for key, value in request.map_string_string.items()
        }
    else:
        output["map_string_string"] = None

    if request.map_int32_bytes is not None:
        output["map_int32_bytes"] = {
            key: value
            for key, value in request.map_int32_bytes.items()
        }
    else:
        output["map_int32_bytes"] = None

    if request.map_int32_enum is not None:
        output["map_int32_enum"] = {
            key: str(value)
            for key, value in request.map_int32_enum.items()
        }
    else:
        output["map_int32_enum"] = None

    if request.map_int32_all_types is not None:
        output["map_int32_all_types"] = {
            key: marshal_PostAllTypesMessage(value, defaults)
            for key, value in request.map_int32_all_types.items()
        }
    else:
        output["map_int32_all_types"] = None

    if request.map_int32_ip is not None:
        output["map_int32_ip"] = {
            key: value
            for key, value in request.map_int32_ip.items()
        }
    else:
        output["map_int32_ip"] = None

    if request.map_int32_std_duration is not None:
        output["map_int32_std_duration"] = {
            key: value
            for key, value in request.map_int32_std_duration.items()
        }
    else:
        output["map_int32_std_duration"] = None

    if request.map_int32_std_long_duration is not None:
        output["map_int32_std_long_duration"] = {
            key: value
            for key, value in request.map_int32_std_long_duration.items()
        }
    else:
        output["map_int32_std_long_duration"] = None

    if request.map_int32_size is not None:
        output["map_int32_size"] = {
            key: value
            for key, value in request.map_int32_size.items()
        }
    else:
        output["map_int32_size"] = None

    if request.map_int32_uint64_size is not None:
        output["map_int32_uint64_size"] = {
            key: value
            for key, value in request.map_int32_uint64_size.items()
        }
    else:
        output["map_int32_uint64_size"] = None

    if request.map_int32_uint64value_size is not None:
        output["map_int32_uint64value_size"] = {
            key: value
            for key, value in request.map_int32_uint64value_size.items()
        }
    else:
        output["map_int32_uint64value_size"] = None

    if request.map_int32_string_ip is not None:
        output["map_int32_string_ip"] = {
            key: value
            for key, value in request.map_int32_string_ip.items()
        }
    else:
        output["map_int32_string_ip"] = None

    if request.map_int32_string_value_ip is not None:
        output["map_int32_string_value_ip"] = {
            key: value
            for key, value in request.map_int32_string_value_ip.items()
        }
    else:
        output["map_int32_string_value_ip"] = None

    if request.map_int32_ipv4 is not None:
        output["map_int32_ipv4"] = {
            key: value
            for key, value in request.map_int32_ipv4.items()
        }
    else:
        output["map_int32_ipv4"] = None

    if request.map_int32_string_ipv4 is not None:
        output["map_int32_string_ipv4"] = {
            key: value
            for key, value in request.map_int32_string_ipv4.items()
        }
    else:
        output["map_int32_string_ipv4"] = None

    if request.map_int32_string_value_ipv4 is not None:
        output["map_int32_string_value_ipv4"] = {
            key: value
            for key, value in request.map_int32_string_value_ipv4.items()
        }
    else:
        output["map_int32_string_value_ipv4"] = None

    if request.map_int32_ipv6 is not None:
        output["map_int32_ipv6"] = {
            key: value
            for key, value in request.map_int32_ipv6.items()
        }
    else:
        output["map_int32_ipv6"] = None

    if request.map_int32_string_ipv6 is not None:
        output["map_int32_string_ipv6"] = {
            key: value
            for key, value in request.map_int32_string_ipv6.items()
        }
    else:
        output["map_int32_string_ipv6"] = None

    if request.map_int32_string_value_ipv6 is not None:
        output["map_int32_string_value_ipv6"] = {
            key: value
            for key, value in request.map_int32_string_value_ipv6.items()
        }
    else:
        output["map_int32_string_value_ipv6"] = None

    if request.map_int32_strings_value is not None:
        output["map_int32_strings_value"] = {
            key: value
            for key, value in request.map_int32_strings_value.items()
        }
    else:
        output["map_int32_strings_value"] = None

    if request.map_int32_duration is not None:
        output["map_int32_duration"] = {
            key: value
            for key, value in request.map_int32_duration.items()
        }
    else:
        output["map_int32_duration"] = None


    return output

def marshal_PostAllOptionalMessageNestedMessage(
    request: PostAllOptionalMessageNestedMessage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.s is not None:
        output["s"] = request.s
    else:
        output["s"] = str()


    return output

def marshal_PostAllOptionalMessageNestedMessageWithOptional(
    request: PostAllOptionalMessageNestedMessageWithOptional,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.bb is not None:
        output["bb"] = request.bb
    else:
        output["bb"] = None


    return output

def marshal_PostAllOptionalRequest(
    request: PostAllOptionalRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.optional_int32 is not None:
        output["optional_int32"] = request.optional_int32
    else:
        output["optional_int32"] = None

    if request.optional_int64 is not None:
        output["optional_int64"] = request.optional_int64
    else:
        output["optional_int64"] = None

    if request.optional_uint32 is not None:
        output["optional_uint32"] = request.optional_uint32
    else:
        output["optional_uint32"] = None

    if request.optional_uint64 is not None:
        output["optional_uint64"] = request.optional_uint64
    else:
        output["optional_uint64"] = None

    if request.optional_sint32 is not None:
        output["optional_sint32"] = request.optional_sint32
    else:
        output["optional_sint32"] = None

    if request.optional_sint64 is not None:
        output["optional_sint64"] = request.optional_sint64
    else:
        output["optional_sint64"] = None

    if request.optional_fixed32 is not None:
        output["optional_fixed32"] = request.optional_fixed32
    else:
        output["optional_fixed32"] = None

    if request.optional_fixed64 is not None:
        output["optional_fixed64"] = request.optional_fixed64
    else:
        output["optional_fixed64"] = None

    if request.optional_sfixed32 is not None:
        output["optional_sfixed32"] = request.optional_sfixed32
    else:
        output["optional_sfixed32"] = None

    if request.optional_sfixed64 is not None:
        output["optional_sfixed64"] = request.optional_sfixed64
    else:
        output["optional_sfixed64"] = None

    if request.optional_float is not None:
        output["optional_float"] = request.optional_float
    else:
        output["optional_float"] = None

    if request.optional_double is not None:
        output["optional_double"] = request.optional_double
    else:
        output["optional_double"] = None

    if request.optional_bool is not None:
        output["optional_bool"] = request.optional_bool
    else:
        output["optional_bool"] = None

    if request.optional_string is not None:
        output["optional_string"] = request.optional_string
    else:
        output["optional_string"] = None

    if request.optional_bytes is not None:
        output["optional_bytes"] = request.optional_bytes
    else:
        output["optional_bytes"] = None

    if request.optional_cord is not None:
        output["optional_cord"] = request.optional_cord
    else:
        output["optional_cord"] = None

    if request.optional_nested_message_with_optional is not None:
        output["optional_nested_message_with_optional"] = marshal_PostAllOptionalMessageNestedMessageWithOptional(request.optional_nested_message_with_optional, defaults)
    else:
        output["optional_nested_message_with_optional"] = None

    if request.lazy_nested_message_with_optional is not None:
        output["lazy_nested_message_with_optional"] = marshal_PostAllOptionalMessageNestedMessageWithOptional(request.lazy_nested_message_with_optional, defaults)
    else:
        output["lazy_nested_message_with_optional"] = None

    if request.optional_nested_enum is not None:
        output["optional_nested_enum"] = str(request.optional_nested_enum)
    else:
        output["optional_nested_enum"] = None

    if request.optional_nested_message is not None:
        output["optional_nested_message"] = marshal_PostAllOptionalMessageNestedMessage(request.optional_nested_message, defaults)
    else:
        output["optional_nested_message"] = None

    if request.singular_int32 is not None:
        output["singular_int32"] = request.singular_int32
    else:
        output["singular_int32"] = str()

    if request.singular_int64 is not None:
        output["singular_int64"] = request.singular_int64
    else:
        output["singular_int64"] = str()

    if request.nested_message is not None:
        output["nested_message"] = marshal_PostAllOptionalMessageNestedMessage(request.nested_message, defaults)
    else:
        output["nested_message"] = None

    if request.singular_double_value is not None:
        output["singular_double_value"] = request.singular_double_value
    else:
        output["singular_double_value"] = None

    if request.singular_float_value is not None:
        output["singular_float_value"] = request.singular_float_value
    else:
        output["singular_float_value"] = None

    if request.singular_int64_value is not None:
        output["singular_int64_value"] = request.singular_int64_value
    else:
        output["singular_int64_value"] = None

    if request.singular_uint64_value is not None:
        output["singular_uint64_value"] = request.singular_uint64_value
    else:
        output["singular_uint64_value"] = None

    if request.singular_int32_value is not None:
        output["singular_int32_value"] = request.singular_int32_value
    else:
        output["singular_int32_value"] = None

    if request.singular_uint32_value is not None:
        output["singular_uint32_value"] = request.singular_uint32_value
    else:
        output["singular_uint32_value"] = None

    if request.singular_bool_value is not None:
        output["singular_bool_value"] = request.singular_bool_value
    else:
        output["singular_bool_value"] = None

    if request.singular_string_value is not None:
        output["singular_string_value"] = request.singular_string_value
    else:
        output["singular_string_value"] = None

    if request.singular_bytes_value is not None:
        output["singular_bytes_value"] = request.singular_bytes_value
    else:
        output["singular_bytes_value"] = None

    if request.singular_timestamp is not None:
        output["singular_timestamp"] = request.singular_timestamp.isoformat()
    else:
        output["singular_timestamp"] = None

    if request.singular_any is not None:
        output["singular_any"] = request.singular_any
    else:
        output["singular_any"] = None

    if request.singular_struct is not None:
        output["singular_struct"] = request.singular_struct
    else:
        output["singular_struct"] = None

    if request.singular_money is not None:
        output["singular_money"] = marshal_Money(request.singular_money, defaults)
    else:
        output["singular_money"] = None

    if request.singular_strings_value is not None:
        output["singular_strings_value"] = request.singular_strings_value
    else:
        output["singular_strings_value"] = None

    if request.singular_duration is not None:
        output["singular_duration"] = request.singular_duration
    else:
        output["singular_duration"] = None

    if request.map_string_string is not None:
        output["map_string_string"] = request.map_string_string
    else:
        output["map_string_string"] = None

    if request.timeseries is not None:
        output["timeseries"] = marshal_TimeSeries(request.timeseries, defaults)
    else:
        output["timeseries"] = None


    return output

def marshal_PostAllTypesRequest(
    request: PostAllTypesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="oneof_uint32", value=request.oneof_uint32,marshal_func=None
            ),
            OneOfPossibility(param="oneof_nested_message", value=request.oneof_nested_message,marshal_func=marshal_PostAllTypesMessageNestedMessage
            ),
            OneOfPossibility(param="oneof_string", value=request.oneof_string,marshal_func=None
            ),
            OneOfPossibility(param="oneof_bytes", value=request.oneof_bytes,marshal_func=None
            ),
        ]),
    )

    if request.singular_int32 is not None:
        output["singular_int32"] = request.singular_int32
    else:
        output["singular_int32"] = 0

    if request.singular_int64 is not None:
        output["singular_int64"] = request.singular_int64
    else:
        output["singular_int64"] = 0

    if request.singular_uint32 is not None:
        output["singular_uint32"] = request.singular_uint32
    else:
        output["singular_uint32"] = 0

    if request.singular_uint64 is not None:
        output["singular_uint64"] = request.singular_uint64
    else:
        output["singular_uint64"] = 0

    if request.singular_sint32 is not None:
        output["singular_sint32"] = request.singular_sint32
    else:
        output["singular_sint32"] = 0

    if request.singular_sint64 is not None:
        output["singular_sint64"] = request.singular_sint64
    else:
        output["singular_sint64"] = 0

    if request.singular_fixed32 is not None:
        output["singular_fixed32"] = request.singular_fixed32
    else:
        output["singular_fixed32"] = 0

    if request.singular_fixed64 is not None:
        output["singular_fixed64"] = request.singular_fixed64
    else:
        output["singular_fixed64"] = 0

    if request.singular_sfixed32 is not None:
        output["singular_sfixed32"] = request.singular_sfixed32
    else:
        output["singular_sfixed32"] = 0

    if request.singular_sfixed64 is not None:
        output["singular_sfixed64"] = request.singular_sfixed64
    else:
        output["singular_sfixed64"] = 0

    if request.singular_float is not None:
        output["singular_float"] = request.singular_float
    else:
        output["singular_float"] = 0.0

    if request.singular_double is not None:
        output["singular_double"] = request.singular_double
    else:
        output["singular_double"] = 0.0

    if request.singular_bool is not None:
        output["singular_bool"] = request.singular_bool
    else:
        output["singular_bool"] = False

    if request.singular_string is not None:
        output["singular_string"] = request.singular_string
    else:
        output["singular_string"] = str()

    if request.singular_bytes is not None:
        output["singular_bytes"] = request.singular_bytes
    else:
        output["singular_bytes"] = str()

    if request.singular_nested_message is not None:
        output["singular_nested_message"] = marshal_PostAllTypesMessageNestedMessage(request.singular_nested_message, defaults)
    else:
        output["singular_nested_message"] = None

    if request.singular_nested_enum is not None:
        output["singular_nested_enum"] = str(request.singular_nested_enum)
    else:
        output["singular_nested_enum"] = None

    if request.repeated_int32 is not None:
        output["repeated_int32"] = request.repeated_int32
    else:
        output["repeated_int32"] = None

    if request.repeated_int64 is not None:
        output["repeated_int64"] = request.repeated_int64
    else:
        output["repeated_int64"] = None

    if request.singular_string_ip is not None:
        output["singular_string_ip"] = request.singular_string_ip
    else:
        output["singular_string_ip"] = str()

    if request.singular_string_ipv4 is not None:
        output["singular_string_ipv4"] = request.singular_string_ipv4
    else:
        output["singular_string_ipv4"] = str()

    if request.singular_string_ipv6 is not None:
        output["singular_string_ipv6"] = request.singular_string_ipv6
    else:
        output["singular_string_ipv6"] = str()

    if request.singular_uint64_size is not None:
        output["singular_uint64_size"] = request.singular_uint64_size
    else:
        output["singular_uint64_size"] = 0

    if request.singular_string_ipnet is not None:
        output["singular_string_ipnet"] = request.singular_string_ipnet
    else:
        output["singular_string_ipnet"] = str()

    if request.repeated_uint32 is not None:
        output["repeated_uint32"] = request.repeated_uint32
    else:
        output["repeated_uint32"] = None

    if request.repeated_uint64 is not None:
        output["repeated_uint64"] = request.repeated_uint64
    else:
        output["repeated_uint64"] = None

    if request.repeated_sint32 is not None:
        output["repeated_sint32"] = request.repeated_sint32
    else:
        output["repeated_sint32"] = None

    if request.repeated_sint64 is not None:
        output["repeated_sint64"] = request.repeated_sint64
    else:
        output["repeated_sint64"] = None

    if request.repeated_fixed32 is not None:
        output["repeated_fixed32"] = request.repeated_fixed32
    else:
        output["repeated_fixed32"] = None

    if request.repeated_fixed64 is not None:
        output["repeated_fixed64"] = request.repeated_fixed64
    else:
        output["repeated_fixed64"] = None

    if request.repeated_sfixed32 is not None:
        output["repeated_sfixed32"] = request.repeated_sfixed32
    else:
        output["repeated_sfixed32"] = None

    if request.repeated_sfixed64 is not None:
        output["repeated_sfixed64"] = request.repeated_sfixed64
    else:
        output["repeated_sfixed64"] = None

    if request.repeated_float is not None:
        output["repeated_float"] = request.repeated_float
    else:
        output["repeated_float"] = None

    if request.repeated_double is not None:
        output["repeated_double"] = request.repeated_double
    else:
        output["repeated_double"] = None

    if request.repeated_bool is not None:
        output["repeated_bool"] = request.repeated_bool
    else:
        output["repeated_bool"] = None

    if request.repeated_string is not None:
        output["repeated_string"] = request.repeated_string
    else:
        output["repeated_string"] = None

    if request.repeated_bytes is not None:
        output["repeated_bytes"] = request.repeated_bytes
    else:
        output["repeated_bytes"] = None

    if request.repeated_nested_message is not None:
        output["repeated_nested_message"] = [marshal_PostAllTypesMessageNestedMessage(item, defaults) for item in request.repeated_nested_message]
    else:
        output["repeated_nested_message"] = None

    if request.repeated_nested_enum is not None:
        output["repeated_nested_enum"] = [str(item) for item in request.repeated_nested_enum]
    else:
        output["repeated_nested_enum"] = None

    if request.singular_double_value is not None:
        output["singular_double_value"] = request.singular_double_value
    else:
        output["singular_double_value"] = None

    if request.singular_float_value is not None:
        output["singular_float_value"] = request.singular_float_value
    else:
        output["singular_float_value"] = None

    if request.singular_int64_value is not None:
        output["singular_int64_value"] = request.singular_int64_value
    else:
        output["singular_int64_value"] = None

    if request.singular_uint64_value is not None:
        output["singular_uint64_value"] = request.singular_uint64_value
    else:
        output["singular_uint64_value"] = None

    if request.singular_int32_value is not None:
        output["singular_int32_value"] = request.singular_int32_value
    else:
        output["singular_int32_value"] = None

    if request.singular_uint32_value is not None:
        output["singular_uint32_value"] = request.singular_uint32_value
    else:
        output["singular_uint32_value"] = None

    if request.singular_bool_value is not None:
        output["singular_bool_value"] = request.singular_bool_value
    else:
        output["singular_bool_value"] = None

    if request.singular_string_value is not None:
        output["singular_string_value"] = request.singular_string_value
    else:
        output["singular_string_value"] = None

    if request.singular_bytes_value is not None:
        output["singular_bytes_value"] = request.singular_bytes_value
    else:
        output["singular_bytes_value"] = None

    if request.singular_timestamp is not None:
        output["singular_timestamp"] = request.singular_timestamp.isoformat()
    else:
        output["singular_timestamp"] = None

    if request.singular_any is not None:
        output["singular_any"] = request.singular_any
    else:
        output["singular_any"] = None

    if request.singular_struct is not None:
        output["singular_struct"] = request.singular_struct
    else:
        output["singular_struct"] = None

    if request.singular_money is not None:
        output["singular_money"] = marshal_Money(request.singular_money, defaults)
    else:
        output["singular_money"] = None

    if request.singular_strings_value is not None:
        output["singular_strings_value"] = request.singular_strings_value
    else:
        output["singular_strings_value"] = None

    if request.singular_duration is not None:
        output["singular_duration"] = request.singular_duration
    else:
        output["singular_duration"] = None

    if request.singular_ip is not None:
        output["singular_ip"] = request.singular_ip
    else:
        output["singular_ip"] = None

    if request.singular_string_value_ip is not None:
        output["singular_string_value_ip"] = request.singular_string_value_ip
    else:
        output["singular_string_value_ip"] = None

    if request.singular_ipv4 is not None:
        output["singular_ipv4"] = request.singular_ipv4
    else:
        output["singular_ipv4"] = None

    if request.singular_string_value_ipv4 is not None:
        output["singular_string_value_ipv4"] = request.singular_string_value_ipv4
    else:
        output["singular_string_value_ipv4"] = None

    if request.singular_ipv6 is not None:
        output["singular_ipv6"] = request.singular_ipv6
    else:
        output["singular_ipv6"] = None

    if request.singular_string_value_ipv6 is not None:
        output["singular_string_value_ipv6"] = request.singular_string_value_ipv6
    else:
        output["singular_string_value_ipv6"] = None

    if request.singular_std_duration is not None:
        output["singular_std_duration"] = request.singular_std_duration
    else:
        output["singular_std_duration"] = None

    if request.singular_std_long_duration is not None:
        output["singular_std_long_duration"] = request.singular_std_long_duration
    else:
        output["singular_std_long_duration"] = None

    if request.singular_size is not None:
        output["singular_size"] = request.singular_size
    else:
        output["singular_size"] = None

    if request.singular_uint64value_size is not None:
        output["singular_uint64value_size"] = request.singular_uint64value_size
    else:
        output["singular_uint64value_size"] = None

    if request.singular_string_value_ipnet is not None:
        output["singular_string_value_ipnet"] = request.singular_string_value_ipnet
    else:
        output["singular_string_value_ipnet"] = None

    if request.repeated_double_value is not None:
        output["repeated_double_value"] = request.repeated_double_value
    else:
        output["repeated_double_value"] = None

    if request.repeated_float_value is not None:
        output["repeated_float_value"] = request.repeated_float_value
    else:
        output["repeated_float_value"] = None

    if request.repeated_int64_value is not None:
        output["repeated_int64_value"] = request.repeated_int64_value
    else:
        output["repeated_int64_value"] = None

    if request.repeated_uint64_value is not None:
        output["repeated_uint64_value"] = request.repeated_uint64_value
    else:
        output["repeated_uint64_value"] = None

    if request.repeated_int32_value is not None:
        output["repeated_int32_value"] = request.repeated_int32_value
    else:
        output["repeated_int32_value"] = None

    if request.repeated_uint32_value is not None:
        output["repeated_uint32_value"] = request.repeated_uint32_value
    else:
        output["repeated_uint32_value"] = None

    if request.repeated_bool_value is not None:
        output["repeated_bool_value"] = request.repeated_bool_value
    else:
        output["repeated_bool_value"] = None

    if request.repeated_string_value is not None:
        output["repeated_string_value"] = request.repeated_string_value
    else:
        output["repeated_string_value"] = None

    if request.repeated_bytes_value is not None:
        output["repeated_bytes_value"] = request.repeated_bytes_value
    else:
        output["repeated_bytes_value"] = None

    if request.repeated_timestamp is not None:
        output["repeated_timestamp"] = request.repeated_timestamp
    else:
        output["repeated_timestamp"] = None

    if request.repeated_any is not None:
        output["repeated_any"] = request.repeated_any
    else:
        output["repeated_any"] = None

    if request.repeated_struct is not None:
        output["repeated_struct"] = request.repeated_struct
    else:
        output["repeated_struct"] = None

    if request.repeated_money is not None:
        output["repeated_money"] = [marshal_Money(item, defaults) for item in request.repeated_money]
    else:
        output["repeated_money"] = None

    if request.repeated_strings_value is not None:
        output["repeated_strings_value"] = request.repeated_strings_value
    else:
        output["repeated_strings_value"] = None

    if request.repeated_duration is not None:
        output["repeated_duration"] = request.repeated_duration
    else:
        output["repeated_duration"] = None

    if request.repeated_ip is not None:
        output["repeated_ip"] = request.repeated_ip
    else:
        output["repeated_ip"] = None

    if request.repeated_string_ip is not None:
        output["repeated_string_ip"] = request.repeated_string_ip
    else:
        output["repeated_string_ip"] = None

    if request.repeated_string_value_ip is not None:
        output["repeated_string_value_ip"] = request.repeated_string_value_ip
    else:
        output["repeated_string_value_ip"] = None

    if request.repeated_ipv4 is not None:
        output["repeated_ipv4"] = request.repeated_ipv4
    else:
        output["repeated_ipv4"] = None

    if request.repeated_string_ipv4 is not None:
        output["repeated_string_ipv4"] = request.repeated_string_ipv4
    else:
        output["repeated_string_ipv4"] = None

    if request.repeated_string_value_ipv4 is not None:
        output["repeated_string_value_ipv4"] = request.repeated_string_value_ipv4
    else:
        output["repeated_string_value_ipv4"] = None

    if request.repeated_ipv6 is not None:
        output["repeated_ipv6"] = request.repeated_ipv6
    else:
        output["repeated_ipv6"] = None

    if request.repeated_string_ipv6 is not None:
        output["repeated_string_ipv6"] = request.repeated_string_ipv6
    else:
        output["repeated_string_ipv6"] = None

    if request.repeated_string_value_ipv6 is not None:
        output["repeated_string_value_ipv6"] = request.repeated_string_value_ipv6
    else:
        output["repeated_string_value_ipv6"] = None

    if request.repeated_std_duration is not None:
        output["repeated_std_duration"] = request.repeated_std_duration
    else:
        output["repeated_std_duration"] = None

    if request.repeated_std_long_duration is not None:
        output["repeated_std_long_duration"] = request.repeated_std_long_duration
    else:
        output["repeated_std_long_duration"] = None

    if request.repeated_size is not None:
        output["repeated_size"] = request.repeated_size
    else:
        output["repeated_size"] = None

    if request.repeated_uint64_size is not None:
        output["repeated_uint64_size"] = request.repeated_uint64_size
    else:
        output["repeated_uint64_size"] = None

    if request.repeated_uint64value_size is not None:
        output["repeated_uint64value_size"] = request.repeated_uint64value_size
    else:
        output["repeated_uint64value_size"] = None

    if request.repeated_string_ipnet is not None:
        output["repeated_string_ipnet"] = request.repeated_string_ipnet
    else:
        output["repeated_string_ipnet"] = None

    if request.repeated_string_value_ipnet is not None:
        output["repeated_string_value_ipnet"] = request.repeated_string_value_ipnet
    else:
        output["repeated_string_value_ipnet"] = None


    return output

def marshal_PostBodyAndPathSimpleMessage(
    request: PostBodyAndPathSimpleMessage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.path is not None:
        output["path"] = request.path
    else:
        output["path"] = str()

    if request.body is not None:
        output["body"] = request.body
    else:
        output["body"] = str()


    return output

def marshal_PostBodyAndPathAndQueryRequest(
    request: PostBodyAndPathAndQueryRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.query is not None:
        output["query"] = request.query
    else:
        output["query"] = str()

    if request.body is not None:
        output["body"] = marshal_PostBodyAndPathSimpleMessage(request.body, defaults)
    else:
        output["body"] = None


    return output

def marshal_PostBodyAndPathComplexRequest(
    request: PostBodyAndPathComplexRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.body is not None:
        output["body"] = marshal_PostBodyAndPathSimpleMessage(request.body, defaults)
    else:
        output["body"] = None


    return output

def marshal_PostBodyAndPathSimple2Request(
    request: PostBodyAndPathSimple2Request,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.body is not None:
        output["body"] = request.body
    else:
        output["body"] = str()


    return output

def marshal_PostBodyAndPathSimpleRequest(
    request: PostBodyAndPathSimpleRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.body is not None:
        output["body"] = request.body
    else:
        output["body"] = str()


    return output

def marshal_ComplexValidateMsg(
    request: ComplexValidateMsg,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="x", value=request.x,marshal_func=None
            ),
            OneOfPossibility(param="y", value=request.y,marshal_func=None
            ),
        ]),
    )

    if request.const is not None:
        output["const"] = request.const
    else:
        output["const"] = str()

    if request.int_const is not None:
        output["int_const"] = request.int_const
    else:
        output["int_const"] = str()

    if request.bool_const is not None:
        output["bool_const"] = request.bool_const
    else:
        output["bool_const"] = str()

    if request.float_const is not None:
        output["float_const"] = request.float_const
    else:
        output["float_const"] = str()

    if request.nested is not None:
        output["nested"] = marshal_ComplexValidateMsg(request.nested, defaults)
    else:
        output["nested"] = None

    if request.float_val is not None:
        output["float_val"] = request.float_val
    else:
        output["float_val"] = None

    if request.dur_val is not None:
        output["dur_val"] = request.dur_val
    else:
        output["dur_val"] = None

    if request.ts_val is not None:
        output["ts_val"] = request.ts_val.isoformat()
    else:
        output["ts_val"] = None

    if request.another is not None:
        output["another"] = marshal_ComplexValidateMsg(request.another, defaults)
    else:
        output["another"] = None

    if request.double_in is not None:
        output["double_in"] = request.double_in
    else:
        output["double_in"] = str()

    if request.enum_const is not None:
        output["enum_const"] = str(request.enum_const)
    else:
        output["enum_const"] = str()

    if request.rep_ts_val is not None:
        output["rep_ts_val"] = request.rep_ts_val
    else:
        output["rep_ts_val"] = str()

    if request.map_val is not None:
        output["map_val"] = {
            key: value
            for key, value in request.map_val.items()
        }
    else:
        output["map_val"] = str()

    if request.bytes_val is not None:
        output["bytes_val"] = request.bytes_val
    else:
        output["bytes_val"] = str()

    if request.any_val is not None:
        output["any_val"] = request.any_val
    else:
        output["any_val"] = None


    return output

def marshal_PostComplexValidateRequest(
    request: PostComplexValidateRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.val is not None:
        output["val"] = marshal_ComplexValidateMsg(request.val, defaults)
    else:
        output["val"] = None


    return output

def marshal_PostDeprecatedOrganizationRequest(
    request: PostDeprecatedOrganizationRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.organization is not None:
        output["organization"] = request.organization
    else:
        output["organization"] = None


    return output

def marshal_PostDeprecatedProjectRequest(
    request: PostDeprecatedProjectRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project is not None:
        output["project"] = request.project
    else:
        output["project"] = None


    return output

def marshal_PostEchoRequest(
    request: PostEchoRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.str_ is not None:
        output["str"] = request.str_
    else:
        output["str"] = None

    if request.strs is not None:
        output["strs"] = request.strs
    else:
        output["strs"] = None


    return output

def marshal_PostEchoTimeSeriesRequest(
    request: PostEchoTimeSeriesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.metrics is not None:
        output["metrics"] = marshal_TimeSeries(request.metrics, defaults)
    else:
        output["metrics"] = None


    return output

def marshal_PostEnumRequest(
    request: PostEnumRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.type_ is not None:
        output["type"] = str(request.type_)
    else:
        output["type"] = None

    if request.type2 is not None:
        output["type2"] = str(request.type2)
    else:
        output["type2"] = None

    if request.type3 is not None:
        output["type3"] = str(request.type3)
    else:
        output["type3"] = str()


    return output

def marshal_PostIPRequest(
    request: PostIPRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.ip_v4 is not None:
        output["ip_v4"] = request.ip_v4
    else:
        output["ip_v4"] = None

    if request.ip_v6 is not None:
        output["ip_v6"] = request.ip_v6
    else:
        output["ip_v6"] = None

    if request.ip is not None:
        output["ip"] = request.ip
    else:
        output["ip"] = None


    return output

def marshal_EchoMessage(
    request: EchoMessage,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.str_ is not None:
        output["str"] = request.str_
    else:
        output["str"] = str()

    if request.strs is not None:
        output["strs"] = request.strs
    else:
        output["strs"] = str()


    return output

def marshal_PostOneOfRequest(
    request: PostOneOfRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    output.update(
        resolve_one_of([
            OneOfPossibility(param="test", value=request.test,marshal_func=None
            ),
            OneOfPossibility(param="test2", value=request.test2,marshal_func=None
            ),
        ]),
    )
    output.update(
        resolve_one_of([
            OneOfPossibility(param="test_nested", value=request.test_nested,marshal_func=marshal_EchoMessage
            ),
            OneOfPossibility(param="test3", value=request.test3,marshal_func=None
            ),
        ]),
    )


    return output

def marshal_PostOrganizationIdRequest(
    request: PostOrganizationIdRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.organization_id is not None:
        output["organization_id"] = request.organization_id or defaults.default_organization_id
    else:
        output["organization_id"] = None


    return output

def marshal_PostProjectIdRequest(
    request: PostProjectIdRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.project_id is not None:
        output["project_id"] = request.project_id or defaults.default_project_id
    else:
        output["project_id"] = None


    return output

def marshal_PostScalarTypesRequest(
    request: PostScalarTypesRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.double_field is not None:
        output["double_field"] = request.double_field
    else:
        output["double_field"] = str()

    if request.float_field is not None:
        output["float_field"] = request.float_field
    else:
        output["float_field"] = str()

    if request.int32_field is not None:
        output["int32_field"] = request.int32_field
    else:
        output["int32_field"] = str()

    if request.int64_field is not None:
        output["int64_field"] = request.int64_field
    else:
        output["int64_field"] = str()

    if request.uint32_field is not None:
        output["uint32_field"] = request.uint32_field
    else:
        output["uint32_field"] = str()

    if request.uint64_field is not None:
        output["uint64_field"] = request.uint64_field
    else:
        output["uint64_field"] = str()

    if request.bool_field is not None:
        output["bool_field"] = request.bool_field
    else:
        output["bool_field"] = str()

    if request.string_field is not None:
        output["string_field"] = request.string_field
    else:
        output["string_field"] = str()


    return output

def marshal_PostTagsRequest(
    request: PostTagsRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.tags is not None:
        output["tags"] = request.tags
    else:
        output["tags"] = None


    return output

def marshal_PostWaitRequest(
    request: PostWaitRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.duration is not None:
        output["duration"] = request.duration
    else:
        output["duration"] = None


    return output

def marshal_RegionalApiPostEchoRequest(
    request: RegionalApiPostEchoRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.str_ is not None:
        output["str"] = request.str_
    else:
        output["str"] = None

    if request.strs is not None:
        output["strs"] = request.strs
    else:
        output["strs"] = None


    return output

def marshal_ZoneApiPostEchoRequest(
    request: ZoneApiPostEchoRequest,
    defaults: ProfileDefaults,
) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    if request.str_ is not None:
        output["str"] = request.str_
    else:
        output["str"] = None

    if request.strs is not None:
        output["strs"] = request.strs
    else:
        output["strs"] = None


    return output
