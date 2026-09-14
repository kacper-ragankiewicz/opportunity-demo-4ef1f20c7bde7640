from flask import Flask, jsonify, request

app = Flask(__name__, static_folder="static", static_url_path="/static")

VALID_STATUSES = {"planned", "in_progress", "done"}
WORK_ITEMS = [
    {"id": 101, "title": "Auth service cleanup", "owner": "Maya", "status": "planned", "priority": "medium"},
    {"id": 102, "title": "Usage events API", "owner": "Noah", "status": "in_progress", "priority": "high"},
    {"id": 103, "title": "Billing webhook retries", "owner": "Leah", "status": "done", "priority": "high"},
    {"id": 104, "title": "Admin table pagination", "owner": "Maya", "status": "in_progress", "priority": "medium"},
]


@app.get("/")
def index():
    return app.send_static_file("index.html")


@app.get("/api/work-items")
def work_items():
    status = request.args.get("status", "").strip()
    if status and status not in VALID_STATUSES:
        return jsonify({
            "error": "invalid_status",
            "allowed": sorted(VALID_STATUSES),
        }), 400

    items = [item for item in WORK_ITEMS if not status or item["status"] == status]
    summary = {
        current: sum(1 for item in WORK_ITEMS if item["status"] == current)
        for current in sorted(VALID_STATUSES)
    }
    return jsonify({
        "items": items,
        "summary": summary,
        "filters": {"status": status or None},
    })


if __name__ == "__main__":
    app.run(debug=True)
