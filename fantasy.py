import random
class Player(object):
    """Represents a Major League Baseball position player
    Attributes:
            hr: projected home runs
            avg: projected batting average
            rbi: projected runs batted in
            runs: projected runs
            sb: projected stolen bases
            pos: player's position
            name: player's name
            status: player's draft eligibility (1 is available,
                                                0 is drafted)
    """

    def __init__(self, name, hr, runs, rbi, sb, avg, pos, status):
        self.name = name
        self.pos = pos
        self.runs = runs
        self.avg = avg
        self.hr = hr
        self.rbi = rbi
        self.sb = sb
        self.status = 1

    def printStats(self):
        print(self.name)
        print("Pos: ", self.pos)
        print("Runs: ", self.runs)
        print("Avg: ", self.avg)
        print("Hr: ", self.hr)
        print("RBI: ", self.rbi)
        print("SB: ", self.sb)
        print("Status: ", self.status)
        print('\n')


class Team(object):
    """Represents a hypothetical team as a list of Player objects (of which there are 13)"""

    def __init__(self, roster):
        self.roster = roster
        self.fBase = roster[0]
        self.sBase = roster[1]
        self.tBase = roster[2]
        self.short = roster[3]
        self.catcher = roster[4]
        self.of1 = roster[5]
        self.of2 = roster[6]
        self.of3 = roster[7]
        self.util1 = roster[8]
        self.util2 = roster[9]
        self.ben1 = roster[10]
        self.ben2 = roster[11]
        self.ben3 = roster[12]
        self.totRuns, self.totAvg, self.totHr, self.totRbi, self.totSb, self.points = 0, 0, 0, 0, 0, 0

    def updateRoster(self):
        self.roster = [self.fBase, self.sBase, self.tBase, self.short, self.catcher,
                       self.of1, self.of2, self.of3, self.util1, self.util2, self.ben1,
                       self.ben2, self.ben3]

    def add(self, player):
        self.roster.append(player)


def getPosition(fname, pos):
    """This function will populate a list of potential players by position.
    The function returns the list and the number of players avaiable for that
    position.
    Parameters:
        pos: position of the players
        fname: file with the players of that position
    """
    count = 0
    infile = open(fname, "r")
    n_line = infile.readline()
    temp = []
    for line in infile:
        words = line.split(',')
        temp.append(Player(words[0], int(words[1]), int(words[2]), int(words[3]),
                           int(words[4]), float(words[5]), pos, 1))
        count += 1
    infile.close()
    return temp, count


def getDups(fname):
    """This function will populate a list of players eligible at multiple
    positions. Each element of the list is a string value corresponding to the player's name.
    """
    count = 0
    infile = open(fname, "r")
    n_line = infile.readline()
    temp = []
    for line in infile:
        words = line.split(',')
        temp.append(words[0])
        count += 1
    infile.close()
    return temp, count


def blankTeam():
    """Template for creating a blank team of Player objects.
    """
    temp = [Player("Some dude", 0, 0, 0, 0, 0, 0) for x in range(2)]
    return temp


def printPos(positionList):
    """Outputs to the screen the players available at the given position followed
    by the number of available players.
    Parameters:
        positionList: the list of players at a specific position
            ex. printPos(catchers)
    """
    print
    "Available players at position %s:\n" % (positionList[0].pos)
    i = 0  # used to count number of players at that pos.
    for player in positionList:
        if player.status == 1:
            print
            player.name
            i += 1
    print
    "\nTotal available: %d" % i


def markDrafted(name, pool):
    """Marks a player as drafted at all eligible positions.
    Parameters:
        name: string value for the name of the player; must be an EXACT match
        pool: the roster of all players at all positions
            ex. markDrafted("Miguel Cabrera",pool)
    """
    splitStr = name.split()
    if len(splitStr) == 1:
        print ("Please specify either a last name or a last initial")
        return

    for positionList in pool:
        for player in positionList:
            if name in player.name:
                player.status = 0
                print ("Player", player.name, " is no longer eligible at ", player.pos)


def markUndrafted(name, pool):
    """Marks a player as UNDRAFTED at all eligible positions; used if a mistake is made.
    Parameters:
        name: string value for the name of the player; must be an EXACT match
        pool: the roster of all players at all positions
            ex. markUndrafted("Miguel Cabrera",pool)
    """
    #TODO: Create logic that removes a player from the masterList when he's ineligible
    splitStr = name.split()
    if len(splitStr) == 1:
        print ("Please specify either a last name or a last initial")
        return

    for positionList in pool:
        for player in positionList:
            if name == player.name:
                player.status = 1
                print ("Player", player.name, " is now eligible at ", player.pos)


