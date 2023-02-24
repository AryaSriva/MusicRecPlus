'''Names: Aryaman Srivastava, Michael Klikushin, Sabrina Trestin
CS115-C Group Project Part 2
We pledge our honor that we have abided by the Stevens Honor System'''
file = open("musicrecplus.txt", "a")
def menu(name, file):
    '''Prompts the user to enter a letter and will redirect the user based on the option they pick and will continue to prompt the user until the user picks a valid option
authors: Aryaman'''
    i = 0
    while i == 0:
      ans = input("Enter a letter to choose an option:\ne - Enter Preferences\nr - Get Recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - which user has the most likes\nq - save and quit \n")
      if ans == "e":
        enterPreferences(name)
      elif ans == "r":
        getRecommendations(name)
      elif ans == "p":
        showMostPopular()
      elif ans == "h":
        howPopular()
      elif ans == "m":
        mostLikes()
      elif ans == "q":
        saveAndQuit(name, file)
        break

def enterPreferences(name):
  '''Change the preferences of the user with the given username with new preferences that the user inputs
authors: Aryaman, Michael, Sabrina'''
  newArtists = input("Enter an artist that you like ( Enter to finish ):")
  correctArtist = newArtists.strip().title()
  database[name] = []
  while newArtists != "":
    database[name].append(correctArtist)
    newArtists = input("Enter an artist that you like ( Enter to finish ):")
    correctArtist = newArtists.strip().title()

def getRecommendations(name):
  '''Prints recommendations for the user based of users with similar likes. If no users with similar likes are found, the function will print "No recommendations available at this time." authors: Aryaman, Sabrina, Michael'''
  userArtists = database[name]
  localMax = 0
  maxUser = ["no artist reccomendations found"]
  for person in database:
    sameArtists = 0
    if person != name and person[-1] != "$":
      for song in database[person]:
        if song in userArtists:
          sameArtists += 1
      if sameArtists > localMax and sameArtists != len(userArtists):
        localMax = sameArtists
        maxUser[0] = person
  if maxUser[0] == "no artist reccomendations found":
    print("No recommendations available at this time.")
    return None
  else:
    for artist in database[maxUser[0]]:
      if artist not in userArtists:
        print(artist)

def showMostPopular():
  '''Prints the 3 most popular music artists across all users(i.e. the music artist liked by the most users)
authors: Aryaman, Michael'''
  numDict = artistsAndLikes()
  max = mostPopular(numDict)
  usedArtist = []
  i = 1
  while i <= 3:
    for artist in numDict:
      if artist == max and artist[-1] != "$":
        numDict[artist] = 0
        max = mostPopular(numDict)
        usedArtist += [artist]
        i += 1

  for i in range(len(usedArtist)):
    if i <= 2:
      print(usedArtist[i])
    else:
      break

def artistsAndLikes():
  '''returns a dictionary with all the artists in the text file and their respective number of likes
authors: Aryaman'''
  numDict = {}
  for user in database:
    if user[len(user) - 1] != "$":
      for artist in database[user]:
        if artist not in numDict:
          numDict[artist] = 1
        else:
          numDict[artist] += 1
  return numDict

def mostPopular(numDict):
  '''returns the most popular music artist
  authors: Aryaman'''
  mostPopular = {0: ""}
  max = 0
  for artist in numDict:
    if numDict[artist] > max:
      mostPopular[0] = artist
      max = numDict[artist]
  return mostPopular[0]
  
def howPopular():
  '''prints the number of likes of the most popular artist
  authors: Michael'''
  numDict = artistsAndLikes()
  max = 0
  for artist in numDict:
    if numDict[artist] > max:
      max = numDict[artist]
  print(max)
  

def mostLikes():
  '''returns the user with the most number of liked artists
  authors: Michael and Sabrina'''
  localmax = 0
  greatestUser = ""
  for user in database:
    if len(database[user]) > localmax:
      localmax = len(database[user])
      greatestUser = user
  print(greatestUser)
    

def saveAndQuit(name, file):
  '''saves the users preferences into the file and then closes the file
  authors: Aryaman'''
  write_file("", "musicrecplus.txt")
  for user in database:
    append_file(user + ":", "musicrecplus.txt")
    for i in range(len(database[user])):
      if i != len(database[user]) - 1:
        append_file(database[user][i] + ",", "musicrecplus.txt")
      else:
        append_file(database[user][i] + "\n", "musicrecplus.txt")
  file.close()

def read_preferences(filename):
  '''read the users and their preferences in the file
  authors: Aryaman'''
  dic = {}
  with open(filename, "r") as f:
      for line in f:
          [username, singers] = line.strip().split(":")
          singersList = singers.split(",")
          dic[username] = singersList
  return dic

database = read_preferences("musicrecplus.txt")
def startup():
  '''start of the program: opens the file and prompts the user to enter their name, if their name is in the text file, they will be prompted to a menu. If their name is not in the text file, they will be prompted to enter their preferences
  authors: Aryaman, Michael, Sabrina'''
  #file = open("musicrecplus.txt", "a")
  name = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
  #database = read_preferences("musicrecplus.txt")
  if name not in read_file("musicrecplus.txt"):
    database[name] = []
    preference = input("Enter an artist you like (Enter to finish) \n")
    correctArtist = preference.strip().title()
    while preference != "":
      database[name].append(correctArtist)
      preference = input("Enter an artist you like (Enter to finish) \n")
      correctArtist = preference.strip().title()
  menu(name, file)
       

def read_file(filename):
  '''read contents of a file with the given filename
  authors: Aryaman'''
  myfile = open(filename, "r")
  contents = myfile.read()
  myfile.close()
  return contents

def write_file(string, filename):
  '''write a string to the file of the given filename
  authors: Aryaman'''
  myfile = open(filename, "w")
  myfile.write(string)
  myfile.close()

def append_file(string, filename):
  '''append a string to the file of the given filename
  authors: Aryaman'''
  myfile = open(filename, "a")
  myfile.write(string)
  myfile.close()

startup()