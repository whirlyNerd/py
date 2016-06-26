# I would always recommend using parentheses
# to indicate the start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.

zoo = ('python', 'elephant', 'penguin')

print 'The number of animals in the zoo is', len(zoo)

new_zoo = ('monkey', 'camel', zoo)

print 'Number of cages in the new zoo is', len(new_zoo)
print 'All animals in the new_zoo are', new_zoo
print 'Animals from from the old zoo are', new_zoo[2]
print 'Last animal from the old zoo is', new_zoo[2][2]
print 'Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2])
