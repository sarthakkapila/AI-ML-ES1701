import pandas as pd
import matplotlib.pyplot as plt

# (a) 
diamonds_df = pd.read_csv('diamonds.csv')
print("Top 5 rows of the diamonds DataFrame:")
print(diamonds_df.head())

# (b) 
selected_series = diamonds_df['carat']
print("\nContent of the 'carat' series:")
print(selected_series)

# (c) 
diamonds_df.rename(columns={'x': 'length', 'y': 'width'}, inplace=True)
print("\nDataFrame with 'x' column renamed to 'length' and 'y' to 'width':")
print(diamonds_df.head())

# (d) 
sorted_cut_series = diamonds_df['cut'].sort_values()
print("\nSorted 'cut' column in ascending order:")
print(sorted_cut_series)

# (e) 
selected_diamonds = diamonds_df[diamonds_df['cut'].isin(['Fair', 'Good', 'Premium'])]
print("\nDiamonds with Fair, Good, or Premium cut:")
print(selected_diamonds)

# (f) 
cut_stats = diamonds_df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("\nCount, minimum, maximum price for each cut:")
print(cut_stats)

# (g) 
diamonds_df['cut'].value_counts().plot(kind='bar')
plt.title("Value Counts for Cut")
plt.xlabel("Cut")
plt.ylabel("Count")
plt.show()

# (h) 
print("\nConcise summary of diamonds DataFrame:")
print(diamonds_df.info())
