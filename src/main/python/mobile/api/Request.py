from mobile.domain.plan.Plan import Plan


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
