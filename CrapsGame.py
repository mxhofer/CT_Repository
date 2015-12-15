"""------------- crabs gambling game"""
from statistics import *

class CrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0  # attributes for holding the data
        self.dpWins, self.dpLosses, self.dpTies = 0, 0, 0  # dp = dont't pass

    def playHand(self):
        throw = rollDie() + rollDie()
        if throw == 7 or throw == 11:
            self.passWins += 1
            self.dpLosses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.passLosses += 1
            if throw == 12:
                self.dpTies += 1
            else:
                self.dpWins += 1
        else:
            point = throw
            while True:
                throw = rollDie() + rollDie()
                if throw == point:
                    self.passWins += 1
                    self.dpLosses += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    self.dpWins += 1
                    break

    def passResults(self):
        return (self.passWins, self.passLosses)

    def dpResults(self):
        return (self.dpWins, self.dpLosses, self.dpTies)

    def crapsSim(handsPerGame, numGames):
        # Play numGames games
        games = []
        for t in range(numGames):
            c = CrapsGame()
            for i in range(handsPerGame):
                c.playHand()
            games.append(c)

        # Produce statistics for each game
        pROIPerGame, dpROIPerGame = [], []
        for g in games:
            wins, losses = g.passResults()
            pROIPerGame.append((wins - losses)/handsPerGame)
            wins, losses, ties = g.dpResults()
            dpROIPerGame.append((wins - losses)/handsPerGame)

        # Produce and print summary statistics
        print("Craps Simulation: hands per game = {} number of games = {}".format(handsPerGame,numGames))

        meanROI = 100.0 * mean(pROIPerGame)
        sigma = 100.0 * stdev(pROIPerGame)
        print ("Pass: Mean ROI = {:.4g}% Std. Dev. = {:.4g}%95% Conf. Int. = {:.4g}% to {:.4g}%"
                .format(meanROI, sigma, meanROI-2*sigma, meanROI+2*sigma))

        meanROI = 100.0 * mean(dpROIPerGame)
        sigma = 100.0 * stdev(dpROIPerGame)
        print ("Don\'t pass: Mean ROI = {:.4g}% Std. Dev. = {:.4g}%95% Conf. Int. = {:.4g}% to {:.4g}%"
                .format(meanROI, sigma, meanROI-2*sigma, meanROI+2*sigma))


# >>>CrapsGame.crapsSim(5,10)
# >>>CrapsGame.crapsSim(5,10)
