import os
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your Stripe secret key and webhook secret
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        # Invalid payload
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return jsonify({'error': 'Invalid signature'}), 400

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        # Payment is complete, add your logic here
        print(f"PaymentIntent was successful: {payment_intent['id']}")
    elif event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Checkout session completed, add your logic here
        print(f"Checkout session completed: {session['id']}")
    # ... handle other event types as needed

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=4242)
