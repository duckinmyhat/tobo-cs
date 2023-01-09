def make_decision(data):
  # Use an AI algorithm (such as a decision tree or neural network) to analyze the data and make a recommendation
  recommendation = AI_algorithm(data)
  
  # Return the recommendation to the manager
  return recommendation

# Test the decision support system
data = [{'sales': 500, 'cost': 400}, {'sales': 600, 'cost': 450}, {'sales': 700, 'cost': 500}]
print(make_decision(data))