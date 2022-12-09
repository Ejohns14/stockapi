import csv
import statistics as stats
import matplotlib.pyplot as plt
filenames=["AMZN.csv", "HD.csv", "LYFT.csv", "NXPI.csv", "TGT.csv"]
#save our data into a list of dictionaries
for file in filenames:
    HD_data =[]
    with open(f"data/{file}", "r") as infile:
        reader = csv.DictReader(infile)
        # save this dictReader object into a list of dictionaries to analyze
        for row in reader:
                HD_data.append(row)
    # get each week of stock data, 5 iterations at a time
    i = 0
    HD_stdev = []# standard deviation shouuld be listed
    while i < len(HD_data):
        # if my i+5 will result  in me going out of bounds, just break
        if i+4>=len(HD_data):
                break
        day1 = HD_data[i]
        price1=float(day1["price"])
        day2 = HD_data[i + 1]
        price2=float(day2["price"])
        # how can I get days 3, 4, and 5?
        day3 = HD_data[i + 2]
        price3=float(day3["price"])
        day4 = HD_data[i + 3]
        price4=float(day4["price"])
        day5 = HD_data[i + 4]
        price5=float(day5["price"])
        # how can I analyze the pop std dev on all these closing prices?
        dev=stats.pstdev([price1, price2, price3, price4, price5])
        # how can I save this std dev into the list `stock1_stdev`
        HD_stdev.append(dev)
        # how can i increment my “i” by 5 to represent 5 day skips?
        i += 5
        print(dev)
    #create plot line graph
    fig,ax= plt.subplots()
    ax.plot(HD_stdev)
    ax.set_ylabel("STDEV of price")
    ax.set_xlabel("weeks since March29")
    ax.set_title("STANDARD DEVIATION OF STOCKS")
    plt.savefig(f"data{file}.png")











































