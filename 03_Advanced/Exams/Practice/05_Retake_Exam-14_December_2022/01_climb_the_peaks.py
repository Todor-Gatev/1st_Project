from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))

conquered_peaks = []
peaks = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])

for i in range(7):
    f = food_portions.pop()
    s = stamina.popleft()

    if f + s >= peaks[0][1]:
        conquered_peaks.append(peaks[0][0])
        peaks.popleft()

        if not peaks:
            break

if peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if conquered_peaks:
    print(f"Conquered peaks:", *conquered_peaks, sep="\n")
