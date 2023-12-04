rdictionary = {"fruit":"apple",
               22 : "popcorn",
               99.99 : 77
               }

rdictionary["newkey"] = "newvalue"
rdictionary["fruit"] = "bananna"

del rdictionary [22]

for k in rdictionary:
    print(f"key : {k}  -> value: {rdictionary[k]}")


print(rdictionary)



