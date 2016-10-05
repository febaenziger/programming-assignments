# CSC 243-601/610
# Assignment 6
# Fiona Baenziger

# I worked alone

# Question 1
def makeAvgLst(fname):
    'returns list containing lists with city names & precipitation averages'
    try:
        file = open(fname, "r")
        fContent = file.readlines()
        file.close()
        
        cityLst = []
        for i in fContent:
            i = i.split()
            avg = 0
            city = i[0]
            for j in i[1:]:
                num = float(j)
                avg += num
            try:
                avg = avg/(len(i)-1)
            except ZeroDivisionError:
                avg = 0.0
            cityLst.append([city, avg])

        return cityLst
            
    except IOError:
        print("{} could not be opened.".format(fname))
        return []

# Question 2
def ticker(fname):
    'stores file data in dictionary & prints stock name associated with input' 
    try:
        file = open(fname, "r")
        fContent = file.readlines()
        file.close()
        
        newLst = []
        for i in fContent:
            i = i.strip()
            if i != "":
                newLst.append(i)

        tickD = {}
        for i in range(int(len(newLst)/2)):
            tickD[newLst[2*i]] = newLst[(2*i)+1]
            
        cond = True
        while cond == True:
            comp = input("Enter Company Name: ").upper()
            if comp == "":
                print("Thank you for using the ticker lookup system!")
                cond = False
            elif comp in tickD:
                print("Ticker Symbol: {}".format(tickD[comp]))
            else:
                print("{} is not a company in the ticker system.".format(comp))
                    
    except IOError:
        return "{} could not be opened. Exiting...".format(fname)

# Question 3
def takePoll(options):
    'returns the dictionary created from a poll'
    pollD = {}       
    cond = True
    while cond == True:
        print("The options are: {}".format(options))
        choice = (input("Enter your choice: ")).lower()
        if choice == "":
            cond = False
        elif choice in pollD:
            pollD[choice] += 1
        else:
            if choice in options:
                pollD[choice] = 1
            else:
                if "other" in pollD:
                    pollD["other"] += 1
                else:
                    pollD["other"] = 1
    print("Thanks for choosing!")           
    return pollD
        
        
