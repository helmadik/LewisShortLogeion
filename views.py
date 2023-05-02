from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap

views = Blueprint(__name__, "views")

plays = [{"play":"Play"}, 
    {"play":"Amphitryon"}, {"play":"Asinaria"}, {"play":"Aulularia"}, 
    {"play":"Bacchides"}, {"play":"Captivi"}, {"play":"Casina"}, 
    {"play":"Cistellaria"}, {"play":"Curculio"}, {"play":"Epidicus"}, 
    {"play":"Menaechmi"}, {"play":"Mercator"}, {"play":"Miles Gloriosus"},
    {"play":"Mostellaria"}, {"play":"Persa"}, {"play":"Poenulus"}, 
    {"play":"Pseudolus"}, {"play":"Rudens"}, {"play":"Stichus"}, 
    {"play":"Trinummus"}, {"play":"Truculentus"}]

@views.route("/", methods=["GET", "POST"])
def enter_info():
    lineNum = 0
    if request.method == "POST":
        req = request.form

        act = int(req["act"])
        scene = req.get("scene")
        if (scene == ""):
            scene = 1
        else:
            scene = int(scene)
        line = int(request.form["line"])
    
        play = request.form.get("play")

        print(act, scene, line, play)

        lineNum = convert_combo(act, scene, line, play)
        if lineNum == 0:
            flash("Please enter a valid act scene line combo.")
            return redirect(url_for('views.enter_info'))
        return render_template("result.html", act = str(act), scene = str(scene),
        line = str(line), play = play, lineNum = str(lineNum))
    """
    if error:
        print("true")
        flash("Please enter a valid act scene line combo.")"""

    return render_template("enter_info.html", plays=[{"play":"Play"}, 
    {"play":"Amphitryon"}, {"play":"Asinaria"}, {"play":"Aulularia"}, 
    {"play":"Bacchides"}, {"play":"Captivi"}, {"play":"Casina"}, 
    {"play":"Cistellaria"}, {"play":"Curculio"}, {"play":"Epidicus"}, 
    {"play":"Menaechmi"}, {"play":"Mercator"}, {"play":"Miles Gloriosus"},
    {"play":"Mostellaria"}, {"play":"Persa"}, {"play":"Poenulus"}, 
    {"play":"Pseudolus"}, {"play":"Rudens"}, {"play":"Stichus"}, 
    {"play":"Trinummus"}, {"play":"Truculentus"}])


def convert_combo(act, scene, line, play):
    newLine = 0
    if play == 'Amphitryon':
        newLine = amphNum(act, scene, line)
    elif play == 'Asinaria':
        newLine = asNum(act, scene, line)
    elif play == 'Aulularia':
        newLine = aulNum(act, scene, line)
    elif play == 'Bacchides':
        newLine = baccNum(act, scene, line)
    elif play == 'Captivi':
        newLine = captNum(act, scene, line)
    elif play == 'Casina':
        newLine = casNum(act, scene, line)
    elif play == 'Cistellaria':
        newLine = cistNum(act, scene, line) 
    elif play == 'Curculio':
        newLine = curcNum(act, scene, line)
    elif play == 'Epidicus':
        newLine = epidNum(act, scene, line)
    elif play == 'Menaechmi':
        newLine = menNum(act, scene, line)
    elif play == 'Mercator':
        newLine = mercNum(act, scene, line)
    elif play == 'Miles Gloriosus':
        newLine = milNum(act, scene, line)
    elif play == 'Mostellaria':
        newLine = mostNum(act, scene, line)
    elif play == 'Persa':
        newLine = persNum(act, scene, line)
    elif play == 'Poenulus':
        newLine = poenNum(act, scene, line)
    elif play == 'Pseudolus':
        newLine = psNum(act, scene, line)
    elif play == 'Rudens':
        newLine = rudNum(act, scene, line)
    elif play == 'Stichus':
        newLine = stichNum(act, scene, line)
    elif play == 'Trinummus':
        newLine = trinNum(act, scene, line)
    elif play == 'Truculentus':
        newLine = trucNum(act, scene, line)
    
    return newLine


def amphNum(act, scene, line):
    lineNum = 0
    if act == 1:
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
        elif scene == 3:
            lineNum = line + 1143
    return lineNum

