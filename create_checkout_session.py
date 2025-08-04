import os
import stripe
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv('.env')
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

app = Flask(__name__)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1RcWlUGdHUGbdWWBexePo1Qe',  # Replace with your actual price ID for prod_SWszGRzTjNFUj7
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.json.get('success_url', 'https://yourdomain.com/success'),
            cancel_url=request.json.get('cancel_url', 'https://yourdomain.com/cancel'),
        )
        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(port=4242)
