from flask import Blueprint, render_template

contact = Blueprint('contact', __name__)

@contact.route('/')
def show_contact():
    # Contact information
    contact_info = {
        'email': 'support@gridirongear.com',
        'phone': '(555) 123-4567',
        'address': {
            'street': '123 NFL Boulevard',
            'city': 'Canton',
            'state': 'OH',
            'zip': '44708'
        },
        'hours': {
            'weekdays': '9:00 AM - 8:00 PM EST',
            'weekends': '10:00 AM - 6:00 PM EST'
        }
    }
    
    return render_template('contact.html', contact=contact_info)