from sys import argv
from bottle import route, run

@route('/')
def index():
    return """
    <h1>Halló heimur</h1>
    <h2>Verkefni 1.</h2>
    <p><a href="/about">Um okkur</a></p>
    <p><a href="/bio">Ferilskrá</a></p>
    <p><a href="/pics">Myndir</a></p>
    """
@route("/about")
def jobs():
    return "Hér eru uppsýsingar um Stefán Vinnumann"

@route("/bio")
def jobs():
    return "Hér er ferilskrá Stefán Vinnumann"

@route("/pics")
def jobs():
    return "Hér eru myndir af Stefán Vinnumann"

run(host='0.0.0.0', port=argv[1])
