from flask import Flask, jsonify, render_template_string, url_for
from app.routes.task_routes import task_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(task_routes, url_prefix="/tasks")

    @app.route("/openapi.json")
    def openapi_spec():
        return jsonify({
            "openapi": "3.0.0",
            "info": {
                "title": "Task API",
                "version": "1.0.0",
                "description": "A simple task management API"
            },
            "paths": {
                "/tasks/": {
                    "get": {
                        "summary": "Get all tasks",
                        "responses": {
                            "200": {
                                "description": "A list of tasks",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "array",
                                            "items": {
                                                "$ref": "#/components/schemas/Task"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "post": {
                        "summary": "Create a new task",
                        "requestBody": {
                            "required": True,
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "description": {
                                                "type": "string"
                                            }
                                        },
                                        "required": ["description"]
                                    }
                                }
                            }
                        },
                        "responses": {
                            "201": {
                                "description": "Task created",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/Task"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "/tasks/{task_id}/start": {
                    "put": {
                        "summary": "Start a task",
                        "parameters": [
                            {
                                "name": "task_id",
                                "in": "path",
                                "required": True,
                                "schema": {
                                    "type": "integer"
                                }
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Task started",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/Task"
                                        }
                                    }
                                }
                            },
                            "404": {
                                "description": "Task not found"
                            }
                        }
                    }
                },
                "/tasks/{task_id}/complete": {
                    "put": {
                        "summary": "Complete a task",
                        "parameters": [
                            {
                                "name": "task_id",
                                "in": "path",
                                "required": True,
                                "schema": {
                                    "type": "integer"
                                }
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Task completed",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/Task"
                                        }
                                    }
                                }
                            },
                            "404": {
                                "description": "Task not found"
                            }
                        }
                    }
                },
                "/tasks/{task_id}": {
                    "delete": {
                        "summary": "Delete a task",
                        "parameters": [
                            {
                                "name": "task_id",
                                "in": "path",
                                "required": True,
                                "schema": {
                                    "type": "integer"
                                }
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Task deleted",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "object",
                                            "properties": {
                                                "message": {"type": "string"}
                                            }
                                        }
                                    }
                                }
                            },
                            "404": {
                                "description": "Task not found"
                            }
                        }
                    }
                }
            },
            "components": {
                "schemas": {
                    "Task": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "integer"},
                            "description": {"type": "string"},
                            "status": {
                                "type": "string",
                                "enum": ["pending", "in_progress", "complete"]
                            }
                        },
                        "required": ["id", "description", "status"]
                    }
                }
            }
        })

    @app.route("/swagger")
    def swagger_ui():
        swagger_url = url_for("openapi_spec")
        return render_template_string(
            """<!doctype html>
            <html lang='en'>
              <head>
                <meta charset='utf-8'>
                <title>Swagger UI</title>
                <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui.css'>
              </head>
              <body>
                <div id='swagger-ui'></div>
                <script src='https://cdn.jsdelivr.net/npm/swagger-ui-dist@latest/swagger-ui-bundle.js'></script>
                <script>
                  window.onload = function () {
                    SwaggerUIBundle({
                      url: "{{ swagger_url }}",
                      dom_id: '#swagger-ui',
                      presets: [SwaggerUIBundle.presets.apis],
                      layout: 'BaseLayout'
                    });
                  };
                </script>
              </body>
            </html>
            """,
            swagger_url=swagger_url,
        )

    return app
