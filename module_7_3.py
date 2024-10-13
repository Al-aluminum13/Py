
file_name = 'poem.txt'


with open(file_name, 'w', encoding='utf-8') as file:
    file.write("# -*- coding: utf-8 -*-n")
    file.write("My soul is dark - Oh! quickly stringn")
    file.write("The harp I yet can brook to hear;n")
    file.write("And let thy gentle fingers flingn")
    file.write("Its melting murmurs o'er mine ear.n")
    file.write("If in this heart a hope be dear,n")
    file.write("That sound shall charm it forth again:n")
    file.write("If in these eyes there lurk a tear,n")
    file.write("'Twill flow, and cease to burn my brain.n")
    file.write("But bid the strain be wild and deep,n")
    file.write("Nor let thy notes of joy be first:n")
    file.write("I tell thee, minstrel, I must weep,n")
    file.write("Or else this heavy heart will burst;n")
    file.write("For it hath been by sorrow nursed,n")
    file.write("And ached in sleepless silence, long;n")
    file.write("And now 'tis doomed to know the worst,n")
    file.write("And break at once - or yield to song.n")


with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
