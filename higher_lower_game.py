#get two random items from the list
import art
import game_options

#get the two options to be presented to the player
def get_options(option1):
  options = []

  if option1 is None:
    #get two random options for the first try
    options = game_options.get_random_options(2)
  else:
    #continue the winning option from the previous try
    options.append(option1)
    #add a second random option which is different from the winning option from previous try
    option2 = game_options.get_random_option_except(1, option1.name)[0]
    options.append(option2)

  return options

  #display art
def display(option1, option2, message_last_round = ''):
  print(f'{art.logo} \n {message_last_round} \n Compare A:{option1.name}  a {option1.description}, from {option1.country} \n {art.vs}\n Against B:{option2.name}  a {option2.description}, from {option2.country}')


#get player response to the options presented
def get_player_response():
  response = input("Who has more followers? Type A or B: ")
  return response


#compare the follower count of the two option. 
#check player responses

def check_player_response(options, response):
  #return true if the follwer count of the choosen option is bigger else return false
  if response == 'A':
    if options[0].follower_count > options[1].follower_count:
      return True
    else:
      return False
  elif response == 'B':
    if options[1].follower_count > options[0].follower_count:
      return True
    else:
      return False
  else:
    return False

#this function is called only when the player gets the answer right and used to refresh the options presented to the player
def refresh_player_options(options, response):
  if response == 'A':
    del options[1]
  elif response == 'B':
    del options[0]
  
  return get_options(options[0])



def play():
  score = 0
  options = get_options(option1 = None)
  display(options[0],options[1])

#play as long as the player is able to pick the correct choice
  continue_playing = True
  while continue_playing:
    response = get_player_response()

    if check_player_response(options, response) == True:
      #increment the player score by 1 if they got it right
      score += 1
      message = 'You are right!! your current score is ' + str (score)
      options = refresh_player_options(options, response)

      display(options[0],options[1],message)
    else:
      print(f'You are wrong!! your current score is {score}')
      continue_playing = False



