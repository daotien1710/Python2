import streamlit as st
import streamlit_lottie as lottie
import pandas as pd
from streamlit_extras.let_it_rain import rain
import plotly as pl
from streamlit_extras.stoggle import stoggle
# Set the page configuration
st.set_page_config(page_title = "Project Python 2", page_icon = "💫", layout="wide")

st.subheader("Group 16 - Business IT 2")
st.title("HI! WELCOME TO OUR DATASET :wave:")
st.write("We are a group of business students who are interested in the UK resident' smoking habits. Therefore, we decided to analyze a set of data about the smoking fluctuation in the UK between male and female smokers across different areas, such as age, region, etc. Through this visualization, we hope to bring a clear vision to people about which region has the largest of smokers and which type of cigarettes is the most favourable.")

rain(
    emoji="✨",
    font_size=40,
    falling_speed=5,
    animation_length="3",
)

stoggle("Group information",
    """
    \n 1. Dao Thi Cam Tien - 10323034
    \n 2. Le Diem My - 10323054
    \n 3. Pham Phuong Thao - 10323031
    \n 4. Nguyen Quang Linh - 10323013""",
)

st.markdown("---")
def colored_header(label, color):
    html_str = f"""
    <div style='background-color:{color};padding:10px;border-radius:10px'>
        <h2 style='color:white;text-align:center;'>{label}</h2>
    </div>
    """
    st.markdown(html_str, unsafe_allow_html=True)

colored_header("Let's get to know about our dataset", "pink")

cl1, cl2 = st.columns(2)
with cl1:
    st.write("**Our goal:** To display our study and findings, we use several types of graphs, including line graphs, bar graphs, and violins. We expect that by using these visualizations, we will be able to provide the most thorough illustration possible from such a large data collection.")
with cl2:
    st.lottie("https://lottie.host/0235bc61-e7ca-4bd4-ae2e-259cbbf9c968/E3SPWwFEQu.json", height=400, width=400, key="data")

st.write("**Our data set:** Our data collection includes Gender, Age, Marital Status with Levels, Highest Education Levels, Nationality, Ethinicity, Gross Income, Regions, Smoking Status, Numbers of Cigarettes Smoked per Week and per Day, Type of Cigarettes Smoked with Levels.")
st.header(":blue[**Dataset' variables introduction**] ✨")
st.caption(' Here are 12 variables with detailed descriptions below 👇')
st.markdown("1. :blue[**gender:**] Female and Male")
st.markdown("2. :blue[**age:**] Age varies from 16 to 97")
st.markdown("3. :blue[**marital_status:**] Highest education level with levels A Levels, Degree, GCSE/CSE, GCSE/O Level, Higher/Sub Degree, No Qualification, ONC/BTEC and Other/Sub Degree")
st.markdown("4. :blue[**highest_qualification:**] Highest education level with levels A Levels, Degree, GCSE/CSE, GCSE/O Level, Higher/Sub Degree, No Qualification, ONC/BTEC and Other/Sub Degree")
st.markdown("5. :blue[**nationality:**] Nationality with levels British, English, Irish, Scottish, Welsh, Other, Refused and Unknown")
st.markdown("6. :blue[**ethnicity:**] Ethnicity with levels Asian, Black, Chinese, Mixed, White, Refused and Unknown")
st.markdown("7. :blue[**gross_income:**] Income with levels Under 2,600, 2,600 to 5,200, 5,200 to 10,400, 10,400 to 15,600, 15,600 to 20,800 to 28,600, 28,600 to 36,400, above 36,400, Refused and Unknown")
st.markdown("8. :blue[**region:**] Region with levels London, Midlands And East Anglia, Scotland, South East, South West, The North and Wales")
st.markdown("9. :blue[**smoke:**] Smoking status with levels No and Yes")
st.markdown("10. :blue[**amt_weekends:**] Number of cigarettes smoked per day on weekends")
st.markdown("11. :blue[**amt_weekdays:**] Number of cigarettes smoked per day on weekdays")
st.markdown("12. :blue[**type:**] Type of cigarettes smoked with levels Packets, Hand-Rolled, Both/Mainly Packets and Both/Mainly Hand-Rolled")

st.markdown("---")

st.header("Data Frame📈")

st.write("[> Accessing our original dataset <](https://www.kaggle.com/code/tanshihjen/eda-statistical-analysis-smoking-dataset-from-uk)")
st.caption("Or you can view the dataset here:")

df = pd.read_csv('C:/Users/asus/Downloads/smoking(1).csv')

st.dataframe(df)
