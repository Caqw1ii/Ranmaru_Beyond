# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Ranmaru = Character('Ranmaru', color="#B2E0FF")
image bg_computer = "images/bg bg computer.png"


# The game starts here.


label start:
play music "audio/background_music.ogg" fadein 1.0 volume 0.5
# Your story starts here
"Another day in high schol... Same old routine, how boring."
scene sara id
with fade
"Joe hasn't shown up in a while." 
"He's a second year high school student, so we’ve had a lot of classes together since last year."
"I'm glad that we became close friends so quickly."
"Not that I miss him, just having some trouble easing around other people."
"It’s not like I’m really trying to fit in, anyway."
"..."
"For me, they're all the same, It's like they just... exist."
"If someone approached me, I wouldn't mind to have a talk, but if they don't, whatever, I dont care."
"As I recall, Joe talked to me first. If he hadn't, we wouldn't be as close as we are now."
"For some reason now the days seem to be the same, gray and dull."
"???" "Uhh.. hey there."
"???" "I'm pretty sure that you already know my name, but... just in case."
scene black
with fade
"(Huh, he never approached me before. Right, that's Ranmaru, the guy from another class.)"
"(Don't know much about him.)"
"(How haven't I noticed someone standing next to me this whole time?)"

"Ranmaru" "What's good?"
"Ranmaru" "..."

show ranmaru first
with fade
"Ranmaru" "You've been staring nowhere for some time already."
"Ranmaru" "Seems like you were alone for a couple of days."
"Ranmaru" "Honestly, I don't really have anyone to talk to either."
show ranmaru loo
"Ranmaru" "Recently, just being here kinda feels weird for me."
"Ranmaru" "Feels like the whole world’s just... on pause or something."
show ranmaru ha 
"Ranmaru" "Sorry for the random question, but I'm curious..."

label choices1:
    show ranmaru loo
    "Ranmaru" "Are you scared of the future?"

    # Menu block with indentation and choice handling
    menu:
        "yes":
            jump choices2_a
        "no":
            jump choices2_b

label choices2_a:
    show ranmaru shy
    "Ranmaru" "Me too, to be honest."
    "Ranmaru" "There is absolutely no way to predict what's gonna happen."
    show ranmaru look
    "Ranmaru" "Anything can occur, just when you think you've got it all figured out."
    "Ranmaru" "You may already start planning everything for the future."
    show ranmaru first
    "Ranmaru" "And imagine, things turn out in such a way that everything you planned and worked hard for becomes futile."
    "Ranmaru" "Or even worse..."
    show ranmaru shocked
    "Ranmaru" "What if you die much earlier than expected, without fulfilling any of your dreams and desires?"
    show ranmaru loo
    "Ranmaru" "That's so sad if you just think about it."
    show ranmaru smile
    "Ranmaru" "..."
    show ranmaru ha
    "Ranmaru" "Constantly thinking about future made me accept it."
    "Ranmaru" "If things don’t go as planned, maybe they just weren’t meant to be. Maybe there’s something else out there for us."
    "Ranmaru" "Which means that what you wanted wasn't something aligned to you, and you can't really do anything about it."
    show ranmaru shy
    "Ranmaru" "Still kinda sad though."
    jump choices2_common

label choices2_b:
    show ranmaru ha
    "Ranmaru" "Hmmm, I see."
    show ranmaru happy
    "Ranmaru" "That's a good way to live."
    "Ranmaru" "It means you're able to focus on what's happening now without any fear about what will happen next."
    "Ranmaru" "If you try to plan every detail of your life for the future, you risk missing things that are right in front of you."
    jump choices2_common

label choices2_common:
    show ranmaru happy
    "Ranmaru" "Looks like you understand."
    show ranmaru smile
    "Ranmaru" "..."
    show ranmaru ha
    "Ranmaru" "It's nice to meet someone who’s not caught up in the usual noise around here."
    show ranmaru loo
    "Ranmaru" "Well, I’ll let you get back to... whatever you were doing."
    show ranmaru loo
    hide ranmaru loo
    with fade

    # Thoughts
    "(Damn, someone actually approached me.)"
    "(I wonder what that guy is up to.)"
    "(Will he talk to me again one day?)"

    "Some time passed..."
    "(It's so noisy again...)"
