
import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)
    #reload = true means that the server will automatically reload if any changes are made to the code, which is useful during development.


