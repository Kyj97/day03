#6.1

for k in [3, 2, 1, 0]:
    print(k)

6.2
guess_me = 7
number = 1

while True:
    if number > guess_me:
        print('oops')
        break
    elif number == guess_me:
        print('found it!')
        break

    else:
        number < guess_me
        print('too low')
        number = number + 1


#6.3
guess_me = 5
for number in range(1, 10):
    if number > guess_me:
        print('oops')
        break
    elif number == guess_me:
        print('found it!')
        break
    else:
        number < guess_me
        print('too low')
