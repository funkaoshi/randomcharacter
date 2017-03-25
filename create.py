import json

from flask import request, Response, redirect, render_template, url_for, Flask

import adventuregame
import character
import characterclass
import dangertime
import dice
import fifth
import mazerats
import troika
import demoncity

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

SYSTEMS = {
    'lbb': character.LBBCharacter,
    'holmes': character.HolmesCharacter,
    'basic': character.BasicCharacter,
    'pahvelorn': character.PahvelornCharacter,
    'apollyon': character.ApollyonCharacter,
    'carcosa': character.CarcosaCharacter,
    'moc': character.MastersOfCarcosaCharacter,
    'dd': character.DelvingDeeperCharacter,
    'lotfp': character.LotFPCharacter
}


@app.template_filter()
def with_sign(number):
    return "+{0}".format(number) if number > 0 else str(number)


@app.route('/5e/')
def fifth_edition():
    return render_template("5e.html", c=fifth.Character())

@app.route('/3d6/')
def three_dee_six():
    roll = [dice.xdy(3,6) for _ in range(6)]
    return render_template("3d6.html", roll=roll)

@app.route('/equipment/', defaults={'system': "basic"})
@app.route('/equipment/<system>/')
def equipment(system):
    system = SYSTEMS.get(system, None)
    if not system:
        # default to basic for unknown systems
        return redirect(url_for('equipment', system='basic'))

    equipment = system().equipment
    return render_template("equipment.html", equipment=equipment)

@app.route('/4d6/')
def four_dee_six():
    roll = [sum(sorted(dice.d(6) for _ in xrange(4))[1:]) for _ in range(6)]
    return render_template("4d6.html", roll=roll)

@app.route('/adventuregame/')
def make_adventure_game_char():
    return render_template("adventuregame.html", c=adventuregame.Character())

@app.route('/dangertime/')
def make_danger_time_char():
    return render_template("dangertime.html", c=dangertime.Character())

@app.route('/troika/')
def make_troika_char():
    return render_template("troika.html", c=troika.Character())
    
@app.route('/demoncity/text/')
def make_demoncity_text_char():
    mimetype = "text/plain"
    content = render_template("demoncity.txt", c=demoncity.Character())
    return Response(content, status=200, mimetype=mimetype)

@app.route('/demoncity/')
def make_demoncity_char():
    return render_template("demoncity.html", c=demoncity.Character())    

@app.route('/mazerats/', defaults={'number': 1})
@app.route('/mazerats/<int:number>/')
def make_mazerats_char(number):
    if number >= 20:
        number = 20
    characters = [mazerats.Character() for _ in range(number)]
    return render_template("mazerats.html", characters=characters)

@app.route('/npcs/', defaults={'number': 10})
@app.route('/npcs/<int:number>/')
def generate_npcs(number):
    if number > 1000:
        number = 1000
    characters = [character.BasicCharacter(testing=True) for _ in xrange(number)]
    return render_template("npcs.html", characters=characters)

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
    elif fmt == "yaml":
        template = "yaml.txt"
        mimetype ="text/plain"
    elif fmt == "json":
        mimetype = "application/json"
    else:
        # default to HTML for unknown display formats
        return redirect(url_for('generate', system=system, fmt="html"))

    system = SYSTEMS.get(system, None)
    if not system:
        # default to basic for unknown systems
        return redirect(url_for('generate', system='basic', fmt=fmt))

    c = get_class(request.args.get('class'))
    context = system(classname=c)
    if fmt == "json":
        content = json.dumps(context.to_dict())
    else:
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
