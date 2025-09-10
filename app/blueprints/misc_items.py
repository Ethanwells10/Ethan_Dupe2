from flask import Blueprint, render_template

misc_items = Blueprint('misc_items', __name__)

@misc_items.route('/')
def show_misc_items():
    # AFC North Division miscellaneous items data
    misc_data = {
        'cincinnati_bengals': {
            'team_name': 'Cincinnati Bengals',
            'team_colors': ['#FB4F14', '#000000'],  # Orange and Black
            'products': [
                {
                    'name': 'Bengals Team Logo Keychain',
                    'category': 'Keychain',
                    'description': 'Metal keychain featuring the iconic Bengals tiger head logo. Perfect for keys or backpack.',
                    'price': '$8.99',
                    'image_placeholder': 'bengals-keychain.jpg',
                    'features': ['Metal Construction', 'Team Logo', 'Keyring Included']
                },
                {
                    'name': 'Bengal Stripes Coffee Mug',
                    'category': 'Drinkware',
                    'description': 'Ceramic mug with Bengal orange and black stripes. Dishwasher and microwave safe.',
                    'price': '$16.99',
                    'image_placeholder': 'bengals-mug.jpg',
                    'features': ['Dishwasher Safe', '15oz Capacity', 'Team Colors']
                },
                {
                    'name': 'Bengals Team Flag',
                    'category': 'Home Decor',
                    'description': 'Large 3x5 feet outdoor flag with grommets. Show your Bengal pride at home or tailgating.',
                    'price': '$24.99',
                    'image_placeholder': 'bengals-flag.jpg',
                    'features': ['3x5 Feet', 'Weather Resistant', 'Grommets Included']
                },
                {
                    'name': 'Mini Bengals Helmet',
                    'category': 'Collectible',
                    'description': 'Authentic mini replica helmet perfect for display. Official NFL licensed product.',
                    'price': '$34.99',
                    'image_placeholder': 'bengals-mini-helmet.jpg',
                    'features': ['Official Replica', 'Display Stand', 'NFL Licensed']
                }
            ]
        },
        'baltimore_ravens': {
            'team_name': 'Baltimore Ravens',
            'team_colors': ['#1e4d8b', '#9E7C0C'],  # Purple and Gold
            'products': [
                {
                    'name': 'Ravens Logo Keychain',
                    'category': 'Keychain',
                    'description': 'Sleek purple and gold keychain with the Ravens shield logo. Durable and stylish.',
                    'price': '$9.99',
                    'image_placeholder': 'ravens-keychain.jpg',
                    'features': ['Purple & Gold', 'Shield Logo', 'Premium Materials']
                },
                {
                    'name': 'Ravens Travel Mug',
                    'category': 'Drinkware',
                    'description': 'Insulated travel mug with Ravens logo. Keeps drinks hot or cold for hours.',
                    'price': '$22.99',
                    'image_placeholder': 'ravens-travel-mug.jpg',
                    'features': ['Double Insulated', 'Leak Proof', 'Team Logo']
                },
                {
                    'name': 'Ravens Purple Reign Flag',
                    'category': 'Home Decor',
                    'description': 'Premium flag celebrating the Ravens purple reign. Perfect for game day display.',
                    'price': '$27.99',
                    'image_placeholder': 'ravens-flag.jpg',
                    'features': ['Premium Quality', 'Purple Theme', 'Championship Pride']
                },
                {
                    'name': 'Ravens Mini Helmet Collectible',
                    'category': 'Collectible',
                    'description': 'Detailed mini helmet with authentic Ravens colors and decals. Great for collectors.',
                    'price': '$37.99',
                    'image_placeholder': 'ravens-mini-helmet.jpg',
                    'features': ['Collector Quality', 'Authentic Decals', 'Display Ready']
                }
            ]
        },
        'pittsburgh_steelers': {
            'team_name': 'Pittsburgh Steelers',
            'team_colors': ['#FFB612', '#000000'],  # Gold and Black
            'products': [
                {
                    'name': 'Steelers Steel Logo Keychain',
                    'category': 'Keychain',
                    'description': 'Heavy-duty steel keychain with the three diamonds logo. Built Steel City tough.',
                    'price': '$11.99',
                    'image_placeholder': 'steelers-keychain.jpg',
                    'features': ['Steel Construction', 'Three Diamonds', 'Pittsburgh Strong']
                },
                {
                    'name': 'Terrible Towel Mug',
                    'category': 'Drinkware',
                    'description': 'Mug inspired by the legendary Terrible Towel. A must-have for any Steelers fan.',
                    'price': '$18.99',
                    'image_placeholder': 'steelers-mug.jpg',
                    'features': ['Terrible Towel Design', 'Gold Accents', 'Steelers Legacy']
                },
                {
                    'name': 'Six-Time Champions Flag',
                    'category': 'Home Decor',
                    'description': 'Commemorative flag celebrating six Super Bowl championships. Black and gold excellence.',
                    'price': '$32.99',
                    'image_placeholder': 'steelers-flag.jpg',
                    'features': ['Championship Theme', 'Black & Gold', 'Six Rings Pride']
                },
                {
                    'name': 'Steelers Mini Helmet',
                    'category': 'Collectible',
                    'description': 'Classic mini helmet with authentic Steelers logo placement. Represents decades of tradition.',
                    'price': '$36.99',
                    'image_placeholder': 'steelers-mini-helmet.jpg',
                    'features': ['Classic Design', 'Authentic Logos', 'Steelers Tradition']
                }
            ]
        },
        'cleveland_browns': {
            'team_name': 'Cleveland Browns',
            'team_colors': ['#311D00', '#FF3C00'],  # Brown and Orange
            'products': [
                {
                    'name': 'Dawg Pound Keychain',
                    'category': 'Keychain',
                    'description': 'Brown and orange keychain celebrating the legendary Dawg Pound faithful fans.',
                    'price': '$7.99',
                    'image_placeholder': 'browns-keychain.jpg',
                    'features': ['Dawg Pound Pride', 'Brown & Orange', 'Fan Tribute']
                },
                {
                    'name': 'Browns Helmet Logo Mug',
                    'category': 'Drinkware',
                    'description': 'Classic mug featuring the Browns helmet logo. Simple, clean, and Cleveland strong.',
                    'price': '$15.99',
                    'image_placeholder': 'browns-mug.jpg',
                    'features': ['Helmet Logo', 'Classic Design', 'Cleveland Strong']
                },
                {
                    'name': 'Browns Dawg Flag',
                    'category': 'Home Decor',
                    'description': 'Show your Dawg Pound loyalty with this vibrant Browns flag. Perfect for tailgating.',
                    'price': '$23.99',
                    'image_placeholder': 'browns-flag.jpg',
                    'features': ['Dawg Theme', 'Vibrant Colors', 'Tailgate Ready']
                },
                {
                    'name': 'Browns Classic Mini Helmet',
                    'category': 'Collectible',
                    'description': 'Retro-style mini helmet representing Browns tradition and Cleveland football heritage.',
                    'price': '$33.99',
                    'image_placeholder': 'browns-mini-helmet.jpg',
                    'features': ['Retro Style', 'Cleveland Heritage', 'Browns History']
                }
            ]
        }
    }
    
    return render_template('misc_items.html', teams=misc_data)