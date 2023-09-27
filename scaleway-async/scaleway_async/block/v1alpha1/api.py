# This file was automatically generated. DO NOT EDIT.
# If you have any remark or suggestion do not hesitate to open an issue.

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
    ListSnapshotsRequestOrderBy,
    ListVolumesRequestOrderBy,
    CreateVolumeRequestFromEmpty,
    CreateVolumeRequestFromSnapshot,
    ListSnapshotsResponse,
    ListVolumeTypesResponse,
    ListVolumesResponse,
    Snapshot,
    SnapshotSummary,
    Volume,
    VolumeType,
    CreateVolumeRequest,
    UpdateVolumeRequest,
    CreateSnapshotRequest,
    UpdateSnapshotRequest,
)
from .content import (
    SNAPSHOT_TRANSIENT_STATUSES,
    VOLUME_TRANSIENT_STATUSES,
)
from .marshalling import (
    marshal_CreateSnapshotRequest,
    marshal_CreateVolumeRequest,
    marshal_UpdateSnapshotRequest,
    marshal_UpdateVolumeRequest,
    unmarshal_Volume,
    unmarshal_ListSnapshotsResponse,
    unmarshal_ListVolumeTypesResponse,
    unmarshal_ListVolumesResponse,
    unmarshal_Snapshot,
)


