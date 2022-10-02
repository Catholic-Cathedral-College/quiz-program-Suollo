def main():
  #this is all init stuff e.g resetting score
  #random function
  import random
  #set score
  score = 0
  #set ans 1 integer value
  answer1 = 0
  #set ans 2 integer value
  answer2 = 0
  #set ans 3 integer value
  answer3 = 0
  #set easy difficulty integer value
  diffe=0
  #set medium difficulty integer value
  diffm=0
  #set hard difficulty integer value
  diffq=0
  #rng lists
  listeasy = [1, 2, 3]
  listmedium = [1, 2, 3]
  listhard = [1, 2, 3]
  #set tries to 0
  tries = 0
  #set gamemode integer value
  gamemode = 0

#-----------------Beginning of code---------------------#
#asking user for gamemode 
  strgamemode = input("WELCOME TO ELI'S QUIZ GAME FOR MY DIGITECH CLASS WORK ASSESMENT THING\n PLEASE CHOOSE A GAMEMODE OUT OF THE FOLLOWING\n 1 = SET AMOUNT MODE 2 = SCORE REACH MODE")
  #checks if its an integer and continues based on that output
  if strgamemode.isdigit():
    gamemode = int(strgamemode)
    if gamemode == 1:
      #this is set question mode
      while True:
        #asks for how many questions you want
        strloop = input("How many questions do u wantt?")
        #checks to see if this is a valid input and parses it into an int
        if strloop.isdigit():
          loop = int(strloop)
          #asks at what difficulty you wish to play at
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
              print("please input an integer corresponding to a difficulty")
          
            
            #these are getting diff 1 question answers
            #this line checks to see if the random number is corresponding to its question
            if diffe == 1:
              #this resets the number to insure the question is not repeated next turn, i had quite an issue with this a week ago and the fix was surprisingly easy
              diffe = 0
              #this asks the question and is prompting the user to input an integer corresponding to the correct answer
              answer1 = int(input("What is the official name of the car driven by the main antagonist in Tokyo drift\n          1                     2                     3                     4\n      Skyline R34           Fairlady z           Trueno AE86           Levin AE85\n"))
              #this checks if the user inputted answer is correct
              if answer1 == 2:
                #this adds one to the score and prints the result
                score = score + 1
                print("correct")
              else:
                #this prints the incorrect message
                print("Incorrect")
            
            elif diffe == 2:
              diffe = 0
              answer2 = int(input("what does JDM stand for?""\n 1           2          3        4  ""\nJeep      John's     Japanese  Jalpa\nDump      Demon      Domestic  Dominated\nMachines  Machines   Market    Market\n"))
              if answer2 == 3:
                score = score + 1
                print("correct")
              else:
                
                print("Incorrect")
            elif diffe == 3:
              diffe = 0
              answer3 = int(input("Where did JDM originate?""\n    1        2        3        4   \n Jermany    China    USA      Japan\n"))
            
              if answer3 == 4:
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
              answer1 = int(input("What is considered as one of the most popular Car media pieces ever\n   1         2         3          4        \nNaruto   Initial d  RE:zero   Yoko ono\n"))
              if answer1 == 2:
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
              answer1 = int(input("what is an alternate name for the Mazda Rx-7 FD\n  1           2           3            4\n Rxv2         Jdm4        FD3          MR7\n"))
              if answer1 == 3:
                score = score + 1
                print("correct")
              else:
                print("Incorrect")
            
            if diffq == 2:
              diffq = 0
              answer1 = int(input("What car was used to win all races between 1990 to 1993 in the Japanese touring car championships\n         1            2          3                  4        \n    Porche 918    Mazda Rx7  Ferrari Fxx    Nissan skyline \n"))
              if answer1 == 4:
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
          break
          #o
        else:
          print("please input an integer ")
    elif gamemode == 2:
      #this is set score mode
      strgamescoregoal = input("To how much score do you wish to play to")
      if strgamescoregoal.isdigit():
        gamescoregoal = int(strgamescoregoal)
        while score != gamescoregoal:
          diff = input("What difficulty would you like to play at? 1 = easy    2 = medium    3 = hard")
          #this uses a random number generator to randomly choose a question from the three difficultys
          if diff == "1":
            diffe = random.choice(listeasy)
          elif diff == "2":
            diffm = random.choice(listmedium)
          elif diff == "3":
            diffq = random.choice(listhard)
          else:
            print("please input an integer corresponding to a difficulty")
        
          
