relative_value = [7.5, -5.4, 3.2, -11.8]

relative_value_sorted_asc = sorted(relative_value, key=abs)
print(relative_value_sorted_asc)

relative_value_sorted_dec = sorted(relative_value, key=abs, reverse=True)
print(relative_value_sorted_dec)
