import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px
import re

# A function to extract individaul choices, including the once enclosed in a string and separated by ;
# Each item is extracted to a list and the list is returned
def column_extract(column):
    listed = column.tolist()
    new=[]
    buffer =[]
    for item in listed:
        if re.search(r'[A-Za-z]+;[A-Za-z]',item):
            buffer=item.split(';')
            new = new+buffer
        else:
            new.append(item)
    return new

#create another function to bring out the unique items witgout including thier count value
#this is achived by converting the list from column extract to a set which does not support repeated items
#it is converted back to a list and returne it
def column_unique(column):
    new = column_extract(column)
    unique_values =set(new)
    unique_values=list(unique_values)
    return unique_values
#create a function to return a table of the content for a columnn with  their count value
def column_count(column):
    count = {}
    new = column_extract(column)
    unique_values = column_unique(column)
    
    for i in unique_values: 
        count[i]= new.count(i)
    return pd.DataFrame(list(count.items()), columns = ['answer','count']).sort_values(by='count',ascending=False)
    #this function returns the unique values sorted by their count in descending order

# A function to handle everything in bar plotting. The function takes in a column name as an argument
# It returns a barplot and mapped label dictionary
# the mapped database is used to create a a bar plot bacuse it allow plotting without covering the page with words
# To create a new compressed database, it calls the column_count function
def plotter(name):
#where name is data[selected_column]
    MB =column_count(name)
#make a copy before enconding
    DB = MB.copy()
    b =list(range(97,123)) + list(range(65,91))
    encode = [chr(i) for i in b]
    index = 0
    ansmap ={}
    # let's specify two groups of plot based on column types. for float we will plot line graph 
    # for string varaibles we will plot barchart
    c =len(MB['count'])
    if c > 30:
        #This field checked for columns that have over 30 unique value and 
        MB = MB.head(30)
        ansmap[c]='Total unique value for this category'
        for i in MB.answer:
            ansmap[i] =encode[index]
            index = index+1
        #ansmap = a dictionary for graph label definition
    
        DB.answer = DB.answer.map(ansmap)
        graph = px.bar(DB, x = "answer", y ="count", color = "answer", title="Top 30 responds",height=300)
        pie ='none'
        return graph,ansmap, pie
    elif c <=10:
        for i in MB.answer:
            ansmap[i] =encode[index]
            index = index+1
            #ansmap = a dictionary for graph label definition
    
        DB.answer = DB.answer.map(ansmap)
        graph = px.bar(DB, x = "answer", y ="count", color = "answer", height=300)
        pie = px.pie(DB, names = "answer", values ="count", color = "answer", height=400)
        return graph,ansmap,pie
    else:
        for i in MB.answer:
            ansmap[i] =encode[index]
            index = index+1
            #ansmap = a dictionary for graph label definition
    
        DB.answer = DB.answer.map(ansmap)
        graph = px.bar(DB, x = "answer", y ="count", color = "answer", height=300)
        pie = 'none'
        return graph,ansmap,pie

#A line graph plotter which returns graph and custom text dictionary
def plotline(name):
    word ={}
    word['check trend'] ='Line graph'
    MB =name[name!="none"].value_counts()
    DB = pd.DataFrame(MB).sort_values(by='WorkExp',ascending=False)
    graph = px.line(DB,y='count',title="work experience in year")
    return graph,word

#let's create a record of our columns to allow us to create drop down menu with it
record = ['ResponseId', 'Q120', 'MainBranch', 'Age', 'Employment', 'RemoteWork',
       'CodingActivities', 'EdLevel', 'LearnCode', 'LearnCodeOnline',
       'LearnCodeCoursesCert', 'YearsCode', 'YearsCodePro', 'DevType',
       'OrgSize', 'PurchaseInfluence', 'TechList', 'BuyNewTool', 'Country',
       'Currency', 'CompTotal', 'LanguageHaveWorkedWith',
       'LanguageWantToWorkWith', 'DatabaseHaveWorkedWith',
       'DatabaseWantToWorkWith', 'PlatformHaveWorkedWith',
       'PlatformWantToWorkWith', 'WebframeHaveWorkedWith',
       'WebframeWantToWorkWith', 'MiscTechHaveWorkedWith',
       'MiscTechWantToWorkWith', 'ToolsTechHaveWorkedWith',
       'ToolsTechWantToWorkWith', 'NEWCollabToolsHaveWorkedWith',
       'NEWCollabToolsWantToWorkWith', 'OpSysPersonal use',
       'OpSysProfessional use', 'OfficeStackAsyncHaveWorkedWith',
       'OfficeStackAsyncWantToWorkWith', 'OfficeStackSyncHaveWorkedWith',
       'OfficeStackSyncWantToWorkWith', 'AISearchHaveWorkedWith',
       'AISearchWantToWorkWith', 'AIDevHaveWorkedWith', 'AIDevWantToWorkWith',
       'NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq', 'SOComm',
       'SOAI', 'AISelect', 'AISent', 'AIAcc', 'AIBen',
       'AIToolInterested in Using', 'AIToolCurrently Using',
       'AIToolNot interested in Using', 'AINextVery different',
       'AINextNeither different nor similar', 'AINextSomewhat similar',
       'AINextVery similar', 'AINextSomewhat different', 'TBranch', 'ICorPM',
       'WorkExp', 'Knowledge_1', 'Knowledge_2', 'Knowledge_3', 'Knowledge_4',
       'Knowledge_5', 'Knowledge_6', 'Knowledge_7', 'Knowledge_8',
       'Frequency_1', 'Frequency_2', 'Frequency_3', 'TimeSearching',
       'TimeAnswering', 'ProfessionalTech', 'Industry', 'SurveyLength',
       'SurveyEase', 'ConvertedCompYearly']

no_float = ['Q120', 'MainBranch', 'Age', 'Employment', 'RemoteWork',
       'CodingActivities', 'EdLevel', 'LearnCode', 'LearnCodeOnline',
       'LearnCodeCoursesCert', 'YearsCode', 'YearsCodePro', 'DevType',
       'OrgSize', 'PurchaseInfluence', 'TechList', 'BuyNewTool', 'Country',
       'Currency', 'LanguageHaveWorkedWith',
       'LanguageWantToWorkWith', 'DatabaseHaveWorkedWith',
       'DatabaseWantToWorkWith', 'PlatformHaveWorkedWith',
       'PlatformWantToWorkWith', 'WebframeHaveWorkedWith',
       'WebframeWantToWorkWith', 'MiscTechHaveWorkedWith',
       'MiscTechWantToWorkWith', 'ToolsTechHaveWorkedWith',
       'ToolsTechWantToWorkWith', 'NEWCollabToolsHaveWorkedWith',
       'NEWCollabToolsWantToWorkWith', 'OpSysPersonal use',
       'OpSysProfessional use', 'OfficeStackAsyncHaveWorkedWith',
       'OfficeStackAsyncWantToWorkWith', 'OfficeStackSyncHaveWorkedWith',
       'OfficeStackSyncWantToWorkWith', 'AISearchHaveWorkedWith',
       'AISearchWantToWorkWith', 'AIDevHaveWorkedWith', 'AIDevWantToWorkWith',
       'NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq', 'SOComm',
       'SOAI', 'AISelect', 'AISent', 'AIAcc', 'AIBen',
       'AIToolInterested in Using', 'AIToolCurrently Using',
       'AIToolNot interested in Using', 'AINextVery different',
       'AINextNeither different nor similar', 'AINextSomewhat similar',
       'AINextVery similar', 'AINextSomewhat different', 'TBranch', 'ICorPM',
       'WorkExp', 'Knowledge_1', 'Knowledge_2', 'Knowledge_3', 'Knowledge_4',
       'Knowledge_5', 'Knowledge_6', 'Knowledge_7', 'Knowledge_8',
       'Frequency_1', 'Frequency_2', 'Frequency_3', 'TimeSearching',
       'TimeAnswering', 'ProfessionalTech', 'Industry', 'SurveyLength',
       'SurveyEase']