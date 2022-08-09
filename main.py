def strRotation(s1: str, s2: str) -> str:
  tmp1 = s2
  tmp2 = s2
  leftRotation = 0
  rightRotation = 0

  if len(s1) != len(s2):
    return "Invalid strings. Must contain same length."

  while s1!=tmp1:
    rightRotation += 1
    tmp1 = tmp1[1:len(s1)] + tmp1[0]
    print("tmp1", tmp1)
    if rightRotation >= len(s1):
      break

  while s1!= tmp2:
    leftRotation+=1
    tmp2 = tmp2[len(s1)-1:] + tmp2[:len(s1)-1]
    print("tmp2", tmp2)
    if leftRotation >= len(s1):
      break
  print("rightRotation", rightRotation)
  print("leftRotation", leftRotation)
  if leftRotation < rightRotation:
    return "Output" + str(leftRotation-rightRotation)
  elif leftRotation == rightRotation:
    return "Output" + str(rightRotation)
  else:
    return "Output" + str(rightRotation)

print(strRotation('abc','cab'))
