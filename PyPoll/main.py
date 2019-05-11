import os
import csv

# using relative path
poll_data = "Resources/election_data.csv"

# reading the csv and converting the csv into a list
with open(poll_data, newline="") as csvfile:
    pollDataCSV = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    pollDataList = [row for row in pollDataCSV]

#* The total number of votes cast

totalVotes = len(pollDataList)

# * A complete list of candidates who received votes
listOfCandidates = []


for i in range(0,totalVotes):
    if pollDataList[i][2] not in listOfCandidates:
        listOfCandidates.append(pollDataList[i][2])

print("Election Results")
print("----------------------------")
print("Total Votes: ", totalVotes, sep='')
print("----------------------------")

# Open a Text file to print the results
Line1 = "Election Results"
Line2 = "----------------------------"
Line3 = "Total Votes: " + str(totalVotes)
Line4 = "----------------------------"
pollDataTxt=open("PollDataAnalysisOoutput.txt","w")
pollDataTxt.write("%s\n%s\n%s\n%s" % (Line1, Line2, Line3, Line4))
pollDataTxt.close

#* The percentage of votes each candidate won

highestVoteCount=0
highestVoteCandidate = []
for x in listOfCandidates: 
    voteCountCandidate = sum(1 for i in pollDataList if i[2] == x)
    votePercentageCandidate =round(voteCountCandidate/totalVotes*100,3)
    print(x,": ","{0:.3f}".format(votePercentageCandidate),"% (", int(voteCountCandidate),")",sep='')
    LineX= x +": " + str("{0:.3f}".format(votePercentageCandidate))+"% ("+ str(int(voteCountCandidate)) +")"
    pollDataTxt=open("PollDataAnalysisOoutput.txt","a")
    pollDataTxt.write("\n%s" % (LineX))
    pollDataTxt.close

#* The winner of the election based on popular vote.

    highestVoteCount_new=max(highestVoteCount,voteCountCandidate)
    if highestVoteCount_new!=highestVoteCount:
        highestVoteCandidate=x
        highestVoteCount=highestVoteCount_new



print("----------------------------")
print("Winner: ",highestVoteCandidate)
print("----------------------------")

Line5 = "----------------------------"
Line6 = "Winner: " + str(highestVoteCandidate)
Line7 = "----------------------------"


pollDataTxt=open("PollDataAnalysisOoutput.txt","a")
pollDataTxt.write("\n%s\n%s\n%s" % (Line5, Line6, Line7))
pollDataTxt.close