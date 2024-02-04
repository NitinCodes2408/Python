# Lists

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim","Jim", "Oscar", "Tomy"]
friends.extend(lucky_numbers)                   # names with numbers
friends.append("nitin")                         # attach one more name 
print(friends)
friends.insert(2, "Joseph")                     # name insert with index
print(friends)
# friends.remove("Sham")                        # remove from list
# friends.clear()                               # clear all list
friends.pop()                                   # remove last name from list
print(friends)
print(friends.index("Karen"))                   # checking index
print(friends.count("Jim"))                     # counting the names
Nitin = ["mayur", "rohan", "aryan"]
print(Nitin)
Nitin.sort()
print(Nitin)
Nitin.reverse()
print(Nitin)

# friends = ["Kevin", "Karen", "Jim", "Oscer", "Toby"]
# friends[1] = "Nitin"
# print(friends)