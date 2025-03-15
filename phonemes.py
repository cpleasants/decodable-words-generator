# use some basic words to find the 
hard_consonants = {
    "b" : ["B"],
    "c" : ["K"],
    "d" : ["D"],
    "f" : ["F"],
    "g" : ["G"],
    "h" : ["HH"],
    "j" : ["JH"],
    "k" : ["K"],
    "l" : ["L"],
    "m" : ["M"],
    "n" : ["N", "NG"], # NG like in "blanket"
    "p" : ["P"],
    "r" : ["R"],
    "s" : ["S"],
    "t" : ["T"],
    "v" : ["V"],
    "w" : ["W"],
    "x" : [("K", "S")],
    "y" : ["Y", "AY"], #AY like dry should be learned second
    "z" : ["Z"]
}
soft_consonants = {
    "c" : ["S"],
    "g" : ["JH"],
}
short_vowels = {
    "a" : ["AE"],
    "e" : ["EH"],
    "i" : ["IH"],
    "o" : ["AA"],
    "u" : ["AH"]
}
long_vowels = {
    "a" : ["EY"],
    "e" : ["IY"],
    "i" : ["AY"],
    "o" : ["AO", "OW"],
    "u" : ["UW"]
}

vowel_teams = {
    "ee" : ["IY"],
    "ea" : ["EH", "IY"], #IY like 'eat' should be second
    # "(eat)" : ["IY"],
    "ai" : ["EY"],
    "ay" : ["EY"],
    "oa" : ["OW"],
    # "oo" : ["UW", "UH"], #UW like 'zoo' is first, UH like 'good' is second
    "ow" : ["AW", "OW"], #OW like 'grow' should be second
    # "(grow)" : ["OW"],
    "igh" : ["AY"],
    # "y (dry)" : ["AY"],
    # "oo (zoo)" : ["UW"],
    # "oo (good)" : ["UH"]
}

digraphs = {
    "ow" : ["OW", "AW"], #TODO: handle the difference. I think OW is supposed to be taught first
    "ch" : ["CH"],
    "th" : ["TH", "DH"],
    "ng" : ["NG"],
    "oy" : ["OY"],
    "sh" : ["SH"],
    "qu" : [("K", "W")],
    "ck" : ["K"],
    "wh" : ["W"],
    "er" : ["ER"]
}

double_letters = {
    "aa" : ["AA"],
    "bb" : ["B"],
    "cc" : ["K", ("K", "S")],
    "dd" : ["D"],
    "ff" : ["F"],
    "gg" : ["G"],
    "jj" : ["J"],
    "kk" : ["K"],
    "ll" : ["L"],
    "mm" : ["M"],
    "nn" : ["N"], # NG like in "blanket"
    "pp" : ["P"],
    "rr" : ["R"],
    "ss" : ["S"],
    "tt" : ["T"],
    "xx" : [("K", "S")],
    "zz" : ["Z"]
}

prefix_digraphs = {
    "wr-" : ["R"], 
    "kn-" : ["n"], 
    "ph-" : ["F"], 
    "gh-" : ["G"], 
    "gn-" : ["G"],
}

prefix_blends = {
    "bl-" : [("B", "L")], "cl-" : [("K", "L")], "fl-" : [("F", "L")], "gl-" : [("G", "L")], "pl-" : [("P", "L")], "sl-" : [("S", "L")],
    "br-" : [("B", "R")], "cr-" : [("K", "R")], "dr-" : [("D", "R")], "fr-" : [("F", "R")], "gr-" : [("G", "R")], "pr-" : [("P", "R")], "tr-" : [("T", "R")],
    "sc-" : [("S", "C")], "shr-" : [("SH", "R")], "sk-" : [("S", "K")], "sm-" : [("S", "M")], "sn-" : [("S", "N")], "sp-" : [("S", "P")], "squ-" : [("S", "K", "W")], "st-" : [("S", "T")], "sw-" : [("S", "W")],
}

suffix_blends = {
    "-lp" : [("L", "P")], "-st" : [("S", "T")], "-ct" : [("K", "T")], "-pt" : [("P", "T")], "-sk" : [("S", "K")], "-lk" : ["K"], "-lf" : [("L", "F")], "-xt" : [("K", "S", "T")], "-ft" : [("F", "T")], "-nd" : [("N", "D")], "-mp" : [("M", "P")], "-st" : [("S", "T")], "-lt" : [("L", "T")], "-nch" : [("N", "CH")],
    "-mb" : [("M", "B")], "-tch" : ["CH"], "-dge" : ["JH"],
}

common_endings = {
    "-ing" : [("IH", "NG")], "-ang" : [("AE", "NG")], "-ong" : [("AO", "NG")], "-ung" : [("AH", "NG")],
    "-ank" : [("AE", "NG", "K")], "-ink" : [("IH", "NG", "K")], "-onk" : [("AA", "NG", "K")], "-unk" : [("AH", "NG", "K")],
    # "-er" : ["ER"],
    "-oe" : ["OW"],
    "-ed" : [('EH', 'D'), 'D'],
    "-s" : ["S", "Z"]
}




# tbd = {
#     # ur as in hurt is ER
#     # z in seizure is ZH
# }