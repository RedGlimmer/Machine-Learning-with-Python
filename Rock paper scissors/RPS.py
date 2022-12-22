def player(prev_play, opponent_history=[], my_history=['']):
  guess = "S"
  predict = None

  # Opponent moves history
  opponent_history.append(prev_play)

  # level of insight
  level = 3
  # Predict opponent's next move
  for i in range(len(opponent_history)):
    match = 0
    for j in range(level):
      if i - j > 0 and opponent_history[-1] == opponent_history[i]:
        if opponent_history[-1 - j] == opponent_history[i - j]:
          if my_history[-1 - j] == my_history[i - j]:
            match += 1
    if match >= level and i + 2 <= len(opponent_history):
      predict = opponent_history[i+1]
      break

  # Act according to prediction
  if predict == "R":
    guess = "P"
  elif predict == "P":
    guess = "S"
  elif predict == "S":
    guess = "R"

  # My moves history
  my_history.append(guess)
  
  return guess