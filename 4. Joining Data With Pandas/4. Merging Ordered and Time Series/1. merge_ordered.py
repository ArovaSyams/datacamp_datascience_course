# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[["gdp", "returns"]]

# Print gdp_returns correlation
print (gdp_returns.corr())

=====

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, on="date", how="inner")

# Print inflation_unemploy 
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind="scatter", x="unemployment_rate", y="cpi")
plt.show()

==========

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=["country", "date"], fill_method="ffill")

# Print date_ctry
print(date_ctry)