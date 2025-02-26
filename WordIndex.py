#WordIndex.py
#Name: Ella Falk
#Date: 2/26/25
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  
  wordList = {} #create an empty dictionary
  lineNum = 0

  for line in textFile:
    lineNum = lineNum + 1
    words = line.split()
    for word in words:
      #process word to make uniform
      word = word.lower()
      word = word.replace("," , " ")
      word = word.replace("." , " ")
      word = word.replace("/n" , " ")
      word = word.replace("!" , " ")


      if word in wordList:
        wordList[word].append(lineNum)      #add to existing entry
      else:
        wordList[word] = [lineNum]          #add word to list
  #print results
  for word in wordList:
    print(word, wordList[word])


  """
  print ("fish" in words) #is a word already in the dictionary?
  words["fish"] = [2]     #add a list to the dictionary
  print ("fish" in words) #is the word there now?
  words["fish"].append(5) #add to an existing list
  print(words)
  """

if __name__ == '__main__':
  main()
