import streamlit as st
import stripe
import webbrowser
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Stripe secret key from environment variables
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

# In-memory storage for payment status
if 'payment_status' not in st.session_state:
    st.session_state['payment_status'] = None

base_url = "http://localhost:8501"

def create_checkout_session(price_id):
    """
    Creates a new Stripe Checkout Session.
    """
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url=base_url + '?success=true&session_id={CHECKOUT_SESSION_ID}',
            cancel_url = base_url + '?canceled=true',
        )
        return session.url
    except Exception as e:
        st.error(f"An error occurred while creating the checkout session: {e}")
        return None

def check_payment_status(session_id):
    """
    Retrieves the Stripe Checkout Session to check its payment status.
    """
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            return True
    except Exception as e:
        st.error(f"An error occurred while retrieving the session: {e}")
    return False

# --- Streamlit App UI ---

st.title("Stripe Checkout App")
st.write("This is a simple example of integrating Stripe Checkout with Streamlit.")

# Define a product and price in your Stripe dashboard and get the price ID.
# This is an example price ID. You must replace it with your own.
# You can get this from the Stripe Dashboard under Products.
PRICE_ID = "price_1RbpDJGdHUGbdWWBrVLmXOUs"

if st.button("Buy Now"):
    checkout_url = create_checkout_session(PRICE_ID)
    if checkout_url:
        st.markdown(
            f"""
            <a href="{checkout_url}" target="_self">
                <button style="background-color: #4CAF50; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border: none; border-radius: 8px;">
                    Proceed to Checkout
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
        st.info("You will be redirected to Stripe to complete the payment.")

# --- Handle the redirect from Stripe ---

query_params = st.experimental_get_query_params()

if 'success' in query_params:
    session_id = query_params.get('session_id', [None])[0]
    if session_id:
        if check_payment_status(session_id):
            st.session_state['payment_status'] = 'success'
        else:
            st.session_state['payment_status'] = 'error'

elif 'canceled' in query_params:
    st.session_state['payment_status'] = 'canceled'

# --- Display the payment result from memory ---

st.header("Payment Status")

if st.session_state['payment_status'] == 'success':
    st.success("Successful payment! Thank you for your purchase.")
    st.balloons()
elif st.session_state['payment_status'] == 'error':
    st.error("Error okay payment. The payment was not successful.")
elif st.session_state['payment_status'] == 'canceled':
    st.warning("Payment was canceled. You can try again.")
elif st.session_state['payment_status'] is None:
    st.info("Awaiting payment...")