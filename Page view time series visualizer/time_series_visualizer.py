import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters() # To plot data with dates as indexes

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
# We are using a DateTimeIndex, not the dates as strings

# Get info about the data
if __name__ == "__main__":
    print("number of dates = ",df.size)
    print(df.head())
    df.info()
    
    
# Clean data (remove 2.5% top and bottom, considered outliers)
Filter = (df["value"]>df["value"].quantile(0.025)) & (df["value"]<df["value"].quantile(0.975))
df = df.loc[Filter]

# Get info about the data
if __name__ == "__main__":
    print("number of samples after cleaning = ", df.size)
    
    
def draw_line_plot():
    # Draw line plot

    fig , ax = plt.subplots(figsize=(20,10))

    ax.plot(df["value"], "r-")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    
       
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

if __name__ == "__main__":
    draw_line_plot()
    
    
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy() # Copy the original dataFrame
    df_bar.reset_index(inplace=True) # We use numbers as index, and date as a column
    
    # Create year and month columns to group
    df_bar['year'] = df_bar["date"].dt.year
    # df_bar['month'] = [d.month for d in df_bar.date] # This needs legend = "full" and change the labels of the legend
    df_bar['month'] = df_bar["date"].dt.strftime("%B") # Saves months with the full name
    
    # Group by year and month, calculate average daily page views
    df_bar = df_bar.groupby(by = ['year', 'month'])['value'].mean().reset_index()
    # If we do not reset the index we receive a serie, not a dataframe
    
    if __name__ == "__main__":
        print("df_bar : ", df_bar)
        
        
    # Month names for legend and the order
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    # Create the plot with seaborn
    fig, ax = plt.subplots(figsize=(12, 6))
    # sns.barplot(data=df_bar, x='year', y='value', 
                    #  hue='month', legend="full", palette= "rainbow", ax=ax) # This creates extra rectangles which make the test fails
    
    sns.barplot(data=df_bar, x='year', y='value', hue='month', hue_order=month_names, palette= "rainbow", ax = ax)
    
    # handles, _ = ax.get_legend_handles_labels() # We need the original handles to keep the colors
    # ax.legend(handles, month_names, title='Months', loc='upper left') # Needed when we manage months the other way
    ax.legend(title='Months')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

if __name__ == "__main__":
    draw_bar_plot()
    
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (axYear, axMonth) = plt.subplots(1,2, figsize = (20,10))

    sns.boxplot(data= df_box, x = "year", y="value", ax=axYear, palette="flare")
    axYear.set_xlabel("Year")
    axYear.set_ylabel("Page Views")
    axYear.set_title("Year-wise Box Plot (Trend)")
    
    Month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
                   "Nov", "Dec"]
    sns.boxplot(data= df_box, x = "month", y="value", ax = axMonth, palette="bright", order=Month_order)
    axMonth.set_xlabel("Month")
    axMonth.set_ylabel("Page Views")
    axMonth.set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

if __name__ == "__main__":
    draw_box_plot()