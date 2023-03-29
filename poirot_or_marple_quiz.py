print("=== Poirot or Marple? Agatha Christie TV Episode Recommendations===")
print()
print("You will be asked a series of questions, based on your answers you will receive a recommendation from TV episodes of Agatha Christie's famous detectives, Hercule Poirot and Jane Marple.")
print()
print("Before you begin, please note that this recommendation tool is CAsE SEnsITivE. That means that you need to pay close attention to both spelling and case.")
print()
print("Ready? Let's go!")
print()
tvDetective  = input("What are you in the mood to watch today, Poirot or Miss Marple? >")
if tvDetective == "Poirot":
  print()
  print("OK, let's recommend an episode of 'Poirot' for you!")
  print()
  print("For the next question, use either 'David Suchet or 'Peter Ustinov' as a response.")
  print()
  tvPoirot = input("Would you like to watch an episode from the ITV series starring Sir David Suchet, or from the feature-length films starring Sir Peter Ustinov? >")
  if tvPoirot == "David Suchet":
    print()
    print("Aha! You're a fan of this superbly observed and executed canonical series. Good choice!")
    print()
    print("For the next question, use either 'Short' or 'Long' as a response, depending on which type of episode you want to watch!")
    print()
    epLength = input("Next question: Are you in the mood for one of the earlier, shorter episodes from Series 1-5 or any of the longer, feature-length episodes? >")
    print()
    if epLength == "Short":
      print("""There are many wonderful shorter episodes from Series 1-5.However, may I recommend:
      'The Million Dollar Bond Robbery', Series 3 - Episode 3
      'The Yellow Iris', Series 5 - Episode 3""")
    else:
      print("A longer episode, great!")
      print()
      epLengthLong = input("Would you prefer a longer episode from the earlier canon, Series 2-7? Or would you prefer a feature-length episdode from the later canon, Series 8-13?. Type 'Earlier' or 'Later', depending on your preference.>")
      if epLengthLong == "Earlier":
        print("""May I recommend:
        'The Mysterious Affair at Styles', Series 3 - Episode 1
        'The ABC Murders', Series 4 - Episode 1
        'Murder on the Links', Series 6 - Episode 3""")
      else:
        print()
        print("Okay. There are a lot of fantastic feature-length episodes from the later series, so I need to ask a couple of further follow-up questions.")
        print()
        poirotOliver = input("Would you like to watch an episode featuring Zoe Wannamaker as fictional author Ariadne Oliver? Answer 'Yes' or 'No'.>")
        if poirotOliver == "Yes":
          print("""May I recommend: 
          'Mrs McGinty's Dead', Series 11 - Episode 1
          'Cards on the Table', Series 10 - Episode 2""")
        else:
          print()
          print("OK then.")
          print()
          finalSeries = input("Would you like to watch an episode from the final series, Series 13? >")
          if finalSeries == "Yes":
            print()
            print("May I recommend 'The Labours of Hercules', Series 13 - Episode 4")
          else:
            print("""May I recommend: 
            'The Mystery of the Blue Train', Series 10 - Episode 1 
            'Murder of the Orient Express', Series 12 - Episode 3
            'An Appointment with Death', Series 11 - Episode 4""")
  else:
    print()
    print("So you're a fan of Sir Ustinov's 'Poirot' films, are you?")
    print("For the next question, answer either '1' or '2'.")
    print()
    tvPoirotUs = input("From which era of Sir Peter Ustinov's Poirot would you like to watch? (1) 1978-1982 or, (2) 1986-1988? >")
    if tvPoirotUs == "1":
      print()
      print("May I recommend 'Evil Under the Sun' (1982).")
      print("It stars Dame Maggie Smith, Dame Diana Rigg, Jane Birkin, Nicholas Clay, and Roddy McDowall.")
    else:
      print()
      print("May I recommend 'Appointment with Death'.")
      print("It stars Lauren Bacall, Carrie Fisher, Sir John Gielgud, Hayley Mills, David Soul, and Piper Laurie.")
elif tvDetective == "Miss Marple": 
  print()
  print("So you'd like to watch a Miss Marple crime story?")
  print()
  print("For the next question, please respond with either 'Joan Hickson', 'Geraldine McEwan' or, 'Julia Mckenzie'.")
  print()
  tvMarple = input("Would you like to watch from the BBC series starting Joan Hickson or from the ITV series starring Geraldine McEwan and Julia McKenzie? >")
  if tvMarple == "Joan Hickson":
    print()
    print("Excellent choice.")
    print()
    seriesHickson = input("Which Joan Hickson series would you like to watch? Answer 'Series 1', 'Series 2', or 'Series 3'>")
    if seriesHickson == "Series 1":
      print()
      print("Series 1 it is! May I recommend 'A Murder is Announced'.")
    elif seriesHickson == "Series 2":
      print()
      print("Series 2 it is! May I reccomend 'At Bertram's Hotel'.")
    elif seriesHickson == "Series 3":
      print()
      print("Series 3 is also a good choice!")
      print("> May I recommend 'The 4:50 From Paddington'.")
    else:
      print("Maybe you're not such a Joan Hickson fan after all!")
  elif tvMarple == "Geraldine McEwan":
    print()
    print("Superb! The later series on ITV represent an excellent choice, although some details of the plot and characters have been altered from the original, and in ways that in some instances change the meaning of the storyline.")
    print()
    print("""For Geraldine McEwan as Miss Marple, may I recommend:
    'A Murder is Announced', Series 1 - Episode 4
    'Sleeping Murder', Series 2 - Episode 1
    'At Bertram's Hotel', Series 3 - Episode 1
    'Ordeal by Innocence', Series 3 - Episode 2""")
  elif tvMarple == "Julia McKenzie":
    print()
    print("Superb! The later series on ITV represent an excellent choice, although some details of the plot and characters have been altered from the original, and in ways that in some instances change the meaning of the storyline.")
    print()
    print("""For Julia McKenzie as Miss Marple, may I recommend:
    'Murder is Easy', Series 4 - Episode 2
    'The Secret of Chimneys', Series 5 - Episode 2
    'At Bertram's Hotel', Series 3 - Episode 1
    'Endless Night', Series 6 - Episode 3""")
  else:
    print("Looks like you're not such a fan of the ITV Miss Marple after all!")
else: 
  print()
  print("Are you sure you want to watch a Poirot or Miss Marple today?")
  print("> It seems like you didn't type 'Poirot' or 'Miss Marple'.")
