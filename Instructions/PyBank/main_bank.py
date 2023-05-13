import os
import csv

csvpath=os.path.join("Resources", "budget_data.csv")

#The total number of months included in the dataset
with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvfile)
    months=[]
    alist=[]

    blist=[]

    for row in csvreader:
        months.append(row[0])
        alist.append(row[1])
        blist.append(row[1])
    #print(str(len(months)))
    #print(str(alist))
    
    #sum of all profit and losses
    total=0
    for amount in blist:
        total+= int(amount) 
        #print(total)

    total_str=str(total)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

    alist.pop(0)
    #could also write as: del alist[0]
    #print(str(blist))
    #print(str(alist))
    #print(str(alist))
    subtracted = []
    for i in range(len(alist)):
        item = int(alist[i]) - int(blist[i])
        subtracted.append(item)
    #print(subtracted)


    netsubtracted=sum(subtracted)
    #print(netsubtracted)
    averagepl=str(round(netsubtracted/len(subtracted),2))
    #print(averagepl)
    #
 #The greatest increase in profits (date and amount) over the entire period
    greatest_amount=0
    for x in subtracted:
        if x>int(greatest_amount):
            greatest_amount=x
            loc_greatest_amount=subtracted.index(x)
#index code help from https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array
    month_greatest_increase=str(months[(loc_greatest_amount+1)])
    
    # print('this is the greatest'+str(greatest_amount))
    # print('month'+str(month_greatest_increase))
    # greatest=0
    # for x in blist:
    #     if int(x) > int(greatest):
    #         greatest=x
    # print(greatest)

    # for y in blist:
    #     if greatest==y:
    #         print("The greatest increase in profits was in "+row[0]+ " with the amount of $" +greatest)
    #         month_increase=str(row[0])
    #         amount_increase=str(greatest)
    
    
    # rowline=0
    # for y in blist:
    #     if greatest==blist[y]:
    #         print(str(row[0]))


    # for y in len(blist):
    #     if y!= greatest:
    #         rowline+= int(y)
    #     elif y==greatest:
    #         rowline+= int(y)
    #         print(str(y))


#The greatest decrease in profits (date and amount) over the entire period
    least=0
    for x in subtracted:
        if x<int(least):
            least=x
            loc_least_amount=subtracted.index(x)

    month_least_increase=str(months[(loc_least_amount+1)])
    #print(f'month {month_least_increase} amount {least}')

#number of months in dataset
    number_months=str(len(months))
    #print(number_months)
print('Financial Analysis')
print(f'Total months {number_months}')
print('Total:  $'+total_str)
print('Average Change: $'+averagepl)
print(f'Greatest Increase in Profits: {month_greatest_increase}  $ ({greatest_amount})')
print(f'Greatest Decrease in Profits: {month_least_increase}  $ ({least})')

with open ('analysis.txt','w') as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write('Total Months: '+number_months)
    f.write('\n')
    f.write('Total:  $'+total_str)
    f.write('\n')
    f.write('Average Change: $'+averagepl)
    f.write('\n')
    f.write(f'Greatest Increase in Profits: {month_greatest_increase}  $ ({greatest_amount})')
    f.write('\n')
    f.write(f'Greatest Decrease in Profits: {month_least_increase}  $ ({least})')
   

    # for row in alist:
    #   #  x=next(alist)
    #     print(str(x))
    #    # x=int(row[1])-int(
       # blist.append(next(alist))

   # print (str(blist))

        

    # Open and read csv
# with open(cereal_csv) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")

#     # Read the header row first (skip this part if there is no header)
#     csv_header = next(csv_file)
#     print(f"Header: {csv_header}")

#     # Read through each row of data after the header
#     for row in csv_reader:

#         # Convert row to float and compare to grams of fiber
#         if float(row[7]) >= 5:
#             print(row)



#profit loss



        



#The net total amount of "Profit/Losses" over the entire period



#The changes in "Profit/Losses" over the entire period, and then the average of those changes



