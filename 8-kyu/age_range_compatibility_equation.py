# Rank  : 8 kyu
# Title : Age Range Compatibility Equation
# Link  : https://www.codewars.com/kata/5803956ddb07c5c74200144e


def dating_range(age):
    if age > 14:
        min, max = age / 2 + 7, 2 * (age - 7)
    else:
        min, max = age - 0.10 * age, age + 0.10 * age

    return f"{int(min)}-{int(max)}"


print(dating_range(17), "\t15-20")
print(dating_range(40), "\t27-66")
print(dating_range(15), "\t14-16")
print(dating_range(35), "\t24-56")
print(dating_range(10), "\t9-11")
print(dating_range(53), "\t33-92")
print(dating_range(19), "\t16-24")
print(dating_range(12), "\t10-13")
print(dating_range(7), "\t6-7")
print(dating_range(33), "\t23-52")
