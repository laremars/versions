from flask import Flask
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

app = Flask(__name__)
app.config['SECRET_KEY'] = '6fadf2875131666b089848483978d632'

from tiny import routes