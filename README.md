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

The Python program then opens the election CSV file and processes the lines of data to tally the total votes and capture the candidate and county names by the means of a For loop.

@image of the For loop

When the program finds a new candidate, it adds the new name to its list and tallies that individauls information with the previous For loop. The program continues this process until all lines of data have been analyzed.

Once this data has been processed the program prints this information to the command line and saves it in the "election_results" file.

@Image of total votes being saved and printed

The county votes are determined with a For loop similar to the loop that was used to process the total votes for each candidate.

@Image of county votes For loop.

This section of the code also uses the total votes to calculates the percentage of votes for each county and declares the county with the largest number of votes. This information is printed and saved to the TXT file.

@Image of print and save.

Conditional formatting is applied at the end of the script to process and report the winning candidate, their vote count, and winning percentage, as well as print the information to the command line and save it to the TXT file.


@@@Images of the Python code.
