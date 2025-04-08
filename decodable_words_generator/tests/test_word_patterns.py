import pytest
from decodable_words_generator.word import Word

vc_words:list = [
    "at", "in", "up", "it", "on", "am", "as", "ax", "us", "um"
]

cvc_words:list = [
    "cab", "dab", "gab", "jab", "lab", "nab", "tab", "blab", "crab", "grab", 
    "scab", "stab", "slab", "bat", "cat", "fat", "hat", "mat", "pat", "rat", 
    "sat", "vat", "brat", "chat", "flat", "gnat", "spat", "bad", "dad", "had", 
    "lad", "mad", "pad", "sad", "tad", "glad", "ban", "can", "fan", "man", 
    "pan", "ran", "tan", "van", "clan", "plan", "scan", "than", "bag", "gag", 
    "hag", "lag", "nag", "rag", "sag", "tag", "wag", "brag", "drag", "flag", 
    "snag", "stag", "cap", "gap", "lap", "map", "nap", "rap", "sap", "tap", 
    "yap", "zap", "chap", "clap", "flap", "slap", "snap", "trap", "bam", "dam", 
    "ham", "jam", "ram", "yam", "clam", "cram", "scam", "slam", "spam", "swam", 
    "tram", "wham", "back", "hack", "jack", "lack", "pack", "rack", "sack", 
    "tack", "black", "crack", "shack", "snack", "stack", "quack", "track", 
    "bash", "cash", "dash", "gash", "hash", "lash", "mash", "rash", "sash", 
    "clash", "crash", "flash", "slash", "smash", "gal", "pal", "gas", "yak", 
    "wax", "tax", "bath", "math", "bed", "fed", "led", "red", "wed", "bled", 
    "bred", "fled", "pled", "sled", "shed", "beg", "keg", "leg", "peg", "bet", 
    "get", "jet", "let", "met", "net", "pet", "set", "vet", "wet", "yet", 
    "fret", "den", "hen", "men", "pen", "ten", "then", "when", "beck", "deck", 
    "neck", "peck", "check", "fleck", "speck", "wreck", "bell", "cell", "dell", 
    "jell", "sell", "tell", "well", "yell", "dwell", "shell", "smell", "spell", 
    "swell", "yes", "web", "gem", "hem", "pep", "step", "bit", "fit", "hit", 
    "kit", "lit", "pit", "sit", "wit", "knit", "quit", "slit", "spit", "bid", 
    "did", "hid", "kid", "lid", "rid", "skid", "slid", "big", "dig", "fig", 
    "gig", "jig", "pig", "rig", "wig", "zig", "twig", "dim", "him", "rim", 
    "brim", "grim", "skim", "slim", "swim", "trim", "whim", "dip", "hip", "lip", 
    "nip", "rip", "sip", "tip", "zip", "chip", "clip", "drip", "flip", "grip", 
    "ship", "skip", "slip", "snip", "trip", "whip", "kick", "lick", "nick", 
    "pick", "sick", "tick", "wick", "brick", "chick", "click", "flick", "quick", 
    "slick", "stick", "thick", "trick", "fish", "dish", "wish", "swish", "bin", 
    "din", "fin", "pin", "sin", "tin", "win", "chin", "grin", "shin", "skin", 
    "spin", "thin", "twin", "him", "this", "mix", "six", "fix", "crib", "cot", 
    "dot", "got", "hot", "jot", "lot", "not", "pot", "rot", "tot", "blot", 
    "knot", "plot", "shot", "slot", "spot", "cob", "gob", "job", "lob", "mob", 
    "rob", "sob", "blob", "glob", "knob", "slob", "snob", "bog", "cog", "dog", 
    "fog", "hog", "jog", "log", "blog", "clog", "frog", "cop", "hop", "mop", 
    "pop", "top", "chop", "crop", "drop", "flop", "glop", "plop", "shop", 
    "slop", "stop", "dock", "lock", "rock", "sock", "tock", "block", "clock", 
    " flock", "rock", "shock smock", "stock", "box", "fox", "pox", "rod", "sod", 
    "mom", "but", "cut", "gut", "hut", "jut", "nut", "rut", "shut", "cub", 
    "hub", "nub", "rub", "sub", "tub", "grub", "snub", "stub", "bug", "dug", 
    "hug", "jug", "lug", "mug", "pug", "rug", "tug", "drug", "plug", "slug", 
    "snug", "bum", "gum", "hum", "mum", "sum", "chum", "drum", "glum", "plum", 
    "scum", "slum", "bun", "fun", "gun", "nun", "pun", "run", "sun", "spun", 
    "stun", "bud", "cud", "dud", "mud", "spud", "stud", "thud", "buck", "duck", 
    "luck", "muck", "puck", "suck", "tuck", "yuck", "chuck", "cluck", "pluck", 
    "stuck", "truck", "gush", "hush", "lush", "mush", "rush", "blush", "brush", 
    "crush", "flush", "slush", "pup", "cup", "bus"
]

