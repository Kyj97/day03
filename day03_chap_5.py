#5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song.replace(' m', ' M'))

#idx = song.rfind('m')
#song2 = song.replace(song[idx], song[idx].upper())
#print(song2.endswith('moray!'))

# song_list = song.split()
# print(song_list)
# song_list[14] = song_list[14].title()
# song_string = ' '.join(song_list)
# print(song_string)


#5.2
#Q: question
#A: answer

questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed kont.",
    "'Pop!' goes the weasel."
]
print(f'Q:{questions[0]}')
print(f'A:{answers[0]}')
print(f'Q:{questions[1]}')
print(f'A:{answers[1]}')
print(f'Q:{questions[2]}')
print(f'A:{answers[2]}')



#5.3
print("""My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.""" %('roast beef', 'ham', 'head', 'clam'))
print("My kitty cat likes %s,\nMy kitty cat likes %s,\nMy kitty cat fell on his %s And now thinks he's a %s." %('roast beef', 'ham', 'head', 'clam'))



#5.4
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room},especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our test, is {percent}% less likely to have {verbed}.

Thank you for your support. 
Sincerely,
{spokesman}
{job_title}"""

#5.5
print(letter.format(salutation='aa', name='me', product='mouse', verbed='is', room='bang', animals='cats', amount='bb', percent='40', spokesman='cc', job_title='backsu'))


#5.6
duck = 'duck'
gourd = 'gourd'
spitz = 'spitz'
print("%sy Mc%sface" % (duck, duck))
print("%sy Mc%sface" % (gourd, gourd))
print("%sy Mc%sface" % (spitz, spitz))

#5.7
print("{0}y Mc{0}face" .format (duck, gourd, spitz))
print("{1}y Mc{1}face" .format (duck, gourd, spitz))
print("{2}y Mc{2}face" .format (duck, gourd, spitz))


#5.8
print(f"{duck}y Mc{duck}face")
print(f"{gourd}y Mc{gourd}face")
print(f"{spitz}y Mc{spitz}face")
