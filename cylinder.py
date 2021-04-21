import streamlit as st
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
#st.set_page_config(layout="wide")

col1, col2= st.beta_columns([55,15])
with col1:
    st.markdown('<h1 style ="color: #ec4646;font-size: 38px;">Analyzing Gas Cylinders Data</h1>', unsafe_allow_html=True)
with col2:
    #st.markdown('<h1 style ="color: #630000;font-size: 40px;">Analyzing Gas Cylinders Data</h1>', unsafe_allow_html=True)
    st.image('gas cylinder.png', width = 70)
header = st.beta_container()
dataset = st.beta_container()
graphs = st.beta_container()

with header:
    st.markdown("<p>This app analyzes the Gas Cylinders Data and layout plots. So here is a list of questions we would like to obtain from the data.<br> Which company's cylinder is being most frequently used? <br> How many people use large cylinders and short cylinders? <br>How many gas cylinders are mostly registered by these people in a month? <br>On which date they've booked the gas cylinders most?<br>Which area has ordered the most cylinders? <br>How many people have used most of the gas from the gas cylinder?</p>",unsafe_allow_html=True)
with dataset:
    st.markdown('<h2> Cylinder Dataset 📊</h2>',unsafe_allow_html = True)
    st.write('Cylinders Dataset comprises of the number of cylinders, Candidate Name, Account ID, Phone Number, Area, Company Name, No of gas registered per user, Gross weight, Purchased date,Amount of gas consumed, Cost. Here, Account Id represents the users account Id. Gross weight represents the weight and amount of the gas in a cylinder, Area represents the address of the people, and declaration represents the status of the cylinder in the sense how many liters of gas has it consumed, which will be added later.')
    cylinders_df = pd.read_csv('Cylinders Dataset.csv')
    st.write(cylinders_df.head(10))

with graphs:
    st.markdown('<h2>Here are some bar plots which are plotted based on the available data 📈</h2>',unsafe_allow_html = True)

    st.write("Let's start with the first question, Which company's cylinder is being most frequently used? This bar chart shows that the HP named company's gas cylinders are mostly used by the people. And next Bharat named company's gas cylinder are mostly used by the people. The graph is plotted between the Company name on the x-axis and count values on the y-axis.")
    company = pd.DataFrame(cylinders_df['Company Name'].value_counts())
    st.bar_chart(company)

    st.write("Let's see the outcome of the next question, So there are nearly hundered people who are using the large cylinders weighted around 29.5 KG and there are only twenty people who use the short gas cylinder weighted around 14.4 KG. This graph is plotted between Gross weight and count values. Here is the glimpse of the graph.")
    weight = pd.DataFrame(cylinders_df['Gross Weight'].value_counts())
    st.bar_chart(weight)

    st.write("Let's go with the third question. Around 52 people have booked three gas bottles most of the time within a month. 33 people have booked two gas cylinders within a month. 19 people have booked four gas bottles within the month and 13 people have booked one gas bottles within the month. Here is the glimpse of the graph")
    register = pd.DataFrame(cylinders_df['No. of Cylinders registered per user'].value_counts())
    st.bar_chart(register)

    st.write("Let's go with the fourth question. On this date, 15-12-20, about eight people have booked more gas cylinders.")
    date = pd.DataFrame(cylinders_df['Purchased Date'].value_counts())
    st.bar_chart(date)

    st.write("Let's go with the next question, People from Bapatla has ordered the most gas cylinders and people from Inturu has ordered the least cylinder. This bar chart is plotted between Area and count values on the x-axis and y-axis.")
    area = pd.DataFrame(cylinders_df['Area'].value_counts())
    st.bar_chart(area)

    st.write("Let's go with the last question, Around ten people have used most of the gas from the cylinder. This bar chart is plotted between Amount of gas consumed (Kg) on the x-axis and count values on the y-axis. Here is the glimpse of the graph")
gas_used = pd.DataFrame(cylinders_df['Amount of gas consumed (Kg)'].value_counts())
st.bar_chart(gas_used)
st.write("So, here we are adding a new column called Declaration which represents the status of the cylinder in the sense how many litres of gas has it consumed. If the gas in the cylinder is above 20 KG then it'll update it as a 'Full'. If the gas in the cylinder is below 5 then it'll update it as an 'Almost Complete'. If the above statements are not satisfied with the condition, then it will update it as 'In Use'.")
def declaration(amount_consumed):
    Gas_Used = amount_consumed
    if Gas_Used > 20:
        return 'Full'

    elif Gas_Used < 5:
        return 'Almost Complete'
    else:
        return 'In Use'
st.write('The final dataset after adding up the new column.')
cylinders_df['Declaration'] = cylinders_df['Amount of gas consumed (Kg)'].apply(declaration)
cylinders_df[0:6]
agree = st.checkbox("Bar Plot")
if agree:
    st.write('So from this plot, we can say that there are around 32 people whose gas in their cylinders are about to complete, nearly 72 people are using it and 12 people whose cylinders are full. This bar chart is plotted between Declaration and count values. Here is the glimpse of the graph')
    status = pd.DataFrame(cylinders_df['Declaration'].value_counts())
    st.bar_chart(status)
agree = st.checkbox("Pie Chart")
if agree:
    st.write('Here, the circular diagram shows that people use HP gas bottles more than any other.')
    pie_chart = px.pie(cylinders_df, values = 'No. of Cylinders registered per user', names = 'Company Name', title = 'Pie Chart')
    st.plotly_chart(pie_chart)
