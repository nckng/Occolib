
from flask import Flask, render_template
from utils import occupations

app = Flask(__name__)

def bello():
    return occupations.OCUPATIONES
def yello():
    return occupations.OCUPATIONES.values()

@app.route("/occupations")
def test_tmplt():

    return render_template( 'model_tmplt.html', foo=occupations.randomizer(),too = bello().items(),they='https://www.wikipedia.org')
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
