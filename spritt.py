"""
Describe your program.
Yoav Bierkatz, Jude Averitt | September 2026
"""

def main() -> None:
  n, x, = input().split(" ")
  n = int(n)
  x= int(x)
  total:int =0 

  for _ in range (n):
    a: int = int (input(""))
    total += a
    
  if total <= x: 
    print("Jebb")
  else:
    print("Neibb")

  

if __name__ == "__main__":
  main()
    
