#
# Example file for working with conditional statements
#

def main():
  x, y = 510, 100
  
  # conditional flow uses if, elif, else  
  if(x < y):
    st= "x is less than y"  # paid attention
  elif (x == y):
    st= "x is same as y"  # paid attention
  else:
    st= "xc  Nana  is  greater than y ain't that true by Duvan -bla bla bla kjskdjks xzx"
    print()
    print()

  print (st)
  print() 
 


  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x < y) else "x is greater  than or equal to y_ Really Chris bayala x 2??   xcxcxcxcxc"  
  print()
  print (st)
  print() 

  
  # Python does not have support for higher-order conditionals
  # like "switch-case" in other languages
  
if __name__ == "__main__":
  main()
