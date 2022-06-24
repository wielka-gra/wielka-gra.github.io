class NPC:
    def __init__(self) -> None:
        self.next_dialog = "0000"

        # self.dialog = <{"0000": ...}
        self.dialog =  {
        "0000": {
            "NPC": "Dzien dobry Pani profesor...",
            "User": {
                "[1] O matko ale jestem zajęta": "0001",
                "[2] Nie zawracaj mi głowy głupcze":"0001",
                "[3] Dzień dobry. W czym mogę pomóc?":"0002"
            }
        },
        "0001": {
            "NPC":"Przepraszam, ze przeszkadzam, ale czy mogłbym poznać swoje oceny?",
            "User":{
                "[1] Już mówiłam! Wkrótce sprawdzę":"0003"
            }
        },
        "0002": {
            "NPC":"Przepraszam, ze przeszkadzam, ale czy mogłbym poznać swoje oceny?",
            "User":{
                "[1] Aj przepraszam. Daj mi chwile, znajdę twoją pracę i od razu ci ocenię.":"0003"
            }
        }
    }


        
    def talk(self):
        odp = self.dialog[self.next_dialog]
        print(odp["NPC"])
        # print(odp["User"].keys())
        for line in odp["User"].keys():
            print(line)
        self.next_dialog = str(list(odp["User"].values())[int(input()) - 1])
        

x  =NPC()
while 1 > 0:
    try:
        x.talk()
    except:
        pass