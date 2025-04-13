from flask import Blueprint, render_template, request, flash
from app.models_utils import predict_planet

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            radius = float(request.form['radius_km'])
            mass = float(request.form['mass_10^24kg'])
            orbital_period = float(request.form['orbital_period_days'])
            temperature = float(request.form['temperature_avg_c'])

            prediction = predict_planet([radius, mass, orbital_period, temperature])
            
            flash(f'Förutsägelse: {prediction}', 'success')
        except ValueError:
            flash('Ogiltiga värden. Var god försök igen.', 'danger')
    return render_template('index.html')



