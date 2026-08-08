# fast api 

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError

# from fast_api.app import app


app = FastAPI(title="Fast API", version="1.0.0")

# a decorator is used because it is a function that takes another function as an argument and extends its behavior without explicitly modifying it. In this case, the decorator is used to define a route for the FastAPI application.
@app.get("/hello-world")
def hello_world():
    return {"message": "Hello from Fast API!"}


text_posts = {
    # sample data for text posts, which is a dictionary containing two text posts with their respective IDs, titles, and content.
    #create ten
    1: {"id": 1, "title": "First Post", "content": "This is the first text post."},
    2: {"id": 2, "title": "Second Post", "content": "This is the second text post."},
    3: {"id": 3, "title": "Third Post", "content": "This is the third text post."},
    4: {"id": 4, "title": "Fourth Post", "content": "This is the fourth text post."},
    5: {"id": 5, "title": "Fifth Post", "content": "This is the fifth text post."},
    6: {"id": 6, "title": "Sixth Post", "content": "This is the sixth text post."},
    7: {"id": 7, "title": "Seventh Post", "content": "This is the seventh text post."},
    8: {"id": 8, "title": "Eighth Post", "content": "This is the eighth text post."},
    9: {"id": 9, "title": "Ninth Post", "content": "This is the ninth text post."},
    10: {"id": 10, "title": "Tenth Post", "content": "This is the tenth text post."}
}

@app.get("/text-posts")
def get_all_text_posts(limit: int = 10):
    if limit:
        return list(text_posts.values())[:limit]
    # this will return the text_posts dictionary as a JSON response when the /text-posts endpoint is accessed via a GET request.
    return JSONResponse(content={k: v for k, v in list(text_posts.items())[:limit]})

@app.get("/text-posts/{post_id}")
def get_text_post(post_id: int):
    # this will return a specific text post based on the post_id provided in the URL path. If the post_id does not exist in the text_posts dictionary, it will return a 404 error with a message indicating that the post was not found.
    if post_id in text_posts:
        return JSONResponse(content=text_posts[post_id])
    else:
        return JSONResponse(status_code=404, content={"message": "Post not found"}) , HTTPException(status_code=404, detail="Post not found")

@app.post("/text-posts")
def create_text_post(post: dict):
    # this will create a new text post based on the data provided in the request body. The post parameter is expected to be a dictionary containing the title and content of the new post. The new post will be added to the text_posts dictionary with a unique ID, and a JSON response will be returned with a message indicating that the post was created successfully.
    new_id = max(text_posts.keys()) + 1
    text_posts[new_id] = {"id": new_id, "title": post["title"], "content": post["content"]}
    return JSONResponse(status_code=201, content={"message": "Post created successfully", "post": text_posts[new_id]})
    