class BlockV1Alpha1API(API):
    """
    Scaleway Block Storage (SBS) API.

    This API allows you to use and manage your Block Storage volumes.
    Scaleway Block Storage (SBS) API.
    """

    async def list_volume_types(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ListVolumeTypesResponse:
        """
        List volume types.
        List all available volume types in a specified zone. The volume types listed are ordered by name in ascending order.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :return: :class:`ListVolumeTypesResponse <ListVolumeTypesResponse>`

        Usage:
        ::

            result = await api.list_volume_types()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volume-types",
            params={
                "page": page,
                "page_size": page_size or self.client.default_page_size,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumeTypesResponse(res.json())

    async def list_volume_types_all(
        self,
        *,
        zone: Optional[Zone] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[VolumeType]:
        """
        List volume types.
        List all available volume types in a specified zone. The volume types listed are ordered by name in ascending order.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :return: :class:`List[ListVolumeTypesResponse] <List[ListVolumeTypesResponse]>`

        Usage:
        ::

            result = await api.list_volume_types_all()
        """

        return await fetch_all_pages_async(
            type=ListVolumeTypesResponse,
            key="volume_types",
            fetcher=self.list_volume_types,
            args={
                "zone": zone,
                "page": page,
                "page_size": page_size,
            },
        )

    async def list_volumes(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListVolumesRequestOrderBy = ListVolumesRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        product_resource_id: Optional[str] = None,
    ) -> ListVolumesResponse:
        """
        List volumes.
        List all existing volumes in a specified zone. By default, the volume listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned volumes.
        :param project_id: Only list volumes of this project ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param name: Filter the return volumes by their names.
        :param product_resource_id: Filter by a Product Resource Id linked to this volume (such as an Instance Server Id).
        :return: :class:`ListVolumesResponse <ListVolumesResponse>`

        Usage:
        ::

            result = await api.list_volumes()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volumes",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "product_resource_id": product_resource_id,
                "project_id": project_id or self.client.default_project_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListVolumesResponse(res.json())

    async def list_volumes_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListVolumesRequestOrderBy] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        name: Optional[str] = None,
        product_resource_id: Optional[str] = None,
    ) -> List[Volume]:
        """
        List volumes.
        List all existing volumes in a specified zone. By default, the volume listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned volumes.
        :param project_id: Only list volumes of this project ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param name: Filter the return volumes by their names.
        :param product_resource_id: Filter by a Product Resource Id linked to this volume (such as an Instance Server Id).
        :return: :class:`List[ListVolumesResponse] <List[ListVolumesResponse]>`

        Usage:
        ::

            result = await api.list_volumes_all()
        """

        return await fetch_all_pages_async(
            type=ListVolumesResponse,
            key="volumes",
            fetcher=self.list_volumes,
            args={
                "zone": zone,
                "order_by": order_by,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "name": name,
                "product_resource_id": product_resource_id,
            },
        )

    async def create_volume(
        self,
        *,
        name: str,
        zone: Optional[Zone] = None,
        perf_iops: Optional[int] = None,
        project_id: Optional[str] = None,
        from_empty: Optional[CreateVolumeRequestFromEmpty] = None,
        from_snapshot: Optional[CreateVolumeRequestFromSnapshot] = None,
        tags: Optional[List[str]] = None,
    ) -> Volume:
        """
        Create a new empty volume by specifying the `size`.
        To create a volume from an existing snapshot, specify the `snapshot_id` in the request payload instead, size is optional and can be specified if you need to extend the original size.
        In that case the created volume will have the same volume class (and underlying IOPS limitations) as the originating snapshot.
        You can specify the desired performance of the volume by setting `requirements` accordingly.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param name: Name of the volume you want to create.
        :param perf_iops: The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).

        One-of ('requirements'): at most one of 'perf_iops' could be set.
        :param project_id: UUID of the project the volume belongs to.
        :param from_empty: Create a new and empty volume.

        One-of ('from_'): at most one of 'from_empty', 'from_snapshot' could be set.
        :param from_snapshot: Create a volume from an existing snapshot.

        One-of ('from_'): at most one of 'from_empty', 'from_snapshot' could be set.
        :param tags: List of tags assigned to the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.create_volume(name="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/volumes",
            body=marshal_CreateVolumeRequest(
                CreateVolumeRequest(
                    name=name,
                    zone=zone,
                    perf_iops=perf_iops,
                    project_id=project_id,
                    from_empty=from_empty,
                    from_snapshot=from_snapshot,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def get_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> Volume:
        """
        Get a volume.
        Retrieve technical information about a specific volume. Details such as size, type, and status are returned in the response.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: UUID of the volume you want to get.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.get_volume(volume_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def wait_for_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        options: Optional[WaitForOptions[Volume, Union[bool, Awaitable[bool]]]] = None,
    ) -> Volume:
        """
        Waits for :class:`Volume <Volume>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: UUID of the volume you want to get.
        :param options: The options for the waiter
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = api.wait_for_volume(volume_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in VOLUME_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_volume,
            options=options,
            args={
                "volume_id": volume_id,
                "zone": zone,
            },
        )

    async def delete_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a detached volume.
        You must specify the `volume_id` of the volume you want to delete. The volume must not be in the `in_use` status.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: UUID of the volume.

        Usage:
        ::

            result = await api.delete_volume(volume_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "DELETE",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
        )

        self._throw_on_error(res)
        return None

    async def update_volume(
        self,
        *,
        volume_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        size: Optional[int] = None,
        tags: Optional[List[str]] = None,
        perf_iops: Optional[int] = None,
    ) -> Volume:
        """
        Update a volume.
        Update technical details about a volume, such as its name, tags, or its new size and `volume_type` (within the same Block Storage class).
        You can only resize a volume to a larger size. It is not possible for now to change your Block Storage Class.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: UUID of the volume.
        :param name: When defined, is the new name of the volume.
        :param size: Optional field for growing a volume (size must be equal or larger than the current one).
        Size in bytes of the volume, with a granularity of 1 GB (10^9 bytes).
        Must be compliant with the minimum and maximum allowed size.
        :param tags: List of tags assigned to the volume.
        :param perf_iops: The maximum IO/s expected, according to the different options available in stock (`5000 | 15000`).
        The selected value must be available on the Storage Class where is currently located the volume.
        :return: :class:`Volume <Volume>`

        Usage:
        ::

            result = await api.update_volume(volume_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_volume_id = validate_path_param("volume_id", volume_id)

        res = self._request(
            "PATCH",
            f"/block/v1alpha1/zones/{param_zone}/volumes/{param_volume_id}",
            body=marshal_UpdateVolumeRequest(
                UpdateVolumeRequest(
                    volume_id=volume_id,
                    zone=zone,
                    name=name,
                    size=size,
                    tags=tags,
                    perf_iops=perf_iops,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Volume(res.json())

    async def list_snapshots(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: ListSnapshotsRequestOrderBy = ListSnapshotsRequestOrderBy.CREATED_AT_ASC,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        volume_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ListSnapshotsResponse:
        """
        List all snapshots.
        List all available snapshots in a specified zone. By default, the snapshots listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned snapshots.
        :param project_id: Only list snapshots of this project ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param volume_id: Filter the return snapshots by the volume it belongs to.
        :param name: Filter the return snapshots by their names.
        :return: :class:`ListSnapshotsResponse <ListSnapshotsResponse>`

        Usage:
        ::

            result = await api.list_snapshots()
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/snapshots",
            params={
                "name": name,
                "order_by": order_by,
                "page": page,
                "page_size": page_size or self.client.default_page_size,
                "project_id": project_id or self.client.default_project_id,
                "volume_id": volume_id,
            },
        )

        self._throw_on_error(res)
        return unmarshal_ListSnapshotsResponse(res.json())

    async def list_snapshots_all(
        self,
        *,
        zone: Optional[Zone] = None,
        order_by: Optional[ListSnapshotsRequestOrderBy] = None,
        project_id: Optional[str] = None,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        volume_id: Optional[str] = None,
        name: Optional[str] = None,
    ) -> List[SnapshotSummary]:
        """
        List all snapshots.
        List all available snapshots in a specified zone. By default, the snapshots listed are ordered by creation date in ascending order. This can be modified via the `order_by` field.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param order_by: Sort order of the returned snapshots.
        :param project_id: Only list snapshots of this project ID.
        :param page: Positive integer to choose the page to return.
        :param page_size: Positive integer lower or equal to 100 to select the number of items to return.
        :param volume_id: Filter the return snapshots by the volume it belongs to.
        :param name: Filter the return snapshots by their names.
        :return: :class:`List[ListSnapshotsResponse] <List[ListSnapshotsResponse]>`

        Usage:
        ::

            result = await api.list_snapshots_all()
        """

        return await fetch_all_pages_async(
            type=ListSnapshotsResponse,
            key="snapshots",
            fetcher=self.list_snapshots,
            args={
                "zone": zone,
                "order_by": order_by,
                "project_id": project_id,
                "page": page,
                "page_size": page_size,
                "volume_id": volume_id,
                "name": name,
            },
        )

    async def get_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> Snapshot:
        """
        Get a snapshot.
        Retrieve technical information about a specific snapshot. Details such as size, volume type, and status are returned in the response.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param snapshot_id: UUID of the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.get_snapshot(snapshot_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "GET",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def wait_for_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
        options: Optional[
            WaitForOptions[Snapshot, Union[bool, Awaitable[bool]]]
        ] = None,
    ) -> Snapshot:
        """
        Waits for :class:`Snapshot <Snapshot>` to be in a final state.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param snapshot_id: UUID of the snapshot.
        :param options: The options for the waiter
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = api.wait_for_snapshot(snapshot_id="example")
        """

        if not options:
            options = WaitForOptions()

        if not options.stop:
            options.stop = lambda res: res.status not in SNAPSHOT_TRANSIENT_STATUSES

        return await wait_for_resource_async(
            fetcher=self.get_snapshot,
            options=options,
            args={
                "snapshot_id": snapshot_id,
                "zone": zone,
            },
        )

    async def create_snapshot(
        self,
        *,
        volume_id: str,
        name: str,
        zone: Optional[Zone] = None,
        project_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Snapshot:
        """
        Create a snapshot of a volume.
        To create a snapshot, the volume must be in the `in_use` or the `available` status.
        If your volume is in a transient state, you need to wait until the end of the current operation.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param volume_id: UUID of the volume from which creates a snpashot.
        :param name: Name of the snapshot.
        :param project_id: UUID of the project the volume and the snapshot belong to.
        :param tags: List of tags assigned to the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.create_snapshot(
                volume_id="example",
                name="example",
            )
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)

        res = self._request(
            "POST",
            f"/block/v1alpha1/zones/{param_zone}/snapshots",
            body=marshal_CreateSnapshotRequest(
                CreateSnapshotRequest(
                    volume_id=volume_id,
                    name=name,
                    zone=zone,
                    project_id=project_id,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())

    async def delete_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
    ) -> Optional[None]:
        """
        Delete a snapshot.
        You must specify the `snapshot_id` of the snapshot you want to delete. The snapshot must not be in use.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param snapshot_id: UUID of the snapshot.

        Usage:
        ::

            result = await api.delete_snapshot(snapshot_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "DELETE",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
        )

        self._throw_on_error(res)
        return None

    async def update_snapshot(
        self,
        *,
        snapshot_id: str,
        zone: Optional[Zone] = None,
        name: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> Snapshot:
        """
        Update a snapshot.
        Update name or tags of the snapshot.
        :param zone: Zone to target. If none is passed will use default zone from the config.
        :param snapshot_id: UUID of the snapshot.
        :param name: When defined, is the name of the snapshot.
        :param tags: List of tags assigned to the snapshot.
        :return: :class:`Snapshot <Snapshot>`

        Usage:
        ::

            result = await api.update_snapshot(snapshot_id="example")
        """

        param_zone = validate_path_param("zone", zone or self.client.default_zone)
        param_snapshot_id = validate_path_param("snapshot_id", snapshot_id)

        res = self._request(
            "PATCH",
            f"/block/v1alpha1/zones/{param_zone}/snapshots/{param_snapshot_id}",
            body=marshal_UpdateSnapshotRequest(
                UpdateSnapshotRequest(
                    snapshot_id=snapshot_id,
                    zone=zone,
                    name=name,
                    tags=tags,
                ),
                self.client,
            ),
        )

        self._throw_on_error(res)
        return unmarshal_Snapshot(res.json())
