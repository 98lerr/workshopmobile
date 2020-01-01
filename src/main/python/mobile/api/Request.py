from mobile.domain.plan.Plan import Plan
from mobile.domain.option.エンタメフリーオプション import エンタメフリーオプション
from mobile.domain.contract.契約 import 契約


class Request:
    def __init__(self, plan: str, entame_free: str):
        self.plan = plan
        self.entame_free = entame_free

    def get_plan(self):
        if self.plan == "g1":
            return Plan.plan_1ギガ
        if self.plan == "g3":
            return Plan.plan_3ギガ
        if self.plan == "g30":
            return Plan.plan_30ギガ
        raise RuntimeError("failed")

    def get_entame_free(self) -> エンタメフリーオプション:
        if self.entame_free == "true":
            return エンタメフリーオプション.あり
        if self.entame_free == "false":
            return エンタメフリーオプション.なし
        raise RuntimeError("failed")

    def get_contract(self) -> 契約:
        return 契約(self.get_plan(), self.get_entame_free())
