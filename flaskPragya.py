from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from sdsExtractor import SDS

app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSECUREKEY"
app.config['UPLOAD_FOLDER'] = "static/files"
#keys = ['PRODUCT NAME', 'PRODUCT NUMBER', 'BRAND']
keys = ['PRODUCT NAME', 'PRODUCT NUMBER', 'BRAND', 'EMERGENCY PHONE #', 'SIGNAL WORD','STORAGE CLASS']

class UploadForm(FlaskForm):
    file = FileField('file', validators=[InputRequired()])
    submit = SubmitField('Upload File')


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(filepath)
        sds = SDS(filepath)
        res = sds.extract(keys)
        return render_template('showSDS.html', result=res)
    return render_template('home.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
