from datetime import datetime
from flask import Flask, jsonify, request

import config
from object.IP import IP
from database.db import BanHeimDB
from database.QueryBuilder import QueryBuilder
from database.table import ReportedTable

app = Flask(__name__)


@app.route("/api/v1/report/", methods=["GET"])
def get_reported():
    db = BanHeimDB(config.SQL_DB_URL)
    qb = QueryBuilder(db)

    res = db.execute(qb.select(ReportedTable))

    result = []

    for row in list(res):
        result.append(row[0].to_dict())

    return jsonify({"status": "ok", "response": result})


@app.route("/api/v1/report/<string:ip>", methods=["POST"])
def report(ip):
    if IP.is_address(ip):
        try:
            data = request.json
            reporter = data["reporter"] or "unknown"
            reason = data["reason"] or "unknown"
            timestamp = data["timestamp"] or datetime.now()

            ip = IP(ip)
            ip.add_report(reporter, reason, timestamp)

            return jsonify({"status": "ok"})

        except Exception:
            return jsonify({"status": "error", "response": "Unable to retrieves data"})


if __name__ == "__main__":
    app.run()
