import streamlit as st
import pandas as pd

# Sample data for bootcamps
data = {
    'Bootcamp': ['Data Science Bootcamp', 'AI Bootcamp', 'Web Development Bootcamp'],
    'Provider': ['Rekha Chauhan(5 star rating)', 'Raj Shikri(4.5 star rating)', 'Bhanu Yadav(4 star rating)'],
    'Duration': ['8 weeks', '12 weeks', '6 weeks'],
    'Description': ['An intensive course covering data analysis, machine learning, and data visualization.',
                    'Learn the fundamentals of artificial intelligence and neural networks.',
                    'Master web development skills with HTML, CSS, and JavaScript.'],
    'Price': ['INR3000', 'INR3500', 'Free']
}

df = pd.DataFrame(data)

# Streamlit page layout
st.title('Bootcamp Details')

# Displaying bootcamp details
for idx, row in df.iterrows():
    st.subheader(row['Bootcamp'])
    st.write(f"Provider: {row['Provider']}")
    st.write(f"Duration: {row['Duration']}")
    st.write(f"Description: {row['Description']}")
    st.write(f"Price: {row['Price']}")
    
    # Booking button
    if row['Price'] != 'Free':  # Display button only for paid bootcamps
        booking_button = st.button(f"Book {row['Bootcamp']}")  # Button text includes bootcamp name
        if booking_button:
            st.write(f"You have booked the {row['Bootcamp']} bootcamp!")
    
    st.write('---')
    
if row['Price'] != 'Free':  # Display button only for paid bootcamps
        if st.button(f"Book {row['Bootcamp']}"):  # Button text includes bootcamp name
            st.session_state['current_page'] = 'payment'  # Switch to payment page

st.write('---')

# Payment page
if st.session_state.get('current_page') == 'payment':
    st.title("Payment Page")    