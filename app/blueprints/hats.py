from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.cart_utils import add_to_cart

hats = Blueprint('hats', __name__)

@hats.route('/')
def show_hats():
    # AFC North Division hat data
    hat_data = {
        'cincinnati_bengals': {
            'team_name': 'Cincinnati Bengals',
            'team_colors': ['#FB4F14', '#000000'],  # Orange and Black
            'hats': [
                {
                    'name': 'Bengals Snapback',
                    'style': 'Snapback',
                    'description': 'Official New Era fitted cap with authentic team logo and premium construction.',
                    'price': '$39.99',
                    'image_placeholder': 'bengals-fitted.jpg',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-new-era-black-cincinnati-bengals-team-basic-59fifty-fitted-hat_ss5_p-200028668+u-nrxhntxmrrmznbtjdw3f+v-2oygeslgigsf8fvjzs1e.jpg?_hv=2',
                    'features': ['New Era Official', 'Fitted Sizing', 'Premium Quality']
                },
                {
                    'name': 'Bengals Beanie',
                    'style': 'Beanie',
                    'description': 'Warm knit beanie in team colors with pom pom. Essential for cold weather games.',
                    'price': '$24.99',
                    'image_placeholder': 'bengals-beanie.jpg',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-new-era-black/orange-cincinnati-bengals-2021-nfl-sideline-sport-official-pom-cuffed-knit-hat_pi4224000_altimages_ff_4224098-0c8f9a8f2d0bd9d60da2alt1_full.jpg?_hv=2&w=900',
                    'features': ['Warm Knit', 'Team Colors', 'Pom Pom Detail']
                }
            ]
        },
        'baltimore_ravens': {
            'team_name': 'Baltimore Ravens',
            'team_colors': ['#1e4d8b', '#9E7C0C'],  # Purple and Gold
            'hats': [
                {
                    'name': 'Ravens Snapback',
                    'style': 'Snapback',
                    'description': 'Bold purple snapback with gold Ravens logo. Show your purple pride in style.',
                    'price': '$36.99',
                    'image_placeholder': 'ravens-snapback.jpg',
                    'image': 'https://fanatics.frgimages.com/baltimore-ravens/mens-new-era-black-baltimore-ravens-omaha-59fifty-fitted-hat_pi2539000_ff_2539476_full.jpg?_hv=2&w=900',
                    'features': ['Purple & Gold', 'Snapback Style', 'Team Logo']
                },
                {
                    'name': 'Ravens Beanie',
                    'style': 'Beanie',
                    'description': 'Official sideline beanie worn by coaches. Warm and stylish for winter games.',
                    'price': '$26.99',
                    'image_placeholder': 'ravens-sideline.jpg',
                    'image': 'https://i.ebayimg.com/images/g/ZAgAAOSwU~5lqDbj/s-l1200.jpg',
                    'features': ['Sideline Style', 'Coach Approved', 'Warm Fleece']
                }
            ]
        },
        'pittsburgh_steelers': {
            'team_name': 'Pittsburgh Steelers',
            'team_colors': ['#FFB612', '#000000'],  # Gold and Black
            'hats': [
                {
                    'name': 'Steelers Snapback',
                    'style': 'Snapback',
                    'description': 'Black and gold snapback featuring the iconic Steelers logo. A classic choice for Steel City fans.',
                    'price': '$35.99',
                    'image_placeholder': 'steelers-snapback.jpg',
                    'image': 'https://img.hatshopping.com/59Fifty-NFL-Pittsburgh-Steelers-Cap-by-New-Era.64538_f4.jpg',
                    'features': ['Black & Gold', 'Steel Logo', 'Classic Design']
                },
                {
                    'name': 'Steelers Beanie',
                    'style': 'Beanie',
                    'description': 'Inspired by the legendary Terrible Towel. Knit beanie in team colors with Steelers pride.',
                    'price': '$27.99',
                    'image_placeholder': 'steelers-beanie.jpg',
                    'image': 'https://shop.steelers.com/media/catalog/product/cache/3f2d8d848c7696150338d1a021206cc6/1/9/191633_191637-1.jpg',
                    'features': ['Terrible Towel Inspired', 'Knit Construction', 'Team Colors']
                }
            ]
        },
        'cleveland_browns': {
            'team_name': 'Cleveland Browns',
            'team_colors': ['#311D00', '#FF3C00'],  # Brown and Orange
            'hats': [
                {
                    'name': 'Browns Snapback',
                    'style': 'Snapback',
                    'description': 'Brown snapback with orange accents celebrating the legendary Dawg Pound faithful.',
                    'price': '$33.99',
                    'image_placeholder': 'browns-snapback.jpg',
                    'image': 'https://www.neweracap.com/cdn/shop/products/9227624382494.jpg?v=1648169097',
                    'features': ['Dawg Pound Pride', 'Brown & Orange', 'Fan Favorite']
                },
                {
                    'name': 'Browns Beanie',
                    'style': 'Beanie',
                    'description': 'Warm beanie featuring classic Browns script logo. Perfect for Cleveland winters.',
                    'price': '$25.99',
                    'image_placeholder': 'browns-beanie.jpg',
                    'image': 'https://fanatics.frgimages.com/cleveland-browns/mens-new-era-cream/brown-cleveland-browns-2023-sideline-historic-pom-cuffed-knit-hat_ss5_p-200016745+pv-1+u-8omnume1m15013qcmmf2+v-cl0sirdj4so592dswijt.jpg?_hv=2&w=900',
                    'features': ['Script Logo', 'Winter Ready', 'Cleveland Style']
                }
            ]
        }
    }
    
    return render_template('hats.html', teams=hat_data)

