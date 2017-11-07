from flask import Flask, request, abort, Response
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

@app.route('/fwdxml', methods=['GET'])
def xml_gen():

    fwd_num = db.session.execute("select fwd, id from forward where id=161616161616")
    for row in fwd_num:
        fwd_dst =  row['fwd']
        src  = row['id']
    print "forward number for this is -->", str(fwd_dst)
    src = src
    dst = fwd_dst
    text = "Hi ALL THIS IS FROM FLASK"

    xml = '''<Response><Message callbackMethod="POST" callbackUrl="https://requestb.in/1md8ubo1" dst="{}" src="{}" type="sms">{}</Message></Response>'''.format(dst,src,text)
    return Response(xml, mimetype='text/xml')




@app.route('/input', methods=['POST'])
def forward():
    if not request.json:
        abort(400)
    data = request.get_json()
    src = data['src']
    dst = data['dst']
    fwd_1 = Forward(src,dst)
    db.session.add(fwd_1)
    db.session.commit()
    return "You have updated the DB with source as {} and destination as {}".format(src,dst)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run()