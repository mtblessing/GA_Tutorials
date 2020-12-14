cities = ['London','Paris','Harare','Gaberone','Johanessburg']

#Instead of this use this code
# i = 0
# for city in cities:
#     i+=1
#     print(i, city)

#Use this instead

for i,city in enumerate(cities, 1):
    print(i,city)