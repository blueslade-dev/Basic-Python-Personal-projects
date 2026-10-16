import random
import time
import pyttsx3

print("==QUEERAI==")
msg = "Hi I am QueerAI hope I can make you feel very naughty today!"
print(msg)
pyttsx3.speak(msg)

subjects = ['Anna','Rahul','Mohan','Jingping','Biggy Booms','Yesungchinchungandrenath']
actions = ['saw','thought of','ate','likes']
adjectives = ['delicious','yummy','Suspicious','Gut-smashing','Optimistic','Auspicious']
objects = ['pancake','pizza','burger','waffle','juang-chang','lemons','juicy melons']
vowels = ['a','e','i','o','u']

subject = random.choice(subjects)
action = random.choice(actions)
adjective = random.choice(adjectives)
x = adjective[0]  
object = random.choice(objects)
y = object[-1]

def get_article(string):
  if string[0] in vowels and string[-1] != "s":
    article = "an"
  elif string[-1] == "s":
    article = "the"
  else:
    article = "a"
  return article

def get_adverb():
  if adjective[-1] == "y":
    adverb = adjective[:-1] + "ily"
  elif adjective[-2:] == "le":
    adverb = adjective[:-1] + "y"
  elif adjective[-2:] == "ic":
    adverb = adjective + "ally"
  else:
    adverb = adjective + "ly"
  return adverb

def get_sentence():
  def template1():
    sentence =  f"I see {get_article(f"{object}")} {object}, {subject} {action} it {get_adverb()}."
    return sentence
  def template2():
    sentence = f"{subject} {action} {get_article(f"{object}")} {object} {get_adverb()}"
    return sentence
  def template3():
    sentence = f"{subject} {action} {get_article(f"{adjective} {object}")} {adjective} {object}."
    return sentence
  sentence_choices = [template1(),template2(),template3()]
  return random.choice(sentence_choices)

i = 0
sussy_set = set()
print("Here are twenty special sussy sentences for you:")
pyttsx3.speak("Here are twenty special sassy sentences for you:")
while i < 20:
  subject = random.choice(subjects)
  action = random.choice(actions)
  adjective = random.choice(adjectives)
  x = adjective[0]  
  object = random.choice(objects)
  y = object[-1]
  
  sentence = get_sentence()
  if sentence not in sussy_set:
    print(sentence)
    pyttsx3.speak(sentence)
    sussy_set.add(sentence)
    i += 1
    time.sleep(0.01)
  else:
    continue
time.sleep(0.75)
msg2 = "I hope you liked my juicy sentences!"
print(msg2)
pyttsx3.speak("I hope you liked my juicy sentences!")