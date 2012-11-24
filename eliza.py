import os
import random

def say(message):
    os.system("say '%s'" % (message))

def say_and_print(message):
    print message
    say(message)

def get_contextual_reply(message):
    l = [
        ('james', 'What is your favorite thing about James?'),
        ('mommy', 'What color does mommy like the best?'),
        ('daddy', 'What food does daddy like to eat the most?'),
        ('no', 'Tell me.  Why not?'),
        ('you', 'We are talking about you. Not me.'),
        ('I', 'Do you always talk about yourself so much?'),
        ('me', 'Do you always talk about yourself so much?')
    ]
    for pattern, reply in l:
        if message.find(pattern) != -1:
            return reply
    return ''

def get_random_reply():
    l = [
        'Does my head smells like poop?',
        'Anyone like tennis?',
        'Is Mommy is a silly goose',
        'What do you want to talk about?',
        'What is your favorite game?'
        'What movie do you like the most?']
    return l[random.randint(0, len(l) - 1)]

def get_reply(message):
    return  get_contextual_reply(message) or get_random_reply()

def should_exit(s):
    return s == 'bye' or s == 'quit'
        
def main():
    random.seed()
    say_and_print('Hello. How can I help you?')
    human = ''
    while True:
        human = raw_input('> ')
        if should_exit(human):
            break
        say_and_print(get_reply(human))
    say_and_print('Goodbye.')

if __name__=='__main__':
    main()
