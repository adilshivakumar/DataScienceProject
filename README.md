# DataScienceProject
DataScienceProject's goal is to create a program that helps discern the information of stocks. For example, the earnings, the gain and loss of the stock, the percentage difference all compared to the earnings date over a certain period of time.
## Design 
The input of the code part of the project is the stock tickers and start and end dates of the quarterly periods of the stocks. 
### Output
| Fiscal Quarter End | (Stock Ticker) - Reported Earnings Date| -30...+30 | Standard Dev  |
| ------ | ------ | ----- | ------ |
| 3/31/2008 | 4/23/2008 | 4.55 - 6.46 | 0.41(calculated) |
## Implementation
### Step 1
1. Take the input from Google Sheets(https://docs.google.com/spreadsheets/d/1BHSrJi_nlKPLkTT-Lzua_v7K67042yAl-jZ6KKpKQNs/edit#gid=575233713) and save it as CSV File. 
2. Use the CSV file to calculate the standard deviation using pandas. 
### Step 2 
1. Automate Dataframe #1-6b 


