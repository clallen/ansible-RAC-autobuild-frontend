from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class ClusterNameForm(Form):
    clname = StringField("clname", validators=[DataRequired()])

class StorageForm(Form):
    name = StringField("blockname", validators=[DataRequired()])
    pool = StringField("blockpool", validators=[DataRequired()])
    ports = StringField("blockports", validators=[DataRequired()])
    begin = StringField("blockbegin", validators=[DataRequired()])
    end = StringField("blockend", validators=[DataRequired()])
    size = StringField("blocksize", validators=[DataRequired()])
    chassis = StringField("blockchassis", validators=[DataRequired()])
    addbtn = SubmitField(label="Add Storage Block")
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")

class ChassisForm(Form):
    name = StringField("domname", validators=[DataRequired()])
    cores = StringField("domcores", validators=[DataRequired()])
    ram = StringField("domram", validators=[DataRequired()])
    pvid = StringField("dompvid", validators=[DataRequired()])
    pclass = SelectField("dompclass", choices=[ ("dev", "Dev"), ("test", "Test"), ("prod", "Prod") ])
    pg = SelectField("dompg", choices=[ ("pre_release", "Pre-release"), ("release", "Release"), ("post_release", "Post-release") ])
    racdisks = StringField("domracdisks", validators=[DataRequired()])
    chassis = StringField("domchassis", validators=[DataRequired()])
    backbtn = SubmitField(label="<< Back")
    nextbtn = SubmitField(label="Next >>")