def genRandTeam(nPos, totPlayers):
    """Generates a random team of players to be returned as a list of integers. Integers represent
    a player's encoding in masterList.
    Paramter:
        nPos: list of total number of players at every position
        totPlayers: list of total number of players at every position
    """
    #          0         1       2       3       4       5    6
    # nPos = [nFirst, nSecond, nThird, nShort, nCatcher, nOf, nDh]
    chromosome = []
    sum = 0
    count = 0


    for i in nPos:  # general loop
        if count == 6:  # when loop enters the nDh players it instead chooses from ALL positions five times
            for j in range(5):  # to represent the 2 util positions and the 3 benches
                rNum = random.randint(0, totPlayers - 1)  # random number of ANY player
                chromosome.append(rNum)  # picks a random pos
            break  # no more work needs to be done
        if count == 5:  # this will occur before the previous loop; nOF must be iterated 3 times for 3 outfield spots
            for j in range(2):
                rNum2 = random.randint(0, i - 1)
                chromosome.append(rNum2 + sum)  # nOF must be iterated 3 times for 3 outfield spots; i is on oF
        rNum3 = random.randint(0, i - 1)
        chromosome.append(rNum3 + sum)
        sum += i
        count += 1
    # first = random.randint(0,nPos[0])
    # second = random.randint(0,nPos[1])
    # third = random.randint(0,nPos[2])
    # short = random.randint(0,nPos[3])
    # catcher = random.randint(0,nPos[4])
    # of = [random.randint(0,nPos[5]), random.randint(0,nPos[5]), random.randint(0,nPos[5])] #THREE outfielders
    # rNum = [random.randint(0,6) for i in range(5)] #random numbers representing one of the nPos rosters
    # util = [random.randint(0,nPos[rNum[0]]), random.randint(0,nPos[rNum[1]])] #picks 2 random players from ANY roster
    # ben = [random.randint(0,nPos[rNum[2]]), random.randint(0,nPos[rNum[3]]), random.randint(0,nPos[rNum[4]])] # picks 3 random players form any roster
    # print first,second,third,short,catcher,of,util,ben
    # temp = Team()
    return chromosome


def findDups(chromosome, nPos, totPlayers):
    """Enforces the rule that no chromosome can have the same player twice.
    """
    duplicate = 1
    while (duplicate == 1):
        dupsFound = 0
        tempList = [player for player in chromosome]
        tempList.sort()
        last = -1
        for current in tempList:
            if current == last:
                chromosome = genRandTeam(nPos, totPlayers)
                dupsFound = 1
                break
            last = current
        if dupsFound == 0:
            return chromosome


def genWorkingTeam(nPos, totPlayers):  # rename
    """Combines the genRandTeam() and findDups() functions to generate a
    working team.
    """
    chromosome = genRandTeam(nPos, totPlayers)
    chromosome = findDups(chromosome, nPos, totPlayers)
    newTeam = Team(chromosome)
    return newTeam


def genFirstPop(nPos, totPlayers, masterList, popSize=1000):
    """Generates the first population.
    """
    #TODO: replace genWorking team with a for loop that consolidates genRandTeam & findDups into this block
    population = [genWorkingTeam(nPos, totPlayers) for i in range(popSize)]
    population = getStats(population, masterList)
    return population


def getStats(population, masterList):
    """Will apply the stats of each individual player to the entirety of the team. Usually called after a new team
    is created.

    :param population:
    :param masterList:
    :return:
    """
    for team in population:
        for i in range(13): #13 are the number of roster spots?
            team.totHr += masterList[team.roster[i]].hr
            team.totAvg += masterList[team.roster[i]].avg
            team.totRuns += masterList[team.roster[i]].runs
            team.totSb += masterList[team.roster[i]].sb
            team.totRbi += masterList[team.roster[i]].rbi
            if i == 12:
                team.totAvg = team.totAvg / 13
    return population


