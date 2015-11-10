from app import app,db, models
from flask_jwt import jwt_required
from flask import jsonify, request
import pprint

@app.route('/body/<body_id>')
def body_get(body_id):
    return '%s' % body_id

@app.route('/body',methods=["POST"])
@jwt_required()
def body_post():
    print "MOO\n\n"
    pprint.pprint(db)

    content = request.get_json()

    body = models.Body(name=content['name'], abrv=content['abrv'], url=content['url'])
    db.session.add(body)
    db.session.commit()
    tmp = models.Body.query.all()
    return jsonify(**tmp)

@app.route('/body',methods=["GET"])
def body_get_all():
    bodies = models.Body.query.all()
    resp = bodies
    resp.status_code = 200
    return resp
