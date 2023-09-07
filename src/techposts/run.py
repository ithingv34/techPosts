import uvicorn


def start() -> None:
    """Launched with 'poetry run start' at root level"""
    uvicorn.run(app="techposts.app.main:app", host="127.0.0.1", port=8000, reload=True)
