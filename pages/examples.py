import streamlit as st
import pandas as pd

def show_examples():
    st.title("Examples")
    
    # Add CSS for consistent styling
    st.markdown("""
        <style>
        @font-face {
            font-family: 'David';
            src: local('David');
        }
        .content-text {
            font-size: 16px;
            font-family: 'David', Arial, sans-serif;
            direction: ltr;
            text-align: left;
            background-color: white;
            color: black;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            border: 1px solid #ddd;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Information about the examples page
    st.write("This page shows examples of rated content for reference. You can filter the examples by rating criteria.")
    
    # Create embedded data from the text file you provided
    data = {
        'title': [
            "idek.",
            "I don't know anymore",
            "My best friend killed himself",
            "Lost",
            "living is so boring",
            "i want to hang myself is this hurt",
            "i wish my friends didn't stop me from killing myself",
            "My rabbit died and I want to die too.",
            "I do not know what to do anymore",
            "Envy",
            "suicidal ideation due to short term disability denial",
            "Please",
            "Life sucks and then you die.",
            "Desire, but no intent",
            "I wish it were easier to die",
            "I want to blow my brains out",
            "I want to kill myself tonight.",
            "Might just kill myself lol",
            "I'm so exhausted. I think I want to finish my letters to my family",
            "I don't know how to be a living person",
            "failed my resits",
            "i'm not scared...",
            "A classic without a sufficient answer since the centuries...",
            "I can't save anyone",
            "I just need some words of support, ready to end it all",
            "I'm ready to go right now.",
            "Why are all the good people suicidal?",
            "Haven't been here for a long time",
            "I wish I deserved to be happy",
            "I think I'm a narcissist and I don't want to be me anymore.",
            "Help my girlfriend wants to die",
            "Want to end it",
            "Okey... so hii",
            "I don't want to throw 3 months of being self harm free away",
            "Just a big rant",
            "counting the days",
            "Why do i sometimes have suicidial thoughts and sometimes even attempt at it?",
            "i'm trying not to kill myself because my boyfriend is my entire world but it's so hard",
            "I know I have no value"
        ],
        'content': [
            "hi? um tbh i donג€™t even know what to say fr cuz currently my mind is all over the place. but im freshly 21 (july 9th), canג€™t keep a job, depressed, an addict *i donג€™t have a drug of choice per say but i get high everyday* with sometimes ecstasy, fentanyl, xanax, percocets, weed, lean etc. i have ptsd from the things iג€™ve done and the things iג€™ve seen. i have a fiancֳ©, who is basically going through the same things i went thru but she recently moved back home to find a better job for us and im hoping she can get clean and move on with her life so she wonג€™t have to worry about me anymore, anyways idk why im rambling and not just getting on with it. i want to kill myself but i dont have the balls to do it. today was the first time i came really close to it because i actually put my finger on the trigger and imagined how it would be if i did it. i felt numb about it because for the first time i thought about what my family would think, i didnג€™t care about it. but here comes my mom i will continue later.",
            "\"I'm 14 (male) and lost and don't even understand myself anymore so I just decided to post here. \nFor this entire summer I've been having more depressive and suicidal thoughts than ever before. I've been laying in bed late at night and contemplating ending it all but then during the day I manage to forget all the sadness. I want to kill myself but I can't. I feel sorry for my parents, who are going to have to live without me.\nWhy? Because I hate myself. I have the \"\"perfect\"\" life. Loving parents, good grades, excellent home, decent friends yet I manage to fuck up in every fucking way possible. I get into fights with my friends all the time because I'm an asshole. I lie to my parents daily, I go behind their backs to do some things. I hate the way I look, act and basically every part of me. I feel like a waste of space, like I don't deserve this life.\nWhy can't I just fucking be normal? Should I just jump off a balcony? Idk anymore. I feel lost.\"",
            "He was 24. We met when we were teenagers. We were in a romantic relationship for a while, broke up, and then decided to stay friends. He was the only person I could confide in. He faced a couple of setbacks and had a few shitty days and 2 months ago, killed himself. I woke up to a call from his boss saying he didn't show up to work (I was his emergency contact, that's how close we were). I went to his house and found him dead. I wont say what method he used. We were gonna move in together. Now I'm alone, I have no friends who I can talk about deep stuff with like I could with him. I saw how he did it and I want to copy him. I can't live the rest of my life with this feeling. I go on the suicide bereavement subreddit every day and see the pain that people are still in 10, 20 years on. I found comfort in knowing there are others who relate at first but now, it doesn't make me feel anything. I feel hopeless. I hated this world anyway even before this happened. It was me and him against the stupid culture we live in. Now I'm alone and I'm going to kill myself too.",
            "24m, no job, no friends, no gf, no studies, sometimes i feel like crying but the tears won't come out, sometimes i feel like ending with everything but i know I'm not brave enough. sometimes I feel like I shouldn't be born, I can't find a really good reason to live for, i have no goals, I just don't what i am or what should I do, i feel lost ",
            "like im so tempted to down a bottle of pills bc i could literally just sleep forever. i love sleeping and im honestly done with this life. im not afraid of death at all bc 2 of my loved ones have died and idk what im gonna do after highschool. im not even sad im just over all of this.",
            "i tried overdosing medication 7 times at extreme dose i always went in reainiomation i need to finish plz tell me to hang myselfkdsls",
            "\"im drunk rn ognore typos and stuff\n\nso last night i got blackout and tried to kms apparently like 16 times even tho i can only remember 3? (its all a blur) and i just wosh they wouldve let me do it cause not im left witht eh regret and guilt that i put them through seeing me like that, and oh god the embarassment\n\nand i had the courage, i had the courage and they stopped me and im kinda angry but grayeful too cause im not sure if i want to die cause i dont always i just have mad moods swings like happy to suicidal in an hour on repeat all day but usually sad and i feel like i would be free from eevrything if they didnt stop me running into the traffic\"",
            "\"My parents took my rabbit to the vet while I was at work and they put him to sleep. He was a disabled rabbit with a splayed leg and arm, but we take him in just like that, and I decided to take good care of him, I gave him everything I had, to this little innocent rabbit, because of his disabilities he was so sweet and docile, he would never growl or bite, my rabbit really gave me unconditional love everyday. I wish he was still alive, I will never forgive my parents. My rabbit was having loose stools for quite some time, and we didnג€™t know why, even if he was eating the best food and hay. The vet said he was having loose stools because of his lack of mobility his body was not working well. The stool was sticking to his fur everywhere so I had to wash him everyday, I really loved that rabbit and I still do, he developed sores, had his skin open, once I took him to get his fur trimmed and the vet made a cut to his legs bc he moved too much that never healed properly maybe because he dragged that leg, so his wounds started to get worse and have a bad smell, the vet said his wounds would never heal and that it was better to put him down, thatג€™s what my parents told me. I would have said no to put him down and try something else, now Iג€™m so hurt. Iג€™m so sad, I wish I was dead so I donג€™t have to deal with his loss, I go everyday where he is buried and I bring his food, hay and write him letters everyday, Iג€™m not going to work because I got medical leave due to depression. Iג€™m planning to go visit him everyday that I can and bring him food and hay, so at least I can feel that I can still take care of him. \n\"",
            "\"Guess I will start at the beginning. I've been struggling with suicidal thoughts since as far as I can recall 12 years old. I didn't start going to therapy until 4 years later. For these 4 years I've had countless attempts, all failed because I am honestly scared of dying. Not like my big sister who got a panic attack several times and was immediately rushed to therapists and psychiatrists and now she is fine while I suffered with those thoughts telling me to hang or cut myself until I was caught during one of my attempts. I took antidepressants but that made my situation worse.  \nSome people tell me to \"\"thug that shit out\"\" but I've been doing it for 5 years and I am tired. I don't even see myself alive in the next 2 years maximum.  \nLast Year I got into art and for some reason it feels like the only thing that makes sense to me and at the same time it is what is destroying me. I keep comparing myself to other artists who are far better than me but have less experience and that has led me to self harm and back to the hole of suicidal thoughts. I want to draw more but at the same time every time I draw I either fight the urge stab myself with my stylus. Like I feel I've pass the point where I can't stop otherwise I will become worse.\n\nI've been wanting to just tell somebody about this because I have no one I can talk to right now that understands what I have been going through\"",
            "\"I envy the people who have committed suicide . I wish I had the guts to do the same.\n\nThe urge to end it all is overwhelming. Life feels like a relentless, joyless struggle, and even though I'm trying to hold on, each day is a battle. There are fleeting moments where I feel a sliver of hope, but mostly, it's just a constant, heavy numbness. Everyone says they have their bad days, but for me, it feels like every day is just another fight to survive.\"",
            "\"i'm losing my mind. i don't know what to do or who to turn to. i went on short term disability in april for a severe mental health crisis. my claim was approved without issue but the treatment i was receiving in my home state was insufficient, so i was sent out of state for a specialized PHP program. since being down here (1.5 months) my disability extension has been pending and my adjustor has been working with me to get the proper documentation from my new care team. i've been scraping by on pennies with the anticipation that i will be backpaid.\n\n i finally got word that my extension is denied and i will not be receiving back pay or future payments. i am devastated. i can't afford a flight back to my home state, all of my bills are past due, and i don't have anyone to ask for financial assistance. i'm about to lose my phone service. i could lose my job. my care team doesn't know WHAT to do for me. they had me do a risk assessment on friday because i was having some suicidal and self injurious thoughts, but i have weekends to myself (they provide patients apartments to stay in) and i am spiraling. \n\ni have spent my entire life in so much pain. i have an eating disorder, severe PTSD from childhood abuse and sexual assault, depression, and panic attacks. i am impulsive and dangerous to myself. i have been in poverty most of my life. i finally tried to prioritize myself and get better, but i'm seeing how fucking futile an effort it was. i can't see a way forward. i can't get home. \"",
            "Can someone please talk to me so I donג€™t go buy a gun or put my head in this noose?",
            "My wife hates me. My career is non existent. It's probably all my fault. I've been working since I was 17 to make a life and provide for a family and it all feels wasted. My wife has made it very clear she is not attracted to me anymore. But I'm the bad guy for wanting sex in a fucking marriage? She gets to be a stay at home mom. Very rare in today's economy. Her bitch ass sister lives with us because she's a usless piece of shit. I want to kill myself because what did I work so hard for wanting a family just to have a spoiled ass resentful family that doesn't appreciate shit? I've been seriously considering eating a bullet for awhile now and it only gets more enticing the long er this trashcan situation goes on. The literal only reason I haven't done it yet is because of my daughter. Damn what I would give to let someone else pay for all my shit so I could shit at home and raise my kid...  fucking unappreciative cunts is all I can come up with. At this point it is all only my fault for letting myself be taken advantage of. I can't wait to either get the courage to pull the trigger. Or just get hit by a bus at this point. Life is truly pointless. I wish I was never born. This world is trash. ",
            "\"I am just tired from living much more. It all seems even more bleak and hopeless from now on, and I honestly think anyone, including myself, would be better off if I was never born into existence.\n\nI do not think I should kill myself, and I am not gonna try this any time soon, but I qould be a liar if I said I do not want to finaly be set free from everything.\"",
            "Iג€™m tired of the constant fatigue and depression. Nothing ever works out for me ever. I donג€™t have a job or anything. My only will to live left me for another woman. I donג€™t love the people that love me I really donג€™t care I just want to be gone and at peace Iג€™m tired of suffering with this bs. ",
            "\"Everyday the voices just get louder and louder\nlouder. I'm a sacrareligious weirdo. A piece of garbage. The second someone hands me a gun I'm killing myself. Might as well join the army.\n\n\nI can't wait to let the voices win.\"",
            "\"The urge is stronger than ever.\n\nIt is over my gender, I hate being seen as an object- I hate the way men are, I hate it all. \n\nI know men are in this subreddit more and wi get comments saying their life is bad, I know.\n\nI really want to die, I donג€™t want to be seen as an object I hate it, I hate it all.\n\nI wish I was a man so bad, Iג€™ll never be a man.\n\nMy worth on this world is based off how I look and itג€™ll always be like that I canג€™t cope anymore \"",
            "\"Might just jump off a bridge or blow my brains out lol. Might overdose lol. \n\nHahג€¦ but not really. Iג€™m too pussy to take myself out of this life. And in the grand scheme of things, whatג€™s the difference between dying now and a few decades from now? Only a lot of torment, right? I can handle a few decades of torment \"",
            "Nothing's getting better. Therapy isn't working. Meds aren't working. Even professionals are stumped and think there's nothing more they can do. I'd like to watch some videos of people who saw the afterlife to soothe me and finish up my letters. I'm so scared every day. I used to stay for my pets but my pets died and no one in my family wants to get anymore. It'll take me a while to finish these letters but I hope it's worth it. I need to get rid of all my things and give them away or sell them. Maybe I can give the money to my sibling. I won't need it. I don't have a plan for suicide but I've come far enough to see that there really isn't another option anymore. ",
            "\nI am sick and tired of getting up and out of bed everyday. My body feels like living itself is an illness. I feel like with every breath of air I take I am being suffocated. I am an adult in the world, but I lack the common sense, drive and energy it takes to be one. I canג€™t drive, donג€™t cook, keep my filthy room a rotting sanctuary, and donג€™t clean. Because I am so helpless and canג€™t do simple things I have always had to ask for help. But even as a kid being hungry, sick, needing a ride or just being sad I have found that I have been felt like a burden. Iג€™ve grown to hate asking for help. The groans and complaints to why I canג€™t do it myself. The inconvenience I bring to others. I am the problem. I know that if it was for others it would be okay. I would even be okay helping others, if I could even do that. Iג€™m the burden. I hear it all the time. There is little I can do. I spend so much time rotting in bed. I donג€™t even see the point of getting out of it anymore. Iג€™ve expressed so much times as a kid wanting to kill myself. Maybe it was real, or just a cry for help. But the lack of concern, and even the voices by my own parents saying to just ג€do itג€ is enough to know that I wonג€™t be missed. Iג€™ve seen them express so much content, love and excitement for all my other siblings. Even the ones who do next to nothing, or even when theyג€™re being rude straight to their face.  Nobody in my life is excited to see me. Thereג€™s no point in asking what Iג€™ve done, because they know itג€™s nothing and they see it everyday. Maybe because they have far much more accomplishments than I do, have all left at some point, and do their own things. But Iג€™m just here. It feels like I always will be and it eats me alive. I donג€™t have the means to leave my home, and if I did who knows if it will solve anything. The only thing I do is live, which doesnג€™t feel like enough. If I kill myself, it will finally be my turn to have done something great. I havenג€™t truly lived or been myself, and donג€™t see the point anymore. I feel like I donג€™t even understand how to be a person.To the people who havenג€™t felt like themselves, there has to have been a time where you were yourself. Who was that? How did you become yourself at any point in life and be content with it? Is there even a point to figuring it out anymore? ",
            "I have my year 2 uni resits tomorrow and already know I'm going to fail. I'm thinking of just ending it rather than dealing with the fallout that'll come from it.",
            "\"i just don't want to hurt the ones i would leave behind.\n\nif i wasn't married this would be it.\n\ndid you know that most people who have survived attempted drownings say that it was euphoric and peaceful, after the initial fear?\n\naconite is common in gardens. so is belladonna. don't people know what they are growing?\n\ni've been here too long, way way too long. i am tired like you wouldn't believe.\n\ni wish i didn't have him. i'm so lucky i have him.\n\nwhy is it so hard to say goodbye, if it's so hard to be alive?????\"",
            "What's the point of living if we are going to die one day with leaving everything behind that we have received. What's the thing that stopping us from taking \"the action\"?",
            "I canג€™t even save myself, because I never want to be saved. I keep sabotaging anything good in my life because I donג€™t want to be stuck living here. I canג€™t help anyone by being here, my existence has caused more hurt to other people rather than helping, so I donג€™t know why anyone wants me here. It feels so pointless. Iג€™m so tired of hurting and Iג€™m sure that everyone else will tire of me one day, Iג€™d rather not be around to cause anymore inconvenience. Why does everything have to hurt so much?",
            "\"Hi everyone, I just need some words of support, maybe someone to talk me off the ledge.\nI went through a nasty break up 3 weeks ago with someone I was ready to spend my life with. The breakup was bad, he assaulted me and my child. I had no choice but to call the police. He was arrested and charged but released on conditions not to contact me. \nMy mind is so confusing and I hate myself for it. Iג€™m terrified of this man and what he did was awful but you donג€™t just stop loving someone so a part of me is sad we canג€™t talk and itג€™s all so confusing. I was so in love. \nIג€™m 29 and felt like that was my last chance at a relationship. Iג€™m so lonely. I feel like Iג€™m too old and my time to be in a relationship has passed. Everyone my age is already married or in relationships.\nI just want to end it all. Iג€™m not happy. Iג€™m only alive because of my son but I feel he would be better off without me. Every day is just so hard and I donג€™t know how long I can go on like this.\"",
            "My situation couldnג€™t get any worse. Im homeless, cold and hungry. Iג€™m in mountains of debt and canג€™t see a way out. I canג€™t carry on any longer. I donג€™t want pity and I donג€™t want to be talked out of it. Im going to take my life tonight as I canג€™t even look after myself and this isnג€™t a life. Death is a lot easier then dealing with all these issues Iג€™ve created in life. Ever since I was child Iג€™ve struggled with my mental health. I have no idea why I canג€™t be normal and be self efficient like everyone else. I have no family anymore and no friends. Iג€™m going to tie a bag to my head tonight and end my pain. Im writing this post because I want someone to know I existed. I have no family or friends. The burden of debt has worn me down. I love history, sports and walking outdoors. Please look after yourselves and donג€™t make the stupid mistakes Iג€™ve made.",
            "Every day I am on this sub reddit, reading the comments and stuff. I just noticed that almost all the good and kind people are suicidal. Why tf is that? Is the World that evil? ",
            "\"So, I guess this is my return post. I (M) thought I really was better. But now I realise, things around me are just better. Temporarily. I'm angry at everything, at times. I miss my boyfriend. I thought that having one would make things better. But I guess my love for him and my hate for life can coexist. Not just my hate for life, but for myself too. I often wish bad things would happen to me. Particularly torture. I ask other people to do torture me, and I always hate it in the moment, but love it in hindsight. I wish someone would go further than the slaps and punches I've suffered so far. And the choking. I wish someone would maybe beat me bloody. Or brand me.\n\nI don't even really know why I made this post, guess I just wanted to let things out. I feel like a coward, a pussy. I feel like I'm immature for being so angry. But how can I not be? I think I was made to always be angry, but I'm too cowardly and too fucking lazy to do shit about it. So I just lay in bed. Angry, but I guess really just fuckin tired and pathetic. Somebody who is angry but does nothing, just lays in bed all day. I would call that pathetic \"",
            "\"I'm so fucking tired, barely hanging on by a thread. I miss a day of pills and suddenly I have a knife to my throat. I don't when it stopped but I know I stopped feeling happy before my preteens.\n\nI just want to feel happy, to not want to blow my brains out every passing moment of my worthless life. To not wake up and spend an hour in bed, scrolling mindlessly otherwise I have a breakdown.\"",
            "\"so yea. title is pretty self explanatory. ever since I was fourteen I thought I had bpd. but since last summer I realized that itג€™s more likely that I am a narcissist. I donג€™t care about anyone or anything I just fake it. Iג€™ve always had weird jealousy issues and have been jealous of pretty much anyone including exes. I would be jealous that he had so many genuine connections meanwhile I had none because I donג€™t know how to connect with people. I donג€™t know how to care when I just donג€™t. And I am tired of pretending. I donג€™t want to live life as this soul sucking void. And I donג€™t want to live with my mistakes either. not because I care about how my actions have effected others. I care about my reputation. I care about how others now view me in a horribly negative light. and I donג€™t know how to fucking fix that. Iג€™ve done so many horrible things. nobody likes me and I know exactly why but I canג€™t. change. it. It is just who I am. And I donג€™t want to be me anymore. I am rotten to the core and sick of myself. Iג€™m sick of my ugly thoughts. Iג€™m sick of how I secretly judge people in my head when they are such kind and genuine people. Iג€™m sick of how I feel so entitled to everything, how I feel like people owe me things, Iג€™m fucking sick of being so selfish, and itג€™s frustrating because I donג€™t know how to NOT be selfish I just AM. I donג€™t care about anyone. I only care about myself. I canג€™t even empathize with my own mother. I canג€™t empathize with my own sister. My mom works so hard every single day with no days off, she is worked to the bone but still somehow stays strong and keeps going, and here I am a lousy useless piece of shit who canג€™t even tell her the truth about who I am. I know what she is going through, but for some reason I just canג€™t empathize. I donג€™t fucking feel anything. I donג€™t know how else to explain it. But I just know that I am terrible. And I need to eradicate myself. Itג€™s all I can think about. I am so fucking ashamed of who I truly am and everybody knows. I can never escape myself. And nobody understands. Nobody ever could if I told them. If I told them the truth they would see me differently and probably even be scared of me. \n\nI first had the realization I may be a narcissist last summer and I almost killed myself then for the same reasons I want to now. I forgot all about it and went on with my lifeג€¦ and then I hurt more people. and now Iג€™m right back where I was before. the same realization is hitting me. I am an empty void. I am nothing and will never be anyone. I am a miserable witch like someone has said about me. And I should kill myself. I DONT WANT TO BE ME ANYMORE. I canג€™t be me. I have to kill myself. I donג€™t want to be here anymore I just donג€™t I just donג€™t Iג€™m just done. I fucking hate myself so much to the very core and my mother will never understand. every time I think about it I start crying because I know that it would devastate my mother. but she just doesnג€™t understand. because I can never tell her who I really am. I want to go so so badly but I donג€™t abt to hurt her. but I know that I am terrible. everybody hates me. and it will always be that way. I will never learn from my mistakes I just keep doing them over and over again with no remorse. hurting and using people for my own gain. messing with people emotions for fun. I always say Iג€™m going to change Iג€™m going to work on myself and I really do want to, but once I try, I get discouraged because I realize that Iג€™m a soulless and emotionless piece of shit who doesnג€™t actually give a fuck like I say I do. so itג€™s like whats the point when Iג€™m like this. when it canג€™t be changed. I canג€™t make myself care when I donג€™t. \"",
            "I dont know what else to do other than ask people who might be able to help, my girlfriend has wanted to die for sometime now. For years because of something in her past she wont tell me about and I am the only thing keeping her alive. The day I met her she was going to kill herself. That was two months ago. She doesnt sleep, shes depressed, she posts tiktoks about suicide everyday and she said shes going to do it. I plead with her to help her but she said she doesnt want help. What can I possibly do to save her? I dont know why she is so sad and she wont tell me. Someone help please",
            "\n\nThereג€™s no meaning, no purpose for me to be here. I have nothing to do and i keep repeating the same day over and over again.",
            "I've cut myself, and told my boy best friend about that, and he got mad, saying that nothing is missing from my life and that I cut myself without a reason, but I really struggle everyday... I could end it all right now but I can't. I could really use someone I could talk to.  So if anyone s up and wants to talk, I'm all up",
            "\"Not in a good place atm. Trying to figure out how to be an adult model without any form of help from my boyfriend, who yells at me if I ask him for help. I don't know why I continue to ask him for help. \n\nI said I'd stop. He ignores me. I'm doing it for validation for myself and to be worthy of him. I don't want my legs to be cut up again. I'm trying so hard not to do it.\n\nPlease brain don't make me do this. The relief won't help. Don't make me give in. \"",
            "\"Iג€™ve been begging everyone I can think of for help, Iג€™ve even told people I feel suicidal. I kept thinking things would get better, and sometimes I feel like they are, but then I crash so so hard and feel compelled to hurt myself. My parents are my only support but theyג€™re elderly, sick, critical, and always talking about how stressed they are because theyג€™re going to die soon and Iג€™ve amounted to nothing. Finally have a job I love but I only work 3 days a week and couldnג€™t live on what I would make full time anyway. And itג€™s not enough that I love my job, everyone tells me I need to do something better because I have a degree. I donג€™t know what else to do because I canג€™t figure out what my options are and how to choose if many options sound theoretically awesome. No one wants to be around me, my ex broke up with me nearly a year ago and Iג€™m still broken by the things they said about how they couldnג€™t be around me and I have too many issues. Iג€™m on thin ice with everyone all the time because Iג€™m very forgetful and canג€™t stop talking about it whatever my latest special interest is even though I try. So many failed relationships and friendships throughout my whole life. \n\nI have migraines all the time and I keep failing treatments. People suspected I had adhd when I was in middle school and I took cognitive tests but I never got ג€officiallyג€ tested. All of my blood relatives have adhd (Iג€™m adopted). But I canג€™t get help, no one will take me seriously, Iג€™ve tried so many doctors and psychiatrists. Iג€™ve been a textbook example my entire life but no one believes me, they all think Iג€™m nuts to bring it up or that Iג€™m a drug seeker. They keep giving me drugs for anxiety and depression but nothing works at all. I canג€™t function, Iג€™m crippled by exhaustion and pain and executive dysfunction. Canג€™t sleep, canג€™t engage in my hobbies. Canג€™t do anything but doomscroll which I donג€™t even want to do. Canג€™t feed myself properly. Canג€™t clean up my room. I keep forgetting about doctors appointments and therapy appointments and trying to remember to reschedule them is a nightmare. But they donג€™t help anyway. I try to make positive changes but cannot keep them going. When I try to get out of the house or spend time with friends I feel exhausted and just want to disintegrate into nothing. \n\nMy dad had a stroke recently and when Iג€™m alone I scream and cry like a child about how I wish it had been me. It should have been me. I was diagnosed with a growth in my brain and while waiting to hear if it was benignג€¦I was the happiest Iג€™ve been in many, many years. I didnג€™t want to have brain cancer but at the same time when I found out it was benign and not growing my mood crashed majorly. \n\nJust venting here because I canג€™t tell anyone. Iג€™ve never wanted to live and the help that people claim is out there remains elusive to me. \"",
            "been horribly depressed for my whole life... childhood trauma, then it just kept getting worse despite trying to find religion, tons of therapy, inpatient and outpatient hospitalization, medication, etc... .. eventually inability to work led to legal issues despite me having skills and some work ethic... pulled it together long enough to raise a kid, but all that energy was brutal.... now he is in his mid-20s and won't even talk to me anyway... lost love of my life.. she is with another man but wants to stay in touch, and I cannot say no to that even though it is pure torture for me.... exhausted, poor health... have nightmares every time I close my eyes... but still so tired I sleep more and more every day... just waiting to die so what is the. point? None. ... and then it got worse a few years ago... arrest for downloading child porn, which was not even on purpose.... for real, they knew it so they gave me the lightest sentence possible (no jail, off registry in 5 years, allowed to live anywhere, allowed to even encounter kids at work...etc). but still made me unemployable so I will be homeless within 2-3 years as I am having to cash in my retirement to live.... have a woman who loves me... met her abroad and lived with her there, but they won't give her a visa because I can't make enough money to get the visa, but I know if she could somehow come, maybe my loneliness might improve enough for me to make it out of this hell... so i have to let her go... i will do that then fast until I die... I almost did that once before but family caught on and stopped me... this time they won't as i have been cut off by them for the most part.... yeah, i am posting so maybe this is asking for help but I think i am more stating that everyone should know some situations are truly lost and dying is the only way for some. It is rare, but it happens. sometimes there is only one way. i hope that anyone does try everything possible... i have tried for 40 years... i am 52 and really have been trying for 40 years.... after that long, it is okay to give up... just please people, try evertying else first.. but then forgive yourself and let go as i am doing.",
            "Like i have no idea why i attempt at suicide but then can't do it and just leave, then talk to myself in my head why i should've just killed myself. What should i do?",
            "no comment.if k don't ",
            "\"Iג€™m a gay man to start off, already devalues me in the world but thatג€™s not why Iג€™m here.\n\nMy first relationship at 18 my ex bf gave me HIV because he was an escort on the side, in secret.\n\nMy next relationship wasnג€™t until 3 years later (because prep hadnג€™t been invented yet and everyone I got close to saw me as a risk). He ended up being physically and emotionally abusive for the 4 years we were together.\n\nIt wasnג€™t until I met my current partner that I felt safe. However I have PTSD from the previous relationships and Iג€™ve had moments where I put things on him he didnג€™t deserve, but I always owned them, sought help in therapy and through SNRIs.\n\nRecently, after almost 4 years together he tried to fuck my friend about 100 feet from me, I found out about it and he told me he was no longer in love with me. But ultimately he wanted to try to get past it. I spent this weekend away to give us time and he ended up turning off our homeג€™s dog camera was on grindr, and another man who doesnג€™t live nearby was at our address. \n\nI know my anxiety isnג€™t healthy, Iג€™m not healthy and havenג€™t been since I was 15 and failed my first suicide attempt. Iג€™ve had ideations since I was 14 growing up in a hyper Christian household, and I always knew this was likely going to be my only way at peace.\n\nI hate myself, every little fraction of myself I feel is a burden to others even though I know that that isnג€™t the reality. Iג€™ve been so tough on myself through the years trying to prevent myself from accepting the cold reality that Iג€™ll never feel happiness, I can only hope for peace. \n\nAnd donג€™t get me wrong, this isnג€™t about relationships ending there is a whole lot of unpacking surrounding my history but Iג€™m just so tired, itג€™s just that when I was with these people I thought it was enough to stave off these thoughts but even what I thought was my healthiest relationship with the most wonderful person ended up being bullshit because the people I find end up not having the tools to maintain a long term relationship in terms of communication.\n\nMy self worth has been in the gutter since my teenage years, and my willingness to move forward has eroded away day by day independently of these relationships, but given how traumatic some of these were it only makes sense that these ideations I deal with on even my best of days are more punctuated. \n\nIג€™m losing if not already lost hope, I simply cannot love myself and Iג€™ve tried, and I just canג€™t go through this heartbreak again, because at this point, I just donג€™t have it in me.\n\nI just want it to end but Iג€™m terrified of failing at that too. I have a bunch of Xanax and booze, will that do it? I have access to ketamine if I ask around, coke too probably. Or will I just ruin my liver and die painfully and slowly, I need to know what the solution is, because the only other thing I think would work is a shit ton of random street drugs in the hopes of finding it being laced with fentanyl.\n\nIג€™m petrified of heights so jumping is out, overcoming a phobia as well as accepting in the moment that youג€™re actually safe because peace is coming is another story. Iג€™ve never tried cutting myself before and I donג€™t want to go out in pain. I donג€™t have access to a firearm either. I feel like some overdose is probably the best but itג€™s risky. \""
        ],
        'Emotional Source Present': [
            "1", 
            "1", 
            "1", 
            "1", 
            "0", 
            "0", 
            "1", 
            "1", 
            "0", 
            "0", 
            "1", 
            "0", 
            "1", 
            "0", 
            "1", 
            "0", 
            "1", 
            "0", 
            "1", 
            "1", 
            "1", 
            "0", 
            "0", 
            "1", 
            "1", 
            "1", 
            "0", 
            "1", 
            "0", 
            "1", 
            "1", 
            "0", 
            "0", 
            "0", 
            "1", 
            "1", 
            "0", 
            "0", 
            "1"
        ],
        'Scale of Emotional Attribution': [
            4, 
            3, 
            3, 
            3, 
            2, 
            1, 
            4, 
            3, 
            3, 
            2, 
            5, 
            1, 
            4, 
            1, 
            3, 
            2, 
            4, 
            1, 
            3, 
            4, 
            5, 
            0, 
            1, 
            3, 
            5, 
            5, 
            1, 
            4, 
            1, 
            5, 
            3, 
            2, 
            1, 
            2, 
            4, 
            3, 
            1, 
            1, 
            5
        ]
    }
    
    # Create DataFrame from the embedded data
    df = pd.DataFrame(data)
    
    # Create only the requested filters (for Scale and Emotional Source)
    st.write("### Filter Examples")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Convert to strings to handle numeric values stored as strings
        sources = [str(s) for s in sorted(df["Emotional Source Present"].unique())]
        source_labels = {"0": "No", "1": "Yes"}
        emotional_source_filter = st.multiselect(
            "Filter by Emotional Source Present:", 
            options=sources,
            default=[],
            format_func=lambda x: source_labels.get(x, x)
        )
    
    with col2:
        min_scale, max_scale = st.slider(
            "Filter by Scale of Emotional Attribution:",
            min_value=int(df["Scale of Emotional Attribution"].min()),
            max_value=int(df["Scale of Emotional Attribution"].max()),
            value=(int(df["Scale of Emotional Attribution"].min()), 
                  int(df["Scale of Emotional Attribution"].max()))
        )
    
    # Apply filters
    filtered_df = df.copy()
    
    # Apply emotional source filter
    if emotional_source_filter:
        filtered_df = filtered_df[filtered_df["Emotional Source Present"].isin(emotional_source_filter)]
    
    # Apply scale filter
    filtered_df = filtered_df[
        (filtered_df["Scale of Emotional Attribution"] >= min_scale) & 
        (filtered_df["Scale of Emotional Attribution"] <= max_scale)
    ]
    
    # Display filtered dataframe
    st.write(f"### Showing {len(filtered_df)} of {len(df)} examples")
    
    # Convert values for display
    display_df = filtered_df.copy()
    display_df["Emotional Source Present"] = display_df["Emotional Source Present"].map({"0": "No", "1": "Yes"})
    st.dataframe(display_df[["title", "Emotional Source Present", "Scale of Emotional Attribution"]])
    
    # Display detailed view of content
    if not filtered_df.empty:
        st.write("### Detailed Content View")
        selected_index = st.selectbox(
            "Select an example to view detailed content:",
            range(len(filtered_df)),
            format_func=lambda x: f"Example {x+1}: {filtered_df.iloc[x]['title']}"
        )
        
        selected_row = filtered_df.iloc[selected_index]
        
        st.write("#### Selected Example Details")
        
        # Display title
        st.write(f"**Title:** {selected_row['title']}")
        
        # Display Scale and Emotional Source (with user-friendly labels)
        source_value = "Yes" if selected_row['Emotional Source Present'] == "1" else "No"
        st.write(f"**Emotional Source Present:** {source_value}")
        st.write(f"**Scale of Emotional Attribution:** {selected_row['Scale of Emotional Attribution']}")
        
        # Display content in formatted box
        st.write("**Content:**")
        st.markdown(f'<div class="content-text">{selected_row["content"]}</div>', unsafe_allow_html=True)
    
    if st.button("Return to Rating Page"):
        st.switch_page("text_labeler.py")

if __name__ == "__main__":
    show_examples()