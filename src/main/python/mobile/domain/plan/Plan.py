from enum import Enum
from mobile.domain.fee.MonthlyFee import MonthlyFee


class Plan(Enum):
    plan_1ギガ = MonthlyFee(1000)
    plan_3ギガ = MonthlyFee(2000)
    plan_30ギガ = MonthlyFee(6000)

