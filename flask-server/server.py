from flask import Flask

app = Flask(__name__)


@app.route('/create_url', methods=['GET'])  # This creates the endpoint
def create_short_url():  # TODO Edit parameters
    # TODO Implement API logic here
    return "Vince + Kim's URL Shortener"


if __name__ == "__main__":
    app.run(debug=True)
