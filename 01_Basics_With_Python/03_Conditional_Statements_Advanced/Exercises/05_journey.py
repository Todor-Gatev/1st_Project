# Read user input
budget = float(input())
season = input()

# Logic
accommodation = ""
destination = ""
percent_of_budget = 0

if season == "summer":
    accommodation = "Camp"
elif season == "winter":
    accommodation = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        percent_of_budget = 0.3
    elif season == "winter":
        percent_of_budget = 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        percent_of_budget = 0.4
    elif season == "winter":
        percent_of_budget = 0.8
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    percent_of_budget = 0.9

spent_amount = budget * percent_of_budget

# Print Output
print(f"Somewhere in {destination}")
print(f"{accommodation} - {spent_amount:.2f}")
