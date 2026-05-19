import streamlit as st
from chains.first_aid_chain import get_first_aid_response
from utils.safety import emergency_check

st.set_page_config(page_title="First Aid AI Assistant", page_icon="🩺")

st.title("🩺 First Aid AI Assistant")
st.subheader("Temporary health guidance when doctor is unavailable")

st.warning("This AI gives temporary first-aid guidance only. Always consult a doctor.")

# User Inputs
disease = st.text_input("Enter disease / symptoms (e.g. fever, cough, headache):")
days = st.number_input("How many days symptoms have lasted?", min_value=1, max_value=30, step=1)

if st.button("Get First Aid Advice"):
    if disease:
        # Emergency Safety Check
        emergency_msg = emergency_check(disease)

        if emergency_msg:
            st.error(emergency_msg)
        else:
            with st.spinner("Analyzing symptoms..."):
                response = get_first_aid_response(disease, days)

            st.success("AI Guidance:")
            st.write(response)
    else:
        st.warning("Please enter symptoms first.")