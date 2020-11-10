from flask import Flask, render_template, request, url_for, flash
import pytesseract
import os

from PIL import Image

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'images'
app.secret_key = 'Joso'


class GetText(object):

    def __init__(self, file):
        self.file = pytesseract.image_to_string(Image.open(project_dir + '/images/' + file))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'there is no photo in form'
        name = request.form['img-name'] + '.jpg'
        photo = request.files['photo']
        path =os.path.join(app.config['UPLOAD_FOLDER'], name)
        textObject = GetText(name)

        flash('Traitement réussi')
        return render_template('index.html', result = textObject.file)

    return render_template('index.html')


if __name__ == "__main__":
    app.run()

