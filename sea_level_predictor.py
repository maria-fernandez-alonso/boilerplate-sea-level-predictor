import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color='blue')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(df['Year'].min(), 2051)
    y = slope * x + intercept

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = range(2000, 2051)
    y_2000 = slope_2000 * x_2000 + intercept_2000

    # Add labels and title
    ax.plot(x, y, color='red', label='Best Fit Line')
    ax.plot(x_2000, y_2000, color='green', label='Best Fit Line after 2000')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()