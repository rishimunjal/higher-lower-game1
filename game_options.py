import random
import game_data

#encapsulate game data in option class
class game_option:
  
  def __init__(self):
    self.name = ''  
    self.follower_count = 0
    self.description = ''
    self.country = ''

def __map_option(game_data_option):
  opt = game_option()
  opt.name = game_data_option['name']
  opt.follower_count = game_data_option['follower_count']
  opt.description = game_data_option['description']
  opt.country = game_data_option ['country']
  return opt
  

def __map_options(game_data_options):
  mapped_options = []
  for item in game_data_options:
    mapped_options.append(__map_option(item))
  return mapped_options

  

def get_random_options(number_of_options):
  data = random.choices(population = game_data.data,k = number_of_options)
  return __map_options(data)

def get_random_option_except(number_of_options, exclude_name):
  data = random.choices(population = game_data.data,k = number_of_options + 1)
  #print(data)
  
  filtered_data  = [item for item in data if item['name']!=exclude_name]
  #print(filtered_data[:number_of_options])

  if len(filtered_data) == number_of_options:
    return __map_options(filtered_data[:number_of_options])
  else:
    return __map_options(filtered_data)

  
    