import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["temp"].to_list()

def random_set_of_mean(counter):
    dataset=[]
    

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()


def setup():
    mean_list=[]
    
    

setup()
