import plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
import streamlit as st
import warnings
from plot import record
warnings.filterwarnings("ignore")

#configure the app
st.set_page_config(
    page_title="stackoverflow_EDA",
    page_icon="📊",
    layout="wide"
    )
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html= True)
st.title('stackoverflow developer survey 2023\n (skilharvest 2.0 project)')
st.markdown(":arrow_upper_left: Go to next page")

#importing data and caching it to minimize loading time
@st.cache_data
def read():
    df= pd.read_csv(r"C:\Users\anibr\Desktop\skillharvest\final\survey_results_public_EDA.csv")
    d = df.fillna('none')
    #processing and eliminating columns with more than 40 none
    filter = []
    for i in d.index:
        p = (d.iloc[i,:]=='none').value_counts()[True]
        #The line above returns the number of columns which has 'none' for each row to p 
        #p is tested against 40, and if over 40, its index is saved to filter
        if p >40:
            filter.append(i)
    return d.drop(filter).reset_index(drop =True)
data = read()

st.sidebar.title("Analysis page selection")
#creating pages for my app
page=st.sidebar.radio("select page", ['basic_information','tech_tools','ai_tools',
                                      'stack_overflow','more_ai','others','Group by',"About Us"])


if page =='basic_information':
    st.subheader('welcome to basic information chart page')
    select = st.selectbox('choose a column',record[2:20])
    if select:       
        graph,label,pie = plot.plotter(data[select])
        if pie !='none':
            option =st.radio('change chart',['bar','pie'])
            match option:
                case 'bar':
                    st.plotly_chart(graph)
                case 'pie':
                    st.plotly_chart(pie)
        else:
            st.plotly_chart(graph)
        st.markdown('Label definition')
        container = st.container(border=True,height=200)
        with container:
            st.write("N/E: if 'none': The participant did not input or choose any of the options")
            for i in label:
                st.write(label[i],":",i)

if page =='tech_tools':
    st.subheader('welcome to tech_tools chart page')
    select = st.selectbox('choose a column',record[21:41])
    if select:       
        graph,label,pie = plot.plotter(data[select])
        if pie !='none':
            option =st.radio('change chart',['bar','pie'])
            match option:
                case 'bar':
                    st.plotly_chart(graph)
                case 'pie':
                    st.plotly_chart(pie)
        else:
            st.plotly_chart(graph)
        st.markdown('Label definition')
        container = st.container(border=True,height=200)
        with container:
            st.write("N/E: if 'none': The participant did not input or choose any of the options")
            for i in label:
                st.write(label[i],":",i)
        

if page =='ai_tools':
    st.subheader('welcome to ai_tools chart page')
    select = st.selectbox('choose a column',record[41:45])
    if select:       
        graph,label,pie = plot.plotter(data[select])
        if pie !='none':
            option =st.radio('change chart',['bar','pie'])
            match option:
                case 'bar':
                    st.plotly_chart(graph)
                case 'pie':
                    st.plotly_chart(pie)
        else:
            st.plotly_chart(graph)
        st.markdown('Label definition')
        container = st.container(border=True,height=200)
        with container:
            st.write("N/E: if 'none': The participant did not input or choose any of the options")
            for i in label:
                st.write(label[i],":",i)

if page =='stack_overflow':
    st.subheader('welcome to stack_overflow details chart page')
    select = st.selectbox('choose a column',record[45:51])
    if select:       
        graph,label,pie = plot.plotter(data[select])
        if pie !='none':
            option =st.radio('change chart',['bar','pie'])
            match option:
                case 'bar':
                    st.plotly_chart(graph)
                case 'pie':
                    st.plotly_chart(pie)
        else:
            st.plotly_chart(graph)
        st.markdown('Label definition')
        container = st.container(border=True,height=200)
        with container:
            st.write("N/E: if 'none': The participant did not input or choose any of the options")
            for i in label:
                st.write(label[i],":",i)

if page =='more_ai':
    st.subheader('welcome to more_ai_tool chart page')
    select = st.selectbox('choose a column',record[51:63])
    if select:       
        graph,label, pie = plot.plotter(data[select])
        if pie !='none':
            option =st.radio('change chart',['bar','pie'])
            match option:
                case 'bar':
                    st.plotly_chart(graph)
                case 'pie':
                    st.plotly_chart(pie)
        else:
            st.plotly_chart(graph)
        st.markdown('Label definition')
        container = st.container(border=True,height=200)
        with container:
            st.write("N/E: if 'none': The participant did not input or choose any of the options")
            for i in label:
                st.write(label[i],":",i)

if page =='others':
    st.subheader('welcome to others chart page')
    select = st.selectbox('choose a column',record[63:83])
    #'ConvertedCompYearly' eliminated because of errors in the entry 
    #it's suppossed to be number 84 the compTotal was also eliminated
    #see basic_information section of the original data
    if select:
        if select == 'WorkExp':
            graph,label = plot.plotline(data[select])
            st.plotly_chart(graph)
        else:     
            graph,label,pie = plot.plotter(data[select])
            if pie !='none':
                option =st.radio('change chart',['bar','pie'])
                match option:
                    case 'bar':
                        st.plotly_chart(graph)
                    case 'pie':
                        st.plotly_chart(pie)
            else:
                st.plotly_chart(graph)
            st.markdown('Label definition')
            container = st.container(border=True,height=200)
            with container:
                st.write("N/E: if 'none': The participant did not input or choose any of the options")
                for i in label:
                    st.write(label[i],":",i)


if page =='Group by':
    st.subheader('welcome to Group-by page')
    expander = st.expander('you can only group two columns')
    with expander:
        choice1,choice2 = 'Age', 'Employment'
        choice1,choice2 = expander.multiselect('choose two columns from the list',plot.no_float)
        check=st.button('display')
    if check:
        group = data.groupby(choice1)[choice2].value_counts()
        st.dataframe(pd.DataFrame(group),width=1000)


if page =='About Us':
    st.subheader('welcome to About Us page')
    tab1,tab2=st.tabs(['Developers','Send us a message'])
    with tab1:
        container =st.container(border =True)
        container.markdown(
            '''This project was developed by **Aniekan Udo**, alongside **Theophilus** and **Umar**, for group 8 at skilharvest 2.0.
            It is a dashboard for EDA done for stackoverflow survey data.
            The original data is made of 84 columns and over 80,000 entry. The processed data has 71,029 rows,
            after over 18,000 rows which had over 40 unfilled columns were eliminated.
            Developers who responded gave consent for data usage.
            Please, treat data with ethical responsibility.
            Download processed data which is used in this app with 'Get data' button below\n
            NUll replaced with 'none' in this data
            '''
        )
        st.download_button("Get Data", data = data.to_csv().encode("utf-8"),
                       file_name = "stack_overflow_processed.csv", mime ="text/csv")
    with tab2:
        with st.form("send us a message"):            
            name =st.text_input("Enter your fullname")
            email =st.text_input('Enter your email')
            message=st.text_area('Write your message')
            button = st.form_submit_button('Send')
            if button:
                st.success('submitted')

