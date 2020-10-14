def get_word(word_type):
    if word_type.lower() == 'adjective' or 'adverb':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input('Enter a word that is {0} {1}: '.format(a_or_an, word_type))

def fill_in_the_blanks(noun, verb, adjective, adverb):
    story = "Today I went to the zoo. I saw {2} {0} jumping up and down in its tree. "\
            "He {1} {3} through the large tunnel that led to its {2} {0}. "\
            "I got some peanuts and passed them through the cage to a gigantic gray {0} towering above my head. "\
            "Feeding that animal made me hungry. "\
            "I went to get a {2} scoup of icecream. It filled my stomach. "\
            "Afterwards I had to {1} {3} to catch our bus. "\
            "When I got home I {1} my mom for a {2} day at the zoo. ".format(noun, verb, adjective, adverb)
    return story

def display_story(story):
    print("")
    print("Here is the story you created. Enjoy!")
    print("")
    print(story)

def create_story():
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')
    adverb = get_word('adverb')

    the_story = fill_in_the_blanks(noun, verb, adjective, adverb)
    display_story(the_story)

create_story()

"""
Today I went to the zoo. I saw a(n)
___________(adjective)
_____________(Noun) jumping up and down in its tree.
He _____________(verb, past tense) __________(adverb)
through the large tunnel that led to its _______(adjective)
__________(noun). 
I got some peanuts and passed
them through the cage to a gigantic gray _______(noun)
towering above my head. Feeding that animal made
me hungry. I went to get a __________(adjective) scoop
of ice cream. It filled my stomach. Afterwards I had to
__________(verb) __________ (adverb) to catch our bus.
When I got home I __________(verb, past tense) my
mom for a __________(adjective) day at the zoo.
"""