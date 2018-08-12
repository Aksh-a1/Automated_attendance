from flask import Flask, request, Response
import time

PATH_TO_TEST_IMAGES_DIR = './templates/f'

app = Flask(__name__)

@app.route('/')
def ind():
    return Response(open('./templates/indexx.html').read(), mimetype="text/html")

@app.route('/facecapture')
def index():
    return Response(open('./templates/facecapture.html').read(), mimetype="text/html")

# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))

    return Response("%s saved" % f)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
