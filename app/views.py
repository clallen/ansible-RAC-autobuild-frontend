import re
from flask import render_template, flash, redirect, request, session
from .forms import *
from app import app

@app.route("/")
@app.route("/start", methods=["GET", "POST"])
def start():
    form = ClusterNameForm()
    if request.method == "POST":
        if form.validate():
            session["clname"] = form.name.data.lower()
            return redirect("/storage")
    else:
        if re.search(r"/storage$", str(request.referrer)) is None:
            session.clear()
            session["blocks"] = {}
            session["domains"] = {}
        else:
            form.name.data = session["clname"]

    return render_template("start.html", title="Start", form=form)

@app.route("/storage", methods=["GET", "POST"])
def storage():
    form = StorageForm()

    def clear_form():
        form.name.data = ""
        form.pool.data = ""
        form.ports.data = ""
        form.begin.data = ""
        form.end.data = ""
        form.size.data = ""
        form.chassis.data = ""

    if request.method == "POST":
        if form.addbtn.data:
            blanks = False
            for data in form.data.itervalues():
                if isinstance(data, unicode):
                    if len(data) == 0:
                        blanks = True
                        break
            if not blanks:
                if form.validate():
                    session["blocks"][form.name.data] = { "pool": form.pool.data,
                                                          "ports": form.ports.data.upper(),
                                                          "begin": form.begin.data.upper(),
                                                          "end": form.end.data.upper(),
                                                          "size": form.size.data,
                                                          "chassis": form.chassis.data.lower() }
                    clear_form()
            else:
                flash("All fields are required")
        elif "rmbtn" in request.form:
            session["blocks"].pop(request.form["rmbtn"].split()[1])
        elif form.backbtn.data:
            return redirect("/start")
        elif form.nextbtn.data:
            if len(session["blocks"]) == 0:
                flash("Storage must be defined before continuing")
            else:
                return redirect("/domain")
    else:
        clear_form()

    return render_template("storage.html", title="Storage", form=form)

@app.route("/domain", methods=["GET", "POST"])
def domain():
    form = DomainForm()

    def clear_form():
        form.name.data = ""
        form.cores.data = ""
        form.ram.data = ""
        form.pvid.data = ""
        form.pclass.data = ""
        form.pgroup.data = ""
        form.powner.data = ""
        form.chassis.data = ""

    if request.method == "POST":
        if form.addbtn.data:
            blanks = False
            for data in form.data.itervalues():
                if isinstance(data, unicode):
                    if len(data) == 0:
                        blanks = True
                        break
            if not blanks:
                if form.validate():
                    session["domains"][form.name.data.lower()] = { "cores": form.cores.data,
                                                                   "ram": form.ram.data,
                                                                   "pvid": form.pvid.data,
                                                                   "pclass": form.pclass.data,
                                                                   "pgroup": form.pgroup.data,
                                                                   "powner": form.powner.data,
                                                                   "chassis": form.chassis.data.lower() }
                    clear_form()
            else:
                flash("All fields are required")
        elif "rmbtn" in request.form:
            session["domains"].pop(request.form["rmbtn"].split()[1])
        elif form.backbtn.data:
            return redirect("/storage")
        elif form.nextbtn.data:
            if len(session["domains"]) == 0:
                flash("At least one domain must be defined before continuing")
            else:
                return redirect("/confirm")
    else:
        clear_form()

    return render_template("domain.html", title="Domain", form=form)

@app.route("/confirm", methods=["GET", "POST"])
def confirm():
    form = ConfirmForm()

    if request.method == "POST":
        if form.backbtn.data:
            return redirect("/domain")
        elif form.cfmbtn.data:
            pass

    return render_template("confirm.html", title="Confirmation", form=form)
