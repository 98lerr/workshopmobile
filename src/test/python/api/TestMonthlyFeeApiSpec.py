from mobile.api.MonthlyFeeApi import app
import json
import pytest

@pytest.mark.parametrize("plan, entame_free",
                         [
                             ("g1", "true"),
                         ])
def test_1ギガプランでエンタメフリーありならエラー(plan, entame_free):
    response = app.test_client().get(
        "/monthly-fee?plan={plan}&entame_free={entame_free}".format(
            plan=plan, entame_free=entame_free
        )
    )

    assert response.status_code >= 400


@pytest.mark.parametrize("plan, entame_free, monthly_fee",
                         [
                             ("g1", "false", 1000),
                             ("g3", "false", 2000),
                             ("g30", "false", 6000),
                             ("g3", "true", 2000 + 1200),
                             ("g30", "true", 6000 + 1200),
                         ])
def test_プランとエンタメフリーオプション(plan, entame_free, monthly_fee):
    response = app.test_client().get(
        "/monthly-fee?plan={plan}&entame_free={entame_free}".format(
            plan=plan, entame_free=entame_free
        )
    )

    data_dict = response.get_data(as_text=True)
    data = json.loads(data_dict)

    assert response.status_code == 200
    assert data["monthly_fee"] == monthly_fee
