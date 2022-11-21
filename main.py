import random

_options = {"taş", "kağıt", "makas"}
_options = list(_options)
AI = ""
Player = ""


while True:
    a = random.randrange(0, 2)
    AI = _options[a]
    a += 1
    
    print("Seçenekler: TAŞ || KAĞIT || MAKAS")
    _playerInput = input()
    
    s = 0
    i = -1
    while i < 2:
        if _options[i] == _playerInput:
            Player = _playerInput
            s = i + 1
            break
        else:
            i += 1
    
    print("\nSizin Seçiminiz: " + Player)
    print("Bilgisayarın Seçimi: " + AI)
    
    if (a-1) == s:
        print("\n-----BİLGİSAYAR KAZANDI-----\n")
    elif (s-2) == a:
        print("\n-----BİLGİSAYAR KAZANDI-----\n")
    elif (a-2) == s:
        print("\n-----SEN KAZANDIN-----\n")
    elif (s-1) == a:
        print("\n-----SEN KAZANDIN-----\n")
    elif a == s:
        print("\n-----BERABERE-----\n")
    
