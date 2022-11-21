import xml.dom.minidom as md
import io
# Script to resolve antiquated line identification scheme in Plautus references.
# Function should take in a file, read it (prob should use helper function),
# and then RegEx find every <bibl> tag with an author subtag of "Plaut."
# read the title of the play, check it against the act-scene values & calculate
# the line number (helper function). Then use that to update the Perseus link from
# e.g. Perseus:abo:phi,0119,006:5:2:41 to Perseus:abo:phi,0119,006:912. Also
# add a parenthetical with the actual line number to the citation to go from
# 5, 2, 41 to 5, 2, 41 (912).

def main():
    file_name = input("Which file would you like to resolve?\n")
    file = md.parse(file_name)
    print( file.nodeName )

    print(file.firstChild.tagName)

    bibliography = file.getElementByTagName( "bibl" )

    for entry in bibliography:
        link = entry.getAttribute("n")
        tokens = link.split(':')
        authPlay = tokens[2]
        apToks = authPlay.split(',')
        author = apToks[1]
        play = apToks[2]
        if tokens.len() == 6:
            act = int(tokens[3])
            scene = int(tokens[4])
            line = int(tokens[5])
        elif tokens.len() == 5:
            act = int(tokens[3])
            scene = 0
            line = int(tokens[4])
        elif tokens.len() == 4:
            act = 0
            scene = 0
            line = tokens[3]
        newLine = 0
        if author == '0119':
            if play == '001':
                print('Am. or Amph., Amphitruo.')
                newLine = amphNum(act, scene, line)
            elif play == '002':
                print('As. or Asin., Asinaria.')
                newLine = asNum(act, scene, line)
            elif play == '003':
                print('Aul., Aulularia.')
                newLine = aulNum(act, scene, line)
            elif play == '004':
                print('Bacch., Bacchides.')
                newLine = baccNum(act, scene, line)
            elif play == '005':
                print('Capt., Captivi.')
                newLine = captNum(act, scene, line)
            elif play == '006':
                print('Cas., Casina.')
            elif play == '007':
                print('Cist., Cistellaria.')
            elif play == '008':
                print('Curc., Curculio.')
            elif play == '009':
                print('Ep. or Epid., Epidicus.')
            elif play == '010':
                print('Men., Menaechmi.')
            elif play == '011':
                print('Merc., Mercator.')
            elif play == '012':
                print('Mil., Miles Gloriosus.')
            elif play == '013':
                print('Most., Mostellaria.')
            elif play == '014':
                print('Pers., Persa.')
            elif play == '015':
                print('Poen., Poenulus.')
            elif play == '016':
                print('Ps., Pseudolus.')
            elif play == '017':
                print('Rud., Rudens.')
            elif play == '018':
                print('Stich., Stichus.')
            elif play == '019':
                print('Trin., Trinummus.')
            elif play == '020':
                print('Truc., Truculentus.')
            # switch play title
            # parse act/scene/line
            # call helper function that converts line number for a given play
            # update link and entry text

def amphNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 152
        elif scene == 2:
            lineNum = line + 462
        elif scene == 3:
            lineNum = line + 498
    elif act == 2:
        if scene == 1:
            lineNum = line + 550
        elif scene == 2:
            lineNum = line + 632
    elif act == 3:
        if scene == 1:
            lineNum = line + 860
        elif scene == 2:
            lineNum = line + 881
        elif scene == 3:
            lineNum = line + 955
        elif scene == 4:
            lineNum = line + 983
    elif act == 4:
        if scene == 1:
            lineNum = line + 1008
        elif scene == 2:
            lineNum = line + 1020
        elif scene == 3:
            lineNum = line + 1034
    elif act == 5:
        if scene == 1:
            lineNum = line + 1052
        elif scene == 2:
            lineNum = line + 1130
    return lineNum

def asNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 15
        elif scene == 2:
            lineNum = line + 126
        elif scene == 3:
            lineNum = line + 152
    elif act == 2:
        if scene == 1:
            lineNum = line + 248
        elif scene == 2:
            lineNum = line + 256
        elif scene == 3:
            lineNum = line + 380
        elif scene == 4:
            lineNum = line + 406
    elif act == 3:
        if scene == 1:
            lineNum = line + 503
        elif scene == 2:
            lineNum = line + 544
        elif scene == 3:
            lineNum = line + 590
    elif act == 4:
        if scene == 1:
            lineNum = line + 745
        elif scene == 2:
            lineNum = line + 809
    elif act == 5:
        if scene == 1:
            lineNum = line + 827
        elif scene == 2:
            lineNum = line + 850
    return lineNum

def aulNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 39
        elif scene == 2:
            lineNum = line + 78
    elif act == 2:
        if scene == 1:
            lineNum = line + 119
        elif scene == 2:
            lineNum = line + 177
        elif scene == 3:
            lineNum = line + 267
        elif scene == 4:
            lineNum = line + 279
        elif scene == 5:
            lineNum = line + 326
        elif scene == 6:
            lineNum = line + 349
        elif scene == 7:
            lineNum = line + 362
        elif scene == 8:
            lineNum = line + 370
        elif scene == 9:
            lineNum = line + 397
    elif act == 3:
        if scene == 1:
            lineNum = line + 405
        elif scene == 2:
            lineNum = line + 414
        elif scene == 3:
            lineNum = line + 448
        elif scene == 4:
            lineNum = line + 459
        elif scene == 5:
            lineNum = line + 474
        elif scene == 6:
            lineNum = line + 536
    elif act == 4:
        if scene == 1:
            lineNum = line + 586
        elif scene == 2:
            lineNum = line + 607
        elif scene == 3:
            lineNum = line + 623
        elif scene == 4:
            lineNum = line + 627
        elif scene == 5:
            lineNum = line + 660
        elif scene == 6:
            lineNum = line + 666
        elif scene == 7:
            lineNum = line + 681
        elif scene == 8:
            lineNum = line + 700
        elif scene == 9:
            lineNum = line + 712
        elif scene == 10:
            lineNum = line + 730
    elif act == 5:
        lineNum = line + 807
    return lineNum

def baccNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 34
        elif scene == 2:
            lineNum = line + 108
    elif act == 2:
        if scene == 1:
            lineNum = line + 169
        elif scene == 2:
            lineNum = line + 178
        elif scene == 3:
            lineNum = line + 234
    elif act == 3:
        if scene == 1:
            lineNum = line + 367
        elif scene == 2:
            lineNum = line + 384
        elif scene == 3:
            lineNum = line + 404
        elif scene == 4:
            lineNum = line + 499
        elif scene == 5:
            lineNum = line + 525
        elif scene == 6:
            lineNum = line + 529
    elif act == 4:
        if scene == 1:
            lineNum = line + 572
        elif scene == 2:
            lineNum = line + 582
        elif scene == 3:
            lineNum = line + 611
        elif scene == 4:
            lineNum = line + 639
        elif scene == 5:
            lineNum = line + 760
        elif scene == 6:
            lineNum = line + 769
        elif scene == 7:
            lineNum = line + 798
        elif scene == 8:
            lineNum = line + 841
        elif scene == 9:
            lineNum = line + 924
        elif scene == 10:
            lineNum = line + 978
        elif scene == 11:
            lineNum = line + 1075
    elif act == 5:
        if scene == 1:
            lineNum = line + 1086
        elif scene == 2:
            lineNum = line + 1119
    return lineNum

def captNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 68
        elif scene == 2:
            lineNum = line + 109
    elif act == 2:
        if scene == 1:
            lineNum = line + 194
        elif scene == 2:
            lineNum = line + 250
        elif scene == 3:
            lineNum = line + 360
    elif act == 3:
        if scene == 1:
            lineNum = line + 460
        elif scene == 2:
            lineNum = line + 497
        elif scene == 3:
            lineNum = line + 515
        elif scene == 4:
            lineNum = line + 532
        elif scene == 5:
            lineNum = line + 658
    elif act == 4:
        if scene == 1:
            lineNum = line + 767
        elif scene == 2:
            lineNum = line + 780
        elif scene == 3:
            lineNum = line + 900
        elif scene == 4:
            lineNum = line + 908
    elif act == 5:
        if scene == 1:
            lineNum = line + 921
        elif scene == 2:
            lineNum = line + 953
        elif scene == 3:
            lineNum = line + 977
        elif scene == 4:
            lineNum = line + 997
    return lineNum

## input file

# parse file as xml

# find all bibl tags

# for each bibl tag find author subtag

# check if value == to "Plaut."
# find <author>Plaut.</author>
# get next <title> (text btween) <title></title> after <author>
# get act/scene/line number right after </title> until </bib>
# calculate line number
# grab <bibl n=""> from before <author>
# update 

# if it is, get value of title tag and call helper function to calculate line number

# then replace end of n attribute for perseus link (that is, the num:num:num) with the line number
# and add parenthetical with line number to end of bibl text (that is: "num, num, num (num)")