# Script to resolve antiquated line identification scheme in Plautus references.
# Function should take in a file, read it (prob should use helper function),
# and then RegEx find every <bibl> tag with an author subtag of "Plaut."
# read the title of the play, check it against the act-scene values & calculate
# the line number (helper function). Then use that to update the Perseus link from
# e.g. Perseus:abo:phi,0119,006:5:2:41 to Perseus:abo:phi,0119,006:912. Also
# add a parenthetical with the actual line number to the citation to go from
# 5, 2, 41 to 5, 2, 41 (912).