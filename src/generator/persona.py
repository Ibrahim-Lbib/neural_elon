# "Muskify" phrasing & suffixes
import random 

def muskify(phrase):
    suffixes = [
    " — if that doesn’t blow your mind, you’re not thinking big enough.",
    " The future waits for no one.",
    " Probably needs a flamethrower though.",
    " Could totally be done in 3 months, tops.",
    " If we don’t do it, someone else will… on Mars.",
    " Just another Tuesday at the lab.",
    " Might cause a few explosions first. Worth it.",
    " 10x more insane than it sounds. Perfect.",
    " Failure is just R&D with extra drama.",
    " Needs AI, rockets, and a sense of humor.",
    " Designed to make regulators nervous.",
    " Let’s make it happen before coffee runs out.",
    " Humanity deserves this level of madness.",
    " If it sounds impossible, we’re on the right track.",
    " Could change civilization… or just break Twitter.",
    " Investors might panic. That’s how you know it’s good.",
    " Risk level: spicy.",
    " Honestly, surprised no one tried this yet.",
    " 100% chance of memes, 50% chance of success.",
    " Probably violates several laws of physics — temporarily.",
    " Because boring ideas are for boring planets.",
    " Not sure if it’s genius or insanity. Perfect balance.",
    " Could fund it by selling flamethrowers again.",
    " Launch it, test it, fix it midair. Classic.",
    " Future historians will call this the moment we snapped.",
    " Might break the internet. Hopefully in a good way.",
    " The odds are low. The hype is high.",
    " If this fails, at least it’ll fail spectacularly.",
    " We’ll make it open source after it works… probably.",
    " Elon would 100% tweet this at 3AM.",
    " This idea runs entirely on chaos and caffeine.",
    " Let’s disrupt everything and apologize later.",
    " Someone call NASA. Or a therapist.",
    " Yes, it’s technically legal. Mostly.",
    " Could double as a meme generator.",
    " Would definitely confuse aliens.",
    " Should probably trademark it before Neuralink does.",
    " Warning: may cause existential crises.",
    " Reality distortion field: activated.",
    " Add rockets. Always add rockets."
]
    suffixes_choice = random.choice(suffixes)
    return phrase + suffixes_choice 
