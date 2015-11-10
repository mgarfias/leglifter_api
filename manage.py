# manage.py

from flask.ext.script import Shell,Server,Manager
from flask import url_for
from app import app, models
from app.models import db

def _make_context():
    return dict(app=app, db=db, models=models)


manager = Manager(app)
manager.add_command("runserver", Server())

@manager.command
def hello():
    print "hello"

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line

if __name__ == "__main__":
    manager.run()
