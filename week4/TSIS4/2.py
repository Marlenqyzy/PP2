import re
s = input()
pp = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', s)
if len(pp) == 0:
    print("-1")
else:
    for i in range(len(pp)):
        print(pp[i])