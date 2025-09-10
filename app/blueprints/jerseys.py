from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.cart_utils import add_to_cart

jerseys = Blueprint('jerseys', __name__)

@jerseys.route('/')
def show_jerseys():
    # AFC North Division jersey data
    jersey_data = {
        'cincinnati_bengals': {
            'team_name': 'Cincinnati Bengals',
            'team_colors': ['#FB4F14', '#4A4A4A'],  # Orange and Light Gray
            'jerseys': [
                {
                    'player': 'Joe Burrow',
                    'number': '9',
                    'description': 'Official Nike home jersey featuring the iconic Bengal stripes and premium construction.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-nike-joe-burrow-black-cincinnati-bengals-player-game-jersey_pi4293000_altimages_ff_4293970-e432d0441e1a0c33100ealt1_full.jpg?_hv=2&w=900'
                },
                {
                    'player': 'Ja\'Marr Chase',
                    'number': '1',
                    'description': 'Authentic white away jersey with Bengal orange accents and player name.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-nike-jamarr-chase-black-cincinnati-bengals-game-jersey_pi4326000_ff_4326868-bf0c981f12fb3bd9e5a8_full.jpg?_hv=2'
                }
            ]
        },
        'baltimore_ravens': {
            'team_name': 'Baltimore Ravens',
            'team_colors': ['#4169E1', '#9E7C0C'],  # Royal Blue and Gold
            'jerseys': [
                {
                    'player': 'Lamar Jackson',
                    'number': '8',
                    'description': 'Official Nike home jersey in Ravens purple with gold trim and MVP-quality construction.',
                    'price': '$159.99',
                    'image': 'https://slimages.macysassets.com/is/image/MCY/products/3/optimized/26786613_fpx.tif'
                },
                {
                    'player': 'Roquan Smith',
                    'number': '18',
                    'description': 'Premium white away jersey featuring Ravens logos and linebacker durability.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/baltimore-ravens/mens-nike-roquan-smith-purple-baltimore-ravens-team-game-jersey_ss5_p-200410765+u-14lbf3lyjcv6ky6y9xl3+v-d2ty64m12qa0ri6i06i3.jpg?_hv=2'
                }
            ]
        },
        'pittsburgh_steelers': {
            'team_name': 'Pittsburgh Steelers',
            'team_colors': ['#FFB612', '#000000'],  # Gold and Black
            'jerseys': [
                {
                    'player': 'T.J. Watt',
                    'number': '90',
                    'description': 'Classic black and gold Steelers jersey with Terrible Towel authenticity.',
                    'price': '$154.99',
                    'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRass_1jQzrNI8cFdDDK9e64kFMw_Owo3kOMw&s'
                },
                {
                    'player': 'Kenny Pickett',
                    'number': '8',
                    'description': 'White away jersey with Steel Curtain legacy and quarterback precision.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/pittsburgh-steelers/youth-nike-kenny-pickett-black-pittsburgh-steelers-game-jersey_pi4879000_altimages_ff_4879138-df5b4985467e4d44566calt1_full.jpg?_hv=2&w=900'
                }
            ]
        },
        'cleveland_browns': {
            'team_name': 'Cleveland Browns',
            'team_colors': ['#8B4513', '#FF3C00'],  # Saddle Brown and Orange
            'jerseys': [
                {
                    'player': 'Myles Garrett',
                    'number': '95',
                    'description': 'Authentic Cleveland Browns jersey in classic brown with orange numbers and dawg pound pride.',
                    'price': '$149.99',
                    'image': 'https://images.footballfanatics.com/cleveland-browns/mens-nike-myles-garrett-brown-cleveland-browns-nfl-100-vapor-limited-jersey_pi3455000_ff_3455565-c5a18fc623ed20fd021d_full.jpg?_hv=2'
                },
                {
                    'player': 'Nick Chubb',
                    'number': '24',
                    'description': 'White away jersey featuring Browns orange and built for championship runs.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cleveland-browns/mens-nike-nick-chubb-brown-cleveland-browns-player-game-jersey_pi3901000_altimages_ff_3901576-0bbe46e6aff58133f040alt1_full.jpg?_hv=2&w=900'
                }
            ]
        }
    }
    
    return render_template('jerseys.html', teams=jersey_data)

