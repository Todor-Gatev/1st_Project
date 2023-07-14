class Party:
    def __init__(self):
        self.people = []


# Read user input
command = input()

# Instance
party = Party()

# Logic
while command != "End":
    party.people.append(command)
    command = input()
# End of Logic

# Print Output
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
