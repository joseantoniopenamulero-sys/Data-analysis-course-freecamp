import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1: import data

df = pd.read_csv("medical_examination.csv")


# 2: add overweight (categorical column)
df['overweight'] = (df["weight"]/(df["height"]/100)**2 >25).astype(int) # Height in meters instead of cm and data is binary (not boolean)


# 3: Normalize data for cholesterol and glucose

df["cholesterol"] = (df["cholesterol"]>1).astype(int)
df["gluc"] = (df["gluc"]>1).astype(int)


# 4: draw categorical plot function
def draw_cat_plot():
    # 5: create df_cat
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    # print("df_cat: \n", df_cat)

    # 6: group data
    df_cat = df_cat.groupby(by=["cardio", "variable", "value"], as_index=False).size() # size is supposed to work better than .count and .value_counts for groups
    # If as_index = True, returns a serie (a column). We want for columns for the plot
    # print("df_cat grouped: \n", df_cat)


    # 7: rename for catplot
    df_cat = df_cat.rename(columns={"size": "total"})
    # print("df_cat renamed: \n", df_cat)

    # 8: catplot
    fig = sns.catplot(data=df_cat, x = "variable", y="total", hue = "value", col = "cardio", kind="bar") # hue and col mean to separate vars in the values of hue from column col


    # 9
    fig.savefig('catplot.png')
    # print("Imagen guardada")
    return fig


# 10
def draw_heat_map():
    # 11: Filter data
    # 1) Diastolic press lower than systolic
    # 2) Height and Weight more than 2.5th quantile and less than 97.5th quantile
    
    filter = (df["ap_lo"]<df["ap_hi"]) & (df["height"]>df["height"].quantile(0.025)) & \
        (df["height"]<df["height"].quantile(0.975))& (df["weight"]>df["weight"].quantile(0.025)) & \
            (df["weight"]<df["weight"].quantile(0.975)) 
            
    df_heat = df[filter]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool)) # Create matrix of True values with the shape of corr. Then take the upper triangular matrix



    # 14
    fig, ax = plt.subplots(figsize=(15, 10))

    # 15
    sns.heatmap(
        data=corr,
        annot= True,
        mask=mask,
        fmt='.1f' # To avoid problems with the test (it fails in 3 values bc of a lack of precision rounding)
    )

    # 16
    fig.savefig('heatmap.png')
    return fig
