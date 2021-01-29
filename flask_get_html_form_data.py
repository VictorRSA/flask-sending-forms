from flask  import  Flask ,render_template,request

app = Flask(__name__)

@app.route('/')

def student():
    return render_template("student.html")

#defining another route or url endpoint


@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =="POST":
        result = request.form  #get the data from the form
        return render_template("result_of_form_inputs_rendered.html",result=result)
if __name__ =='__main__':
    app.run(debug=True)
