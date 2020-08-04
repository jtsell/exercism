def recite(start_verse, end_verse):
    song = list()
    while start_verse <= end_verse:
        song.append(verse(start_verse))
        start_verse += 1
    return song


def verse(day: int) -> str:
    song = (
        f"On the {ordinals[day]} day of " "Christmas my true love gave to me: "
    )
    if day == 1:
        return f"{song}{gifts[1][4:]}"
    else:
        for i in range(day, -1, -1):
            song += f"{gifts[i]}"
        return song


ordinals = [
    "",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

gifts = [
    "",
    "and a Partridge in a Pear Tree.",  # [4:]
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]
