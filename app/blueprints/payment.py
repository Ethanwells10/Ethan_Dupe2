from flask import Blueprint, render_template, session, request, redirect, url_for, flash, jsonify
from app.cart_utils import get_cart

payment = Blueprint('payment', __name__)

@payment.route('/')
def checkout():
    # Get cart items from session using cart_utils
    cart_items = get_cart()
    
    if not cart_items:
        order_data = {
            'products': [],
            'original_subtotal': 0.0,
            'subtotal': 0.0,
            'jersey_discount': 0.0,
            'hat_discount': 0.0,
            'total_savings': 0.0,
            'shipping': 0.0,
            'free_shipping_applied': False,
            'tax': 0.0,
            'total': 0.0
        }
        return render_template('payment.html', order=order_data)
    
    # Debug: Print cart items to check structure
    print("Cart items:", cart_items)
    
    # Calculate original subtotal
    original_subtotal = 0.0
    for item in cart_items:
        price = float(item['price'].replace('$', ''))
        original_subtotal += price * item['quantity']
    
    # Apply discounts
    discounted_subtotal = original_subtotal
    jersey_discount = 0.0
    hat_discount = 0.0
    
    # Apply 20% off jerseys
    jersey_items = [item for item in cart_items if item.get('type') == 'jersey']
    print(f"Jersey items found: {len(jersey_items)}")
    if jersey_items:
        jersey_total = 0.0
        for item in jersey_items:
            price = float(item['price'].replace('$', ''))
            jersey_total += price * item['quantity']
        jersey_discount = jersey_total * 0.20
        print(f"Jersey discount: ${jersey_discount}")
    
    # Apply BOGO 50% for hats (second hat 50% off, lower priced item)
    hat_items = [item for item in cart_items if item.get('type') == 'hat']
    print(f"Hat items found: {len(hat_items)}")
    
    # Create list of all hat prices (including quantities)
    hat_prices = []
    for item in hat_items:
        price = float(item['price'].replace('$', ''))
        for _ in range(item['quantity']):
            hat_prices.append(price)
    
    print(f"Total individual hats: {len(hat_prices)}")
    
    if len(hat_prices) >= 2:
        hat_prices.sort()  # Sort ascending, cheapest first
        print(f"Hat prices sorted: {hat_prices}")
        
        # Apply 50% discount to every second hat (pairs)
        pairs = len(hat_prices) // 2
        for i in range(pairs):
            hat_discount += hat_prices[i] * 0.50  # 50% off the cheaper item in each pair
        print(f"Hat discount: ${hat_discount}")
    
    # Calculate final discounted subtotal
    discounted_subtotal = original_subtotal - jersey_discount - hat_discount
    
    # Apply free shipping if order is over $75
    if discounted_subtotal >= 75:
        shipping = 0.0
        free_shipping_applied = True
    else:
        shipping = 12.99 if discounted_subtotal > 0 else 0.0
        free_shipping_applied = False
    
    # Calculate tax on discounted amount
    tax = discounted_subtotal * 0.0825  # 8.25% tax rate
    total = discounted_subtotal + shipping + tax
    
    order_data = {
        'products': cart_items,
        'original_subtotal': round(original_subtotal, 2),
        'subtotal': round(discounted_subtotal, 2),
        'jersey_discount': round(jersey_discount, 2),
        'hat_discount': round(hat_discount, 2),
        'total_savings': round(jersey_discount + hat_discount, 2),
        'shipping': round(shipping, 2),
        'free_shipping_applied': free_shipping_applied,
        'tax': round(tax, 2),
        'total': round(total, 2)
    }
    
    print(f"Order data: {order_data}")
    return render_template('payment.html', order=order_data)

@payment.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get item data from request
    item_data = {
        'name': request.form.get('name'),
        'player': request.form.get('player'),
        'number': request.form.get('number'),
        'team': request.form.get('team'),
        'price': request.form.get('price'),
        'quantity': 1,
        'size': request.form.get('size', 'Large')  # Default size
    }
    
    # Initialize cart in session if it doesn't exist
    if 'cart' not in session:
        session['cart'] = []
    
    # Check if item already exists in cart
    cart = session['cart']
    found = False
    for item in cart:
        if (item['name'] == item_data['name'] and 
            item['player'] == item_data['player'] and 
            item['size'] == item_data['size']):
            item['quantity'] += 1
            found = True
            break
    
    if not found:
        cart.append(item_data)
    
    session['cart'] = cart
    session.modified = True
    
    flash(f"{item_data['player']} jersey added to cart!", 'success')
    
    if request.form.get('ajax') == 'true':
        return jsonify({'success': True, 'message': 'Item added to cart!'})
    
    return redirect(request.referrer or url_for('jerseys.show_jerseys'))

@payment.route('/remove_from_cart/<int:item_index>')
def remove_from_cart(item_index):
    cart = session.get('cart', [])
    if 0 <= item_index < len(cart):
        removed_item = cart.pop(item_index)
        session['cart'] = cart
        session.modified = True
        flash(f"{removed_item['player']} jersey removed from cart.", 'info')
    
    return redirect(url_for('payment.checkout'))