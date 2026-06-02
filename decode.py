# import pandas to handle the reading of the Google Doc
# import numpy to handle the plotting of the grid of characters
# import BeautifulSoup to handle parsing of HTML 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Define function to fetch the Google Doc and return a DataFrame of the data
# Set the parser to (flavor) to Beautiful Soup 4 to render the unicode chars.
# Set the header to 0 via the header param to set the column name to the first row in the table. 
# Finally as the data is in a table the DataFrame needs to be assigned to the target table
def fetch_google_doc(google_doc):
    table = pd.read_html(google_doc, flavor = 'bs4', header=0)
    df = table[0] # as there is only one table in the doc
    return df

# Define function to plot the characters on a grid using numpy
def plot_char(x_cord:list, y_cord:list, char:list):
    max_x = max(x_cord)
    max_y = max(y_cord)
    grid = np.full((max_y+1, max_x+1), ' ') # need to add 1 to the max to ensure that the index from the list is converted to the correct dimensions
    for i in range(len(x_cord)):
        grid[y_cord[i]][x_cord[i]] = char[i]
    grid_2 = []
    for i in range(len(grid)-1, -1 , -1):
        grid_2.append(grid[i])
    for row in grid_2:
        print(''.join(row))


google_doc = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'

# Call the Google Doc via call to the fetch function
google_doc_df = fetch_google_doc(google_doc)

# define variables for the plot function (x_cord, y_cord, char) as 
# lists of values from the DataFrame columns
x_cord = [int(i) for i in list(google_doc_df['x-coordinate'])]
y_cord = [int(i) for i in list(google_doc_df['y-coordinate'])]
char = list(google_doc_df['Character'])

# call the plot function to print out the hidden message passing the lists 
plot_char(x_cord, y_cord, char)

