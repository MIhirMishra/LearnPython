cities_lived_in = ['supaul', 'saharsa', 'Hazaribagh', 'Patna', 'Tumkrur', 'Bangalore', 'Hyderabad', 'Chennai', 'Santa Clara', 'Des Moines']
print("\nNumber of cities Mihir lived in so far: " + str(len(cities_lived_in)))
print("sorted list of cities: " + str(sorted(cities_lived_in)))
print("original order of cities: " + str(cities_lived_in))
cities_lived_in.reverse()
print("reversed list of cities: " + str(cities_lived_in))
cities_lived_in.sort(reverse=True)
print("reverse of reversed list of cities: " + str(cities_lived_in))