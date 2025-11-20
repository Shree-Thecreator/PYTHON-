st = input("Enter message: ")
words = st.split(" ")
coding = True

nWords = []

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nWords.append(stnew)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))

else:
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            if stnew:  # check if stnew is not empty
                stnew = stnew[-1] + stnew[::-1]
            nWords.append(stnew)
        else:
            nWords.append(word[::-1])
    print(" ".join(nWords))