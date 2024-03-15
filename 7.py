kirill, arina, sergey = input().split(sep=' ')
kirill = int(kirill)
arina = int(arina)
sergey = int(sergey)
if kirill >= arina and kirill >= sergey:
    print(kirill)
elif arina >= kirill and arina >= sergey:
    print(arina)
else:
    print(sergey)