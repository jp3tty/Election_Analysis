# Election_Analysis

## Overview
The Colorado Board of Elections requests an audit on the results of a local election. Their voting data was captured in a CSV file named "election_results," and a Python program was used to analyze and write a report for the board to review. The program provides the following information:

* Total number of votes cast
* A complete list of candidates who received votes
* Total number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

and the results are communicated via the programs command line, as well as captured in a TXT file labeled "election_analysis."


## Election-Audit Results

The results of the analysis shows:

Candidates:
* Charles Casper Stockham
* Diana DeGette
* Raymon Anthony Doane

Results of the vote:
* Stockham received 23.0% of the vote with 85,213 votes.
* Diana DeGette received 73.8% of the vote with 272,892 votes.
* Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.


@@@Place Image of command line report.

@@@Include a link to the txt file.

## Election-Audit Summary

Summarize some of the functions in the audit program.

The script begins by utilizing Python modules to interface with the CSV file and write the analysis information to a TXT file.

@image of Python modules

Per the audit request from the Colorade Board of Elections, the script defines its reportable outputs as

* total votes
* candidate names
* votes to candidates
* county names
* votes in each county
* the winning candidate
* the largest county turnout.

@image of defining variables

The Python program then opens the election CSV file and processes the lines of data to tally the listed outputs by the means of a For loop.

@image of the For loop

After the For loop is completed 

@@@Images of the Python code.
