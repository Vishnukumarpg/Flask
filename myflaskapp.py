from flask import Flask, request, Response

class MyResponse(Response):
    default_mimetype = 'application/xml'
class MyFlask(Flask):
    response_class = MyResponse

app = MyFlask(__name__)


@app.route('/')
def display():
    return "Looks like it works!!"

@app.route('/alpha')
def alpha():
    return "This is the aplha version !!"

@app.route('/number')
def input():
    if 'src' in request.args and 'dst' in request.args :
        return "The source of the request is {} and destination is {} ". format(request.args.get('src'), request.args.get('dst'))

@app.route('/beta')
def xml():
    if 'src' in request.args and 'dst' in request.args and 'text' in request.args:
        pass
    src = request.args.get('src')
    dst = request.args.get('dst')
    text = request.args.get('text')

    return '''<Response><Message callbackMethod="POST" callbackUrl="https://requestb.in/1md8ubo1" dst="{}" src="{}" type="sms">{}</Message></Response>'''.format(dst,src,text)


if __name__ == '__main__':
    app.run(debug=True, port=3134)