@jerseys.route('/add_to_cart', methods=['POST'])
def add_jersey_to_cart():
    """Add a jersey to the cart"""
    team = request.form.get('team')
    jersey_index = int(request.form.get('jersey_index'))
    
    # Get the same jersey data as in show_jerseys
    jersey_data = {
        'cincinnati_bengals': {
            'team_name': 'Cincinnati Bengals',
            'team_colors': ['#FB4F14', '#000000'],
            'jerseys': [
                {
                    'player': 'Joe Burrow',
                    'number': '9',
                    'name': 'Joe Burrow #9 Jersey',
                    'description': 'Official Nike home jersey featuring the iconic Bengal stripes and premium construction.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-nike-joe-burrow-black-cincinnati-bengals-player-game-jersey_pi4293000_altimages_ff_4293970-e432d0441e1a0c33100ealt1_full.jpg?_hv=2&w=900'
                },
                {
                    'player': 'Ja\'Marr Chase',
                    'number': '1',
                    'name': 'Ja\'Marr Chase #1 Jersey',
                    'description': 'Authentic white away jersey with Bengal orange accents and player name.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cincinnati-bengals/mens-nike-jamarr-chase-black-cincinnati-bengals-game-jersey_pi4326000_ff_4326868-bf0c981f12fb3bd9e5a8_full.jpg?_hv=2'
                }
            ]
        },
        'baltimore_ravens': {
            'team_name': 'Baltimore Ravens',
            'team_colors': ['#1e4d8b', '#9E7C0C'],
            'jerseys': [
                {
                    'player': 'Lamar Jackson',
                    'number': '8',
                    'name': 'Lamar Jackson #8 Jersey',
                    'description': 'Official Nike home jersey in Ravens purple with gold trim and MVP-quality construction.',
                    'price': '$159.99',
                    'image': 'https://slimages.macysassets.com/is/image/MCY/products/3/optimized/26786613_fpx.tif'
                },
                {
                    'player': 'Roquan Smith',
                    'number': '18',
                    'name': 'Roquan Smith #18 Jersey',
                    'description': 'Premium white away jersey featuring Ravens logos and linebacker durability.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/baltimore-ravens/mens-nike-roquan-smith-purple-baltimore-ravens-team-game-jersey_ss5_p-200410765+u-14lbf3lyjcv6ky6y9xl3+v-d2ty64m12qa0ri6i06i3.jpg?_hv=2'
                }
            ]
        },
        'pittsburgh_steelers': {
            'team_name': 'Pittsburgh Steelers',
            'team_colors': ['#FFB612', '#000000'],
            'jerseys': [
                {
                    'player': 'T.J. Watt',
                    'number': '90',
                    'name': 'T.J. Watt #90 Jersey',
                    'description': 'Classic black and gold Steelers jersey with Terrible Towel authenticity.',
                    'price': '$154.99',
                    'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRass_1jQzrNI8cFdDDK9e64kFMw_Owo3kOMw&s'
                },
                {
                    'player': 'Kenny Pickett',
                    'number': '8',
                    'name': 'Kenny Pickett #8 Jersey',
                    'description': 'White away jersey with Steel Curtain legacy and quarterback precision.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/pittsburgh-steelers/youth-nike-kenny-pickett-black-pittsburgh-steelers-game-jersey_pi4879000_altimages_ff_4879138-df5b4985467e4d44566calt1_full.jpg?_hv=2&w=900'
                }
            ]
        },
        'cleveland_browns': {
            'team_name': 'Cleveland Browns',
            'team_colors': ['#311D00', '#FF3C00'],
            'jerseys': [
                {
                    'player': 'Myles Garrett',
                    'number': '95',
                    'name': 'Myles Garrett #95 Jersey',
                    'description': 'Authentic Cleveland Browns jersey in classic brown with orange numbers and dawg pound pride.',
                    'price': '$149.99',
                    'image': 'https://images.footballfanatics.com/cleveland-browns/mens-nike-myles-garrett-brown-cleveland-browns-nfl-100-vapor-limited-jersey_pi3455000_ff_3455565-c5a18fc623ed20fd021d_full.jpg?_hv=2'
                },
                {
                    'player': 'Nick Chubb',
                    'number': '24',
                    'name': 'Nick Chubb #24 Jersey',
                    'description': 'White away jersey featuring Browns orange and built for championship runs.',
                    'price': '$149.99',
                    'image': 'https://fanatics.frgimages.com/cleveland-browns/mens-nike-nick-chubb-brown-cleveland-browns-player-game-jersey_pi3901000_altimages_ff_3901576-0bbe46e6aff58133f040alt1_full.jpg?_hv=2&w=900'
                }
            ]
        }
    }
    
    if team in jersey_data and 0 <= jersey_index < len(jersey_data[team]['jerseys']):
        jersey = jersey_data[team]['jerseys'][jersey_index]
        if add_to_cart('jersey', team, jersey):
            flash(f'Added {jersey["player"]} #{jersey["number"]} jersey to cart!', 'success')
        else:
            flash('Error adding item to cart', 'error')
    else:
        flash('Invalid item selected', 'error')
    
    return redirect(url_for('jerseys.show_jerseys'))