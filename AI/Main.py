import Library

AI = True
while AI:
    Name = Library.checkDetails('Name')
    MyName = Library.checkDetails('MyName')
    speakable = Library.checkDetails('speakable')
    printable = Library.checkDetails('printable')
    query = Library.takeCommand()
    if 'what is your name' in query:
        Library.speak(Name)
        print(Name)
    elif 'change your name' in query:
        print('Tell that what i need to change my name')
        Library.speak('Tell that what i need to change my name')
        NewName = Library.takeCommand()
        data: dict = Library.LoadMemory('data.json')
        data["Details"][0]["Name"].append(NewName)
        Library.save_memory('data.json', data)
    elif 'exit' in query:
        print('Bye Sir, Nice to meet you.')
        Library.speak('Bye Sir, Nice to meet you.')
        break
        