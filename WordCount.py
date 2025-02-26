#WordCount.py
#Name: Ella Falk
#Date: 2/26/25
#Assignment: Lab 6

def main():
  textFile = open("gettysberg.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  for line in textFile:
    lineCount += 1

    words = line.split()
    
    for word in words:
      wordCount += 1
      
      for letter in word:
        letterCount += 1
  
  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Letters:", letterCount)
        
  

if __name__ == '__main__':
  main()
