def pluralize():
    word = input("Word Please...")
    if word == "moose":
        print("moose") 
    elif word == "automaton":
        print("automata")
    elif word == "mouse":
        print("mice")
    else: 
        print(word + "s")
pluralize()