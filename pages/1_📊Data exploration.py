import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Data exploration",page_icon="📊",layout="wide")
st.subheader("Group 16 - Business IT 2")
st.title("SMOKING ANALYSIS COLLECTION")
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
show_yes = tab2.toggle('Yes', value=True)
show_no = tab2.toggle('No', value=True)

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

###TAB 3: HORIZONTAL CHART
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
tab3.plotly_chart(fig)





