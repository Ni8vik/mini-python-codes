import time as tm


def fashtex (text):
      '''displays your text in fashion like a profashional hacker!!!
      notes:it doesn't need to be in print
      '''
      text = str(text)
      bi = ""
      num = [1, 2, 3, 4, 5, 6, 7, 8, 9, "#"]
      for i in text:
            if i == " ":
                  bi += i
                  print(bi)
                  tm.sleep(0.05)
            for j in range(10):
                  if num[j] == "#" or str(j) == i:
                        print(bi, num[j], sep="")
                        bi += i
                        print(bi)
                        tm.sleep(0.05)
                        break
                  else:
                        print(bi, num[j], sep="")
                        tm.sleep(0.05)

fashtex("hello world")