def showStats(population, masterList, index):
    """Shows the total stats in the five categories of the population entered
    as a parameter.
    """
    count = 0
    if index == "all":
        for team in population:
            print ("Team at index", count)
            print("Tot Avg", team.totAvg)
            print("Tot Runs", team.totRuns)
            print("Tot HRs", team.totHr)
            print("Tot RBIs", team.totRbi)
            print("Tot SB", team.totSb)
            print("Tot points", team.points, '\n')
            count += 1
    else:
        print("Team at index", index)
        print("Tot Avg", population[index].totAvg)
        print("Tot Runs", population[index].totRuns)
        print("Tot HRs", population[index].totHr)
        print("Tot RBIs", population[0].totRbi)
        print("Tot SB", population[0].totSb)
        print("Tot points", population[0].points, '\n')


def swapStats(population, masterList, firstPos, secondPos):
    """Will swap the stats of any two index Teams belonging to a population
    by performing a deep copy onto the Team fields.
    """
    tempTeam = [Team(population[
                         firstPos].roster)]  # has to be a list since getStats takes a list of teams (meant to be used for populations)
    tempTeam = getStats(tempTeam, masterList)
    # print "Showing stats for tempTeam:"
    # showStats(tempTeam,masterList)
    # print tempTeam[0].roster
    population[firstPos].roster = population[secondPos].roster
    population[firstPos].totAvg = population[secondPos].totAvg
    population[firstPos].totSb = population[secondPos].totSb
    population[firstPos].totHr = population[secondPos].totHr
    population[firstPos].totRbi = population[secondPos].totRbi
    population[firstPos].totRuns = population[secondPos].totRuns
    population[firstPos].points = population[secondPos].points

    population[secondPos].roster = tempTeam[0].roster
    population[secondPos].totAvg = tempTeam[0].totAvg
    population[secondPos].totSb = tempTeam[0].totSb
    population[secondPos].totHr = tempTeam[0].totHr
    population[secondPos].totRbi = tempTeam[0].totRbi
    population[secondPos].totRuns = tempTeam[0].totRuns
    population[secondPos].points = tempTeam[0].points


def fitness(population, masterList):
    """Sorts

    :param population:
    :param masterList:
    :return:
    """
    # sorts based on average
    popSize = 0
    population.sort(key=lambda x: x.totAvg, reverse=True)  # sort by avg
    for team in population:  # find population size
        popSize += 1
    sumPoints(popSize, population, "avg")  # assigns fitness points based on ranking for avg

    population.sort(key=lambda x: x.totSb, reverse=True)  # sort by SB
    sumPoints(popSize, population, "sb")  # assigns fitness points based on ranking for SB

    population.sort(key=lambda x: x.totHr, reverse=True)  # sort by HRs
    sumPoints(popSize, population, "hr")  # assigns fitness points based on ranking for HRs

    population.sort(key=lambda x: x.totRbi, reverse=True)  # sort by RBIs
    sumPoints(popSize, population, "rbi")  # assigns fitness points based on ranking for RBIs

    population.sort(key=lambda x: x.totRuns, reverse=True)  # sort by Rs
    sumPoints(popSize, population, "runs")  # assigns fitness points based on ranking for Rs

    population.sort(key=lambda x: x.points, reverse=True)  # sorts by point rankings
    return population


