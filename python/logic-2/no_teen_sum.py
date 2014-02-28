def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  return 0 if n>=13 and n<15 or n>16 and n<= 19 else n
