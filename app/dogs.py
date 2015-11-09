from app import app

@app.route('/dog/<dog_uuid>')
def dog_get(dog_uuid):
    return '%s' % dog_uuid

@app.route('/dog',methods=["POST"])
@jwt_required()
def dog_post():
    print "blah"
