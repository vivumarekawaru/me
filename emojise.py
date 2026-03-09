"""
import requests
"""
#a=requests.get("https://carpedm20.github.io/emoji/emoji.json")
#try:
 #   data = a.json()
  #  print("JSON:", data)
#except Exception as e:
#    print("JSON decode failed:", e)

#print("Status:", a.status_code)
#print("Length:", len(a.text))
#print("Raw:", a.text)
#14176517
"""
a="hey i whould hey i whoul hey i whou hey i who hey i wh hey i w hey i hey i hey  hey"
b=a.replace(" ",'')
b=a.replace("hey"," " )
b=a.split()
i=0
 "hey" in a:
    
    print (f"hey {b[i]}")
    i=i+1
"""
#highest ascii of text other than emoji is 122
"""

url = "https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias"
a = requests.get(url).text

def emojizer(c):
  ind1 = (a.find(f"{c}")-10)
  if ord(a[ind1]) > 122 :             
    return (a[ind1])                                                                                             #jugad
  
  else:
    c=c.replace(":","{",1)
    c=c.replace(":","}")
    ind=a.find(c)     
    proxy=a.rfind(":",0,ind)
    ind2=(a.rfind(":",0,proxy))-10
    return(a[ind2])
"""


#idea 
#split and look with startswith : and replace in a loop 
#check if output is an emoji
#print in the loop
#use emojizer()
"""
#noob code but works------------------------------------------------------------------------------
txt=txt.split()
for id , word in enumerate(txt):
  if word.startswith(":") and word.endswith(":"):                                #only handles codes not alias
    txt[id]=emojizer(word)
    
print(" ".join(txt))

--------------------------------------------------------------------------------------------------
"""
"""
#better code, works, but still not satisfied------------------------------------------------------

txt=input("text to be emojized: ")
txt=txt.split()
ctxt=txt.copy()
cword=""
x=0
for id , word in enumerate(txt):
  if word.startswith(":") and word.endswith(":"):
    txt[id]=emojizer(word)

  elif word.startswith(":") and (not word.endswith(":")):                       #can handle both but only one at a time
    x=10
    for id2,word2 in enumerate(txt[id:]):
      ind=ctxt.index(word2)
      ctxt.pop(ind)
      if word2.endswith(":"):
        cword += " " + (word2)
        cword=cword.strip()
        break
      cword += " " + (word2)
    try:
      ctxt[id]=emojizer(cword)
    except IndexError:
      ctxt.extend([None])
      ctxt[id]=emojizer(cword)



      
if x==10:
  print(' '.join(ctxt))
else:
  print(" ".join(txt))

-----------------------------------------------------------------------------------------------
"""
"""
# first deal with ctxt, and then input the output to deal with txt.

def main(txt,y):
  txt=txt.split()
  ctxt=txt.copy()
  cword=""
  x=0
  for id , word in enumerate(txt):
    if word.startswith(":") and word.endswith(":"):
      txt[id]=emojizer(word)

    elif word.startswith(":") and (not word.endswith(":")):                      
      x=10
      for id2,word2 in enumerate(txt[id:]):
        ind=ctxt.index(word2)
        ctxt.pop(ind)
        if word2.endswith(":"):                                                                         #almost but don't work
          cword += " " + (word2)
          cword=cword.strip()
          break
        cword += " " + (word2)
      try:
        ctxt[id]=emojizer(cword)
      except IndexError:
        ctxt.extend([None])
        ctxt[id]=emojizer(cword)



        
  if x==10:
    y=10
    return(' '.join(ctxt),y)
  else:
    y=0
    return(" ".join(txt),y)



y=0
a,y=main(input("text to be emojized: "),y)
if y==10:
  a,y=main(a,y)
  print(a)
else:
  print(a)




#hey :smiley: hello :SMILING CAT FACE WITH OPEN MOUTH:
#hey :smiley: hello 😺
#hey 😃 hello :SMILING CAT FACE WITH OPEN MOUTH:


---------------------------------------------------------------------------------------------------------------------
"""
# satisfaction-------------------------------------------------------------------------------------------------------
# note to self--- you need to use venv2
import requests

url = "https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias"
a = requests.get(url).text                                                                     #converts to text since i cant use json as its an html

def emojizer(c):
  ind1 = (a.find(f"{c}")-10)                                                                   #gets the index of first : in the text ( since i saw its 10 unit after emoji) (jugaad)
  if ord(a[ind1]) > 122 :                                                                      #confirms that its an emoji
    return (a[ind1])
  
  else:
    c=c.replace(":","{",1)                                                                     
    c=c.replace(":","}")
    ind=a.find(c)     
    proxy=a.rfind(":",0,ind)                                 #this implies its the alias and not the code(i noticed the alice is written after the code so i looked for the code in the form of :...:)
    c=c.replace(":","}")
    ind2=(a.rfind(":",0,proxy))-10
    return(a[ind2])

def easy_pnctn(txt):                                                   #this is the the one wich also avoids issues with punctuation.
  txt=txt.split()
  for id , word in enumerate(txt):
    if word.startswith(":") and word.endswith(":"):                    #no need to woory about single strings as they two would turn to a unit entity in alist due to split
      txt[id]=emojizer(word)
    if word.startswith(":") and (not word.endswith(":")):
      sym_chk=word.replace(":","",1)
      if ":" in sym_chk:
        sym_chk=word.replace(":"," ").split()
        txt[id]=(f"{emojizer(f':{sym_chk[0]}:')}{sym_chk[1]}")
  return(" ".join(txt))


def easy(txt):
  txt=txt.split()                                                                             
  for id , word in enumerate(txt):
    if word.startswith(":") and word.endswith(":"):                    #no need to woory about single strings as they two would turn to a unit entity in alist due to split
      txt[id]=emojizer(word)
  return(" ".join(txt))

def harder(txt):                                                 #it takes a string change it to a list of strings and then checks where : begins starts a new var and remembers the index 
#                                                                  where it began untill another ends with :, and then replace that whole part with the emoji and then goes furthur  
  txt=txt.split()
  ctxt=txt.copy()                                                           
  cword=""
  x=0
  for id,word in enumerate(txt):
    if word.startswith(":") and (not word.endswith(":")):                       
      for _,word2 in enumerate(txt[id:]):                                   #enumerate helps to get rid of i=i+1
        ind=ctxt.index(word2)
        if x==0:                                                            #to do this only once
          nid=ctxt.index(word2)                                             #since index keep changing we need to find new instantanous index
        ctxt.pop(ind)
        if word2.endswith(":"):
          cword += " " + (word2)                                            #append for strings
          cword=cword.strip()
          ctxt.insert(nid,emojizer(cword))                                  #only places it there and shifts everything right
          x=0
          cword=""                                                          #turns cword blank again
          break
        cword += " " + (word2)
    
  return(' '.join(ctxt))    
 
txt=input("text to be emojized: ")
txt=easy_pnctn(txt)
txt=harder(txt)
print(txt)




