from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import ProfileForm
import datetime
from werkzeug.utils import secure_filename
import os
from app import db
from app.models import Users

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')



@app.route("/profile",methods=["GET","POST"])
def profile():
    form = ProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        photo = form.Pic.data
        name = form.firstName.data + " "+ form.lastName.data
        gender = form.gender.data
        email = form.email.data
        location = form.location.data
        bio = form.biography.data
        
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        #print(os.path.join(
          #  app.config['UPLOAD_FOLDER'], filename
        #))
        created_on = getDate()
        user = Users(created_on,name,location,filename,gender,email,bio)
        
        db.session.add(user)
        db.session.commit()
        
        flash("user was successfully added",'success')
        return redirect(url_for("home"))
    print(form.errors)
    return render_template("profile.html",form = form)
    

def format_date_joined(date):
    return  "joined " + date


def getDate():
    now = datetime.datetime.now()
    return now.strftime("%B %d,%Y")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")