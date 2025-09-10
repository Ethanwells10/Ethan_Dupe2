from flask import session
import json

def init_cart():
    """Initialize cart in session if it doesn't exist"""
    if 'cart' not in session:
        session['cart'] = []
    session.permanent = True

def add_to_cart(item_type, team, item_data):
    """Add an item to the cart"""
    init_cart()
    
    cart_item = {
        'type': item_type,  # 'hat' or 'jersey'
        'team': team,
        'name': item_data['name'],
        'price': item_data['price'],
        'description': item_data.get('description', ''),
        'image': item_data.get('image', ''),
        'player': item_data.get('player', ''),
        'number': item_data.get('number', ''),
        'style': item_data.get('style', ''),
        'quantity': 1
    }
    
    # Check if item already exists in cart
    for item in session['cart']:
        if (item['type'] == item_type and 
            item['team'] == team and 
            item['name'] == item_data['name']):
            item['quantity'] += 1
            session.modified = True
            return True
    
    # Add new item to cart
    session['cart'].append(cart_item)
    session.modified = True
    return True

def get_cart():
    """Get cart items from session"""
    init_cart()
    return session['cart']

def get_cart_total():
    """Calculate total price of items in cart"""
    cart = get_cart()
    total = 0.0
    for item in cart:
        # Remove $ and convert to float
        price = float(item['price'].replace('$', ''))
        total += price * item['quantity']
    return total

def get_cart_count():
    """Get total number of items in cart"""
    cart = get_cart()
    return sum(item['quantity'] for item in cart)

def remove_from_cart(index):
    """Remove item from cart by index"""
    init_cart()
    if 0 <= index < len(session['cart']):
        session['cart'].pop(index)
        session.modified = True
        return True
    return False

def clear_cart():
    """Clear all items from cart"""
    session['cart'] = []
    session.modified = True