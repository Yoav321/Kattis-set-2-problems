"""
figures out if a match can fit in a certain size box.
Yoav Bierkatz, Jude Averitt | September 2026
"""

def main() -> None:
  n, a, b = input().split(" ")
  n = int(n)
  a = int(a)
  b = int(b)
  import math
  c = math.sqrt(a**2 + b**2)
  for _ in range (0,n):
    match: int = int(input("")) 
    if match <= c:
      print("DA")
    else:
      print("NE")

if __name__ == "__main__":
  main()
    
