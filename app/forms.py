import re
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Length, Regexp, Required

class ClusterNameForm(Form):
    name = StringField("name", validators=[ Length(min=4, max=9),
                                            Regexp(r"^[a-zA-Z0-9]+$", message="Invalid characters") ])

class StorageForm(Form):
    name = StringField("blockname", validators=[ Length(max=20),
                                                 Regexp(r"^\w+$", message="Invalid characters") ])
    pool = StringField("blockpool", validators=[ Regexp(r"^[0-9]{2}$", message="Must be a 2-digit integer") ])
    ports = StringField("blockports", validators=[ Regexp(r"^(CL\d{1}-[a-z]{1})(,CL\d{1}-[a-z]{1}){1,5}$",
                                                   flags=re.I,
                                                   message="Must be comma-separated, even number of ports, "+
                                                   "in format 'CL1-B'" ) ])
    begin = StringField("blockbegin", validators=[ Regexp("^[a-f0-9]{2}:[a-f0-9]{2}$",
                                                   message="Invalid LDEV", flags=re.I) ])
    end = StringField("blockend", validators=[ Regexp("^[a-f0-9]{2}:[a-f0-9]{2}$",
                                                   message="Invalid LDEV", flags=re.I) ])
    size = StringField("blocksize", validators=[ Length(max=4),
                                                 Regexp(r"^\d+$", message="Must be an integer") ])
    chassis = StringField("blockchassis", validators=[ Regexp("^(\w+)(,\w+)*$", flags=re.I,
                                                       message="Must be either single chassis, "+
                                                       "or a comma-separated list of chassis") ])
    addbtn = SubmitField(label="Add Storage Block")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class DomainForm(Form):
    name = StringField("domname", validators=[ Length(min=4, max=10),
                                               Regexp(r"^[a-zA-Z0-9]+$", message="Invalid characters") ])
    cores = StringField("domcores", validators=[ Length(max=2), Regexp("^\d+$",
                                                 message="Must be an integer") ])
    ram = StringField("domram", validators=[ Length(max=3), Regexp("^\d+$", message="Must be an integer") ])

    pvid = StringField("dompvid", validators=[ Regexp("^\d{4}$", message="Must be a 4-digit integer") ])
    pclass = SelectField("dompclass", choices=[ ("dev", "Dev"), ("test", "Test"), ("prod", "Prod") ])
    pgroup = SelectField("dompgroup", choices=[ ("pre_release", "Pre-release"), ("release", "Release"),
                                                ("post_release", "Post-release") ])
    chassis = StringField("domchassis", validators=[ Regexp(r"^\w+$", message="Invalid characters") ])
    addbtn = SubmitField(label="Add Domain")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class ConfirmForm(Form):
    backbtn = SubmitField(label="<< Back")
    cfmbtn = SubmitField(label="Confirm")
