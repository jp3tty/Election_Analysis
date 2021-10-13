# Election_Analysis

## Overview
The Colorado Board of Elections requests an audit on the results of a local election. Their voting data was captured in a CSV file named "election_results," and a Python program named PyPoll_Challenge ([link](https://github.com/jp3tty/Election_Analysis/blob/main/PyPoll_Challenge.py)) was used to analyze and write a report for the board to review. The program provides the following information:

* Total number of votes cast
* A complete list of candidates who received votes
* Total number of votes each candidate received
* Percentage of votes each candidate won
* The winner of the election based on popular vote
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

The results are communicated via the programs command line, as well as captured in a TXT file labeled "election_analysis." Below we will report the results of the audit and discuss the program used to arrive at its outcome.


## Election-Audit Results

The analysis results produces the following outcome in the Python command line: 

![terminal results](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/terminal_results.PNG)

The TXT file can be accessed through this link: [election_analysis.txt](https://github.com/jp3tty/Election_Analysis/blob/main/analysis/election_analysis.txt).

As we can see from the above results the election information is as follows:
* Total votes cast in this congressional election: 369,733
* Total votes for each county:
  * Jefferson with 38,855 votes (10.5% of total votes)
  * Denver with 306,055 votes (82.8% of total votes)
  * Arapahoe with 24,801 votes (6.7% of total votes)
* County with the largest vote turnout: Denver
* Number of votes for each candidate:
  * Charles Casper Stockham had 85,213 votes (23.0% of total votes)
  * Diana DeGette had 272,892 votes (73.8% of total votes)
  * Raymon Anthony Doane had 11,606 votes (3.1% of total votes)
* Winning candidate: Diana DeGette won the election with 272,892 votes (73.8% of total votes)


## Election-Audit Summary

The script begins by utilizing Python modules to interface with the CSV file and write the analysis information to a TXT file.

![python_mods](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/python_modules.PNG)

Per the audit request from the Colorade Board of Elections, the script defines its reportable outputs as

* total votes
* candidate names (shown below as candidate_options)
* votes to candidates (shown below as candidate_votes)
* county names
* votes in each county (shown below as county_votes)
* the winning candidate
* the largest county turnout.

![Defining Variables](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/defining_variables.PNG)

The Python program then opens the election CSV file and processes the lines of data to tally the total votes and capture the candidate and county names by the means of a For loop.

![Candidate For loop](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/candidate_for_loop.PNG)

When the program finds a new candidate, it adds the new name to its list and tallies that individauls information with the previous For loop. The program continues this process until all lines of data have been analyzed.

Once this data has been processed the program prints this information to the command line and saves it in the "election_results" file.

![Save and print votes for candidates](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/save_print_total_votes.PNG)

The county votes are determined with a For loop similar to the loop that was used to process the total votes for each candidate.

![county votes loop](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/county_votes_loop.PNG)

This section of the code also uses the total votes to determine the percentage of votes for each county and declares the county with the largest number of votes. This information is also printed and saved to the TXT file.

Conditional formatting is applied at the end of the script to process and report the winning candidate, their vote count, and winning percentage, as well as print the information to the command line and save it to the TXT file.

![Condition formatting](https://github.com/jp3tty/Election_Analysis/blob/main/Resources/conditional_format.PNG)
