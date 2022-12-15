from random import randint

def get_tags(tag1: str):
    randy = randint(0,10)

    tags = ["Modivation","Grind","Hustle","Study","Work","Listen","Gaming","School","College","Reading","","","",""]

    return f"{tag1},Music,Compilation,{tags[randy]},{tags[randy+1]},{tags[randy+2]},{tags[randy+3]},{tags[randy+4]}"

def get_title():
    randy = randint(0,10)
    title = "Test"

    titleAddrs = [
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
    ]

    title = title + f" {titleAddrs[randy]}"

    return title

def get_description():
    randy = randint(0,10)
    desc = "Test"

    descAdders = [
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
        "test",
    ]


    desc = desc + f" {descAdders[randy]}"

    return desc