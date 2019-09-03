words = []
# ANSI escape codes for colors found on geeks for geeks at:
# https://www.geeksforgeeks.org/print-colors-python-terminal/


def pr_purple(skk):
    print("\033[95m {}\033[00m" .format(skk))


def pr_red(skk):
    print("\033[91m {}\033[00m" .format(skk))


def pr_yellow(skk):
    print("\033[93m {}\033[00m" .format(skk))


def pr_green(skk):
    print("\033[92m {}\033[00m" .format(skk))


def pr_cyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def pr_light_purple(skk):
    print("\033[94m {}\033[00m" .format(skk))


def inputs():
    x = 0
    while x <= 6:
        if x >= 0 and x <= 0:
            pr_red("Please tell me an adjective: ")
            words.append(input())
            pass
        elif x >= 1 and x <= 2:
            pr_yellow("Please tell me a noun: ")
            words.append(input())
            pass
        elif x >= 3 and x <= 3:
            pr_green("Please tell me a verb: ")
            words.append(input())
            pass
        elif x >= 4 and x <= 4:
            pr_cyan("Please tell me a name: ")
            words.append(input())
            pass
        elif x >= 5 or x <= 6:
            pr_light_purple("Please tell me an adverb: ")
            words.append(input())
            pass
        else:
            words.append("")
            pass
        x = x + 1
        pass


inputs()
pr_purple(f'''This morning I woke up to a very {words[0]} thing.
When I investigated it turned out to be a {words[1]}.
Very {words[5]} I decided to wake up my room mate {words[4]} so we could
marvle at the {words[1]} but before our very eyes it turned into a
{words[2]}. Since we were kind of freaked out we decided to {words[3]}
as {words[6]} as we could away from the still morphing object."
''')
