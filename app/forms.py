import re
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Length, Regexp, Required

class ClusterNameForm(Form):
    name = StringField("name", validators=[ Length(min=4, max=9),
                                            Regexp(r"^[a-zA-Z0-9]+$", message="Invalid characters") ])

class StorageForm(Form):
    name = StringField("blockname", validators=[ Length(max=20) ])
    pool = StringField("blockpool", validators=[ Regexp(r"^[0-9]{2}$", message="Must be a 2-digit number") ])
    ports = StringField("blockports", validators=[ Regexp(r"^CL\d{1}-[a-z]{1},CL\d{1}-[a-z]{1}$", flags=re.I,
                                                   message="Must be comma-separated, even number of ports, in format 'CL1-B'" ) ])
    begin = StringField("blockbegin", validators=[])
    end = StringField("blockend", validators=[])
    size = StringField("blocksize", validators=[])
    chassis = StringField("blockchassis", validators=[])
    addbtn = SubmitField(label="Add Storage Block")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class DomainForm(Form):
    name = StringField("domname", validators=[])
    cores = StringField("domcores", validators=[])
    ram = StringField("domram", validators=[])
    pvid = StringField("dompvid", validators=[])
    pclass = SelectField("dompclass", choices=[ ("dev", "Dev"), ("test", "Test"), ("prod", "Prod") ])
    pgroup = SelectField("dompgroup", choices=[ ("pre_release", "Pre-release"), ("release", "Release"), ("post_release", "Post-release") ])
    chassis = StringField("domchassis", validators=[])
    addbtn = SubmitField(label="Add Domain")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class ConfirmForm(Form):
    backbtn = SubmitField(label="<< Back")
    cfmbtn = SubmitField(label="Confirm")
