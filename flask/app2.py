from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
# path os, glob(regex) / pathlib Path
basedir = os.path.abspath(os.path.dirname(__file__))

# db
# db 위치 지정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
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
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'desc')


# Schema init
todo_schema = TodoSchema()  # one to one
todos_schema = TodoSchema(many=True)  # select multiple rows


# RESTFUL API
# Create todos
@app.route('/todo', methods=['POST'])
def add_todo():
    desc = request.json['desc']
    new_todo = Todos(desc)

    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.jsonify(new_todo)


# get todos
@app.route('/todo', methods=['GET'])
def get_todos():
    all_todos = Todos.query.all()
    # python pickle
    result = todos_schema.dump(all_todos)
    return jsonify(result)


# Get one todo
@app.route('/todo/<id>', methods=['GET'])
def get_todo(id):
    todo = Todos.query.get(id)
    return todo_schema.jsonify(todo)


# Update
@app.route('/todo/<id>', methods=['PUT'])
def update_todo(id):
    todo = Todos.query.get(id)
    desc = request.json['desc']
    todo.desc = desc
    db.session.commit()
    return todo_schema.jsoinfy(todo)


# Delete
@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)


# RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)
