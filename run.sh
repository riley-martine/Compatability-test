rm spreadsheet.csv.old
mv spreadsheet.csv spreadsheet.csv.old
wget --no-check-certificate 'docs.google.com/spreadsheet/ccc?key=THE KEY IS PUT HERE&output=csv' -O spreadsheet.csv
python main.py
