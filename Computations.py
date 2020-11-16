import math
def factorial(n: int)->int:
    if n==1:
        return n
    else:
        return n*factorial(n-1)

def combinations(total_trials: int, specific_outcomes: int)->int:
    return factorial(total_trials)/(factorial(total_trials-specific_outcomes)*factorial(specific_outcomes))
print(combinations(10,3))

#bernouilli or binomial
def discrete_binomial_distributiion(total_trials: int, specific_outcomes:int, probability_p: float):
    return combinations(total_trials,specific_outcomes) * probability_p**specific_outcomes * \
           (1-probability_p)**(total_trials-specific_outcomes)
#positive
def discrete_poission_distribution(parameter_lambda: int, k_num_times_event_occurs: int):
    return parameter_lambda**k_num_times_event_occurs*math.exp(-parameter_lambda)/factorial(k_num_times_event_occurs)

print(discrete_poission_distribution(2.78,11))