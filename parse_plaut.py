import xml.dom.minidom as md
# Script to resolve antiquated line identification scheme in Plautus references.
# Function should take in a file, read it (prob should use helper function),
# and then RegEx find every <bibl> tag with an author subtag of "Plaut."
# read the title of the play, check it against the act-scene values & calculate
# the line number (helper function). Then use that to update the Perseus link from
# e.g. Perseus:abo:phi,0119,006:5:2:41 to Perseus:abo:phi,0119,006:912. Also
# add a parenthetical with the actual line number to the citation to go from
# 5, 2, 41 to 5, 2, 41 (912).

# input file

# parse file as xml

# find all bibl tags

# for each bibl tag find author subtag

# check if value == to "Plaut."

# if it is, get value of title tag and call helper function to calculate line number

# then replace end of n attribute for perseus link (that is, the num:num:num) with the line number
# and add parenthetical with line number to end of bibl text (that is: "num, num, num (num)")