def sumPoints(popSize, population, x):
    """There's some sort of math going on here that I don't quite remember formulating, but it works so I conjure the
    programmer's trusty credo: "We'll fix it in production."

    :param popSize:
    :param population:
    :param x:
    :return:
    """
    skipCount = 0
    for num in range(popSize):
        passParam = 0
        # print "pre-skip check; skip count is: ", skipCount
        if skipCount != 0:
            skipCount -= 1
            # print "skip detected"
            continue
        if num > 0:  # done this way because: if num = 0 population[num-1] will fail
            if x == "avg":  # each category evaluates a different attribute of the team
                if population[num - 1].totAvg == population[num].totAvg:
                    count, sentinel = 1, 1  # count is 1 because 1 data at that value has been detected already
                    while sentinel == 1:
                        if num + count <= popSize - 1:
                            if population[num + count - 1].totAvg == population[num + count].totAvg:
                                count += 1
                            else:
                                sentinel = 0
                        else:
                            sentinel = 0
                    for i in range(
                            count):  # for every n number of duplicates, this action is performed n-1 times since duplicates are treated when the second one is detected
                        population[num + i].points += popSize - num + 1
                        # print "points changed!"
                        # print num+i, population[num+i].points
                    skipCount += count - 1
                    # print "num",num
                    passParam = 1
            elif x == "sb":  # each category evaluates a different attribute of the team
                if population[num - 1].totSb == population[num].totSb:
                    count, sentinel = 1, 1  # count is 1 because 1 data at that value has been detected already
                    while sentinel == 1:
                        if num + count <= popSize - 1:
                            if population[num + count - 1].totSb == population[num + count].totSb:
                                count += 1
                            else:
                                sentinel = 0
                        else:
                            sentinel = 0
                    for i in range(
                            count):  # for every n number of duplicates, this action is performed n-1 times since duplicates are treated when the second one is detected
                        population[num + i].points += popSize - num + 1
                        # print "points changed!"
                        # print num+i, population[num+i].points
                    skipCount += count - 1
                    # print "num",num
                    passParam = 1
            elif x == "hr":
                if population[num - 1].totHr == population[num].totHr:
                    count, sentinel = 1, 1  # count is 1 because 1 data at that value has been detected already
                    while sentinel == 1:
                        if num + count <= popSize - 1:
                            if population[num + count - 1].totHr == population[num + count].totHr:
                                count += 1
                            else:
                                sentinel = 0
                        else:
                            sentinel = 0
                    for i in range(
                            count):  # for every n number of duplicates, this action is performed n-1 times since duplicates are treated when the second one is detected
                        population[num + i].points += popSize - num + 1
                        # print "points changed!"
                        # print num+i, population[num+i].points
                    skipCount += count - 1
                    # print "num",num
                    passParam = 1
            elif x == "rbi":
                if population[num - 1].totRbi == population[num].totRbi:
                    count, sentinel = 1, 1  # count is 1 because 1 data at that value has been detected already
                    while sentinel == 1:
                        if num + count <= popSize - 1:
                            if population[num + count - 1].totRbi == population[num + count].totRbi:
                                count += 1
                            else:
                                sentinel = 0
                        else:
                            sentinel = 0
                    for i in range(
                            count):  # for every n number of duplicates, this action is performed n-1 times since duplicates are treated when the second one is detected
                        population[num + i].points += popSize - num + 1
                        # print "points changed!"
                        # print num+i, population[num+i].points
                    skipCount += count - 1
                    # print "num",num
                    passParam = 1
            elif x == "runs":
                if population[num - 1].totRuns == population[num].totRuns:
                    count, sentinel = 1, 1  # count is 1 because 1 data at that value has been detected already
                    while sentinel == 1:
                        if num + count <= popSize - 1:
                            if population[num + count - 1].totRuns == population[num + count].totRuns:
                                count += 1
                            else:
                                sentinel = 0
                        else:
                            sentinel = 0
                    for i in range(
                            count):  # for every n number of duplicates, this action is performed n-1 times since duplicates are treated when the second one is detected
                        population[num + i].points += popSize - num + 1
                        # print "points changed!"
                        # print num+i, population[num+i].points
                    skipCount += count - 1
                    # print "num",num
                    passParam = 1
            if passParam == 0:  # will only be 0 if no repeats are detected; alterative to putting an else statement in each category if clause
                population[num].points += popSize - num  # in which case: business as usual
                # print "more points yo"
        else:
            population[num].points += popSize - num  # business as usual
            # print "getting them points"
            # print num, population[num].points


def genNextPop(prevPop, masterList, popSize):
    """Generates the next population and performs a crossover operation.

    :param prevPop: previous generation
    :param masterList: full list of all elligible players
    :param popSize: size of the population of each generation (fixed)
    :return: returns a new population (gen)
    """
    parSize = int(popSize / 10) #top 10%
    parentPop = [Team(prevPop[i].roster) for i in range(parSize)]
    parentPop = getStats(parentPop, masterList)  # inefficent
    rosterSize = len(parentPop[0].roster)
    newPop = []
    #parentsList = [] #debug
    for i in range(popSize):
        chromosome = doCrossover(parentPop, parSize, rosterSize)
        newPop.append(Team(chromosome))
    getStats(newPop, masterList)
    #showStats(newPop, masterList, "all")
    #debug code
    #for playerInd in chromosome:
    #   print(masterList[playerInd].pos)

    return newPop