def asNum(act, scene, line):
    lineNum = 0
    if act == 1:
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
    if act == 1:
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
        if scene == 1:
            lineNum = line + 807
        else:
            print(f"error! there is no scene {scene} in act 5 of Aulularia")
    return lineNum

def baccNum(act, scene, line):
    lineNum = 0
    if act == 1:
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
    if act == 1:
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

def casNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 88
        else:
            print(f"error! there is no scene {scene} in act 1 of Casina")
    elif act == 2:
        if scene == 1:
            lineNum = line + 143
        elif scene == 2:
            lineNum = line + 164
        elif scene == 3:
            lineNum = line + 216
        elif scene == 4:
            lineNum = line + 278
        elif scene == 5:
            lineNum = line + 308
        elif scene == 6:
            lineNum = line + 352
        elif scene == 7:
            lineNum = line + 423
        elif scene == 8:
            lineNum = line + 436
    elif act == 3:
        if scene == 1:
            lineNum = line + 514
        elif scene == 2:
            lineNum = line + 530
        elif scene == 3:
            lineNum = line + 562
        elif scene == 4:
            lineNum = line + 590
        elif scene == 5:
            lineNum = line + 620
        elif scene == 6:
            lineNum = line + 719
    elif act == 4:
        if scene == 1:
            lineNum = line + 758
        elif scene == 2:
            lineNum = line + 779
        elif scene == 3:
            lineNum = line + 797
        elif scene == 4:
            lineNum = line + 813
    elif act == 5:
        if scene == 1:
            lineNum = line + 854
        elif scene == 2:
            lineNum = line + 874
        elif scene == 3:
            lineNum = line + 936
        elif scene == 4:
            lineNum = line + 962
    return lineNum

# Something weird is going on with the numbering here
def cistNum(act, scene, line):
    lineNum = 0
    if line == "":
        return lineNum
    #1	1	1 
	#1	2	120
	#1	3	149
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 119
        elif scene == 3:
            lineNum = 148
	#2	1	203
	#2	Frag 1	230
	#2	Frag 2	231
	#2	Frag 3	305
	#2	Frag 4	373
	#2	Frag 5	374
	#2	Frag 6	377
	#2	Frag 7	378
	#2	Frag 8	379
	#2	Frag 9	381
	#2	Frag 10	382
	#2	Frag 11	383
	#2	Frag 12	384
	#2	2	536
	#2	3	543
    elif act == 2:
        if scene == 1:
            lineNum = line + 202
        elif scene == 2:
            lineNum = line + 535
        elif scene == 3:
            lineNum = line + 542
	#3	1	631
    elif act == 3:
        if scene == 1:
            lineNum = line + 630
        else:
            print(f"error! there is no scene {scene} in act 3 of Cistellaria")
	#4	1	653
	#4	2	671
    elif act == 4:
        if scene == 1:
            lineNum = line + 652
        elif scene == 2:
            lineNum = line + 670
	#5	1	774
    elif act == 5:
        if scene == 1:
            lineNum = line + 773
        else:
            print(f"error! there is no scene {scene} in act 5 of Cistellaria")
    return lineNum

def curcNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 95
        elif scene == 3:
            lineNum = line + 157
    elif act == 2:
        if scene == 1:
            lineNum = line + 215
        elif scene == 2:
            lineNum = line + 250
        elif scene == 3:
            lineNum = line + 279
    elif act == 3:
        if scene == 1:
            lineNum = line + 370
        else:
            print(f"error! there is no scene {scene} in act 3 of Curculio")
    elif act == 4:
        if scene == 1:
            lineNum = line + 461
        elif scene == 2:
            lineNum = line + 486
        elif scene == 3:
            lineNum = line + 532
        elif scene == 4:
            lineNum = line + 556
    elif act == 5:
        if scene == 1:
            lineNum = line + 590
        elif scene == 2:
            lineNum = line + 598
        elif scene == 3:
            lineNum = line + 678
    return lineNum

def epidNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 103
    elif act == 2:
        if scene == 1:
            lineNum = line + 165
        elif scene == 2:
            lineNum = line + 180
        elif scene == 3:
            lineNum = line + 305
    elif act == 3:
        if scene == 1:
            lineNum = line + 319
        elif scene == 2:
            lineNum = line + 336
        elif scene == 3:
            lineNum = line + 381
        elif scene == 4:
            lineNum = line + 436
    elif act == 4:
        if scene == 1:
            lineNum = line + 525
        elif scene == 2:
            lineNum = line + 569
    elif act == 5:
        if scene == 1:
            lineNum = line + 606
        elif scene == 2:
            lineNum = line + 665
    return lineNum

def menNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 76
        elif scene == 2:
            lineNum = line + 109
        elif scene == 3:
            lineNum = line + 181
        elif scene == 4:
            lineNum = line + 218
    elif act == 2:
        if scene == 1:
            lineNum = line + 225
        elif scene == 2:
            lineNum = line + 272
        elif scene == 3:
            lineNum = line + 350
    elif act == 3:
        if scene == 1:
            lineNum = line + 445
        elif scene == 2:
            lineNum = line + 465
        elif scene == 3:
            lineNum = line + 523
    elif act == 4:
        if scene == 1:
            lineNum = line + 558
        elif scene == 2:
            lineNum = line + 570
        elif scene == 3:
            lineNum = line + 674
    elif act == 5:
        if scene == 1:
            lineNum = line + 700
        elif scene == 2:
            lineNum = line + 752
        elif scene == 3:
            lineNum = line + 875
        elif scene == 4:
            lineNum = line + 888
        elif scene == 5:
            lineNum = line + 898
        elif scene == 6:
            lineNum = line + 965
        elif scene == 7:
            lineNum = line + 989
        elif scene == 8:
            lineNum = line + 1049
        elif scene == 9:
            lineNum = line + 1059
    return lineNum

def mercNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 110
    elif act == 2:
        if scene == 1:
            lineNum = line + 224
        elif scene == 2:
            lineNum = line + 271
        elif scene == 3:
            lineNum = line + 334
        elif scene == 4:
            lineNum = line + 468
    elif act == 3:
        if scene == 1:
            lineNum = line + 498
        elif scene == 2:
            lineNum = line + 543
        elif scene == 3:
            lineNum = line + 561
        elif scene == 4:
            lineNum = line + 587
    elif act == 4:
        if scene == 1:
            lineNum = line + 666
        elif scene == 2:
            lineNum = line + 691
        elif scene == 3:
            lineNum = line + 699
        elif scene == 4:
            lineNum = line + 740
        elif scene == 5:
            lineNum = line + 802
        elif scene == 6:
            lineNum = line + 816
    elif act == 5:
        if scene == 1:
            lineNum = line + 829
        elif scene == 2:
            lineNum = line + 841
        elif scene == 3:
            lineNum = line + 956
        elif scene == 4:
            lineNum = line + 961
    return lineNum

def milNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        else:
            print(f"error! there is no scene {scene} in act 1 of Miles Gloriosus")
    elif act == 2:
        if scene == 1:
            lineNum = line + 78
        elif scene == 2:
            lineNum = line + 155
        elif scene == 3:
            lineNum = line + 271
        elif scene == 4:
            lineNum = line + 353
        elif scene == 5:
            lineNum = line + 410
        elif scene == 6:
            lineNum = line + 480
    elif act == 3:
        if scene == 1:
            lineNum = line + 595
        elif scene == 2:
            lineNum = line + 812
        elif scene == 3:
            lineNum = line + 874
    elif act == 4:
        if scene == 1:
            lineNum = line + 946
        elif scene == 2:
            lineNum = line + 990
        elif scene == 3:
            lineNum = line + 1093
        elif scene == 4:
            lineNum = line + 1136
        elif scene == 5:
            lineNum = line + 1199
        elif scene == 6:
            lineNum = line + 1215
        elif scene == 7:
            lineNum = line + 1283
        elif scene == 8:
            lineNum = line + 1310
        elif scene == 9:
            lineNum = line + 1377
    elif act == 5:
        if scene == 1:
            lineNum = line + 1393
        else:
            print(f"error! there is no scene {scene} in act 5 of Miles Gloriosus")
    return lineNum

def mostNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 83
        elif scene == 3:
            lineNum = line + 156
        elif scene == 4:
            lineNum = line + 312
    elif act == 2:
        if scene == 1:
            lineNum = line + 347
        elif scene == 2:
            lineNum = line + 430
    elif act == 3:
        if scene == 1:
            lineNum = line + 531
        elif scene == 2:
            lineNum = line + 689
        elif scene == 3:
            lineNum = line + 903
    elif act == 4:
        if scene == 1:
            lineNum = line + 857
        elif scene == 2:
            lineNum = line + 884
        elif scene == 3:
            lineNum = line + 992
    elif act == 5:
        if scene == 1:
            lineNum = line + 1040
        elif scene == 2:
            lineNum = line + 1121
    return lineNum

def persNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 52
        elif scene == 3:
            lineNum = line + 80
    elif act == 2:
        if scene == 1:
            lineNum = line + 167
        elif scene == 2:
            lineNum = line + 182
        elif scene == 3:
            lineNum = line + 250
        elif scene == 4:
            lineNum = line + 271
        elif scene == 5:
            lineNum = line + 301
    elif act == 3:
        if scene == 1:
            lineNum = line + 328
        elif scene == 2:
            lineNum = line + 399
        elif scene == 3:
            lineNum = line + 404
    elif act == 4:
        if scene == 1:
            lineNum = line + 448
        elif scene == 2:
            lineNum = line + 461
        elif scene == 3:
            lineNum = line + 469
        elif scene == 4:
            lineNum = line + 558
        elif scene == 5:
            lineNum = line + 672
        elif scene == 6:
            lineNum = line + 682
        elif scene == 7:
            lineNum = line + 710
        elif scene == 8:
            lineNum = line + 730
        elif scene == 9:
            lineNum = line + 737
    elif act == 5:
        if scene == 1:
            lineNum = line + 752
        elif scene == 2:
            lineNum = line + 776
    return lineNum

def poenNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 128
        elif scene == 2:
            lineNum = line + 209
        elif scene == 3:
            lineNum = line + 409
    elif act == 2:
        if scene == 1:
            lineNum = line + 448
        else:
            print(f"error! there is no scene {scene} in act 2 of Poenulus")
    elif act == 3:
        if scene == 1:
            lineNum = line + 503
        elif scene == 2:
            lineNum = line + 577
        elif scene == 3:
            lineNum = line + 614
        elif scene == 4:
            lineNum = line + 710
        elif scene == 5:
            lineNum = line + 745
        elif scene == 6:
            lineNum = line + 795
    elif act == 4:
        if scene == 1:
            lineNum = line + 816
        elif scene == 2:
            lineNum = line + 822
    elif act == 5:
        if scene == 1:
            lineNum = line + 929
        elif scene == 2:
            lineNum = line + 960
        elif scene == 3:
            lineNum = line + 1119
        elif scene == 4:
            lineNum = line + 1173
        elif scene == 5:
            lineNum = line + 1279
        elif scene == 6:
            lineNum = line + 1337
        elif scene == 7:
            lineNum = line + 1371
    return lineNum

def psNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 2
        elif scene == 2:
            lineNum = line + 131
        elif scene == 3:
            lineNum = line + 229
        elif scene == 4:
            lineNum = line + 393
        elif scene == 5:
            lineNum = line + 414
    elif act == 2:
        if scene == 1:
            lineNum = line + 573
        elif scene == 2:
            lineNum = line + 593
        elif scene == 3:
            lineNum = line + 666
        elif scene == 4:
            lineNum = line + 693
    elif act == 3:
        if scene == 1:
            lineNum = line + 766
        elif scene == 2:
            lineNum = line + 789
    elif act == 4:
        if scene == 1:
            lineNum = line + 904
        elif scene == 2:
            lineNum = line + 955
        elif scene == 3:
            lineNum = line + 1016
        elif scene == 4:
            lineNum = line + 1037
        elif scene == 5:
            lineNum = line + 1051
        elif scene == 6:
            lineNum = line + 1062
        elif scene == 7:
            lineNum = line + 1102
        elif scene == 8:
            lineNum = line + 1237
    elif act == 5:
        if scene == 1:
            lineNum = line + 1245
        elif scene == 2:
            lineNum = line + 1284
    return lineNum

def rudNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 82
        elif scene == 2:
            lineNum = line + 88
        elif scene == 3:
            lineNum = line + 184
        elif scene == 4:
            lineNum = line + 219
        elif scene == 5:
            lineNum = line + 258
    elif act == 2:
        if scene == 1:
            lineNum = line + 289
        elif scene == 2:
            lineNum = line + 305
        elif scene == 3:
            lineNum = line + 330
        elif scene == 4:
            lineNum = line + 413
        elif scene == 5:
            lineNum = line + 457
        elif scene == 6:
            lineNum = line + 484
        elif scene == 7:
            lineNum = line + 558
    elif act == 3:
        if scene == 1:
            lineNum = line + 592
        elif scene == 2:
            lineNum = line + 614
        elif scene == 3:
            lineNum = line + 663
        elif scene == 4:
            lineNum = line + 705
        elif scene == 5:
            lineNum = line + 779
        elif scene == 6:
            lineNum = line + 838
    elif act == 4:
        if scene == 1:
            lineNum = line + 891
        elif scene == 2:
            lineNum = line + 905
        elif scene == 3:
            lineNum = line + 937
        elif scene == 4:
            lineNum = line + 1044
        elif scene == 5:
            lineNum = line + 1190
        elif scene == 6:
            lineNum = line + 1204
        elif scene == 7:
            lineNum = line + 1226
        elif scene == 8:
            lineNum = line + 1264
    elif act == 5:
        if scene == 1:
            lineNum = line + 1280
        elif scene == 2:
            lineNum = line + 1287
        elif scene == 3:
            lineNum = line + 1356
    return lineNum

def stichNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line
        elif scene == 2:
            lineNum = line + 57
        elif scene == 3:
            lineNum = line + 154
    elif act == 2:
        if scene == 1:
            lineNum = line + 273
        elif scene == 2:
            lineNum = line + 324
    elif act == 3:
        if scene == 1:
            lineNum = line + 401
        elif scene == 2:
            lineNum = line + 453
    elif act == 4:
        if scene == 1:
            lineNum = line + 504
        elif scene == 2:
            lineNum = line + 578
    elif act == 5:
        if scene == 1:
            lineNum = line + 640
        elif scene == 2:
            lineNum = line + 648
        elif scene == 3:
            lineNum = line + 672
        elif scene == 4:
            lineNum = line + 682
        elif scene == 5:
            lineNum = line + 741
        elif scene == 6:
            lineNum = line + 761
        elif scene == 7:
            lineNum = line + 768
    return lineNum

def trinNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 22
        elif scene == 2:
            lineNum = line + 38
    elif act == 2:
        if scene == 1:
            lineNum = line + 222
        elif scene == 2:
            lineNum = line + 275
        elif scene == 3:
            lineNum = line + 391
        elif scene == 4:
            lineNum = line + 401
    elif act == 3:
        if scene == 1:
            lineNum = line + 601
        elif scene == 2:
            lineNum = line + 626
        elif scene == 3:
            lineNum = line + 728
    elif act == 4:
        if scene == 1:
            lineNum = line + 819
        elif scene == 2:
            lineNum = line + 842
        elif scene == 3:
            lineNum = line + 1007
        elif scene == 4:
            lineNum = line + 1092
    elif act == 5:
        if scene == 1:
            lineNum = line + 1114
        elif scene == 2:
            lineNum = line + 1124
    return lineNum

def trucNum(act, scene, line):
    lineNum = 0
    if act == 1:
        if scene == 1:
            lineNum = line + 21
        elif scene == 2:
            lineNum = line + 94
    elif act == 2:
        if scene == 1:
            lineNum = line + 208
        elif scene == 2:
            lineNum = line + 255
        elif scene == 3:
            lineNum = line + 321
        elif scene == 4:
            lineNum = line + 351
        elif scene == 5:
            lineNum = line + 447
        elif scene == 6:
            lineNum = line + 481
        elif scene == 7:
            lineNum = line + 550
        elif scene == 8:
            lineNum = line + 630
    elif act == 3:
        if scene == 1:
            lineNum = line + 644
        elif scene == 2:
            lineNum = line + 668
    elif act == 4:
        if scene == 1:
            lineNum = line + 698
        elif scene == 2:
            lineNum = line + 710
        elif scene == 3:
            lineNum = line + 774
        elif scene == 4:
            lineNum = line + 853
    elif act == 5:
        if scene == 1:
            lineNum = line + 892
        else:
            print(f"error! there is no scene {scene} in act 5 of Truculentus")
    return lineNum

if __name__ == '__main__':
    views.run(debug=True)