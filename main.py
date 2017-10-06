from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/error", methods=["POST"])
def error():
    new_user = request.form["username"]
    new_password = request.form["password"]
    verified_password = request.form["verifypassword"]
    new_email=request.form["email"]
    is_error = True

    if (not new_user) or new_user.strip() == "":
        user_error = "Please enter username."
        is_error = False
        return render_template("edit.html", error1=user_error)

    if new_user and (len(new_user) < 3 or len(new_user) > 20 or new_user.isspace()):
        user_error = "Invalid username."
        is_error = False
        return render_template("edit.html", error1=user_error, username=new_user)

    if new_user and "me" in new_user:
        user_error = "Invalid username."
        is_error = False
        return render_template("edit.html", error1=user_error, username=new_user)

    if (not new_password) or (new_password.strip() == ""):
        password_error = "Please enter password."
        is_error = False
        return render_template("edit.html", error2=password_error, username=new_user)

    if (new_password and (len(new_password) < 3 or len(new_password) > 20 or new_password.isspace())):
        password_error = "Invalid password."
        is_error = False
        return render_template("edit.html", error2=password_error, username=new_user)

    if (not verified_password) or (verified_password.strip() == ""):
        veri_error = "Please verify password."
        is_error = False
        return render_template("edit.html", error3=veri_error, username=new_user)

    if (verified_password != new_password):
        veri_error = "Verified password is invalid."
        is_error = False
        return render_template("edit.html", error3=veri_error, username=new_user)

    if new_email:
        if "@" not in new_email or "." not in new_email or len(new_email) < 3 or len(new_email) > 20 or new_email.isspace():
            email_error = "Invalid email."
            is_error = False
            return render_template("edit.html", error4=email_error, username=new_user)

    if is_error:
        return redirect("/welcome?username="+new_user)

@app.route("/welcome")
def welcome():
    new_user = request.args.get("username")
    return render_template("welcome.html", username=new_user)

@app.route("/")
def index():
    return render_template('edit.html')

if __name__ == "__main__":
    app.run()