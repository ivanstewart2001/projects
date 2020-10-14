"""
Building on the previous example, let's also assume that you have saved $918 to fund your new
adventure. You wonder how many days you can keep one server running before your money
runs out. Of course, you hope your social network becomes popular and requires 20 servers to
keep up with the demand. How much will it cost to operate at that point?
"""

print("How much does it cost to operate one server per day?")
per_day = 0.51 * 24
print(per_day)

print("How much does it cost to operate one server per month?")
per_month = 0.51 * 24 * 30
print(per_month)

print("How much does it cost to operate twenty servers per day?")
per_day_20 = 0.51 * 24 * 20
print(per_day_20)

print("How much does it cost to operate twenty servers per month?")
per_month_20 = 0.51 * 24 * 20 * 30
print(per_month_20)

print("How many days can I operate one server with $918?")
one_server_918 = 918 / 0.51
rounded = round(one_server_918)
print(rounded)

