import sys, re
from flask import render_template, flash, redirect, request, session
from .forms import *
from app import app

@app.route("/")
@app.route("/clname", methods=["GET", "POST"])
def clname():
    form = ClusterNameForm()
    if request.method == "POST":
        if form.validate_on_submit():
            session["clname"] = form.clname.data
            return redirect("/storage")
        else:
            flash("Field is required")
    else:
        if re.search(r"/storage$", str(request.referrer)) is None:
            session.clear()
            session["blocks"] = {}
        else:
            form.clname.data = session["clname"]
    return render_template("clname.html", title="Start", form=form)

@app.route("/storage", methods=["GET", "POST"])
def storage():
    form = StorageForm()
    if request.method == "POST":
        if form.addbtn.data:
            if form.validate():
                session["blocks"][form.name.data] = { "pool": form.pool.data,
                                                      "ports": form.ports.data,
                                                      "begin": form.begin.data,
                                                      "end": form.end.data,
                                                      "size": form.size.data,
                                                      "chassis": form.chassis.data }
            else:
                flash("All fields are required")
        elif "rmbtn" in request.form:
            session["blocks"].pop(request.form["rmbtn"].split()[1])
        elif form.backbtn.data:
            return redirect("/clname")
        elif form.nextbtn.data:
            if len(session["blocks"]) == 0:
                flash("Storage must be defined before continuing")
            else:
                return redirect("/chassis")
    form.name.data = ""
    form.pool.data = ""
    form.ports.data = ""
    form.begin.data = ""
    form.end.data = ""
    form.size.data = ""
    form.chassis.data = ""
    return render_template("storage.html", title="Storage", form=form)

@app.route("/chassis", methods=["GET", "POST"])
def chassis():
    form = ChassisForm()
    return render_template("chassis.html", title="Chassis", form=form)
