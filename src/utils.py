def validate_task_data(data):
    """
    Validates the incoming JSON data for creating a task.
    """
    # Intentional Gap: This doesn't check if 'title' is a string 
    # or if 'data' is even a dictionary.
    if "title" not in data:
        return False
    return True

def generate_id(existing_tasks):
    # Very inefficient and prone to collisions if we move to DB
    return len(existing_tasks) + 1
