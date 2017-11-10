from flask import Flask, request, abort, Response
from models import db, Forward, Source

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



@app.route("/cb", methods=['POST'])
def callback():
    print (request.is_json)
    content = request.get_json()
    print content['src'], content['dst'], content['text']
    src = content['src']
    dst = content['dst']
    text = content['text']
    src_data = Source(src, dst, text)
    db.session.add(src_data)
    db.session.commit()

    return ' The JSON posted successfully '

@app.route('/fwdxml', methods=['GET'])
def xml_gen():
    if 'src' in request.args and 'dst' in request.args and 'text' in request.args:
        src = request.args.get('src')
        first_dst = request.args.get('dst')
        text = request.args.get('text')
    else :
        return "Message details were not recieved properly !"

    print "Message is reieved from source {} and to first destination {}".format(src,first_dst)

    fwd_num = db.session.execute("select fwd, id from forward where id=:id", {'id' : first_dst })
    for row in fwd_num:
        fwd_dst =  row['fwd']
    print " Message will be forwarded from first_destination -> {} to final_destination --> {}".format(first_dst,fwd_dst)

    xml = '''<Response><Message callbackMethod="POST" callbackUrl="https://requestb.in/1md8ubo1" dst="{}" src="{}" type="sms">{}</Message></Response>'''.format(fwd_dst,first_dst,text)
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