from flask import Flask, request, Response, render_template
import time

PATH_TO_TEST_IMAGES_DIR = './templates/f'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def ind():
    return render_template('register.html')

@app.route('/facecapture', methods=['GET','POST'])
def inde():
    if request.method == 'POST':
        result = request.form
        print(result)
    return render_template('facecapture.html')

# save the image as a picture
@app.route('/image', methods=['GET','POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    return Response("%s saved" % f)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
