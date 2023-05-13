import os
import csv

#csvpath=os.path.join("..","PyPoll","Resources","election_data.csv")
csvpath=os.path.join("Resources", "election_data.csv")
canoptions=[]
numberballots=[] 
total=0
canvotes={}

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #canged to read csvreader, not csvfile
    csvheader=next(csvreader)
   
    for row in csvreader:
        #total+=1 would be the exact same thing as line below
        total=total+1
        newcandidate=row[2]
        if newcandidate not in canoptions:
            #you could append with row[2], but this way code clearer to others
            canoptions.append(newcandidate)
            canvotes[newcandidate]=0
            #canvote[Keyname]=value
        canvotes[newcandidate]+=1
#prints keyname:keyvalue for each unique keynema 
#print(canvotes)

numbercan=[]

for name in canvotes:
    numbercan.append(canvotes[name])
#print(numbercan)

percentages=[]
y=0
for percent in (numbercan):
    p=round(int(percent)/int(total)*100,2)
    percentages.append(p)
    if y<p:
        y=p
    p=0
#print(percentages)
#print(y)

#print(percentages.index(y))

#printout
print("Election Results")
print("-------------------------------")
print("Total Votes:"+str(total))
list_candidates=[]
for x in range(len(canoptions)):
    print(str(canoptions[x])+": "+str(percentages[x])+"% ("+str(numbercan[x])+")")
    list_candidates.append(str(canoptions[x])+": "+str(percentages[x])+"% ("+str(numbercan[x])+")")
print("Winner: "+ str(canoptions[percentages.index(y)]))
winner=("Winner: "+ str(canoptions[percentages.index(y)]))
    
with open ('analysis.txt','w') as f:
    f.write('Election Results')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(f'Total Votes: {str(total)}')
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(str(list_candidates[0]))
    f.write('\n')
    f.write(str(list_candidates[1]))
    f.write('\n')
    f.write(str(list_candidates[2]))
    f.write('\n')
    f.write('----------------------------')
    f.write('\n')
    f.write(str(winner))
    f.write('\n')
    f.write('----------------------------')


    #print(total)

        #numberballots.append(row[0])


   # print(len(numberballots))

    #why won't this append the dictionary?
    #  candidate={}
    # for row in csvreader:
    #     candidate.append(row[2])
    # print(len(candidate))

    #why is this 0?
    
#     #print(csvreader)
#     for row in csvreader:
#        print(row[2])
#     #newcandidate.append(row[2])

#     #print(len(newcandidate))
    
#     for x in csvreader:
#          newcandidate.append(row[2])
#     #print(len(newcandidate))

# #why is this not being appended?
#     person=[]
#     for x in csvreader:
#         if x== next(x):
#             x=x
#         elif x != next(x):
#             person.append(row[2])
#             x=next(x)

#     print(len(person))

#how to count number of times an instance happens in a list?

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.





