from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def display():
    return "Looks like it works!!"


@app.route('/fwdxml', methods=['GET'])
def xml_gen():
    if 'src' in request.args and 'dst' in request.args and 'text' in request.args and 'fwd_num' in request.args:
        src = request.args.get('src')
        first_dst = request.args.get('dst')
        text = request.args.get('text')
        fwd_num = request.args.get('fwd_num')
    else :
        return "Message details were not recieved properly !"

    print "Message is reieved from source {} and to first destination {}".format(src,first_dst)

    print "Message will be forwarded from first_destination -> {} to final_destination --> {}".format(first_dst,fwd_num)

    xml = '''<Response><Message callbackMethod="POST" callbackUrl="https://requestb.in/1md8ubo1" dst="{}" src="{}" type="sms">{}</Message></Response>'''.format(fwd_num,first_dst,text)
    return Response(xml, mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True, port=3135)
