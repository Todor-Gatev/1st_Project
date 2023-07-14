def return_version(a, b):
    if a > 9:
        a = 0
        b += 1

    return a, b


# Read user input
major, minor, patch = [int(x) for x in input().split('.')]

patch += 1

# Logic
patch, minor = return_version(patch, minor)
minor, major = return_version(minor, major)

# if patch > 9:
#     patch = 0
#     minor += 1
#
#     if minor > 9:
#         minor = 0
#         major += 1

# End of Logic

# Print Output
print(f"{major}.{minor}.{patch}")
