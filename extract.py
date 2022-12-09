from config import key
import requests
import time
import csv

stocks = ["HD","AMZN","TGT","LYFT","NXPI"]

for stock in stocks :
     # constuct a query URL for each stock and requesting data
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&sort=asc&limit=300&apiKey={key}"
    data = requests.get(url)
    jdata =  data.json()
    results = jdata["results"]
    stockdata=[]
    # looping through each day of data and saving into a dictionary
    for day in results:
        print(day)
        closing_p = day["c"]
        closing_t = day ["t"]
          # convert to human readable
        print(closing_p)
        print(closing_t)
        x = time.strftime('%Y-%m-%d', time.localtime(closing_t/1000))
        # create dictionary of data & price
        print(x)
        row = {"date":x, "price": closing_p}
        # append dictionary to stock data
        stockdata.append(row)
    with open(f"{stock}.csv", "w") as outfile:
        writer=csv.DictWriter(outfile, fieldnames=["date", "price"])
        writer.writeheader()
        writer.writerows(stockdata)








