from enum import Enum
from mobile.domain.fee.MonthlyFee import MonthlyFee

class Plan(Enum):
    plan_1ギガ = MonthlyFee(1000)

