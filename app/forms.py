import re
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Length, Regexp, ValidationError

class ClusterNameForm(Form):
    name = StringField("Cluster Name", validators=[ Length(min=4), Regexp(r"^[a-zA-Z0-9]+$",
                                                    message="Invalid characters (alphanumeric only)") ])

class StorageForm(Form):
    name = StringField("Name", validators=[ Regexp(r"^\w+$", message="Invalid characters "+
                                            "(alphanumeric and underscore only)") ])
    pool = StringField("Pool", validators=[ Regexp(r"^[0-9]{2}$", message="Must be a 2-digit integer") ])
    ports = StringField("Ports")
    begin = StringField("Begin LDEV", validators=[ Regexp("^[a-f0-9]{2}:[a-f0-9]{2}$",
                                                   message="Invalid LDEV", flags=re.I) ])
    end = StringField("End LDEV", validators=[ Regexp("^[a-f0-9]{2}:[a-f0-9]{2}$",
                                               message="Invalid LDEV", flags=re.I) ])
    size = StringField("Size", validators=[ Regexp(r"^\d+$", message="Must be an integer") ])
    chassis = StringField("Chassis", validators=[ Regexp("^(\w+)(,\w+)*$", flags=re.I,
                                                  message="Must be either single chassis, "+
                                                  "or a comma-separated list of chassis") ])
    addbtn = SubmitField(label="Add Storage Block")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

    def validate_ports(form, field):
        ports = field.data.split(",")
        if len(ports) & 1 != 0:
            raise ValidationError("Must be comma-separated, even number of ports")
        else:
            for port in ports:
                if re.match(r"CL\d{1}-[a-z]{1}", port, re.I) is None:
                    raise ValidationError("Invalid format: "+port+" (must be in format 'CL1-B')")

class DomainForm(Form):
    name = StringField("Name", validators=[ Length(min=4), Regexp(r"^[a-zA-Z0-9]+$",
                                            message="Invalid characters") ])
    cores = StringField("Cores", validators=[ Regexp("^\d+$", message="Must be an integer") ])
    ram = StringField("Memory", validators=[ Regexp("^\d+$", message="Must be an integer") ])

    pvid = StringField("Public PVID", validators=[ Length(min=4),
                                                   Regexp("^\d{4}$", message="Must be a 4-digit integer") ])
    pclass = SelectField("Class", choices=[ ("dev", "Dev"), ("test", "Test"), ("prod", "Prod") ])
    pgroup = SelectField("Patch Group", choices=[ ("pre_release", "Pre-release"), ("release", "Release"),
                                                ("post_release", "Post-release") ])
    powner = SelectField("Owner", choices=[ ("dba", "DBA"), ("asmt", "ASMT") ])
    chassis = StringField("Chassis", validators=[ Regexp(r"^\w+$", message="Invalid characters") ])
    addbtn = SubmitField(label="Add Domain")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class ConfirmForm(Form):
    backbtn = SubmitField(label="<< Back")
    cfmbtn = SubmitField(label="Confirm")
