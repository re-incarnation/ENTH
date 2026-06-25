from dataclasses import dataclass, asdict
from datetime import datetime
import uuid


STATUS_NEW = "new"
STATUS_SKIPPED = "skipped"
STATUS_PUNISHED = "punished"

SEVERITY_YELLOW = "yellow"
SEVERITY_RED = "red"


@dataclass
class TriggerEvent:
    id: str
    created_at: str

    player: str
    message: str

    rule_id: str
    rule_name: str

    severity: str
    status: str

    @classmethod
    def create(
        cls,
        player: str,
        message: str,
        rule_id: str,
        rule_name: str,
        severity: str
    ):
        return cls(
            id=str(uuid.uuid4()),
            created_at=datetime.now().isoformat(),

            player=player,
            message=message,

            rule_id=rule_id,
            rule_name=rule_name,

            severity=severity,
            status=STATUS_NEW
        )

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)