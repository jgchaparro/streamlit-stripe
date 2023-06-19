import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="30A Bramble Beach Rental",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Section 1: About the Space
st.title("30A Bramble Beach Rental!")
st.markdown("ℹ️ *3 bedrooms, pool, and close to the beach!*")

# Description of the house
st.subheader("About the House")
st.markdown("Our beach house is located in the beautiful 30A area of Florida. It offers the following amenities:")
st.markdown("🏖️ 3 bedrooms")
st.markdown("🏊 Private pool")
st.markdown("🎥 Major streaming services: Hulu Live, Netflix, Peacock")
st.markdown("🚶‍♂️ Just 0.25 miles from public beach access")
st.markdown("🍽️ Walking distance to restaurants and rental shops (bikes, golf carts, etc.)")

# Section 2: Book a Date to Visit the Beach
st.title("Book Your Stay")
st.markdown("🗓️ *Select the week you'd like to stay*")

# Display a calendar for selecting dates
selected_date = st.date_input("Select a week", help="Choose the starting date of your stay.")

# Section 3: Take Payments via Stripe
st.title("Payment")
st.markdown("💳 *Enter your payment details to secure your reservation*")

# Display success message after payment
if st.button("Confirm Payment"):
    st.success("Payment successful! Your reservation is confirmed.")

# End of centered container
st.markdown('</div>', unsafe_allow_html=True)

# Stripe payment integration
stripe_js = """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1NKjSSBY7L5WREAJ0wKVXsQB"
  publishable-key="pk_test_51IhaciBY7L5WREAJwVMBrcxv5kBExAigZ1Ajl8yCSjyTdP3lAhhZ6BsAUAImY9rCrklgbyV6Gj86qHXnSlY3F8l500KHDNOg3s"
></stripe-buy-button>
"""

st.markdown(stripe_js, unsafe_allow_html=True)
