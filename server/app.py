from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages = Message.query.all()
        message_dict = [message.to_dict() for message in messages]
        response = make_response(jsonify(message_dict), 200)
        return response
    elif request.method == 'POST':
        message_data = request.get_json()
        new_message = Message(
            body=message_data['body'],
            username=message_data['username'],
        )

        db.session.add(new_message)
        db.session.commit()

        new_message_dict = new_message.to_dict()
        response = make_response(jsonify(new_message_dict), 201)
        return response


@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    messages_by_id = Message.query.filter_by(id=id).first()
    message_data = request.get_json()
    if request.method == 'PATCH':
        for attr in message_data:
            setattr(messages_by_id, attr, message_data[attr])
        db.session.add(messages_by_id)
        db.session.commit()
        messages_by_id_dict = messages_by_id.to_dict()
        response = make_response(jsonify(messages_by_id_dict), 200)
        return response
    
    elif request.method == "DELETE":
        db.session.delete(messages_by_id)
        db.session.commit()

        response_body = {
            "delete_successful": True,
            "message": "message deleted."
        }

        response = make_response(jsonify(response_body), 200)
        return response

if __name__ == '__main__':
    app.run(port=5555)
