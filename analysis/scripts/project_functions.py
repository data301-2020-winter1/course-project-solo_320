import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(redwine_path, whitewine_path):
 
    #Loaded the data 
    
    df = pd.read_csv(redwine_path, delimiter =";")
    df2 = pd.read_csv(whitewine_path, delimiter =";")
    
    # method chain 1: wrangling red wine data

    redwine = (df
           #Storing the type of red wine as an attribute
           .assign(wine_type = 'red wine') 
           # Create a new column to label quality as a qualitative chracteristic of 'low quality', 'medium quality' and 'high quality'
           .assign(quality_label = df.quality.apply(lambda x: 'low quality' if x <= 5 else 'medium quality' if x<= 7 else 'high quality'))
           #reordering the columns to bring wine_type to the front
           .reindex(columns = ['wine_type', 'citric acid', 'fixed acidity', 'volatile acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'alcohol', 'quality', 'quality_label'])
          )

    # method chain 2: wrangling white wine data

    whitewine = (df2
           #Storing the type of white wine as an attribute
           .assign(wine_type = 'white wine') 
           # Create a new column to label quality as a qualitative chracteristic of 'low quality', 'medium quality' and 'high quality'
           .assign(quality_label = df2.quality.apply(lambda x: 'low quality' if x <= 5 else 'medium quality' if x<= 7 else 'high quality'))
           #reordering the columns to bring wine_type to the front
           .reindex(columns = ['wine_type', 'citric acid', 'fixed acidity', 'volatile acidity', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'alcohol', 'quality', 'quality_label'])
          )

    # method chain 3: Merging both dataframes together for easy analysis
    
    allwines = (pd
            #merge
            .concat([redwine, whitewine], ignore_index = True)
            #re-shuffle the data points
            .sample(frac = 1, random_state = 101)
            .reset_index(drop = True)
            #drop any duplicate rows
            .drop_duplicates()
           )
    # return the latest dataframe

    return allwines

def boxplot1(a, x, y , z):
    boxplot = sns.boxplot(ax = a, 
                data = df, 
            x = x, 
            y = y, 
            hue = z, 
            palette={'red wine': '#ED5CDE', 'white wine': '#09940F'}
           )
    return boxplot



