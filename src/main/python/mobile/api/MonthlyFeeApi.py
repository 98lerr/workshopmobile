from mobile.api.Request import Request
from mobile.domain.plan.Plan import Plan
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/monthly-fee", methods=['GET'])
def monthly_fee():
    request_obj = Request(request.args.get("plan"), request.args.get("entame_free"))
    response = {"monthly_fee": Plan.plan_1ギガ.value.get_value()}

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