#these are getting diff 1 question answers
          #this line checks to see if the random number is corresponding to its question
          if diffe == 1:
            #this resets the number to insure the question is not repeated next turn, i had quite an issue with this a week ago and the fix was surprisingly easy
            diffe = 0
            #this asks the question and is prompting the user to input an integer corresponding to the correct answer
            answer1 = int(input("What is the official name of the car driven by the main antagonist in Tokyo drift\n          1                     2                     3                     4\n      Skyline R34           Fairlady z           Trueno AE86           Levin AE85\n"))
            #this checks if the user inputted answer is correct
            if answer1 == 2:
              #this adds one to the score and prints the result
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              #this prints the incorrect message
              print("Incorrect")
              #this adds one to the tries counter and reduces score by one
              tries = tries + 1
              score = score - 1
          if diffe == 2:
            diffe = 0
            answer2 = int(input("what does JDM stand for?""\n 1           2          3        4  ""\nJeep      John's     Japanese  Jalpa\nDump      Demon      Domestic  Dominated\nMachines  Machines   Market    Market\n"))
            if answer2 == 3:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          if diffe == 3:
            diffe = 0
            answer3 = int(input("Where did JDM originate?""\n    1        2        3        4   \n Jermany    China    USA      Japan\n"))
          
            if answer3 == 4:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          
#these are the diff 2 questions and answers
          if diffm == 1:
            diffm = 0
            answer1 = int(input("Who is the founder of the famous tuner shop : Top Secret\n       1                2                3                4\nSmokey Nagata      Apirana Taylor   Xi jinping      Hideo Kojima\n"))
            if answer1 == 1:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          if diffm == 2:
            diffm = 0
            answer1 = int(input("What is considered as one of the most popular Car media pieces ever\n   1         2         3          4        \nNaruto   Initial d  RE:zero   Yoko ono\n"))
            if answer1 == 2:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          if diffm == 3:
            diffm = 0
            answer1 = int(input("What is the leading japanese car manufacturing company\n   1        2         3        4\nToyota    Nissan   Daihatsu  Honda\n"))
            if answer1 == 1:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
        #these are the diff 3 answers and questions
          if diffq == 1:
            diffq = 0
            answer1 = int(input("what is an alternate name for the Mazda Rx-7 FD\n  1           2           3            4\n Rxv2         Jdm4        FD3          MR7\n"))
            if answer1 == 3:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          
          if diffq == 2:
            diffq = 0
            answer1 = int(input("What car was used to win all races between 1990 to 1993 in the Japanese touring car championships\n         1            2          3                  4        \n    Porche 918    Mazda Rx7  Ferrari Fxx    Nissan skyline \n"))
            if answer1 == 4:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
          
          if diffq == 3:
            diffq = 0
            answer1 = int(input("What, now retired, Japanese Racing gang was widely considered to be the greatest?\n        1                2                3                  4        \nThe midnight club   Bosozoku Yakuza  Akina Speedstars  Shiganshina Samurais\n"))
            if answer1 == 1:
              score = score + 1
              print("correct")
              tries = tries + 1
            else:
              print("Incorrect")
              tries = tries + 1
              score = score - 1
        
        print("good on ya mate, you achieved", gamescoregoal, "in", tries, "tries")
        
    elif gamemode > 2:
      print("Please input a corresponding integer")  
  else:
    print("Please input an integer")
main()
#could you belive I did the entire second gamemode in one day after getting the idea while watching the new cyberpunk anime?
#its true, even rn im listening to its soundtrack