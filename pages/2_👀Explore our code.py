import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.stoggle import stoggle

st.set_page_config(page_title="Explore our code", page_icon="📝", layout="wide")
st.subheader("Group 16 - Business IT 2")
st.write(":blue[Interested in how we build up our app?]")
st.title(":rainbow[LET'S EXPLORE OUR CODE BELOW!]")

st.markdown("✧˚ ༘ ⋆｡˚⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡°✩⋆｡⋆༘✧˚")

option = st.selectbox(
    'Which page would you like to learn more about?',
    ('Homepage', '📊 Data exploration'))

st.caption(f"You selected: {option}")
if option == 'Homepage':
    code1 = '''import streamlit as st
import streamlit_lottie as st_lottie
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
'''
    st.code(code1, language='python')

elif option == '📊 Data exploration':
    code2 = '''import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Data exploration", page_icon="📊", layout="wide")
st.subheader("Group 16 - Business IT 2")
st.header("SMOKING ANALYSIS COLLECTION")
st.write("💞 Let's discover our graphs below with us 💞")

data = pd.read_csv('C:/Users/asus/Downloads/smoking(1).csv')

# Initial 2 tabs for each interactive graph
tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Horizontal Chart"])

### TAB 1: LINE CHART
tab1.subheader("👨‍💻Types of cigarettes consumed by various marital status")

# Define color palette for the lines
color1 = ["#19376D", "#66347F", "#FB2576"]

# Filtering the data based on region and type
data1 = data.query("region not in ['Midlands & East Anglia', 'The North', 'Wales'] and type not in ['NA', 'Both/Mainly Hand-Rolled']")

# Grouping the data
data1 = data1.groupby(['marital_status', 'type']).size().reset_index(name='count')

# Create checkboxes for each type of cigarette
packets = tab1.checkbox("Packets", value=True)
hand_rolled = tab1.checkbox("Hand-Rolled", value=True)
both_mainly_packets = tab1.checkbox("Both/Mainly Packets", value=True)

# Filter the DataFrame based on checkbox selections
selected_types = []
if packets:
    selected_types.append("Packets")
if hand_rolled:
    selected_types.append("Hand-Rolled")
if both_mainly_packets:
    selected_types.append("Both/Mainly Packets")

# Apply the filter to the DataFrame
filtered_data1 = data1[data1['type'].isin(selected_types)]

# Create the line plots
g = sns.FacetGrid(filtered_data1, col="type", hue="type", sharey=False, height=5, aspect=1.5, col_wrap=1, legend_out=False)
g.map(sns.lineplot, "marital_status", "count", marker="o")
for ax in g.axes.flat:
    for label in ax.get_xticklabels():
        label.set_horizontalalignment('right')

# Add titles and labels
g.set_axis_labels("Marital status", "Count")
g.set_titles(col_template="{col_name}", row_template="{row_name}")

g.fig.set_figwidth(13)
# Display the plot in Streamlit
tab1.pyplot(g.fig)

### TAB 2: BAR CHART
tab2.subheader("Smoking Status Plot Based on Gross Income in the UK")

# Filter out rows with 'Refused' and 'Unknown' in 'gross_income'
data2 = data[~data['gross_income'].isin(['Refused', 'Unknown'])]

# Filter out rows with null values in 'smoke' column
data2 = data2.dropna(subset=['smoke'])

# Convert 'gross_income' to a categorical type with the specified order
income_order = ["Under 2,600", "2,600 to 5,200", "5,200 to 10,400", "10,400 to 15,600",
                "15,600 to 20,800", "20,800 to 28,600", "28,600 to 36,400", "Above 36,400"]
data2['gross_income'] = pd.Categorical(data2['gross_income'], categories=income_order, ordered=True)


# Gross Income select box
income_options = ['All'] + income_order
selected_income = tab2.selectbox('Select Gross Income:', income_options)

# Smoking status checkboxes
show_yes = tab2.checkbox('Yes', value=True)
show_no = tab2.checkbox('No', value=True)

# Filter data based on user input
filtered_data = data2.copy()
if selected_income != 'All':
    filtered_data = filtered_data[filtered_data['gross_income'] == selected_income]

if not show_yes:
    filtered_data = filtered_data[filtered_data['smoke'] != 'Yes']

if not show_no:
    filtered_data = filtered_data[filtered_data['smoke'] != 'No']

# Create the plot
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=filtered_data, x='smoke', hue='gross_income', palette='Set2')

# Add counts on each bar
for p in ax.patches:
    height = int(p.get_height())
    if height != 0:  # Check if height is not zero
        ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

# Add labels and title
plt.xlabel('Smoking status', fontsize=12)
plt.ylabel('Number', fontsize=12)

# Conditionally add the legend
if selected_income == 'All':
    plt.legend(title='Gross income', title_fontsize='13', fontsize='11')
else:
    ax.legend_.remove()  # Remove the legend if not 'All'

# Center the plot title
plt.gca().title.set_position([.5, 1.05])

# Display the plot in Streamlit
tab2.pyplot(plt)

### TAB 3: HORIZONTAL CHART
tab3.subheader("Weekly Cigarette Consumption by Education Levels")
# Ensure 'amt_weekends' is positive
data['amt_weekends'] = data['amt_weekends'].abs()

# Drop rows with NaN values in 'amt_weekends' column
data3 = data.dropna(subset=['amt_weekends'])

# Separate data for females and males
female_data = data3[data3['gender'] == 'Female'].sort_values(by='amt_weekends', ascending=False)
male_data = data3[data3['gender'] == 'Male'].sort_values(by='amt_weekends', ascending=False)

# Multiselect to choose qualifications
all_qualifications = sorted(data3['highest_qualification'].unique())
selected_qualifications = tab3.multiselect('Select Qualifications to display:', options=all_qualifications, default=all_qualifications[:3])

# Filter the data to display selected qualifications for both genders
filtered_female_data = female_data[female_data['highest_qualification'].isin(selected_qualifications)]
filtered_male_data = male_data[male_data['highest_qualification'].isin(selected_qualifications)]

# Create the plot
fig = go.Figure()

# Add male bars (negative values for left side)
fig.add_trace(go.Bar(
    y=filtered_male_data['highest_qualification'],
    x=-filtered_male_data['amt_weekends'],
    orientation='h',
    name='Male',
    marker=dict(color='#AB82FF'),
    hovertemplate=None
))

# Add female bars (positive values for right side)
fig.add_trace(go.Bar(
    y=filtered_female_data['highest_qualification'],
    x=filtered_female_data['amt_weekends'],
    orientation='h',
    name='Female',
    marker=dict(color='#CD1076'),
    hovertemplate=None
))
# Customize the layout to display absolute values on x-axis
max_amt_weekends = int(max(data3['amt_weekends']))  # Convert to integer
tickvals = [i for i in range(-max_amt_weekends, max_amt_weekends + 1, 10)]
ticktext = [str(abs(i)) for i in tickvals]

fig.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=tickvals,
        ticktext=ticktext,
        title='Cigarettes per Week'
    ),
    yaxis=dict(
        title='Qualifications'
    ),
    barmode='overlay',
    bargap=0.2,
    bargroupgap=0.1,
    legend=dict(title='Gender'),
    width=1100,
    height=550 
)
# Display the plot in Streamlit
tab3.plotly_chart(fig)'''

    st.code(code2, language='python')

