story = [
    "This morning I woke up to a very ",
    " thing. When I investigated it turned out to be a ", ".Very ",
    "I decided to wake up my room mate ", " so we could marvle at the ",
    "but before our very eyes it turned into a ",
    ".Since we were kind of freaked out we decided to ",
    "as ", " as we could away from the still morphing object."
]

words = []
fullstory = []


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
        elif x < 8 and x > 6:
            words.append(input("Please tell me an adverb: "))
            pass
        else:
            words.append("")
            pass
        x = x + 1
        pass


inputs()

print(story[0] + words[0])
print(story[1] + words[1])
print(story[2] + words[2])
print(story[3] + words[3])
print(story[4] + words[4])
print(story[5] + words[5])
print(story[6] + words[6])
