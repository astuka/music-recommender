rap = ["rap","36 Chambers", "My Beautiful Dark Twisted Fantasy", "Be", "4eva Is A Mighty Long Time", "17", "ALL-AMERIKKKAN BADA$$"]
jazz = ["jazz","The Black Saint and the Sinner Lady", "The Clown", "A Love Supreme"]
electronic = ["electronic", "In Colour", "2012-2017"]
rock = ["rock","The Dark Side of the Moon","Red", "The Velvet Underground & Nico"]
indie = ["indie", "All The Pain Money Can Buy","American Football", "Atta Girl", "Heavenly vs Satan", "OK Computer"]
pop = ["pop", "Art Angels", "Bonito Generation"]

genres = [rap, jazz, electronic, rock,indie,pop]

found = 0

def print_list(li):
  for i in li:
    if li[0] == i:
      print("")
    else:
      print(i)

album = input("What album do you like? ")


for i in genres:
  for j in i:
    if album == j:
      print("Try out these albums: ")
      print_list(i)
      found = 1

if found == 0:
  g = input("Couldn't find it. What genre would you say this album is in? ")
  for i in genres:
    if i[0] == g:
      print("Try out these albums: ")
      print_list(i)
      found = 1
      i.append(album)
