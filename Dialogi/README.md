Jak pisać dialogi:
[1] - niech plik ma rozszerzenie .json (np. dialogi.json)
[2] - pisz według poniższego schematu:

{
    "Nazwa NPC": {
        "unikalny kod rozmowy": {
            "NPC": "To co mowi NPC",
            "User": {
                "[1] Odpowiedz uzytkownika": "Kod kolejnej rozmowy",
                "[2] Odpowiedz uzytkownika":"Kod kolejnej rozmowy",
                ...
            }
        },
        "0001": {
            "NPC":"Przepraszam, ze przeszkadzam, ale czy mogłbym poznać swoje oceny?",
            "User":{
                "[1] Już mówiłam! Wkrótce sprawdzę":"0005"
            }
        },
        ...
    },
    "Kucharz Jan": {
        "0000": {
            "NPC": "Witaj!",
            "User": {
                "Siemanko! Co dzisiaj podajesz?" : "0001"
            },
            ...
        }
    }
}

[3] - Mozesz sprawdzić, czy poprawnie piszesz dialogi. Wystarczy, że skopiujesz zawartość [NPC](NPC.py), wkleisz ją [tutaj](https://www.programiz.com/python-programming/online-compiler/) i odpowiednio wkleisz zawartość swojego jsona do linijki 6.