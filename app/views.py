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
            session["domains"] = {}
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
                                                      "chassis": form.chassis.data,
                                                      "use": form.use.data }
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
                return redirect("/domain")
    form.name.data = ""
    form.pool.data = ""
    form.ports.data = ""
    form.begin.data = ""
    form.end.data = ""
    form.size.data = ""
    form.chassis.data = ""
    form.use.data = ""
    return render_template("storage.html", title="Storage", form=form)

@app.route("/domain", methods=["GET", "POST"])
def domain():
    form = DomainForm()
    if request.method == "POST":
        if form.addbtn.data:
            if form.validate():
                session["domains"][form.name.data] = { "cores": form.cores.data,
                                                       "ram": form.ram.data,
                                                       "pvid": form.pvid.data,
                                                       "pclass": form.pclass.data,
                                                       "pgroup": form.pgroup.data,
                                                       "racdisks": form.racdisks.data,
                                                       "chassis": form.chassis.data }
            else:
                flash("All fields are required")
        elif "rmbtn" in request.form:
            session["domains"].pop(request.form["rmbtn"].split()[1])
        elif form.backbtn.data:
            return redirect("/storage")
        elif form.nextbtn.data:
            pass
    form.name.data = ""
    form.cores.data = ""
    form.ram.data = ""
    form.pvid.data = ""
    form.pclass.data = ""
    form.pgroup.data = ""
    form.racdisks.data = ""
    form.chassis.data = ""
    return render_template("domain.html", title="Domain", form=form)
