
minsea = 1000000
maxsea = 0
maxtime = "None"
mintime = "None"
while True:
    sealev = int(input("Please enter sea level:"))
    time = input("Please record the time of sea level measurement in the format HH:MM  :")
    if sealev > maxsea:
        maxsea = sealev
        maxtime = time
    if sealev < minsea:
        minsea = sealev
        mintime = time
    if sealev == 9999: break
print("The minimum sea level recorded was", minsea,", recorded as the time",mintime,"!")
print("The maximum sea level recorded was", maxsea,", recorded as the time",maxtime,"!")

