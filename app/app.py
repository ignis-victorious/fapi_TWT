#
#  Import LIBRARIES
from fastapi import FastAPI, HTTPException

#  Import FILES
from .data.posts_dic import text_posts

#  #

app: FastAPI = FastAPI()


@app.get(path="/")
def root() -> dict[str, str]:
    return {"message": "Hello Mum"}


@app.get(path="/posts")
def get_all_posts(limit: int | None = None) -> list[dict[str, str]] | dict[int, dict[str, str]]:
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get(path="/posts/{id}")
def get_post(id: int) -> dict[str, str] | None:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found!")
    return text_posts.get(id)


# @app.get(path="/hello-world")
# def hello_world() -> dict[str, str]:
#     return {"message": "Hello World"}


#
#  Import LIBRARIES
#  Import FILES
#  #
# if __name__ == "__main__":
#     main()
