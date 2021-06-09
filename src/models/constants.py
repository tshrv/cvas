import enum
from src.cowin.constants import Vaccine, Dose


class AlertStatus(enum.Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
