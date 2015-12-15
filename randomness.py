"""------------- randomness"""
import random

def rollDie():
    return random.randint(1,6)
    # or alternatively: random.choice([1,2,3,4,5,6])
# random.random()
# random.uniform(1, 10)
# random.randrange
# random.shuffle(items)

# >>>rollDie()

def flip(numFlips):
    ''' returns the relative frequency of heads
    	after numFlips flips '''
    heads = 0.0
    for i in range(numFlips):
        if random.choice(["heads","tails"])=="heads":
            heads += 1
    return heads/numFlips

# >>>flip(10)

def flipSim(numFlips, numTrials):
    ''' returns the mean relative frequency after
    	numTrials trials each with numFlips flips  '''
    freqHeads = []
    for i in range(numTrials):
        freqHeads.append(flip(numFlips))
    mean = sum(freqHeads)/numTrials
    return mean

# >>>flipSim(10,5)


def flipPlot(minExp, maxExp, numFlips=100):
    """Plots results of 2**minExp to 2**maxExp trials"""
    relfreq = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        x = 2**exp
        xAxis.append(x)
        relfreq.append(flipSim(numFlips,x))
    pylab.xlabel('Number of Trials')
    pylab.ylabel('Mean Rel Freq of Heads')
    pylab.plot(xAxis, relfreq, [0,2**maxExp],[0.5,0.5])
    pylab.semilogx()  # this makes the x axis logarithmic
    pylab.show()

random.seed(0)  # initialize the basic random number generator
# >>>flipPlot(1, 14)
