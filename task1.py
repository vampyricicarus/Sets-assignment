
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

print(our_routes.intersection(competitor_routes))
print(our_routes.difference(competitor_routes))
print(our_routes.symmetric_difference(competitor_routes))