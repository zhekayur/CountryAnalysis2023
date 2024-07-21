import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r'C:\Users\user\Desktop\CountryAnalysis\data_countries.csv'
data = pd.read_csv(file_path)

# Strip leading and trailing spaces from the country names
data['Country'] = data['Country'].str.strip()

# Define the indexes and countries to highlight
indexes = [
    'AveragScore', 'SafetySecurity', 'PersonelFreedom', 'Governance',
    'SocialCapital', 'InvestmentEnvironment', 'EnterpriseConditions',
    'MarketAccessInfrastructure', 'EconomicQuality', 'LivingConditions',
    'Health', 'Education', 'NaturalEnvironment'
]

highlight_countries = ['Ukraine', 'Poland']

# Function to create bar plots
def create_bar_plot(index, highlight_countries, ax):
    sorted_data = data[['Country', index]].sort_values(by=index, ascending=False)
    
    top_10 = sorted_data.head(10)
    bottom_10 = sorted_data.tail(10)
    
    # Ensure Ukraine and Poland are included and position them in the middle
    highlighted_data = sorted_data[sorted_data['Country'].isin(highlight_countries)]
    combined_data = pd.concat([top_10, highlighted_data, bottom_10]).drop_duplicates().reset_index(drop=True)

    colors = ['blue'] * len(combined_data)
    for i, country in enumerate(combined_data['Country']):
        if country == 'Ukraine':
            colors[i] = 'yellow'
        elif country == 'Poland':
            colors[i] = 'red'

    sns.barplot(x=index, y='Country', data=combined_data, palette=colors, ax=ax)
    
    for i in range(len(combined_data)):
        ax.text(combined_data[index].iloc[i] + 0.5, i, round(combined_data[index].iloc[i], 2), color='black', ha="left", fontsize=8)

    median_value = data[index].median()
    ax.axvline(median_value, color='green', linestyle='--', label=f'Median: {median_value}')

    ax.set_title(f'{index}', fontsize=10)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.legend(fontsize=8)

# Create a larger figure for subplots
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(24, 18))
axes = axes.flatten()

# Create bar plots for each index in the subplots
for i, index in enumerate(indexes):
    if i < len(axes):
        ax = axes[i]
        create_bar_plot(index, highlight_countries, ax)

# Hide any extra subplots
for j in range(len(indexes), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()