"(Those students are already getting on my nerves.)"
"(I don’t think I’d ever fit in with them.)"
"(Maybe I’ll be alone until Joe gets back.)"
"..."
"(Guess I’ll just wander around the school for a while.)"
"(Nothing’s really caught my attention, until...)"
"(Hmm, I’ve never actually spent much time in the library.)"
"(Looks like a good place to sit quietly and get ready for my classes.)"
"(Most people here are always in groups, so they rarely visit places like that.)"





show ranmaru smile
with fade
"Ranmaru" "......"
show ranmaru ha
"Ranmaru" "Didn't expect you to be somewhere in a place like that."
show ranmaru loo
"Ranmaru" "Or maybe I did."
"Ranmaru" "Joe still didn't come to school?"
"Ranmaru" "Just sitting here and doing nothing, huh."
"Ranmaru" "Noticed that you changed a lot since your friend stopped attending classes."
"(He noticed..?)"
show ranmaru happy
"Ranmaru" "Hold on."
show ranmaru loo
"Ranmaru" "This place is pretty boring don't you think?"
"Ranmaru" "So quiet..."
show ranmaru happy
"Ranmaru" "I think I can show you something."
show ranmaru ha
"Ranmaru" "There's one place that I enjoy staying in while others are busy."
show ranmaru look
"Ranmaru" "Sometimes I’m asked to look for supplies or stuff like that."
show ranmaru loo
"Ranmaru" "Don't really wanna do that right now anyways."
show ranmaru loo
hide ranmaru loo
with fade


"..."
"It's so dark in here.... I can't see a thing."
"O!"
"Ranmaru" "Here we are."




label character:


label background:
scene bg computer
show ranmaru dark
with fade
"Ranmaru" "Its nice, isn't it?"
"Ranmaru" "Especially when the lights are off and only computers are illuminating the room."
show ranmaru blue
"Ranmaru" "I came across this place while having a stroll."
"Ranmaru" "I'm glad that you came here with me, Sara."
show ranmaru dark
"Ranmaru" "This place is pretty empty, so I made it my safe space."
show ranmaru blue
"Ranmaru" "I come to play games here sometimes, or just...to escape for a bit."
show ranmaru gray
"Ranmaru" "..."
show ranmaru dark
"Ranmaru" "People don't usually pay much attention to this place."
"Ranmaru" "You can come here whenever you want to."
scene black
"The next day.."
show ranmaru dark
hide ranmaru dark
with fade
scene black
show ranmaru smile
with fade
"..."
show ranmaru happy
"Ranmaru" "Oh hey, Sara."
"Ranmaru" "Looks like we actually have some classes together now."
show ranmaru loo
"Ranmaru" "To be honest I didn't expect you to change any of them."
show ranmaru happy
"Ranmaru" "But... I'm kind of glad things turned out this way."
label choices:
    Ranmaru "I wonder why.."
    menu:
        "It's just that some of the subjects were too easy for me":
            jump choices1_a
        "Idk":
            jump choices1_b
        "Because of you ofc":
            jump choices1_c


label choices1_a:
    show ranmaru smile
    Ranmaru "..."
    show ranmaru happy
    Ranmaru "So...you're skibidi sigma gyatt like that??"
    Ranmaru "We both are so skibidi smart now."
    Ranmaru "Lemme know if you will need help with anything."
    jump choices1_common


label choices1_b:
    show ranmaru first
    Ranmaru "Are you really that carefree?"
    show ranmaru look
    Ranmaru "How can u change your subjects without knowing why.."
    jump choices1_common


label choices1_c:
    show ranmaru surprised
    Ranmaru "Wow"
    show ranmaru nervous
    Ranmaru "..."
    show ranmaru blush
    Ranmaru "Thanks, I guess."
    jump choices1_common


label choices1_common:
    show ranmaru loo
    Ranmaru "Anyways..."
    show ranmaru nervous
    Ranmaru "I guess I’ll be taking Japanese in a different class now."
    show ranmaru happy
    Ranmaru "See you later."

    


label bgm:


label sfx:
    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show eileen happy


    # These display lines of dialogue.


   


    # This ends the game.


    return
