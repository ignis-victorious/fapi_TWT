#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#  #

app: FastAPI = FastAPI()


@app.get(path="/")
def root() -> dict[str, str]:
    return {"message": "Hello Mum"}


@app.get(path="/hello-world")
def hello_world() -> dict[str, str]:
    return {"message": "Hello World"}


#
#  Import LIBRARIES
#  Import FILES
#  #
# if __name__ == "__main__":
#     main()
