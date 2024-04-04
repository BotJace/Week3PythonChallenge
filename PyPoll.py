import csv

# Define input and output file paths
input_file = "election_data.csv"
output_file = "election_results.txt"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        # Count total number of votes
        total_votes += 1
        
        # Count votes for each candidate
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate percentage of votes and find the winner
results_summary = "Election Results\n" + "-" * 25 + "\n"
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Generate analysis summary
results_summary += "-" * 25 + f"\nWinner: {winner}\n" + "-" * 25

# Print analysis to terminal
print(results_summary)

# Write analysis summary to text file
with open(output_file, "w") as txt_file:
    txt_file.write(results_summary)