@hats.route('/add_to_cart', methods=['POST'])
def add_hat_to_cart():
    """Add a hat to the cart"""
    team = request.form.get('team')
    hat_index = int(request.form.get('hat_index'))
    
    # Get the same hat data as in show_hats
    hat_data = {
        'cincinnati_bengals': {
            'team_name': 'Cincinnati Bengals',
            'team_colors': ['#FB4F14', '#000000'],
            'hats': [
                {
                    'name': 'Bengals Snapback',
                    'style': 'Snapback',
                    'description': 'Official New Era fitted cap with authentic team logo and premium construction.',
                    'price': '$39.99',
                    'image_placeholder': 'bengals-fitted.jpg',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-new-era-black-cincinnati-bengals-team-basic-59fifty-fitted-hat_ss5_p-200028668+u-nrxhntxmrrmznbtjdw3f+v-2oygeslgigsf8fvjzs1e.jpg?_hv=2',
                    'features': ['New Era Official', 'Fitted Sizing', 'Premium Quality']
                },
                {
                    'name': 'Bengals Beanie',
                    'style': 'Beanie',
                    'description': 'Warm knit beanie in team colors with pom pom. Essential for cold weather games.',
                    'price': '$24.99',
                    'image_placeholder': 'bengals-beanie.jpg',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-new-era-black/orange-cincinnati-bengals-2021-nfl-sideline-sport-official-pom-cuffed-knit-hat_pi4224000_altimages_ff_4224098-0c8f9a8f2d0bd9d60da2alt1_full.jpg?_hv=2&w=900',
                    'features': ['Warm Knit', 'Team Colors', 'Pom Pom Detail']
                }
            ]
        },
        'baltimore_ravens': {
            'team_name': 'Baltimore Ravens',
            'team_colors': ['#1e4d8b', '#9E7C0C'],
            'hats': [
                {
                    'name': 'Ravens Snapback',
                    'style': 'Snapback',
                    'description': 'Bold purple snapback with gold Ravens logo. Show your purple pride in style.',
                    'price': '$36.99',
                    'image_placeholder': 'ravens-snapback.jpg',
                    'image': 'https://fanatics.frgimages.com/baltimore-ravens/mens-new-era-black-baltimore-ravens-omaha-59fifty-fitted-hat_pi2539000_ff_2539476_full.jpg?_hv=2&w=900',
                    'features': ['Purple & Gold', 'Snapback Style', 'Team Logo']
                },
                {
                    'name': 'Ravens Beanie',
                    'style': 'Beanie',
                    'description': 'Official sideline beanie worn by coaches. Warm and stylish for winter games.',
                    'price': '$26.99',
                    'image_placeholder': 'ravens-sideline.jpg',
                    'image': 'https://i.ebayimg.com/images/g/ZAgAAOSwU~5lqDbj/s-l1200.jpg',
                    'features': ['Sideline Style', 'Coach Approved', 'Warm Fleece']
                }
            ]
        },
        'pittsburgh_steelers': {
            'team_name': 'Pittsburgh Steelers',
            'team_colors': ['#FFB612', '#000000'],
            'hats': [
                {
                    'name': 'Steelers Snapback',
                    'style': 'Snapback',
                    'description': 'Black and gold snapback featuring the iconic Steelers logo. A classic choice for Steel City fans.',
                    'price': '$35.99',
                    'image_placeholder': 'steelers-snapback.jpg',
                    'image': 'https://img.hatshopping.com/59Fifty-NFL-Pittsburgh-Steelers-Cap-by-New-Era.64538_f4.jpg',
                    'features': ['Black & Gold', 'Steel Logo', 'Classic Design']
                },
                {
                    'name': 'Steelers Beanie',
                    'style': 'Beanie',
                    'description': 'Inspired by the legendary Terrible Towel. Knit beanie in team colors with Steelers pride.',
                    'price': '$27.99',
                    'image_placeholder': 'steelers-beanie.jpg',
                    'image': 'https://shop.steelers.com/media/catalog/product/cache/3f2d8d848c7696150338d1a021206cc6/1/9/191633_191637-1.jpg',
                    'features': ['Terrible Towel Inspired', 'Knit Construction', 'Team Colors']
                }
            ]
        },
        'cleveland_browns': {
            'team_name': 'Cleveland Browns',
            'team_colors': ['#311D00', '#FF3C00'],
            'hats': [
                {
                    'name': 'Browns Snapback',
                    'style': 'Snapback',
                    'description': 'Brown snapback with orange accents celebrating the legendary Dawg Pound faithful.',
                    'price': '$33.99',
                    'image_placeholder': 'browns-snapback.jpg',
                    'image': 'https://www.neweracap.com/cdn/shop/products/9227624382494.jpg?v=1648169097',
                    'features': ['Dawg Pound Pride', 'Brown & Orange', 'Fan Favorite']
                },
                {
                    'name': 'Browns Beanie',
                    'style': 'Beanie',
                    'description': 'Warm beanie featuring classic Browns script logo. Perfect for Cleveland winters.',
                    'price': '$25.99',
                    'image_placeholder': 'browns-beanie.jpg',
                    'image': 'https://fanatics.frgimages.com/cleveland-browns/mens-new-era-cream/brown-cleveland-browns-2023-sideline-historic-pom-cuffed-knit-hat_ss5_p-200016745+pv-1+u-8omnume1m15013qcmmf2+v-cl0sirdj4so592dswijt.jpg?_hv=2&w=900',
                    'features': ['Script Logo', 'Winter Ready', 'Cleveland Style']
                }
            ]
        }
    }
    
    if team in hat_data and 0 <= hat_index < len(hat_data[team]['hats']):
        hat = hat_data[team]['hats'][hat_index]
        if add_to_cart('hat', team, hat):
            flash(f'Added {hat["name"]} to cart!', 'success')
        else:
            flash('Error adding item to cart', 'error')
    else:
        flash('Invalid item selected', 'error')
    
    return redirect(url_for('hats.show_hats'))