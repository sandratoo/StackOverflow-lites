from flask import Blueprint, request,redirect,url_for,render_template

bp = Blueprint("auth", __name__,url_prefix="/auth")

@bp.route("/create", methods=("POST","GET"))
def create():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db.execute(
            "INSERT INTO user (username,password) VALUES (?,?)",
            (username,password),
        )
        db.commit()
        return redirect (url_for("auth.login"))
    else:
        return render_template ("auth/create.html")
