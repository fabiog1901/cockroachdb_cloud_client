from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cmek_key_specification import CMEKKeySpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="CMEKRegionSpecification")


@attr.s(auto_attribs=True)
class CMEKRegionSpecification:
    """CMEKRegionSpecification declares the customer-provided key specification that
    should be used in a given region.

        Attributes:
            region (Union[Unset, str]):
            key_spec (Union[Unset, CMEKKeySpecification]): CMEKKeySpecification contains all the details necessary to use a
                customer-provided
                encryption key. This involves the type/location of the key and the principal
                to authenticate as when accessing it.
    """

    region: Union[Unset, str] = UNSET
    key_spec: Union[Unset, CMEKKeySpecification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region = self.region
        key_spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_spec, Unset):
            key_spec = self.key_spec.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if key_spec is not UNSET:
            field_dict["key_spec"] = key_spec

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region = d.pop("region", UNSET)

        _key_spec = d.pop("key_spec", UNSET)
        key_spec: Union[Unset, CMEKKeySpecification]
        if isinstance(_key_spec, Unset):
            key_spec = UNSET
        else:
            key_spec = CMEKKeySpecification.from_dict(_key_spec)

        cmek_region_specification = cls(
            region=region,
            key_spec=key_spec,
        )

        cmek_region_specification.additional_properties = d
        return cmek_region_specification

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