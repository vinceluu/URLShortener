from flask import Flask, redirect
from URLGenerator import URLGenerator

app = Flask(__name__)
url_generator = URLGenerator()


@app.get("/create_short_url")
def create_short_url():  # TODO Edit parameters
    # TODO Check valid long_url
    short_url = url_generator.insert_short_url(
        "www.youtube.com")  # TODO Edit this to be variable
    return short_url


@app.get("/<string:short_url>")
def redirect_short_url(short_url: str):
    long_url = url_generator.short_url_exists(short_url)
    if long_url is not None:
        new_long_url = "http://" + long_url
        return redirect(new_long_url)
    else:
        return "404 Short URL Not Found"


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
