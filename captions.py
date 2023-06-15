from random import randint

def get_tags(tag1: str):
    tags = ["Modivation","Chill out","Beats","Study","Work","Focus","Gaming","School","College","Reading","Ambient","Walking","Coding","Feel Good","Deep Focus","Brain Power","Brain Boost","Mood","Smooth"]
    tags2 = ["Motivación","Relajarse","Latidos","Estudiar","Trabajar","Enfocar","Juego de azar","Escuela","Colega","Lectura",
             "Ambiente","Caminando","Codificación","Sentirse bien","Enfoque profundo","Poder cerebral","Impulso cerebral","Ánimo","Liso"]

    randy = randint(0,(len(tags)-5))

    return f"{tag1},Music,Compilation,{tags[randy]},{tags[randy+1]},{tags[randy+2]},{tags[randy+3]},{tags[randy+4]},{tags2[randy]},{tags2[randy+1]},{tags2[randy+2]},{tags2[randy+3]},{tags2[randy+4]}"

def get_title(tag: str):
    tag = tag.capitalize()
    title = ""

    titleMains = [
        "Gaming Music 🎮",
        "Study Music 📚",
        "Coding Music 💻",
        "Working Music 🛠️",
        "Music for Concentration 🧠",
        "Music for Creativity 💭",
        "Music for Productivity 🔥"
    ]

    titleMainsEs = [
        "Música Para Juegos 🎮",
        "Estudiar Musica 📚",
        "Música de Codificación 💻",
        "Música de Trabajo 🛠️",
        "Música Para la Concentración 🧠",
        "Música Para la Creatividad 💭",
        "Música Para la Productividad 🔥"

    ]

    titleAddrs = [
        "Calm Your Mind",
        "Ambient",
        "Increase Concentration",
        "Brain Power",
        "Smooth Workflow",
        "Background Music",
        "Laser Focus",
        "Stress Relief",
        "Improve Your Mood",
        "Mind Boosting",
        "Deep Learning"
    ]

    randy1 = randint(0,(len(titleAddrs)-1))
    randy2 = randint(0,(len(titleAddrs)-1))
    randy3 = randint(0,(len(titleAddrs)-1))

    randTitle = randint(0,(len(titleMains)-1))

    while randy2 == randy1:
        randy2 = randint(0,(len(titleAddrs)-1))
    
    while randy3 == randy1 or randy3 == randy2:
        randy3 = randint(0,(len(titleAddrs)-1))

    title = titleMains[randTitle] + f" - {tag} - {titleAddrs[randy1]} - {titleAddrs[randy2]} | {titleMainsEs[randTitle]}"

    return title

def get_description(tag: str):
    tag = tag.capitalize()
    desc = f"{tag} music compilation"

    descAdders = [
        "listen and enjoy while you study and work!",
        "- thank you for listening!",
        "Keep focused with this ambient music.",
        "to help you study, read, concentrate and stay motivated!",
        "thanks for tuning in, hope you enjoy!",
        "to put you in in a good mood and headspace.",
        "for deep focus,",
        "to boost your mood!",
        "to increase your concentration and productivity!",
        "for ambient atmoshperics,",
        "",
    ]

    randy = randint(0,(len(descAdders)-1))

    desc = desc + f" {descAdders[randy]} Please Like and Subscribe!!\n"

    with open('desc_adder.txt') as f:
        for line in f.readlines():
            desc = desc + line

    return desc

# Recopilacion de musica! Por favor, dale me gusta y suscríbete!