def doCrossover(parentPop, parSize, rosterSize):
    """Performs a crossover operation on the provided params and returns a new chromosome;
        crossover point is randomly generated each time. The child gets everything from the beginning
        of the first parent up to the crossover (not including); from the crossover point to the end of the second parent,
        each element is copied onto the remainder of the child.

        :param parentPop: previous generation
        :param parSize: size of the population of each generation (fixed)
        :param rosterSize: size of a roster (const)
        :return: returns a chromosome
        """

    firstPar = random.randint(0, parSize - 1)
    secondPar = random.randint(0, parSize - 1)
    while secondPar == firstPar:
        secondPar = random.randint(0, parSize - 1)

    crossOverPt = random.randint(1, rosterSize - 2)  # random num between second and second-to-last entry

    # debugging code
    # for i in range(rosterSize):
    # parentPop[firstPar].roster[i] = 2*i
    # parentPop[secondPar].roster[i] = 2*i + 1

    # first parent mapping
    chromosome = [parentPop[firstPar].roster[i] for i in range(crossOverPt)]

    # second parent mapping
    remainingLoops = rosterSize - len(chromosome)
    for i in range(remainingLoops):
        chromosome.append(parentPop[secondPar].roster[crossOverPt + i])
    return chromosome

def areTeamStatsEqual(team1, team2):
    if team1.totRuns == team2.totRuns and team1.totAvg == team2.totAvg and team1.totHr == team2.totHr \
            and team1.totRbi == team2.totRbi and team1.totSb == team2.totSb and team1.points == team2.points:
        return 1
    else:
        return 0

def getPlayerPool():
    #TODO: get rid of?
    firstBase, nFirst = getPosition("first.csv", "1B")
    secondBase, nSecond = getPosition("second.csv", "2B")
    thirdBase, nThird = getPosition("third.csv", "3B")
    short, nShort = getPosition("short.csv", "SS")
    catcher, nCatcher = getPosition("catchers.csv", "C")
    of, nOf = getPosition("of.csv", "OF")
    dh, nDh = getPosition("dh.csv", "DH")
    duplicates, nDup = getDups("duplicates.csv")
    pool = [firstBase, secondBase, thirdBase, short, catcher, of, dh]  # roster of all players at all positions; multi-dimensional list
    nPos = [nFirst, nSecond, nThird, nShort, nCatcher, nOf, nDh]

    # construction of masterList below
    # Player order: name, hr, runs, rbi, sb, avg, pos, status
    masterList = []
    totPlayers = nFirst + nSecond + nThird + nShort + nCatcher + nOf + nDh
    for playerList in pool:
        for player in playerList:
            masterList.append(Player(player.name, player.hr, player.runs, player.rbi,
                                     player.sb, player.avg, player.pos, player.status))
    return pool, nPos, masterList, totPlayers

def decodeRoster(nextGen, ind):
    for index in nextGen[ind].roster:
        print(masterList[index].name, " ", masterList[index].pos)

#pre-loading for positions
#TODO: Make global?
firstBase, nFirst = getPosition("first.csv", "1B")
secondBase, nSecond = getPosition("second.csv", "2B")
thirdBase, nThird = getPosition("third.csv", "3B")
short, nShort = getPosition("short.csv", "SS")
catcher, nCatcher = getPosition("catchers.csv", "C")
of, nOf = getPosition("of.csv", "OF")
dh, nDh = getPosition("dh.csv", "DH")
duplicates, nDup = getDups("duplicates.csv")
pool = [firstBase, secondBase, thirdBase, short, catcher, of, dh]  # roster of all players at all positions; multi-dimensional list
nPos = [nFirst, nSecond, nThird, nShort, nCatcher, nOf, nDh]

masterList = []
totPlayers = nFirst + nSecond + nThird + nShort + nCatcher + nOf + nDh
for playerList in pool:
    for player in playerList:
        masterList.append(Player(player.name, player.hr, player.runs, player.rbi,
                                 player.sb, player.avg, player.pos, player.status))
def testRtrn():
    list = [1,2,3,4,5,6]
    for i in range(len(list)):
        print (list[i])


def runSimulation(pool = pool, nPos = nPos, masterList = masterList, totPlayers = totPlayers):

    # creates lists of potential players with their stats
    # first identifier is the list, second identifier is number of players per position

    popSize = 100
    allPops = []

    #First generation creation
    gen0 = genFirstPop(nPos, totPlayers, masterList, popSize)
    fitness(gen0, masterList)
    allPops.append(gen0)

    #Subsequent gens
    sentinel = 1
    timesRun = 0
    gens = [Team(gen0[i].roster) for i in range(popSize)]
    while sentinel:
        timesRun += 1
        gens = genNextPop(gens, masterList, popSize)
        fitness(gens, masterList)
        allPops.append(gens)
        if areTeamStatsEqual(gens[0], gens[1]):
            sentinel = 0
    decodeRoster(gens, 0)
    #for index in nextGen[0].roster:
    #   print(masterList[index].name, " ", masterList[index].pos)
    return gens

#gen = runSimulation()