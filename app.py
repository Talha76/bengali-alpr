from flask import Flask, flash, request, redirect
from werkzeug.utils import secure_filename
import utils

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods = ['GET', 'POST'])
def process_image():
  if 'image' not in request.files:
    flash('No image!')
    return redirect(request.url)
  img_file = request.files['image']

  if  img_file.filename == '':
    flash('No selected file!')
    return redirect(request.url)

  if img_file and allowed_file(img_file.filename):
    filename = secure_filename(img_file.filename)
    file_path = './images/main_image.' + filename.rsplit('.', 1)[1].lower()
    img_file.save(file_path)
    area, number = utils.detect_and_extract_lp_text(file_path)
    token = request.args.to_dict(flat=False)['token'][0]
    redirect_url = 'http://localhost:3000/get-np-info?token=' + token + '&area=' + area + '&number=' + number
    print(redirect_url)
    return redirect(redirect_url)
  
  flash('Invalid file extension!')
  return redirect(request.url)

if __name__ == '__main__':
  app.run(port = 3001, debug = True)