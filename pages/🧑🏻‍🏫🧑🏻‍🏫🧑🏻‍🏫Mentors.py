import streamlit as st
import pandas as pd

# Sample data of software engineers and their mentorship sessions
data = {
    'Name': ['Ramesh Kumar', 'Priya Gupta', 'Amit Patel'],
    'Company': ['Google', 'Facebook', 'Amazon'],
    'Expertise': ['Machine Learning', 'Web Development', 'Cloud Computing'],
    'Bio': ['Ramesh Kumar is a senior software engineer at Google with expertise in Machine Learning.',
            'Priya Gupta is a software engineer at Facebook specializing in Web Development.',
            'Amit Patel works at Amazon and has extensive experience in Cloud Computing.'],
    'Mentorship_Session': ['Available on Mondays and Wednesdays.',
                           'Available on Tuesdays and Thursdays.',
                           'Available on Fridays and Saturdays.'],
    'Hourly_Charges_INR': ['₹500/hour', '₹400/hour', '₹600/hour']
}

df = pd.DataFrame(data)

# Streamlit page layout
st.title('Software Engineer Mentorship Profiles')

# Displaying profiles
for idx, row in df.iterrows():
    st.subheader(row['Name'])
    st.write(f"Company: {row['Company']}")
    st.write(f"Expertise: {row['Expertise']}")
    st.write(f"Bio: {row['Bio']}")
    st.write(f"Mentorship Session: {row['Mentorship_Session']}")
    st.write(f"Session Charges: {row['Hourly_Charges_INR']}")
    st.write('---')

    