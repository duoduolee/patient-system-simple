from flask import Flask
from config import Config
from models import db
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(bp, url_prefix='/api')

@app.before_first_request
def setup():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

