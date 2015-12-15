import pylab

pylab.figure(1)
pylab.plot([1,2,3,4], [2,4,6,8])

pylab.figure(2)
pylab.plot([1,4,2,3])
pylab.show()

"""------------- x and y plots"""
# data
principal, interestRate, years = 10000, 0.05, 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate

# plot the data
pylab.plot(values, 'ro', label="data")  # ro stands for red circles
pylab.plot([0,20], [10000, 28000], color="green", linestyle='dashed', label = "trend")
pylab.axis([0, 20, 0, 30000])  # .axis defines the magnitude of x and y axes
pylab.legend()
pylab.title('5% Growth, \nCompounded Annually', fontsize='xx-large')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')
pylab.savefig('Figure-1')
pylab.show()

"""------------- bar charts"""
# data
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars default width = 0.8, so add 0.1 to the left to centre
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
pylab.bar(xs, num_oscars)
pylab.ylabel("# of Academy Awards")
pylab.title("My Favorite Movies")

# label x-axis with movie names at bar centers
pylab.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

pylab.show()

"""------------- scatterplot"""
# data
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

pylab.scatter(friends, minutes)
# label each point
for label, x, y in zip(labels, friends, minutes):
    pylab.annotate(label,
                 xy=(x, y),  # put the label with its point
                 xytext=(5, -5),  # but slightly offset
                 textcoords='offset points')

pylab.title("Daily Minutes vs. Number of Friends")
pylab.xlabel("# of friends")
pylab.ylabel("daily minutes spent on the site")
pylab.show()
