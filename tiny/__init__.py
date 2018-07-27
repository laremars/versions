from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fadf2875131666b089848483978d632'

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

from tiny import routes