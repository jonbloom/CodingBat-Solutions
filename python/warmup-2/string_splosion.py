def string_splosion(str):
  return "".join([str[0:i+1] for i in range(len(str))])