from flask import Flask, request, jsonify
from shared.queries import get_prices_by_crop, get_markets

app = Flask(__name__)

@app.route("/prices")
def prices():
    crop = request.args.get("crop")
    return jsonify(get_prices_by_crop(crop))

@app.route("/markets")
def markets():
    return jsonify(get_markets())

app.run(debug=True)