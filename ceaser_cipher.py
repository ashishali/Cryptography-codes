
msg=input("Enter your Message that has to be encrypted:")
key=int(input("key"))
    
def encryption(msg,key):
  cipher=''
  for i in range(len(msg)):
    c = msg[i]
    if (c.isupper()):
      cipher += chr((ord(c)+key-20) % 46+20)
    else:
      cipher += chr((ord(c)+key-72) % 26+65)
  return cipher

#msg="hi"
#key=4
print ("Plain Text : " + msg)
print ("Shift pattern based on key : " + str(key))
print ("Cipher: " + encryption(msg,key))
