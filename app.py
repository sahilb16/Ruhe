from flask import Flask ,render_template,request


app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/students", methods =["GET", "POST"])
def student():
    if request.method == "POST":
        # print(request.form)
        mail = request.form.get("mail")
        pswd = request.form.get("pswd") 
        print("password",pswd)
        print("mail:", mail)
    
    return render_template('student.html')


if __name__  == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=80)  