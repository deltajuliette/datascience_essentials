import streamlit as st
import utils

########## Title for the Web App ##########
st.title("🏠 House Price Prediction")

########## Create some Streamlit Number Input fields ##########
# https://docs.streamlit.io/library/api-reference/widgets/st.number_input
OverallQual = st.number_input("⭐ Overall House Quality", min_value=0, max_value=10, value=9, step=1)

FullBath = st.number_input("🛁 Number of Full Bathrooms", min_value=0, max_value=10, value=2)

GarageArea = st.number_input("🚗 Garage Area", min_value=0, max_value=10_000, value=500)

LotArea = st.number_input("🏡 Lot Area", min_value=0, max_value=10_000, value=2_000)


########## Use a Streamlit Button to trigger the API call ##########
# https://docs.streamlit.io/library/api-reference/widgets/st.button
if st.button("Predict House Price"):
    # All the code inside this if condition will get executed when we click on the button on the frontend
    # Get the predicted price by passing all the parameters to the API
    predicted_price = utils.pred_price(OverallQual, FullBath, GarageArea, LotArea)
    
    # Write out the result to the frontend
    st.write(f"Predicted Price is $ {predicted_price}")

    
########## Use a Streamlit Buttons to trigger other routes API call ##########
if st.button("Print Hello World!"):   
    st.write(utils.hello_world())
    
if st.button("Hardcoded HTML Page"):   
    # To render the HTML page on streamlit
    # st.write(utils.html_page())
    st.markdown(utils.html_page(), unsafe_allow_html=True)