from flask import Blueprint, request, jsonify
from app.services import task_service

task_routes = Blueprint("task_routes", __name__)

@task_routes.get("/")
def get_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@task_routes.post("/")
def create_task():
    data = request.get_json()

    if not data or "description" not in data:
        return jsonify({"error": "description is required"}), 400

    task = task_service.create_task(data["description"])
    return jsonify(task.to_dict()), 201

@task_routes.put("/<int:task_id>/start")
def start_task(task_id):
    task = task_service.start_task(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict())

@task_routes.put("/<int:task_id>/complete")
def complete_task(task_id):
    task = task_service.complete_task(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task.to_dict())

@task_routes.delete("/<int:task_id>")
def delete_task(task_id):
    deleted = task_service.delete_task(task_id)

    if not deleted:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task deleted successfully"})