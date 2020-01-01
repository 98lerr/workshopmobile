from enum import Enum
from mobile.domain.fee.MonthlyFee import MonthlyFee


class エンタメフリーオプション(Enum):
    なし = MonthlyFee(0)
    あり = MonthlyFee(1200)
