from flask import Flask, request
from models import db, Forward

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'plivo',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route("/")
def main():
    return 'Hello World !'


@app.route('/input', methods=['GET','POST'])
def forward():
    # Create a form and allow the user to input forwarding number for a given number.
    if 'src' in request.args and 'dst' in request.args :
        pass
    src = request.args.get('src')
    dst = request.args.get('dst')
    fwd_1 = Forward(src,dst)
    db.session.add(fwd_1)
    db.session.commit()
    return "You have updated the DB with source as {} and destination as {}".format(src,dst)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()