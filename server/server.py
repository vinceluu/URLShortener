from flask import Flask

app = Flask(__name__)


@app.get("/create_short_url")
def create_short_url():  # TODO Edit parameters
    # TODO Implement API logic here
    return "Vince + Kim's URL Shortener"


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
