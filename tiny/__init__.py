from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fadf2875131666b089848483978d632'

from tiny import routes