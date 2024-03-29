from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.egress_rule import EgressRule


T = TypeVar("T", bound="GetEgressRuleResponse")


@attr.s(auto_attribs=True)
class GetEgressRuleResponse:
    """GetEgressRuleResponse is the response message to the GetEgressRule RPC.

    Attributes:
        rule (EgressRule): EgressRule represents a network egress rule.
    """

    rule: "EgressRule"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rule = self.rule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.egress_rule import EgressRule

        d = src_dict.copy()
        rule = EgressRule.from_dict(d.pop("rule"))

        get_egress_rule_response = cls(
            rule=rule,
        )

        get_egress_rule_response.additional_properties = d
        return get_egress_rule_response

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
