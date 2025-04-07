# use some basic words to find the 
hard_consonants = {
    "b" : [("B", )],
    "c" : [("K", )],
    "d" : [("D", )],
    "f" : [("F", )],
    "g" : [("G", )],
    "h" : [("HH", )],
    "j" : [("JH", )],
    "k" : [("K", )],
    "l" : [("L", )],
    "m" : [("M", )],
    "n" : [("N", ), ("NG", )], # NG like in "blanket"
    "p" : [("P", )],
    "r" : [("R", )],
    "s" : [("S", ), ("Z", )],
    "t" : [("T", )],
    "v" : [("V", )],
    "w" : [("W", )],
    "x" : [("K", "S")],
    "y" : [("Y", )],
    "z" : [("Z", )]
}
soft_consonants = {
    "c" : [("S", )],
    "g" : [("JH", )],
}
short_vowels = {
    "a" : [("AE", )],
    "e" : [("EH", )],
    "i" : [("IH", )],
    "o" : [("AA", )],
    "u" : [("AH", )]
}
long_vowels = {
    "a" : [("EY", )],
    "e" : [("IY", )],
    "i" : [("AY", )],
    "o" : [("OW", )],
    "u" : [("UW", )]
}
secondary_vowel_pronunciations = {
    "a" : [("AH", ), ("AO", ), ("AA", )], #TODO: consider secondary vowel sounds that are "close enough" to be decodable.
    "e" : [("IH", ), ("AH", )],
    "o" : [("AH", ), ("UW", ), ("AO", )],
    "i" : [('AH', )] # AH like limIted
}

secondary_consonant_pronunciations = {
    "t" : [("CH", )] # CH like in "century"
}

vowel_teams = {
    "ee" : [("IY", )],
    "ea" : [("EH", ), ("IY", )], #IY like 'eat' should be second
    # "(eat)" : [("IY", )],
    "ai" : [("EY", )],
    "ay" : [("EY", )],
    "oa" : [("OW", )],
    # "oo" : [("UW", ), ("UH", )], #UW like 'zoo' is first, UH like 'good' is second
    "ow" : [("AW", ), ("OW", )], #OW like 'grow' should be second
    # "(grow)" : [("OW", )],
    "igh" : [("AY", )], #TODO: Consider OUGH and other GH words.
    # "y (dry)" : [("AY", )],
    # "oo (zoo)" : [("UW", )],
    # "oo (good)" : [("UH", )]
}

digraphs = {
    "ow" : [("OW", ), ("AW", )], #TODO: handle the difference. I think OW is supposed to be taught first
    "ch" : [("CH", )],
    "th" : [("TH", ), ("DH", )],
    "ng" : [("NG", )],
    "oy" : [("OY", )],
    "sh" : [("SH", )],
    "qu" : [("K", "W")],
    "ck" : [("K", )],
    "wh" : [("W", )],
    "er" : [("ER", )],
    "xc" : [('K', 'S')]
}

double_letters = {
    "aa" : [("AA", )],
    "bb" : [("B", )],
    "cc" : [("K", ), ("K", "S")],
    "dd" : [("D", )],
    "ff" : [("F", )],
    "gg" : [("G", )],
    "jj" : [("J", )],
    "kk" : [("K", )],
    "ll" : [("L", )],
    "mm" : [("M", )],
    "nn" : [("N", )],
    "pp" : [("P", )],
    "rr" : [("R", )],
    "ss" : [("S", )],
    "tt" : [("T", )],
    "xx" : [("K", "S")],
    "zz" : [("Z", )]
}

prefix_digraphs = {
    "wr-" : [("R", )], 
    "kn-" : [("N", )], 
    "ph-" : [("F", )], 
    "gh-" : [("G", )], 
    "gn-" : [("G", )],
}

prefix_blends = {
    "bl-" : [("B", "L")], "cl-" : [("K", "L")], "fl-" : [("F", "L")], "gl-" : [("G", "L")], "pl-" : [("P", "L")], "sl-" : [("S", "L")],
    "br-" : [("B", "R")], "cr-" : [("K", "R")], "dr-" : [("D", "R")], "fr-" : [("F", "R")], "gr-" : [("G", "R")], "pr-" : [("P", "R")], "tr-" : [("T", "R")],
    "sc-" : [("S", "C")], "shr-" : [("SH", "R")], "sk-" : [("S", "K")], "sm-" : [("S", "M")], "sn-" : [("S", "N")], "sp-" : [("S", "P")], "squ-" : [("S", "K", "W")], "st-" : [("S", "T")], "sw-" : [("S", "W")],
}

suffix_blends = {
    "-lp" : [("L", "P")], "-st" : [("S", "T")], "-ct" : [("K", "T")], "-pt" : [("P", "T")], 
    "-sk" : [("S", "K")], "-lk" : [("K", )], "-lf" : [("L", "F")], "-xt" : [("K", "S", "T")], "-ft" : [("F", "T")], 
    "-nd" : [("N", "D")], "-mp" : [("M", "P")], "-st" : [("S", "T")], "-lt" : [("L", "T")], "-nch" : [("N", "CH")],
    "-mb" : [("M", "B")], "-tch" : [("CH", )], "-dge" : [("JH", )],
}

common_endings = {
    "-ing" : [("IH", "NG")], "-ang" : [("AE", "NG")], "-ong" : [("AO", "NG")], "-ung" : [("AH", "NG")],
    "-ank" : [("AE", "NG", "K")], "-ink" : [("IH", "NG", "K")], "-onk" : [("AA", "NG", "K")], "-unk" : [("AH", "NG", "K")],
    # "-er" : [("ER", )],
    "-oe" : [("OW", )],
    "-ed" : [('EH', 'D'), ('AH', 'D'), ('D', ), ('IH', 'D')],
    # "-s" : [("S", ), ("Z", )],
    "-ard" : [('ER', 'D')],
    "-y" : [("AY", ), ('IY',)] #AY like dry should be learned second #TODO: Figure out what to do with Y because right now it's considered a LETTER_COMBO, and that's not right either
}




# tbd = {
#     # ur as in hurt is ER
#     # z in seizure is ZH
# }

PHONEME_SETS:dict = {
    "hard_consonants" : hard_consonants,
    "soft_consonants" : soft_consonants,
    "short_vowels" : short_vowels,
    "long_vowels" : long_vowels,
    # "secondary_vowel_pronunciations" : secondary_vowel_pronunciations,
    "vowel_teams" : vowel_teams,
    "digraphs" : digraphs,
    "double_letters" : double_letters,
    "prefix_digraphs" : prefix_digraphs,
    "prefix_blends" : prefix_blends,
    "suffix_blends" : suffix_blends,
    "common_endings" : common_endings
}
