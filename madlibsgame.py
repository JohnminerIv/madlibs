words = []


def inputs():
    x = 0
    while x <= 8:
        if x < 2:
            words.append(input("Please tell me an adjective: "))
            pass

        elif x < 4 and x > 1:
            words.append(input("Please tell me a noun: "))
            pass
        elif x < 6 and x > 3:
            words.append(input("Please tell me a verb: "))
            pass
        elif x < 7 and x > 5:
            words.append(input("Please tell me a name: "))
            pass
        elif x <= 8 and x > 6:
            words.append(input("Please tell me an adverb: "))
            pass
        else:
            words.append("")
            pass
        x = x + 1
        pass


inputs()
print(f'''This morning I woke up to a very {words[0]} thing.
When I investigated it turned out to be a {words[2]}.
Very {words[7]} I decided to wake up my room mate {words[6]} so we could
marvle at the {words[1]} but before our very eyes it turned into a
{words[3]}. Since we were kind of freaked out we decided to {words[4]}
as {words[8]} as we could away from the still morphing object."
''')
