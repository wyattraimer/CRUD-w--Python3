import csv #important
import math

     #open line important
with open('waterservices.usgs.gov_07012025_07312025.txt', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')# delimeter important
    total=0
    totalSquared=0
    count=0
    maximum=0.0
    minimum=0.0
    for row in spamreader:
        if row[0]=="USGS":
            value=float(row[4])
            total+=value
            totalSquared=value*value #a way to calc std dev later without having to do a second pass on data
            if count==0:
                minimum=value
                maximum=value
            else:
                if maximum<value:
                    maximum=value
                if minimum>value:
                    minimum=value
            count+=1
            # print(', '.join(row))
    avg=total/count
    var=totalSquared/count-avg*avg #where you calc std dev later. This is MC question.
    print("Count is: ",count)
    print("Average is: ",avg)
    # print(var)
    # print("Std dev: ",math.sqrt(var))
    print("Std dev: ",math.sqrt(abs(var)))
    print("Minumum is: ",minimum)
    print("Maximum is: ",maximum)