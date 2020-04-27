# report-gsuite-meets

Generates a report using Hangouts Meet audit data. The script outputs a csv file and a png image counting the numbers of Meet conferences and participants daily.

## Setup

This script requires Pandas, which can usually be installed via pip.

```sh
pip install pandas
```

## Usage

Download an export of the Meets audit for the time period you're reporting on using the instructions at [G Suite Admin Help: Google Meet audit log](https://support.google.com/a/answer/9186729?hl=en). Make sure to select **All Columns** and **Comma-seperated values (.csv)** in the export configuration window.

Then run the script with the audit you downloaded as an argument.

```sh
usage: python meet-stats.py input
Writes reports of hangouts meet usage stats
```
