"""
Gabriel Miravite
Feb 13, 2026 (late)
Lab 4: Dictionaries
"""



print("=========== Example 1: Dictionary ===========")
# declare & initialize a dictionary
contacts = {
    'Bill': '718-111-2222',
    'Rick': '917-000-1111',
    'Mary': '800-222-3333',
}
print(f"Original dictionary: {contacts}")

# update value of key 'Rick'
contacts['Rick'] = '347-000-1111'
print(f"Updated dictionary: {contacts}")

# add new key-value pair
contacts['Peter'] = '888-000-1111'
print(f"Added a new key-value pair to the dictionary: {contacts}")



print("\n=========== Example 2: Loop Through a Dictionary ===========")
# for loop to print each KEY in the dictionary
for v in contacts:
    print(v)

# for loop to print each VALUE in the dictionary
for v in contacts:
    print(contacts[v])

# for loop to print each KEY-VALUE PAIR in the dictionary
for v in contacts:
    print(f"The phone number for {v} is {contacts[v]}")



print("\n=========== Example 3: items(), keys(), values() Methods in a Dictionary ===========")
# the items() method returns all of the dictionary's KEY-VALUE PAIRS
print(f"All of the dictionary's KEY-VALUE PAIRS: {contacts.items()}")
# the keys() returns all of the dictionary's KEYS
print(f"All of the dictionary's KEYS: {contacts.keys()}")
# values() returns all of the dictionary's VALUES
print(f"All of the dictionary's VALUES: {contacts.values()}")



print("\n=========== Example 4: Check If a Key Exists in a Dictionary ===========")
check_name = 'Rick'
check = check_name in contacts
print(f"Is {check_name} in the dictionary? {check}")



print("\n=========== Example 5: Length of a Dictionary ===========")
print(f"The 'contacts' dictionary has {len(contacts)} key-value pairs")



print("\n=========== Example 6: Remove a Pair from a Dictionary ===========")
print(f"Original dictionary: {contacts}")
contacts.pop('Mary')
print(f"Updated dictionary: {contacts}")



print("\n=========== Example 7: get() Method in a Dictionary ===========")
# the get() method returns the value of a particular key
print(f"The value for the key 'Bill' is {contacts.get('Bill')}")



print("\n=========== Example 8: update() Method in a Dictionary ===========")
# the update() method updates the value of a key OR adds a new key-value pair
contacts.update({'Annie' : '718-888-9999'})
print(f"{contacts}")