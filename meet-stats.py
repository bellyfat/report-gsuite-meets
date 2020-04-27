import sys
import time

try:
    input_path = sys.argv[1]
except:
    print('usage: meet-stats.py input')
    print('Writes reports of Meet usage stats')
    sys.exit()

import pandas as pd

# define the columns we want while importing
COLUMNS = ['Conference ID','Date','Product Type','Participant Identifier']
# define columns to parse as date type while importing
DATECOLS = ['Date']
# import the data
data = pd.read_csv(input_path, usecols=COLUMNS, 
                    parse_dates=DATECOLS, index_col=False)

# add a column with just date, no times
data['date_only'] = data['Date'].dt.to_period('D')

# filter to Hangouts Meet only, no classic Hangouts
data = data[data["Product Type"] == 'Meet']

report = data.groupby('date_only') \
                .agg('nunique') \
                .drop(['Date','Product Type','date_only'], axis=1) \
                .rename(columns={"Conference ID": "Conferences", "Participant Identifier": "Participants"})

# write the report to csv and a png chart
output_name = f'meet-report-{time.time()}'
report.to_csv(output_name + '.csv')
report.plot(figsize=(11,8.5)).get_figure().savefig(output_name + '.png')