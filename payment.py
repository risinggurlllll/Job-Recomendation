import streamlit as st

def payment_page():
    st.title("Payment Page")

    # Gather payment information
    card_number = st.text_input("Card Number")
    expiration_date = st.text_input("Expiration Date (MM/YYYY)")
    cvv = st.text_input("CVV/CVC")
    amount = st.number_input("Amount")

    # Payment button
    if st.button("Pay Now"):
        # Validate input
        if card_number and expiration_date and cvv and amount:
            st.success(f"Payment Successful! Amount paid: ${amount}")
        else:
            st.error("Please fill in all payment details.")

if __name__ == "__main__":
    payment_page()

# Payment page
if 'selected_bootcamp' in st.session_state:
    st.title("Payment Page")

    # Display selected bootcamp details
    selected_bootcamp = st.session_state['selected_bootcamp']
    st.write(f"Bootcamp: {selected_bootcamp['Bootcamp']}")
    st.write(f"Price: {selected_bootcamp['Price']}")

    # Gather payment information
    card_number = st.text_input("Card Number")
    expiration_date = st.text_input("Expiration Date (MM/YYYY)")
    cvv = st.text_input("CVV/CVC")
    amount = float(selected_bootcamp['Price'].replace('$', ''))  # Convert price to float

    # Payment button
    if st.button("Pay Now"):
        # Validate input
        if card_number and expiration_date and cvv:
            st.success(f"Payment Successful! Amount paid: ${amount}")
        else:
            st.error("Please fill in all payment details.")