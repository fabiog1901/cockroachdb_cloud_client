from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="AWSPrivateLinkServiceDetail")


@attr.s(auto_attribs=True)
class AWSPrivateLinkServiceDetail:
    """
    Attributes:
        service_name (str): ServiceName is the AWS service name customers use to create endpoints on their end.
        service_id (str): ServiceID is the server side of the PrivateLink
            connection. This is the same as AWSPrivateLinkEndpoint.service_id.
        availability_zone_ids (List[str]): AvailabilityZoneIDs are the identifiers for the availability zones that the
            service
            is available in.
    """

    service_name: str
    service_id: str
    availability_zone_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_name = self.service_name
        service_id = self.service_id
        availability_zone_ids = self.availability_zone_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service_name": service_name,
                "service_id": service_id,
                "availability_zone_ids": availability_zone_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_name = d.pop("service_name")

        service_id = d.pop("service_id")

        availability_zone_ids = cast(List[str], d.pop("availability_zone_ids"))

        aws_private_link_service_detail = cls(
            service_name=service_name,
            service_id=service_id,
            availability_zone_ids=availability_zone_ids,
        )

        aws_private_link_service_detail.additional_properties = d
        return aws_private_link_service_detail

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties