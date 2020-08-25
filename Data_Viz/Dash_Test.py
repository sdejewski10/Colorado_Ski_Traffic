#APP SETUP
import pandas as pd 
import plotly.express as px

import dash
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#-------------------------------------------------------
#IMPORT DATA

df = pd.read_csv("CDOT_Ski_Data_V2.csv")


#------------------------
#App Layout

app.layout = html.Div([

    html.H1("Colorado Ski Traffic", style = {'text-align':'center'})

    dcc.Dropdown(id ="Select_Direction",
    options = [
    {"Label":"Westbound","Value":"P"},
    {"Label":"Eastbound","Value":"S"}]
    multi = False,
    
    )