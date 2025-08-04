import streamlit as st
from streamlit.components.v1 import html
import os
from dotenv import load_dotenv
load_dotenv('.env')

stripe_publishable_key = os.environ.get("STRIPE_KEY")

st.set_page_config(
    page_title="Streamlit Stripe Demo",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Payment")

checkout_url = "https://buy.stripe.com/test_7sI6qH3wQ8wH7iYcMM"  # Replace with your actual Stripe Checkout URL for prod_SWszGRzTjNFUj7

pay_button_html = f"""
<button onclick="window.open('{checkout_url}', '_blank', 'width=500,height=700');" style="font-size:24px;padding:12px 32px;background:#635BFF;color:white;border:none;border-radius:6px;cursor:pointer;">
  Pay with Stripe
</button>
"""

html(pay_button_html)