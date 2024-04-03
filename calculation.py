def calc_mean(list_of_measurements : list[int]):
  """ Eine Funktion, die eine Liste von Werten übernimmt und das arithmetische Mittel zurück gibt"""

  mean_value = sum(list_of_measurements) / len(list_of_measurements)
  return mean_value