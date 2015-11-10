from app import app, db
from flask_jwt import jwt_required
from flask import jsonify, request
import pprint

@app.route('/body/<body_id>')
def body_get(body_id):
    return '%s' % body_id

@app.route('/body',methods=["POST"])
@jwt_required()
def body_post():
    content = request.get_json()
    #pprint.pprint(content)
    body = Body(content['name'], content['abrv'], content['url'])
    db.session.add(body)
    db.session.commit()
    return jsonify(**body)

@app.route('/body',methods=["GET"])
def body_get_all():
    bodies = Bodies.query.all()
    resp = jsonify(bodies)
    resp.status_code = 200
    return resp
