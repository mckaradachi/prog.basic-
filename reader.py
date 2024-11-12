import pickle
with open("stud_dict.pkl", "rb") as file:
  stud_dict = pickle.load(file)

  for i in stud_dict:
      print(f"{i} grade:")
      for b in stud_dict[i]:
          print(f" {b}:  \n")
          print(*stud_dict[i][b], sep='\n' + '')
          print()
      print()