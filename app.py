import logzero
from flask import Flask


logger = logzero.setup_logger(__file__)

app = Flask(__name__)
logger.info("Started Flask app!")
logger.debug(f"Configuratioo:\n{app.config}")




@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
