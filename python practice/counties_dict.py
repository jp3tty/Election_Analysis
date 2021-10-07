counties_dict={"Arapahoe": 369237,"Denver":463353,"Jefferson":432438}

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict.[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for county, voters in counties_dict.items():
#     print(county, voters)

# skill drill in 3.2.10
for county, voters in counties_dict.items():
    # print(county + " county has " + str(voters) + " registered voters.")

    print(f"{county} county has {voters:,} registered voters.")
