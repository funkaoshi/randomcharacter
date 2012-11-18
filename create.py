from flask import request, Response, redirect, render_template, url_for, Flask

import character
import characterclass
import dice

# configuration
SECRET_KEY = 'Y\xf6\xf2j\xcf\xc5\xac\xde{\xaf\x1a\xc8\x8dZ0\x9e\x14\xb6\x90\xd7\x02\x03\xf0\x1a'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

SYSTEMS = {
    'lbb': character.LBBCharacter,
    'holmes': character.HolmesCharacter,
    'basic': character.BasicCharacter,
    'pahvelorn': character.PahvelornCharacter,
}

@app.route('/3d6/')
def three_dee_six():
    roll = [dice.xdy(3,6) for _ in range(6)]
    return render_template("3d6.html", roll=roll)

@app.route('/')
def index():
    return redirect('/basic/')

@app.route('/text/')
def index_text():
    return redirect('/basic/text/')

@app.route('/<system>/', defaults={'fmt': "html"})
@app.route('/<system>/<fmt>/')
def generate(system, fmt):
    if fmt == "text":
        template = "plaintext.txt"
        mimetype = "text/plain"
    elif fmt == "html":
        template = "index.html"
        mimetype = "text/html"
    # TODO: As JSON
    # elif fmt == "json":
    #   template = "index.html"
    #   mimetype = "application/json"
    else:
        # default to HTML for unknown display formats
        return redirect(url_for('generate', system=system, fmt="html"))

    system = SYSTEMS.get(system, None)
    if not system:
        # default to basic for unknown systems
        return redirect(url_for('generate', system='basic', fmt=fmt))
    
    c = get_class(request.args.get('class'))
    context = system(classname=c)
    content = render_template(template, c=context)
    response = Response(content, status=200, mimetype=mimetype)
    return response


def get_class(classname):
    """
    Verifies the supplied class paramter is a valid class name.
    """
    if classname not in characterclass.VALID_CLASS_NAMES:
        return None
    return classname


#
# base64.b64encode(pickle.dumps(context))
# 
# @app.route('/character/<b64>/')
# def restore(b64):
#     enc_context = base64.b64decode(b64)
#     context = pickle.loads(enc_context)
#     content = render_template("index.html", c=context)
#     response = Response(content, status=200)
#     return response
#


if __name__ == '__main__':
    app.run("0.0.0.0")
