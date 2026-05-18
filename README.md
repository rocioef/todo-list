# Todo List API

## Project Objective

This project is a simple Flask-based task management API. It allows you to create, list, start, complete, and delete tasks. It also includes an OpenAPI specification endpoint and a built-in Swagger UI for exploring the API.

## Project Structure

- `run.py` - Application entry point for starting the Flask server.
- `app/__init__.py` - Creates and configures the Flask application.
- `app/routes/task_routes.py` - Defines the task-related API routes.
- `app/models/` - Contains task model and status definitions.
- `app/repositories/` - Handles task storage and data access.
- `app/services/` - Implements task business logic.
- `app/schemas/` - Defines request/response schema structures.
- `tasks.json` - Sample task storage file.

## How to Start the Project

1. Open a terminal in the project root:
   ```bash
   cd /Users/rocioencinas7icloud.com/Documents/git-projects/todo-list
   ```

2. Activate the virtual environment if available:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies if needed:
   ```bash
   python3 -m pip install flask
   ```

4. Run the application:
   ```bash
   python3 run.py
   ```

5. Open the API in your browser:
   - `http://127.0.0.1:5000/tasks/`
   - `http://127.0.0.1:5000/swagger`

## Notes

- The app listens on the default Flask port `5000`.
- The `swagger` route loads the OpenAPI spec from `/openapi.json`.
- If `python3` is not available, use `python run.py` instead.
