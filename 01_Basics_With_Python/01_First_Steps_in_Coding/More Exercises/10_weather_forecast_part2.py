# Read user input
temperature = float(input())

# Parameters

# Logic
if 12 > temperature >= 5:
    print('Cold')
elif 15 > temperature >= 12:
    print('Cool')
elif 20 >= temperature >= 15:
    print('Mild')
elif 26 > temperature > 20:
    print('Warm')
elif 35 >= temperature >= 26:
    print('Hot')
else:
    print('unknown')

# End of Logic

# Print Output
