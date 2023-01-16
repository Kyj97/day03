#5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song.replace(' m', ' M'))

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

#5.3
print("""My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s.""" %('roast beef', 'ham', 'head', 'clam'))

letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room},especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our test, is {percent}% less likely to have {verbed}.

Thank you for your support. 
Sincerely,
{spokesman}
{job_title}"""




print(letter)