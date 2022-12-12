from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Postform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    ability = StringField('Ability', validators=[DataRequired()])
    base_experience = IntegerField('Base Experience', validators=[DataRequired()])
    sprite_url = StringField('Sprite URL', validators=[DataRequired()])
    attack_base_stat = IntegerField('Attack Base Stat', validators=[DataRequired()])
    hp_base_stat = IntegerField('HP Base Stat', validators=[DataRequired()])
    defense_base_stat = IntegerField('Defense Base Stat', validators=[DataRequired()])
    submit = SubmitField()