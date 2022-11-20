from flask import Flask, render_template, request, jsonify
from celery import Celery
from celery.result import AsyncResult

import uuid
from pathlib import Path

UPLOAD_PATH = '/site-data/uploads/'  # TODO: env
upload_path = Path(UPLOAD_PATH)


celery = Celery(
    "transformer",
    broker="redis://redis",
    backend="redis://redis"
)

app = Flask(__name__)


@app.route("/api/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return 400
    file = request.files['file']
    filename = str(uuid.uuid1()) + '.jpg'
    file_path = upload_path / filename[:2] / filename
    # TODO: validate jpeg
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file.save(file_path)
    task = celery.send_task(
        'transform', (str(file_path), 0))  # Send task by name
    return {"status": "working", "task-id": task.id}


@app.route("/api/check-result/<taskid>")
def check_result(taskid: str = None):
    if taskid == '':
        return {"status": "error", "message": "taskid required"}
    try:
        task = AsyncResult(taskid)
    except Exception as e:
        return {"status": "error", "error": str(e)}
    if task.state != "SUCCESS":
        return {"status": task.state}
    return {"status": task.state, "result": task.get()}


if __name__ == "__main__":
    HOST = ""
    PORT = 5000
    app.run(HOST, PORT, debug=True)
