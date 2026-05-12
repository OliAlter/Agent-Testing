from flask import Flask, jsonify, request
from models import Task
from utils import validate_task_data, generate_id

app = Flask(__name__)

# Global state (Not thread-safe, intentionally)
tasks = {}

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if not validate_task_data(data):
        return jsonify({"error": "Missing title"}), 400
    
    new_id = generate_id(tasks)
    task = Task(new_id, data['title'], data.get('description', ''))
    tasks[new_id] = task
    return jsonify(task.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Subtle Inconsistency: Sometimes we return 404, sometimes we might crash
    # if the ID isn't an integer (handled by Flask converter here though)
    task = tasks.get(task_id)
    if not task:
        return jsonify({"message": "Not found"}), 404
    return jsonify(task.to_dict())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # BUG: This will crash if task_id doesn't exist because we don't check
    del tasks[task_id] 
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
