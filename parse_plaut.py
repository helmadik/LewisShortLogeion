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
            elif play == '003':
                print('Aul., Aulularia.')
            elif play == '004':
                print('Bacch., Bacchides.')
            elif play == '005':
                print('Capt., Captivi.')
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
    # calculate
    if act == 0:
        #do x
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 153
        elif scene == 2:
            lineNum = line + 463
        elif scene == 3:
            lineNum = line + 499
    elif act == 2:
        if scene == 1:
            lineNum = line + 551
        elif scene == 2:
            lineNum = line + 633
    elif act == 3:
        if scene == 1:
            lineNum = line + 861
        elif scene == 2:
            lineNum = line + 882
        elif scene == 3:
            lineNum = line + 956
        elif scene == 4:
            lineNum = line + 984
    elif act == 4:
        if scene == 1:
            lineNum = line + 1009
        elif scene == 2:
            lineNum = line + 1021
        elif scene == 3:
            lineNum = line + 1035
    elif act == 5:
        if scene == 1:
            lineNum = line + 1053
        elif scene == 2:
            lineNum = line + 1131
    return lineNum

def asNum(act, scene, line):
    lineNum = 0
    if act == 0:
        line = line.strip("prol.")
        line = int(line)
        lineNum = line
    elif act == 1:
        if scene == 1:
            lineNum = line + 16
        elif scene == 2:
            lineNum = line + 127
        elif scene == 3:
            lineNum = line + 153
    elif act == 2:
        if scene == 1:
            lineNum = line + 249
        elif scene == 2:
            lineNum = line + 257
        elif scene == 3:
            lineNum = line + 381
        elif scene == 4:
            lineNum = line + 407
    elif act == 3:
        if scene == 1:
            lineNum = line + 504
        elif scene == 2:
            lineNum = line + 545
        elif scene == 3:
            lineNum = line + 591
    elif act == 4:
        if scene == 1:
            lineNum = line + 746
        elif scene == 2:
            lineNum = line + 810
    elif act == 5:
        if scene == 1:
            lineNum = line + 828
        elif scene == 2:
            lineNum = line + 851
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