from flask import Blueprint, render_template, request, redirect, url_for
from car_collection.forms import CarForm
from flask_login import login_required, current_user
from car_collection.models import Car, CarSchema, db


site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')
    

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    carform = CarForm()

    try:
        if request.method == 'POST' and carform.validate_on_submit():
            make = carform.make.data
            model = carform.model.data
            year = carform.year.data
            color = carform.color.data
            description = carform.description.data
            price = carform.price.data
            miles_per_gallon = carform.miles_per_gallon.data
            max_speed = carform.max_speed.data
            seats = carform.seats.data
            user_token = current_user.token

            car = Car(make, model, year, color, description, price, miles_per_gallon,
                      max_speed, seats, user_token)
            
            db.session.add(car)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Drone not created, please check your form and try again.')
    user_token = current_user.token
    cars = Car.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=carform, cars=cars)



   