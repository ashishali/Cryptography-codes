m=26
def getdata():
  while True:
    print("Encrypt or Decrypt?")
    inp=input().lower()
    if inp in 'encrypt e decrypt d'.split():
      return inp
    else:
      print('Enter either "encrypt" or "e" or "decrypt" or "d"')

def getmsg():
  print("Enter your msg:")
  return input()

def getkey():
  key=0
  while True:
    print('Enter the key number (1-%s)' %(m))
    key=int(input())
    if (key>=1 and key <=m):
      return key

def encmsg(inp,msg,key):
  if inp[0]=='d':
    key=-key
  encrypted=''

  for symbol in msg:
    if symbol.isalpha():
      num=ord(symbol)
      num+=key
    
      if symbol.isupper():
        if num>ord('Z'):
          num-=26
        elif num<ord('A'):
          num+=26
      elif symbol.islower():
        if num > ord('z'):
          num-=26
        elif num< ord('a'):
          num+=26
    
        encrypted += chr(num)
      else:
        encrypted+=symbol
  return encrypted
inp=getdata()
msg=getmsg()
key=getkey()

print("Encrypted msg is:")
print(encmsg(inp,msg,key))

#this does not work for numbers and special characters
