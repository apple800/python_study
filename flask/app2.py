from flask import Flask, request, jsonify
form flask_sqlalchemy import flask_sqlalchemy
from flask_marshmallow import marshmallow
import os

app = Flask(__nama__)
# path os, glob(regex) / pathlib Path
basedir = os.path.abspath(os.path.dirname(__file__))

## db
# db 위치 지정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db init
db = SQLAlchemy(app)

# marshmallow init SERIALIZATION -> JSON
ma = Marshmallow(app)

# db Model
class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(100), nullable=False)

    def __init__(self, desc):
        self.desc = desc

# Produnt schema


# Shema init


# RESTFUL API


# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)