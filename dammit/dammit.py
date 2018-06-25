import random

class Dammit:
  @staticmethod
  def dammit(string):
    words = string.split(' ')
    return_string = list()
    for word in words:
      word = list(word.upper())
      length = len(word)
      indices_array = range(length)
      random_choice = random.choice(indices_array)
      for ind in range(random_choice):
        rand_choice = random.choice(indices_array)
        word[rand_choice] = word[rand_choice].lower() 
      return_string.append(''.join(word))
    return ' '.join(return_string)
  
