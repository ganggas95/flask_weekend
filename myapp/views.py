from flask import render_template, redirect, url_for
from .create_app import app
from .models import Profile


# setting routing to /
@app.route("/")
def index():
    return render_template(
        "index.html", 
        title="Home"
    )

# setting routing to /about/nizar
@app.route("/about/<nickname>")
def about(nickname=None):
    projects = [
        "Website Kota Mataram",
        "Website BPKAD",
        "Website Pemprov NTB",
    ]

    profile = Profile.query.filter(
        Profile.nickname == nickname
    ).first()

    return render_template(
        "about.html", 
        title = "About", 
        projects = projects,
        profile = profile
    )


@app.route("/new_profile")
def new_profile():
    profile = Profile()
    profile.firstname = "Eby"
    profile.lastname = "Sofyan"
    profile.nickname = 'eby'
    profile.email = 'eby@gmail.com'
    profile.address = 'Lombok Tengah'
    profile.work = "Python Programmer"
    profile.save()
    return redirect(url_for('about', nickname=profile.nickname))
