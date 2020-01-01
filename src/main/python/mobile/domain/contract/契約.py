from mobile.domain.plan.Plan import Plan
from mobile.domain.option.エンタメフリーオプション import エンタメフリーオプション


class 契約:
    def __init__(self, プラン:Plan, エンタメフリーオプション: エンタメフリーオプション):
        if プラン == Plan.plan_1ギガ and エンタメフリーオプション == エンタメフリーオプション.あり:
            raise RuntimeError
        self.plan = プラン
        self.entame_free = エンタメフリーオプション

    def 月額を取得(self):
        return self.plan.value.get_value() + self.entame_free.value.get_value()
