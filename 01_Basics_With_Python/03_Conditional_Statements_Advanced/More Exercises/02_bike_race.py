# Read user input
junior_bikers = int(input())
senior_bikers = int(input())
race_type = input()

# Parameters
trail_junior_fee = 5.50
cross_country_junior_fee = 8
downhill_junior_fee = 12.25
road_junior_fee = 20

trail_senior_fee = 7
cross_country_senior_fee = 9.50
downhill_senior_fee = 13.75
road_senior_fee = 21.50

# Variables
total_fee = 0
charity_amount = 0

# Logic
if race_type == 'trail':
    total_fee = junior_bikers * trail_junior_fee \
                + senior_bikers * trail_senior_fee
elif race_type == 'cross-country':
    total_fee = junior_bikers * cross_country_junior_fee \
                + senior_bikers * cross_country_senior_fee
    if junior_bikers + senior_bikers >= 50:
        total_fee *= 0.75
elif race_type == 'downhill':
    total_fee = junior_bikers * downhill_junior_fee \
                + senior_bikers * downhill_senior_fee
elif race_type == 'road':
    total_fee = junior_bikers * road_junior_fee \
                + senior_bikers * road_senior_fee

charity_amount = 0.95 * total_fee
# End of Logic

# Print Output
print(f'{charity_amount:.2f}')
