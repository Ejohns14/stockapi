import csv
import statistics 

#save our data into a list of dictionaries
AMZN_data =[]
with open("AMZN.csv", "r") as infile:
        reader = csv.DictReader(infile)
        # save this dictReader object into a list of dictionaries to analyze
        for row in reader:
                AMZN_data.append(row)
print(AMZN_data)
    # get each week of stock data, 5 iterations at a time
i = 0
AMZN_stdev = []
    # standard deviation shouuld be listed
while i < len(AMZN_data):
        # if my i+5 will result  in me going out of bounds, just break
        if i+4>=len(AMZN_data):
                break
        day1 = float(AMZN_data[i]["Closing_Price"])
        day2 = float(AMZN_data[i + 1]["Closing_Price"])
        day3 = float(AMZN_data[i + 2]["Closing_Price"])
        day4 = float(AMZN_data[i + 3]["Closing_Price"])
        day5 = float(AMZN_data[i + 4]["Closing_Price"])
        # how can I analyze the pop std dev on all these closing prices?
        dev = statistics.pstdev([day1, day2, day3, day4, day5])
        # how can I save this std dev into the list `stock1_stdev`
        AMZN_stdev.append(dev)
        # how can i increment my “i” by 5 to represent 5 day skips?
        i += 5
        print(AMZN_stdev)
   
HD_data =[]
with open("HD.csv", "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
                HD_data.append(row)
print(HD_data)

h = 0
HD_stdev = []
while h < len(HD_data):
        if h+4>=len(HD_data):
                break
        day1 = float(HD_data[h]["Closing_Price"])
        day2 = float(HD_data[h + 1]["Closing_Price"])
        day3 = float(HD_data[h + 2]["Closing_Price"])
        day4 = float(HD_data[h + 3]["Closing_Price"])
        day5 = float(HD_data[h + 4]["Closing_Price"])
        dev = statistics.pstdev([day1, day2, day3, day4, day5])
        HD_stdev.append(dev)
        h += 5
        print(HD_stdev)
        
LYFT_data =[]
with open("LYFT.csv", "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
                LYFT_data.append(row)
print(LYFT_data)

l = 0
LYFT_stdev = []
while l < len(LYFT_data):
        if l+4>=len(LYFT_data):
                break
        day1 = float(LYFT_data[l]["Closing_Price"])
        day2 = float(LYFT_data[l + 1]["Closing_Price"])
        day3 = float(LYFT_data[l + 2]["Closing_Price"])
        day4 = float(LYFT_data[l + 3]["Closing_Price"])
        day5 = float(LYFT_data[l + 4]["Closing_Price"])
        dev = statistics.pstdev([day1, day2, day3, day4, day5])
        LYFT_stdev.append(dev)
        l += 5
        print(LYFT_stdev)

NXPI_data =[]
with open("NXPI.csv", "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
                NXPI_data.append(row)
print(NXPI_data)

n = 0
NXPI_stdev = []
while n < len(NXPI_data):
        if n+4>=len(NXPI_data):
                break
        day1 = float(NXPI_data[i]["Closing_Price"])
        day2 = float(NXPI_data[i + 1]["Closing_Price"])
        day3 = float(NXPI_data[i + 2]["Closing_Price"])
        day4 = float(NXPI_data[i + 3]["Closing_Price"])
        day5 = float(NXPI_data[i + 4]["Closing_Price"])
        dev = statistics.pstdev([day1, day2, day3, day4, day5])
        NXPI_stdev.append(dev)
        n += 5
        print(NXPI_stdev)

TGT_data =[]
with open("TGT.csv", "r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
                TGT_data.append(row)
print(TGT_data)

t = 0
TGT_stdev = []
while t < len(TGT_data):
        if t+4>=len(TGT_data):
                break
        day1 = float(TGT_data[t]["Closing_Price"])
        day2 = float(TGT_data[t + 1]["Closing_Price"])
        day3 = float(TGT_data[t + 2]["Closing_Price"])
        day4 = float(TGT_data[t + 3]["Closing_Price"])
        day5 = float(TGT_data[t + 4]["Closing_Price"])
        dev = statistics.pstdev([day1, day2, day3, day4, day5])
        TGT_stdev.append(dev)
        t += 5
        print(TGT_stdev)








































