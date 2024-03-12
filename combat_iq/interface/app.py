import streamlit as st
import pandas as pd
import requests

# URL of  FastAPI endpoint
api_url = "http://localhost:8000/predict"

# Load the CSV file
@st.cache
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

# Load the data
data = load_data('/Users/tn/code/git-cguinel/ufc_combatiq/website/data.csv')

# Concatenate the two columns containing fighter names
all_fighters = pd.concat([data['R_fighter'], data['B_fighter']])

# Remove any duplicate names
fighters_list = sorted(all_fighters.drop_duplicates().tolist())


st.markdown("<h1 style='text-align: center; color: white;'>UFC Match Winner Prediction</h1>", unsafe_allow_html=True)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



col1, col2 = st.columns(2, gap = "large")
with col1:
    red_fighter = st.selectbox("Select Fighter for the red corner", fighters_list)
    #st.write("age:")
    #st.write("weigth:")
    #st.write("height")
    #st.write("fight records:")


with col2:
#fighter2 = st.selectbox(":red[Select Fighter 2]", fighters_list)
    blue_fighter =st.selectbox("Select Fighter for the blue corner", fighters_list)
    #st.write("age:")
    #st.write("weigth:")
    #st.write("height")
    #st.write("fight records:")


# Your prediction code goes here
if st.button("Predict Winner"):
    # Make a request to the FastAPI endpoint
    response = requests.get(api_url, params={"red_fighter": red_fighter, "blue_fighter": blue_fighter})

    # Check if the request was successful
    if response.status_code == 200:
        prediction_data = response.json()
        fight_outcome = prediction_data['fight_outcome']
        win_rate = prediction_data['win_rate']
        st.write(f"The predicted winner is: {fight_outcome}")
        st.write(f"Win rate: {win_rate}")
    else:
        st.write("Failed to get prediction from the API")

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://media.contentapi.ea.com/content/dam/ufc/images/2017/10/easufc3-overview-championshipfighters.jpg.adapt.crop191x100.628p.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)
