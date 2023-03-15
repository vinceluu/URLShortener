from flask import Flask
from URLGenerator import URLGenerator

app = Flask(__name__)
url_generator = URLGenerator()


@app.get("/create_short_url")
def create_short_url():  # TODO Edit parameters
    # TODO Implement API logic here
    short_url = url_generator.insert_short_url("www.youtube.com")
    return short_url


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
