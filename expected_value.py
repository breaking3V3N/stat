
def square_list(values: list):
    squared_list = []
    for element in values:
        squared_list.append(element**2)
    return squared_list

def discrete_expected_value(values: list, probabilities: list)->float:
    expected = 0
    for x in range (0,len(values)):
        expected += values[x] * probabilities[x]
    return expected
#integrate in class form
def discrete_variance_one(values: list, probabilities: list)->float:
    variance = 0
    expect = discrete_expected_value(values,probabilities)
    for x in range(0,len(values)):
        variance += ((expect-values[x])**2) * probabilities[x]
    return variance
def discrete_variance_two(values: list, probabilities: list)->float:
    variance = 0
    expect = discrete_expected_value(values,probabilities)
    expect_squared = discrete_expected_value(square_list(values),probabilities)
    variance = expect_squared - expect**2
    return variance

