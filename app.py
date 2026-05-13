import streamlit as st
import pickle
import numpy as np
import warnings
import base64

warnings.filterwarnings("ignore", category=UserWarning)

#function to set background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call function (replace 'background.jpg' with your file name)
add_bg_from_local(r"C:\Users\GIBSON\Desktop\Air_Pollution\preview.jpg")

# Sidebar message
st.sidebar.title("About Air Quality 🌍")
st.sidebar.write("""
Air quality is a key factor for a healthier environment and human well-being.  

- Clean air reduces the risk of **respiratory diseases**.  
- Lower pollution levels support **ecosystem balance**.  
- Common factors that affect air quality:  
  *Temperature, Humidity, Industrial Emissions, Vehicle Exhaust, and Population Density.*  
- Monitoring air quality helps us take **steps toward a safer and greener future**. 🌱
""")



# Load the saved model
with open("best_model.pkl", "rb") as f:             #'rb'-read binary/'f'-an variable
    model = pickle.load(f)
    
with open("encoder.pkl","rb") as f1:
    encoder=pickle.load(f1)
    
# Title
st.markdown(
    "<h1 style='color:#006400;'>My Machine Learning App</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:green; font-style:italic; font-size:16px;'>🌱 “Clean air, healthy life. Let's protect our environment!”</p>",
    unsafe_allow_html=True)


# Stronger CSS override for labels
st.markdown(
    """
    <style>
    /* General label style override */
    label {
        color: #333333 !important;   /* dark grey */
        font-weight: bold !important;       #super bold
        font-size: 18px !important;         
        letter-spacing: 0.5px ! important;  #adds spacing for strong effect
    }
    </style>
    """,
    unsafe_allow_html=True
)

#to hide "apply to enter"
st.markdown("""
    <style>
    div[data-testid="InputInstructions"] { visibility: hidden; }        
    </style>
""", unsafe_allow_html=True)





# INPUT FIELDS (Text boxes only) 
def get_number(label):
    return st.number_input(label, value=0.0)


feature1 = get_number("Temperature")        #get_number
feature2 = get_number("Humidity")
feature3 = get_number("PM2.5")
feature4 = get_number("PM10")
feature5 = get_number("NO2")
feature6 = get_number("SO2")
feature7 = get_number("CO2")
feature8 = get_number("Proximity to Industrial Areas")
feature9 = get_number("Population Density")



# Prepare input
user_input = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9]])

# Predict button
if st.button("Predict"):                        #will create a button in streamlit app with label 'predict'
    prediction = model.predict(user_input)      #when click the button the code inside the block runs
    label=encoder.inverse_transform(prediction)[0]
    st.write(f"Prediction: {label}")    #Streamlit's universal output function


#color output

    if label.lower() == "good":
        st.success("✅ Air Quality is GOOD")
    elif label.lower() == "moderate":
        st.warning("⚠️ Air Quality is MODERATE")
    elif label.lower() == "poor":
        st.markdown("<div style='color:orange; font-weight:bold; font-size:20px;'>🟠 Air Quality is POOR</div>", unsafe_allow_html=True)
    elif label.lower() == "hazardous":
        st.error("☠️ Air Quality is HAZARDOUS")