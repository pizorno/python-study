text = """"
    Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

    Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

    Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the la
"""

vogals = {}

for vogal in "AEIOU":
    vogals[vogal] = 0

for charecter in text:
    if charecter.upper() == "A":
        vogals["A"] += 1
    if charecter.upper() == "E":
        vogals["E"] += 1
    if charecter.upper() == "I":
        vogals["I"] += 1
    if charecter.upper() == "O":
        vogals["O"] += 1
    if charecter.upper() == "U":
        vogals["U"] += 1

for vogal, counter in vogals.items():
    print(f"Exists {counter} letters {vogal} in text")
