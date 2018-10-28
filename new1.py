from flask import Flask, request, Response, render_template, redirect, url_for
import time
import sql

IMAGES_DIR = './templates/files'
i = 0
result = 0
f=0
a=0

app = Flask(__name__)

@app.route('/')
def index():
    global a
    a=0
    return render_template('index.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/facecapture', methods=['GET','POST'])
def facp():
    global result
    #result = 0
    if request.method == 'POST':
        result = request.form
        #print(result)

    return render_template('facecapture.html')

# save the image as a picture
@app.route('/image', methods=['GET','POST'])
def image():
    print("inside image")
    global i
    i = request.files['image']  # get the image
    print(i)
    #f = 's.jpeg'
    global f
    f=('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (IMAGES_DIR,f))

    return Response("%s saved" % f)

@app.route('/sen', methods=['GET','POST'])
def sen():
    global i
    global a
    global f
    print("_------------------------",i,f)
    if a==1:
        ret = sql.atten(f)
        if (ret == 1):
            print("success")
        else:
            print("fail")
            return redirect(url_for('facp'))
    elif i==0:
        print("53675674567567___",i)
        return redirect(url_for('facp'))
    else:
        sql.regist(result,f)
    return redirect(url_for('index'))

@app.route('/attendance')
def att():
    global a
    a=1
    return render_template('facecapture.html')

@app.route('/summary')
def summ():
    result = sql.summary()
    print('$$$$$', result)
    return render_template('summary.html',summary = result)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
