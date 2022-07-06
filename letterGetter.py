def letterArrays():

  adjArray = []
  nounArray = []
  verbArray = []
  
  file = open("adjectives.txt", "r")
  for word in file:
    adjArray.append(word.strip())
  file.close()

  file = open("nouns.txt", "r")
  for word in file:
    nounArray.append(word.strip())
  file.close()

  file = open("verbs.txt", "r")
  for word in file:
    verbArray.append(word.strip())
  file.close()

  return adjArray, nounArray, verbArray