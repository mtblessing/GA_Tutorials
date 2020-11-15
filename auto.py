# def fun(x):
#     return 2*x 

# a = fun(2)
# print(a)

# def fun(x, y):
#     return x + y

# a = fun(1, 2)
# print(a)

name1 = "TB"
height_m1 = 2
weight_kg1 = 90

name2 = "TB Sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "TB Brother"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calc(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " Is not overweight"
    else:
        return name + " Is overweight"

result1 = bmi_calc(name1, height_m1, weight_kg1)
result2 = bmi_calc(name2, height_m2, weight_kg2)
result3 = bmi_calc(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)