cvce_words:list = [
    "bake", "bale", "bane", "bare", "base", "bate", "bike", "bile", "bine", 
    "bore", "cage", "cake", "cane", "care", "case", "cave", "cede", "code", 
    "coke", "cole", "cone", "core", "cove", "cude", "daze", "dele", "dine", 
    "dole", "dope", "dose", "dude", "fade", "fame", "fare", "faze", "fine", 
    "fore", "fuse", "gage", "gale", "game", "gape", "gate", "gaze", "hide", 
    "hike", "hone", "hose", "jape", "jute", "kite", "lace", "lame", "lane", 
    "lase", "late", "lave", "laze", "lice", "life", "line", "lobe", "lode", 
    "lone", "lure", "mace", "make", "male", "mane", "mate", "mere", "mice", 
    "mole", "mute", "nape", "note", "pave", "pine", "pole", "rake", "rate", 
    "rave", "raze", "ride", "ripe", "rite", "rove", "rule", "sake", "sane", 
    "save", "sine", "site", "size", "sone", "tame", "tape", "tare", "time", 
    "tune"
]

cvcvc_words:list = [
    "ballet", "buffett", "easy", "below", "tutu", "cocoa", "body", "buddy", 
    "mummy", "cutie", "ditto", "dojo", "foggy", "gummy", "hero", "hooray", 
    "kitty", "polo", "putty", "picky", "payday", "nemo", "mocha", "taco", 
    "lady", "happy", "pillow", "coffee", "hippo", "minnow", "mighty", "many", 
    "lucky", "loopy", "typo", "tv", "tummy", "tuba", "taffy", "solo", "sofa", 
    "soapy", "shaky", "sunny", "repay", "relay", "fuzzy", "pouty", "baby", 
    "cookie", "honey", "yo-yo", "penny", "bunny", "heavy", "ladder", "money", 
    "puppy", " ", "lego", "pony", "mama", "mommy", "dada", "daddy", "papa", 
    "nana", "potty", "dino", "tummy", "pogo", "pouty", "quota", "rainy", 
    "repay", "sauna", "silo", "shaky", "sunny", "solo", "tattoo", "payday", 
    "naysay", "meadow", "loopy", "loony", "limo", "levee"
]

cvcvc_double_cons_words = [
    "bonnet", "muffin", 
    "happen", "sudden", 
    "hiccup", "traffic", 
    "mitten", "glutton", 
    "gossip", "classic", 
    "goddess", "grommet", 
    "possum", "trellis", 
    "rabbit", "trodden", 
    "tennis", "griffin", 
    "fossil", 
]

cvccvc_words = [
    "picnic", "mascot", 
    "magnet", "victim", 
    "rustic", "candid", 
    "basket", "tinsel", 
    "goblin", "submit", 
    "tablet", "nutmeg", 
    "velvet", "cactus", 
    "fabric", "tonsil", 
    "combat", "seldom", 
    "napkin", "public", 
]

cvccvc_with_blends_words = [
    "tantrum", "pilgrim", 
    "inflict", "address", 
    "flipflop", "untwist", 
    "Alfred", "kindred", 
    "acquit", "distress", 
    "pumpkin", "muskrat", 
    "anklet", "abstract", 
    "complex", "hundred", 
    "impress", "dandruff", 
    "culprit", "plankton", 
]

@pytest.mark.parametrize("word", vc_words)
def test_words_are_vc(word):
    w = Word(word)
    assert w.features["is_vc"] == True

@pytest.mark.parametrize("word", cvc_words)
def test_words_are_cvc(word):
    w = Word(word)
    assert w.features["is_cvc"] == True

@pytest.mark.parametrize("word", cvce_words)
def test_words_are_cvce(word):
    w = Word(word)
    assert w.features["is_cvce"] == True

@pytest.mark.parametrize("word", cvcvc_words)
def test_words_are_cvcvc(word):
    w = Word(word)
    assert w.features["is_cvcvc"] == True