import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Look how is the df
    if __name__=="__main__":
        print(df.head())
        print(df.head(-5))
        df.info()
        print(df.describe())
    # Create scatter plot (with matplotlib)
    plt.scatter(x= df["Year"], y= df["CSIRO Adjusted Sea Level"], s= 0.4, color = "blue", marker="o")

    # Create first line of best fit

    years_prediction = range(df["Year"].min(), 2051) # Until 2050 (2051 not included)
    first_fit = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    if __name__=="__main__":
        print("p-value first prediction = ", first_fit.pvalue)
    
    
    first_predict = first_fit.slope * years_prediction + first_fit.intercept
    
    plt.plot(years_prediction, first_predict, "r-")
    
    # Create second line of best fit
    
    
    second_fit = linregress(df.loc[df["Year"]>=2000]["Year"], df.loc[df["Year"]>=2000]["CSIRO Adjusted Sea Level"])

    if __name__=="__main__":
        print("p-value second prediction = ", first_fit.pvalue)
    
    first_year_plot_second_prediction = 2000
    years_second_pred = years_prediction[years_prediction.index(first_year_plot_second_prediction): ] 
    second_predict = second_fit.slope * years_second_pred + second_fit.intercept
    
    plt.plot(years_second_pred, second_predict, "g-")
    
    # Add labels and title

    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    labels= ["Observations", "First Prediction with All the Data", "Second Prediction only since 2000"]
    plt.legend(labels)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__=="__main__":
    draw_plot()