__author__ = 'andrewwhiter'
# good examples of how you use randomness and to calculate pi and integral

import random, time
from statistics import mean, stdev

def throwDarts(numDarts):
    ''' returns the ratio of darts in a quadrant to darts thrown '''
    ''' times value returned by 4 to get an estimate for pi'''
    inQuadrant = 0
    for _ in range(numDarts):
        x, y  = random.random(), random.random()  # random number between 0 and 1 for the x and y coordinate
        if (x**2 + y**2)**0.5 <= 1.0:  # take square root of x plus y squared
            inQuadrant += 1
    return inQuadrant / numDarts

# >>>throwDarts(50000)


def getEst(numDarts, numTrials):
    ''' returns mean of pi given a number of trials and the stdev '''
    ''' requires the throwDarts() function '''
    estimates = []
    for _ in range(numTrials):
        piGuess = 4 * throwDarts(numDarts)
        estimates.append(piGuess)
    sDev = stdev(estimates)
    meanPIEst = mean(estimates)
    print('PI Est. = {:.5f}, Std. dev. = {:.5f}, Darts = {:d}'.format(meanPIEst,sDev,numDarts))
        # .5f defines to only print 5 digits after comma
    return meanPIEst, sDev

# >>>getEst(50000,10)


def runPI(precision, numTrials):  # statistically good to keep number of trials at around 100
    numDarts = 1000
    sDev = precision
    while sDev >= precision/2.0:
        piEst, sDev = getEst(numDarts, numTrials)
        numDarts *= 2
    return piEst

# >>>runPI(0.001, 100)


def timeFunction(fun, arg, iterations):
    timeList=[]
    for i in range(iterations):
        start = time.time()
        fun(arg)
        duration = time.time() - start
        timeList.append(duration)
    return sum(timeList)/iterations

# >>>timeFunction(throwDarts, 50000, 10)


def runInt(numDarts):
    ''' returns the ratio of darts in a quadrant to darts thrown '''
    ''' integral of XYZ form 0 to 1 '''
    inQuadrant = 0
    for _ in range(numDarts):
        x, y  = random.random(), random.random()  # random number between 0 and 1 for the x and y coordinate
        if y < x**2:
            inQuadrant += 1
    return inQuadrant / numDarts  # result approximately 1/3

# >>>runInt(50000)
