from app import app
from flask_jwt import jwt_required

@app.route('/body/<body_id>')
def body_get(body_id):
    return '%s' % body_id

@app.route('/body',methods=["POST"])
@jwt_required()
def body_post():
    return "blah"

@app.route('/body',methods=["GET"])
def body_get_all():
    return "blah"
