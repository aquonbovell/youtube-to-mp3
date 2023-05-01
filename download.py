from convert import convert

with open('links.txt') as links:
  for link in links:
    convert(link)