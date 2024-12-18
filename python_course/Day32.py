# secret code language
# coding and decoding

st = input("Enter the message please: ")
words = st.split(" ")
coding = True
# coding = False
if(coding):
 newords = []
 for word in words:
    if(len(word)>=3):
        r1 = "gdf"
        r2 = "ewr"
        stnew1 = r1 + word[1:] + word[0] + r2
        # print(st)
        newords.append(stnew1)
    else:
      newords.append(word[::-1])    
 print(" ".join(newords))

else:
  newords = []
  for word in words:
    if(len(word)>=3):
      stnew1 = word[3:-3]
      stnew1 = stnew1[-1] + stnew1[:-1]
      newords.append(stnew1)
    else:
      newords.append(word[:])
  print(" ".join(newords))
  
     