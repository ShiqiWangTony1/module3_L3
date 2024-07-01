# Task 1
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)

unique_to_our_airline = our_routes.difference(competitor_routes)

neither_destinations = our_routes.symmetric_difference(competitor_routes)

print("Common destinations:", common_destinations)
print("Unique to our airline:", unique_to_our_airline)
print("Destinations that neither airline shares:", neither_destinations)


# Task 2
def remove_duplicates(customer_ids):
    return set(customer_ids)

# Sets don't contain duplicate elements
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

print("Unique customer IDs:", remove_duplicates(customer_ids))

