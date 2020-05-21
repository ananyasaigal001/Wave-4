def reverseLookup(dictionary,v):
    """Function finds all of the keys in a dictionary that map to a specific value."""
    return[key for key, value in dictionary.items() if value==v]
        
#dictionary and value
d={'george': 16, 'amber': 16,'leo': 15}
value=int(input("Enter the value to be searched for in the dictionary: "))

#output
print(reverseLookup(d,value))
