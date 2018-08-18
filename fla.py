# from flask import Flask,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('front.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form     #this returns a dictionary. takes all the values from the form page and saves it into result variable which is a dictionary
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
