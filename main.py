# Import necessary libraries
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

sns.set(color_codes=True)

# Load data from CSV
df = pd.read_csv('data-numerical-categories.csv', encoding='utf-8-sig')

# ALLCAT
#sns.pairplot(data=df, hue="Category", palette="husl");

# VARCAT
sns.pairplot(data=df, hue="Category", vars=["Views", "Rate"], palette="husl");

'''
# Construct joint plots -> seaborn_joinplot_<??>
#sns.jointplot(x="Rate", y="Length", data=df, kind="kde")
sns.jointplot(x="Rate", y="Views", data=df, kind="kde")
#sns.jointplot(x="Rate", y="Rate", data=df, kind="kde")

# Construct pair grid with 3 rows -> seaborn_pairgrid
g = sns.PairGrid(df)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6)

# Construct strip plot -> seaborn_strip
sns.stripplot(x="Views", y="Category", data=df)

# Construct iris plot -> seaborn_swarm
sns.swarmplot(x="Category", y="Views", data=df)
'''

# Show plot
plt.show()


'''
def main():

    data = pd.read_csv('data-final.csv', encoding='utf-8-sig')


    categoryList = data['Category'].values.tolist()
    lengthList = data['Length'].values.tolist()
    viewsList = data['Views'].values.tolist()
    rateList = data['Rate'].values.tolist()
    ratingsList = data['Ratings'].values.tolist()
    commentsList = data['Comments'].values.tolist()



    entries = data.values.tolist()

    print (entries)

if __name__ == '__main__':
    main()
'''
