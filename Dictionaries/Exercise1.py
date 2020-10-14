def display_facts(facts):
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))

facts = {'Ricky' : 'Is scared of clowns.',
           'Jason' : 'Plays the piano.',
           'David' : 'Can fly an airplane.'}

display_facts(facts)

facts['Bob'] = 'Cant sing.'
facts['Mike'] = 'Plays basketball.'

print()
display_facts(facts)
