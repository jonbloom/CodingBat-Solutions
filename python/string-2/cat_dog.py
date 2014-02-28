def cat_dog(str):
  numCat = 0
  numDog = 0
  for i in range(len(str)):
    if str[i:i+3] == 'cat':
      numCat += 1
    if str[i:i+3] == 'dog':
      numDog += 1
  return numCat==numDog