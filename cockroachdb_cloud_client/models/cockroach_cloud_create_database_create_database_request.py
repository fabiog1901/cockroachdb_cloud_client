from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CockroachCloudCreateDatabaseCreateDatabaseRequest")


@attr.s(auto_attribs=True)
class CockroachCloudCreateDatabaseCreateDatabaseRequest:
    """
    Example:
        {'name': 'example_database_name'}

    Attributes:
        name (str):
    """

    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        cockroach_cloud_create_database_create_database_request = cls(
            name=name,
        )

        cockroach_cloud_create_database_create_database_request.additional_properties = d
        return cockroach_cloud_create_database_create_database_request

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
