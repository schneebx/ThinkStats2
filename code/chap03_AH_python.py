# Exercise 3.2 Calculating mean and variance

# Need this to create a PMF object
import thinkstats2

pmf_test = thinkstats2.Pmf([1, 2, 2, 3, 5]) # Using Pmf from the textbook for testing

def PmfMean(pmf_object):
    output_mean = 0.0
    for key, value in pmf_object.d.items(): # .d to go one level deeper to the dictionary in order to loop through with items(). .d added from referencing solutions but understand the level.
        output_mean += value*key
    return output_mean

def PmfVar(pmf_object):
    output_variance = 0.0
    for key, value in pmf_object.d.items():
        output_variance += value*((key - PmfMean(pmf_object))**2)
    return output_variance

print('Using:', pmf_test)
print('Mean:', PmfMean(pmf_test))
print('Variance:', PmfVar(pmf_test))
