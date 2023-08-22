from flask.views import MethodView
from flask import render_template, Flask, request
from wtforms import Form, StringField, FloatField, IntegerField, SubmitField
from calorie_calulator import calorie, temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class InformationFormPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('information_page.html', calorie_form=calorie_form)

    def post(self):
        """Get inputs from user through form"""
        calorie_form = CalorieForm(request.form)
        weight = calorie_form.weight.data
        height = calorie_form.height.data
        age = calorie_form.age.data
        city = calorie_form.city.data
        country = calorie_form.country.data

        # Call the class Temperature to get the current temperature
        current_temp = temperature.Temperature(city, country).get_temperature()

        # Call the class Calorie to calculate the calorie amount based on user's indications
        calorie_calculator = calorie.Calorie(weight, height, age, current_temp)
        calorie_amount = calorie_calculator.calculating_calories()
        return render_template('information_page.html',
                               calorie_intake=calorie_amount,
                               calorie_form=calorie_form,
                               result=True)


class CalorieForm(Form):  # not a page

    weight = FloatField(label='Weight (kg):', default=65)
    height = IntegerField(label='Height (cm):', default=170)
    age = IntegerField(label='Age:', default=24)

    city = StringField(label='City:', default='london')
    country = StringField(label='Country:', default='uk')

    submit_button = SubmitField(label='Calculate')


app.add_url_rule(rule='/', view_func=HomePage.as_view('home_page'))
app.add_url_rule(rule='/infor_page', view_func=InformationFormPage.as_view('infor_page'))

app.run(debug=True)
