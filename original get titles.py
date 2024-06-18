import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

tables = pd.read_html('https://en.wikipedia.org/wiki/Academy_Award_for_Best_Original_Screenplay#Winners_and_nominees')

# Check the number of tables extracted
print(len(tables))

# Assuming the table you want is the fourth one, you can access it like this:
original_screenplay_table = tables[3]

print(original_screenplay_table.head())  # Display the first few rows of the table
