from fastapi import FastAPI

app = FastAPI()


@app.get("/create_short_url")
def create_short_url():  # TODO Edit parameters
    # TODO Implement API logic here
    return "Vince + Kim's URL Shortener"
