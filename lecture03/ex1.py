testscore1 = int(input("Enter the score for test 1: "))
testscore2 = int(input("Enter the score for test 2: "))
testscore3 = int(input("Enter the score for test 3: "))
allscore = testscore1 + testscore2 + testscore3
averagnscore = allscore / 3
print(averagnscore)
if averagnscore > 95:
    print("Congratulations!")