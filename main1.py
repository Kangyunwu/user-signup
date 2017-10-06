from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/error", methods=["POST"])
def sign_up():
    new_user = request.form["username"]
    new_password = request.form["password"]
    verified_password = request.form["verifypassword"]
    new_email=request.form["email"]
    is_error = False

    if (not new_user) or new_user.strip() == "":
        user_error = "Please enter username."
        is_error = True
        return redirect("/?user-error=" + user_error)

    if new_user and (len(new_user) < 3 or len(new_user) > 20 or new_user.isspace()):
        user_error = "Invalid username."
        is_error = True
        return redirect("/?user-error=" + user_error)

    if new_user and "me" in new_user:
        user_error = "Invalid username."
        is_error = True
        return redirect("/?user-error=" + user_error)

    if (not new_password) or (new_password.strip() == ""):
        password_error = "Please enter password."
        is_error = True
        return redirect("/?password-error=" + password_error)

    if (new_password and (len(new_password) < 3 or len(new_password) > 20 or new_password.isspace())):
        password_error = "Invalid password."
        is_error = True
        return redirect("/?password-error=" + password_error)

    if (not verified_password) or (verified_password.strip() == ""):
        veri_error = "Please verify password."
        is_error = True
        return redirect("/?veri-error=" + veri_error)

    if (verified_password != new_password):
        veri_error = "Verified password is invalid."
        is_error = True
        return redirect("/?veri-error=" + veri_error)

    if new_email:
        if "@" not in new_email or "." not in new_email or len(new_email) < 3 or len(new_email) > 20 or new_email.isspace():
            email_error = "Invalid email."
            is_error = True
            return redirect("/?email-error=" + email_error)

    if not is_error:
        return render_template("welcome.html", username=new_user)

@app.route("/")
def index():
    error1 = request.args.get("user-error")
    error2 = request.args.get("password-error")
    error3 = request.args.get("veri-error")
    error4 = request.args.get("email-error")
    return render_template('edit.html', error1=error1 and cgi.escape(error1, quote=True), error2=error2 and cgi.escape(error2, quote=True), error3=error3 and cgi.escape(error3, quote=True), error4=error4 and cgi.escape(error4, quote=True))

if __name__ == "__main__":
    app.run()