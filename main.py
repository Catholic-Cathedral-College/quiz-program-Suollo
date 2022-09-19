def main():
  #this is all init stuff e.g resetting score
  import random
  import keyboard
  score = 0
  answer1 = 0
  answer2 = 0 
  answer3 = 0
  diffe=0
  diffm=0
  diffq=0
  listeasy = [1, 2, 3]
  listmedium = [1, 2, 3]
  listhard = [1, 2, 3]
  while True:
    if keyboard.read_key() == "x":
      break
    loop = int(input("How many questions do u wantt?"))
    for i in range(loop):
      diff = input("What difficulty would you like to play at? 1 = easy    2 = medium    3 = hard")
      #this uses a random number generator to randomly choose a question from the three difficultys
      if diff == "1":
        diffe = random.choice(listeasy)
      elif diff == "2":
        diffm = random.choice(listmedium)
      elif diff == "3":
        diffq = random.choice(listhard)
      else:
        print("  ____  _      _ \n |  _ \(_) ___| |\n | | | | |/ _ \ |\n | |_| | |  __/_\n |____/|_|\___(_)")
        exit()
      #these are getting diff 1 question answers
      if diffe == 1:
        diffe = 0
        answer1 = int(input("What is the official name of the car driven by the main antagonist in Tokyo drift\n          1                     2                     3                     4\n      Skyline R34           Fairlady z           Trueno AE86           Levin AE85\n"))
        if answer1 == 2:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
      elif diffe == 2:
        diffe = 0
        answer2 = int(input("what does JDM stand for?""\n   1         2          3        4  ""\nJapanese    John's     Jeep      Jalpa\ndomestic    Demon      Dump      Dominated\nMarket      Machines   Machines  Market\n"))
        if answer2 == 1:
          score = score + 1
          print("correct")
        else:
          
          print("Incorrect")
      elif diffe == 3:
        diffe = 0
        answer3 = int(input("Where did JDM originate?""\n  1        2        3        4   \n Japan    China    USA      Jermany\n"))
      
        if answer3 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
    #these are the diff 2 questions and answers
      if diffm == 1:
        diffm = 0
        answer1 = int(input("Who is the founder of the famous tuner shop : Top Secret\n       1                2                3                4\nSmokey Nagata      Apirana Taylor   Xi jinping      Hideo Kojima\n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
      if diffm == 2:
        diffm = 0
        answer1 = int(input("What is considered as one of the most popular Car media pieces ever\n    1         2        3          4        \nInitial d   Naruto  RE:zero   Yoko ono\n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
      if diffm == 3:
        diffm = 0
        answer1 = int(input("What is the leading japanese car manufacturing company\n   1        2         3        4\nToyota    Nissan   Daihatsu  Honda\n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
    #these are the diff 3 answers and questions
      if diffq == 1:
        diffq = 0
        answer1 = int(input("what is an alternate name for the Mazda Rx-7 FD\n  1           2           3            4\n FD3         Jdm4        Rzx          MR7\n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
      if diffq == 2:
        diffq = 0
        answer1 = int(input("What car was used to win all races between 1990 to 1993 in the Japanese touring car championships\n                1            2          3           4        \n        Nissan skyline    Mazda Rx7  Ferrari Fxx Porche 918 \n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
      
      if diffq == 3:
        diffq = 0
        answer1 = int(input("What, now retired, Japanese Racing gang was widely considered to be the greatest?\n        1                2                3                  4        \nThe midnight club   Bosozoku Yakuza  Akina Speedstars  Shiganshina Samurais\n"))
        if answer1 == 1:
          score = score + 1
          print("correct")
        else:
          print("Incorrect")
    if score == loop:
      print("good on ya mate, your score was", score, "out of", loop)
    elif score < loop:
      print("you disappointment! this why you not doctor yet! You only get",score ,"out of", loop)
    
    #oUo
main()