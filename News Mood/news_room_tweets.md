

```python
# Dependencies
import tweepy
import json
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
# Twitter API Keys
consumer_key = 'SYTnLXrii4S3WlaMlvbQkHXY5'
consumer_secret = 'QhpDbZ8qbB971WTKkQtCtKxC4RN7D4zcjDYIcVO8nMchoKv1fv'
access_token = '866777141567991810-cquWcZc7G9knRgPV5l0ga8s74p4QGfq'
access_token_secret = 'igdaEFPXUswtpN1eCdPs84Aq0LMDCXgU0Fx5BfgO3EuNu'

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
# Target Account
target_terms = ("@BBC", "@CBS", "@FoxNews", "@nytimes", "@CNN")
```


```python
# Counter
counter = 1

# Variables for holding sentiments
sentiments = []

# Loop through the list of targets 
for target in target_terms:

   # Get all tweets from home feed
    public_tweets = api.user_timeline(target, count = 100) #(total 500 tweets)
    tweetnumber = 1
    
   # Loop through all tweets
    for tweet in public_tweets:

       # Print Tweets
        print("Tweet %s: %s" % (counter, tweet["text"]))
        
       # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = tweetnumber
        
       # Add sentiments for each tweet into an array
        sentiments.append({"User": target,
                           "Date": tweet["created_at"],
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets Ago": tweetnumber})
        
       
       # Add to counter
        tweetnumber += 1
        counter = counter + 1
```

    Tweet 1: RT @BBCSport: Some sad news to bring you.
    
    Former Stoke City defender Dionatan Teixeira has died at the age of 25.
    
    https://t.co/L2KH7PCvqD…
    Tweet 2: 🤦😂 @LiamPayne &amp; @gregjames, a fake moustache and a lift. What could possibly go wrong? #SLFN is on @BBCiPlayer now.… https://t.co/wA9yBPWNHQ
    Tweet 3: RT @BBCOne: Q: How many tickles does it take to make a squid laugh?
    A: Ten tickles. 
    
    #BluePlanet2 https://t.co/fhKPOUBp5U
    Tweet 4: RT @bbcstrictly: That shock result has left us spinning. RT to show your love for @AstonMerrygold and @JManrara 💖 https://t.co/KJVszLhB2k
    Tweet 5: RT @BBCTwo: Well, you don't see that every day... #RobotWars https://t.co/sLq92M7mqY
    Tweet 6: RT @BBCOne: Can’t beat a good accessory. 👑 #BluePlanet2 https://t.co/mRZZEdwmlO
    Tweet 7: RT @BBCPanorama: Watch our #paradisepapers investigation into the offshore secrets of the rich &amp; famous on iPlayer.  https://t.co/MIH4CMbhZ…
    Tweet 8: RT @BBCBreaking: At least 27 people killed in Texas church shooting, police commissioner in Sutherland Springs tells US media https://t.co/…
    Tweet 9: 🎥 @LouisTheroux meets disaffected former members of the Church of Scientology. #MyScientologyMovie. Tonight at 9pm… https://t.co/5hRLxriwiW
    Tweet 10: When your other half cheats on you with #StrangerThings. 😡 Via @BBCTheSocial. https://t.co/NOpHOfbIKb
    Tweet 11: 😋 Family favourites at their finest. Check out these recipes for 10 absolute classics. 👉 https://t.co/kFD6BsfO6q https://t.co/xw1Q5SYadk
    Tweet 12: Second hand smoke affects our pets too. 🚭🐶 Via @BBCBreakfast. https://t.co/TCdA8m85dm
    Tweet 13: It took more than 1 man on a single night to nearly change the course of British history. 🔥 #BonfireNight.… https://t.co/RnzZm8yh9j
    Tweet 14: 'It's one of those stories you think you know. Then you realise you just don't.'
    
    Do you know the real… https://t.co/M8np5ep1yz
    Tweet 15: 💰🥃 How much would you pay for a cask of rare Scotch whisky? An anonymous buyer in Hong Kong just dropped £285,000.… https://t.co/ZzUInzNqEo
    Tweet 16: #PeakyBlinders series 4 returns to @BBCTwo, Wednesday 15th November at 9pm. https://t.co/lbVlyzhb4p
    Tweet 17: Tonight, #BluePlanet2 makes a groundbreaking journey to the depths of the ocean. 8pm on @BBCOne. 🐟 🐡 🐙… https://t.co/S3gcHqmTMf
    Tweet 18: Moynaq: The port city that lost its water. 💦 Via @BBC_Travel. https://t.co/Qr1ZLExpBb https://t.co/G8QxO8qAZ5
    Tweet 19: Having a bonfire today? 🔥
    Make sure you think about the hedgehogs! Via @BBCSpringwatch.
    
    More 👉… https://t.co/zbHOX6yl9O
    Tweet 20: From wild goats to woodland walks - here are your pictures of beautiful Scotland. 📷 https://t.co/sv03yk0H76 https://t.co/KHKNGXcROU
    Tweet 21: Can @Joe_Sugg zip it for 30s? 
    If chatting is your thing, how about a sponsored silence for #CiN? 
    More ideas here… https://t.co/OPA2UMuuPZ
    Tweet 22: Guy Fawkes: Why do bonfires still burn 400 years on? 🔥 #BonfireNight #GuyFawkesNight. https://t.co/dAKAZY4ZEX https://t.co/lsiivkKSgk
    Tweet 23: 🐙 A group of octopuses were seen taking a leisurely stroll along a Ceredigion beach last Friday night. Via… https://t.co/n3jq0oNT7J
    Tweet 24: 🏙By 2050 70% of the world's population will be living in cities. Time to radically rethink what we want from a city… https://t.co/pz5xleBKWz
    Tweet 25: ⚽️✊ When the boys wouldn't let them play football, these girls took matters into their own hands. Via @BBC100Women. https://t.co/0j68Wbrr3Z
    Tweet 26: .@LindaRobson58, @tomallencomedy, @misJORGIEPORTER &amp; @OreOduba star in @GrumpyLGoodman's Partners in Rhyme:… https://t.co/SLJlz8D01M
    Tweet 27: 🎬 From the new Pixar animation to Oscar-favourite coming-of-age stories, here are 10 films to watch this November.👉… https://t.co/NqtcuUqOXN
    Tweet 28: RT @BBCWthrWatchers: Morning all! Only one way to start our Sunday and that's with a bit of ...
    
    🎆Oooooooooo! 🎆 Aahhhhhhhhhh!🎆 https://t.co…
    Tweet 29: RT @BBCSpringwatch: Stunning capture of puffins at the Isle of May, Scotland. https://t.co/cBWxx9rQav
    Tweet 30: RT @BBCFood: Heading to the fireworks later? Put this in the slow cooker and warm up when you get home https://t.co/EPJfvmFkfS https://t.co…
    Tweet 31: RT @bbcstrictly: Debbie’s Tango gets a remarkable reaction from Craig, and Ruth’s Paso doesn’t quite go to plan. Watch the best bits from #…
    Tweet 32: 🎇🎆 Why do we have Bonfire Night and fireworks displays every November 5 in the UK? https://t.co/lYBHme3LJZ https://t.co/qln8Tk64FN
    Tweet 33: 🥚🍳 Eggs for breakfast anyone? @Nigella_Lawson shares her secret for poached perfection. Via @BBC5Live. https://t.co/vnyAxh4gGU
    Tweet 34: RT @bbcmusic: "What do you think of Chip N Pin House..?" 😆😂
    Did you miss last night's #SLFN with @LiamPayne?
    Catch up 👉 https://t.co/6VxEw9…
    Tweet 35: RT @bbcstrictly: The first 40 of #Strictly 2017! For @thedebbiemcgee and @pernicegiovann1! https://t.co/QOmbUBbH9U
    Tweet 36: Tonight, Josh is back and at his irritated best. @JoshWiddicombe: What Do I Do Now... 9pm on @BBCTwo. 😂… https://t.co/Do2c1i94m7
    Tweet 37: .@LouisTheroux spends time with those battling the psychiatric disorder with the highest death rate.… https://t.co/2BHScuxQB5
    Tweet 38: Tonight, I Know Who You Are returns. 9pm on @BBCFour. https://t.co/DfGhcMNagW https://t.co/ecgQjgPaIx
    Tweet 39: 🥕 You don't have to spend lots of time peeling &amp; chopping to make moreish veggie meals. These are ready in no time.… https://t.co/x8cDwQQVJd
    Tweet 40: 🐝🦋🐛 'Anything that flies &amp; crawls, I illustrate them.' ~ @RLewington2.
    Via @BBCSpringwatch. https://t.co/o2fbgbTVBw
    Tweet 41: 'I lost £5,000 in 48 hours on fixed-odds betting machines.' https://t.co/8wIVhcOP7n https://t.co/D0GELRXjwe
    Tweet 42: Israa &amp; her family fled Syria in 2015. Now granted asylum in Germany, she’s rebuilt her life &amp; can go to school aga… https://t.co/pTFFUJQ3Lj
    Tweet 43: Pro surfer, Heidar Logi braves Iceland's freezing conditions to surf under the Northern Lights. 🌊🏄 Via… https://t.co/6cPd5lVami
    Tweet 44: What would you do if you won the lottery? Buy a house? Travel? 
    
    Rachel Lapierre set up the charity, @LHumanitaire.… https://t.co/Xu0ld6bBAn
    Tweet 45: Amy Winehouse, @Adele, @LoyleCarner &amp; @EllaEyre all went to @TheBRITSchool. But it's more than just a fame academy.… https://t.co/u4UL7qZKCr
    Tweet 46: Trucker culture is dying with automation – and with it millions of jobs. 🚛 https://t.co/UgdVkYIbFU https://t.co/71XSYxlaZt
    Tweet 47: RT @BBCMOTD: Peter Crouch = super sub.
    
    His 15th goal as a sub.
    
    Only Defoe (23), Kanu and Solskjaer (17) have more.
    
    https://t.co/8UftsSAX…
    Tweet 48: RT @BBCSport: FT England 29-10 Lebanon
    
    Get all the reaction on @BBCTwo &amp; @5liveSport Extra 👉 https://t.co/KklI8h3yma #RLWC2017 #bbcrl #ENG…
    Tweet 49: RT @BBCSport: Felipe Massa will retire from #F1  at the end of this season.
    
    Find out more👉 https://t.co/STCmQnwvzK https://t.co/eSlDcW15wV
    Tweet 50: RT @BBCOne: Welcome to the family business. 
    
    @jginorton leads an all-star cast in #McMafia. Coming soon to @BBCOne. https://t.co/We5GwJk4i0
    Tweet 51: RT @bbcthree: This barber reminds us how small actions can make a big difference. https://t.co/YelP68UZxh
    Tweet 52: Did you know there’s a best time to eat, think &amp; do sport? It’s not just our brain's clock that keeps time for us.… https://t.co/76BDqzsz7k
    Tweet 53: Police discover a suspected 'WW2 bomb' is actually a big courgette. https://t.co/YyKrAVnycQ https://t.co/vdZnam8Bjt
    Tweet 54: 'We have our stories, struggles &amp; power. We just need to be represented.' Meet the photographer reframing beauty.📸✊… https://t.co/bPTmyHcNfy
    Tweet 55: 🚀 ✨ Did you know that Disney is the largest consumer of fireworks in the world? More firework facts 👉… https://t.co/QLVen2LXWX
    Tweet 56: Can’t get enough of #BluePlanet2? Take a deeper dive into the science of the show with this podcast. 👉… https://t.co/qhoRuQ0PXz
    Tweet 57: Twitter users were left confused after the name "Sue" was discovered etched into an Oxfordshire field. #WhoIsSue… https://t.co/VZFnZ62n7A
    Tweet 58: To celebrate Murder on the Orient Express hitting UK cinemas, here are seven train movies to set the pulse racing.… https://t.co/PqTALE0vcn
    Tweet 59: Someone has farted on @grahnort's sofa...but who was it? 😂 (Via @BBCOne) https://t.co/zG2YvGvac9
    Tweet 60: There remains intense interest in Ruan Lingyu &amp; the mystery surrounding her death. Who was the enigmatic film star?… https://t.co/hFtAJiePry
    Tweet 61: Gossip travels fast in Shetland. 😂 Via @BBCTheSocial. https://t.co/vzZq1YZUYI
    Tweet 62: RT @BBCCiN: The best brains in Britain are building life-changing solutions for children in the #CiN Big Life Fix special.
    
    @BBCTwo​ Wed 8t…
    Tweet 63: RT @CBeebiesHQ: Whatever the weather, keep your kids entertained this #autumn with these 5 ideas...
    
    🍁🍂 https://t.co/wT8oVaVYqg 🙌
    
    @HEYDUGG…
    Tweet 64: RT @5liveSport: "My kids saw me in a state that a kid should never see his Dad"
    
    This is powerful stuff: 
    Stiliyan Petrov on his brave batt…
    Tweet 65: Happy 2nd birthday @BBCWthrWatchers! 🎈🎉
    Keep those stunning photos rolling in. 📸🌤 https://t.co/FOzCyLKlrB https://t.co/Tcy4xYfHWs
    Tweet 66: The bloodworm is one of the many 'stars' to feature in a venomous animals exhibition at @NHM_London next week. 😵… https://t.co/XxCmXRBhSS
    Tweet 67: And...relax. Spend three minutes in the beautiful British countryside with this footage from @BBCSpringwatch's wild… https://t.co/K3XJtvBbtW
    Tweet 68: RT @bbcmusic: "I'm more of a @CherylOfficial fan actually" 😂
    
    (Sorry @LiamPayne)
    
    #SLFN https://t.co/MXxDilJSq3
    Tweet 69: RT @BBCSport: The perfect recipe for an FA Cup classic.
    
    #WinnerStaysOn #bbcfacup https://t.co/wP1fszdCvU
    Tweet 70: RT @BBCNewsbeat: Beyoncé, here's some advice from the cast of The Lion King musical in London 🦁
    
    "Try not to outshine [the rest of the cast…
    Tweet 71: In childbirth, a simple light can be the difference between life &amp; death. 💡#BBCInnovators #SoCent @BBCWorldService.… https://t.co/mNFqNg0glJ
    Tweet 72: 'When I Google @Harry_Styles worst outfit, it's all the same picture'. 😂 Watch #HarryStylesAtTheBBC 👉… https://t.co/UjOJ1LcyQt
    Tweet 73: 🥐🎄✨ Forget about the Cronut, a mince pie croissant is coming for Christmas! 
    https://t.co/mrTI8CLn2r https://t.co/7BYkA8Vv3n
    Tweet 74: What drives someone to send abusive messages to a stranger online? Via @BBCTheSocial. https://t.co/Cxo8DuEtG6
    Tweet 75: If women suddenly became physically stronger than men, how would society change? 💪👩 https://t.co/qwZ5idgRsX https://t.co/zoJH7Pf6fm
    Tweet 76: 📺 👀 @EdSheeran, @LiamGallagher and @BigNarstie to appear on Celebrity Gogglebox. https://t.co/Fh0SK8VjP4 https://t.co/6re7dX2vf3
    Tweet 77: Jumping into the weekend like... #FridayFeeling https://t.co/Bn7SDR8280
    Tweet 78: 🍟 From @Harry_Styles' love of Sister Act to the way he likes his chips: what we learned from #HarryStylesAtTheBBC.… https://t.co/zHLFRFTXoh
    Tweet 79: There's still time to catch up on last week's #SLFN ahead of tonight's show, guest-hosted by @LiamPayne! 🙌😍
    Watch 👉… https://t.co/gvwjlpjsVJ
    Tweet 80: Ready to watch @Harry_Styles' show again? Us too. 🙌 💜 #HarryStylesAtTheBBC is on @BBCiPlayer now.… https://t.co/V3VkJHKToA
    Tweet 81: RT @bbcpress: Helena Bonham Carter narrates #SayingGoodbye, a special film for #CiN to shed a light on Childhood Bereavement: https://t.co/…
    Tweet 82: RT @BBCSpringwatch: Remember, you can catch up with #Autumnwatch for the next few weeks
    https://t.co/U7yr1lnpLm https://t.co/B1diCYr9zG
    Tweet 83: RT @bbcmusic: 🙌 @LiamPayne we are SO READY 😍
    #SLFN https://t.co/GWU3xAKmpq
    Tweet 84: RT @1Xtra: We've got the awesome @MayaJama for the 1st time 😵 in for @YasminEvans till 16:00 you lucky lucky people 💝
    
    🙏🏾  https://t.co/xZV…
    Tweet 85: RT @BBCTwo: Before the #PeakyBlinders return for Series 4, take an animated walk through the story so far... 😍 https://t.co/3JhEYPsOTc
    Tweet 86: In pictures: here's how the weather looked around the world this week. 🌧🍂🌗 https://t.co/vYCLWW9pu1 https://t.co/KBg4tRImNB
    Tweet 87: Scientists think that we've been wearing shoes for 40,000 years. Where did the different styles of shoes start? 👠… https://t.co/rjLMvh8WmF
    Tweet 88: From #PeakyBlinders to Margaret Atwood adaptation Alias Grace, here are ten TV shows to watch this month. 📺🍁☕️… https://t.co/iiUdktBMcl
    Tweet 89: Could this be the solution to Nairobi's housing crisis? Via BBC Minute. https://t.co/tcBiUVvxQ4
    Tweet 90: Introducing AquaSonic: The concert where musicians sing and play instruments underwater. 🎶💧 https://t.co/Xbrgxyv8mX https://t.co/pibmjQ9vW3
    Tweet 91: Melted cheese ✔️ Pickle ✔️ Russian dressing ✔️ Introducing: The @HairyBikers' Reuben sandwich.… https://t.co/kBSkwbRgSz
    Tweet 92: 📀 @KatieMelua to release @BBCCiN's official 2017 single, ‘Fields of Gold’. https://t.co/r5ihzBuvJS #CiN 
    
    More ➡️… https://t.co/D3Q9JEDnYc
    Tweet 93: RT @BBCSport: Even. More. Live. Sport. 👏
    
    Get ready for 1000 extra hours of live streaming on #BBCSPORT in 2018. https://t.co/91Uz5zo9nt
    Tweet 94: RT @bbcpress: We'll tell you what we want, what we really, really want... @GeriHalliwell on Saturday night TV! https://t.co/4G7WzQgSls http…
    Tweet 95: RT @BBCRadio2: Thanks @liamgallagher for an awesome In Concert Performance. As You Were. https://t.co/RIbPXt0SHT
    Tweet 96: RT @BBCR1: "I hate saying the word 'dumped'... I got... 'let go'"
    
    Totally using 'let go' to describe all our heartbreak now @SamSmithWorld…
    Tweet 97: RT @BBCRadio2: No need for scissors! ✂️ As you were...
    @liamgallagher's full gig is now available to watch on the Red Button...
    #R2InConcer…
    Tweet 98: RT @bbcmusic: ⚡️ #HarryStylesAtTheBBC was everything we dreamed of and more 💕”
    
    https://t.co/3GiJNH6ldv
    Tweet 99: 💦🦈 Sir David Attenborough is back on Sunday night bringing us more #BluePlanet2 action. Check out what's in store.… https://t.co/fgC3IFbybm
    Tweet 100: The village that shall not be named! Saying the name of this hilltop town in Italy brings you bad luck.… https://t.co/2oelVteA2q
    Tweet 101: Get ready for football! Stream NFL on CBS today w/ #CBSAllAccess (not available on mobile phones). Try 1 week FREE:… https://t.co/BJOWnqgBgc
    Tweet 102: Stream the LSU Tigers at Alabama Crimson Tide LIVE tonight at 8PM ET! Try #CBSAllAccess FREE:… https://t.co/L2k6pXwRIp
    Tweet 103: Stream the South Carolina Gamecocks at Georgia Bulldogs LIVE today at 3:30PM ET! Try #CBSAllAccess FREE:… https://t.co/f3nZLlh7Vv
    Tweet 104: Stream the season premiere of #LifeInPieces tonight at 9:30/8:30c with a FREE trial of #CBSAllAccess:… https://t.co/FMHinKs6si
    Tweet 105: RT @swatcbs: .@ShemarMoore takes command tonight on the series premiere of #SWAT at 10/9c on @CBS &amp; CBS All Access: https://t.co/ANyt4qF6iF…
    Tweet 106: It's almost time! Stream the series premiere of #SWAT tonight at 10/9c with a FREE trial of #CBSAllAccess:… https://t.co/lpPKp9ayTJ
    Tweet 107: RT @CBSThisMorning: Listen to @IainLoveTheatre chat w/ @Mistahwax about making @YoungSheldonCBS his own + his love for Broadway &amp; magic: ht…
    Tweet 108: The ladies are back! Stream the season premiere of #Mom tonight at 9/8c with a FREE trial of #CBSAllAccess:… https://t.co/y4vL5wMSEM
    Tweet 109: Buffalo viewers: Due to NFL, stream the CBS lineup on-demand at https://t.co/bbQB95EVxJ tonight. For more:… https://t.co/u9U9P7Ggqq
    Tweet 110: NYC viewers ONLY: Due to NFL, tune in to WLNY for CBS Thursday night lineup, or stream on https://t.co/2XNQAg6gJ6 l… https://t.co/LHJahNFRi3
    Tweet 111: Buffalo viewers ONLY: Due to NFL, stream CBS Thursday night lineup on-demand at https://t.co/bbQB95Wwph. For more:… https://t.co/Fzpq2sTzqY
    Tweet 112: NYC viewers ONLY: Due to NFL, tune in to WLNY for CBS Thursday night lineup, or stream on https://t.co/2XNQAgnRAE l… https://t.co/fnwck6n2uv
    Tweet 113: RT @ManWithAPlan: Hi-five, fans! #ManWithAPlan will premiere Monday, Nov. 13 at 8:30/7:30c on @CBS!🖐🏼 https://t.co/njrMa5S6Qz
    Tweet 114: Ready to trick or treat! Celebrate tonight with Michael Jackson's Halloween special on CBS: https://t.co/T3hlVVTfSB… https://t.co/e9ztbUeae0
    Tweet 115: Happy #Halloween! Grab your friends and watch Michael Jackson's Halloween tonight: https://t.co/T3hlVVTfSB… https://t.co/Kg5bxNqwTp
    Tweet 116: Trick or treat. 🎃 Happy Halloween! Catch up on #MJHalloween now:  https://t.co/T3hlVVTfSB https://t.co/DMyE1q4scs
    Tweet 117: RT @swatcbs: Get ready for a thrill ride this Thursday with the series premiere of #SWAT. https://t.co/xz92zXp6kR
    Tweet 118: Join the fun with Jim Parsons as Hay Man in Michael Jackson's Halloween! Watch the full special:… https://t.co/Y1FKFnRd0p
    Tweet 119: RT @SuperiorDonuts: You won't want to miss the #SuperiorDonuts Season 2 premiere tonight at its new time: 9/8c on CBS &amp; CBS All Access: htt…
    Tweet 120: RT @SuperiorDonuts: Should we blindfold @jermaineFOWLER and see how well he can guess the flavor of donuts? #SuperiorDonuts
    Tweet 121: RT @swatcbs: Sometimes following the rules &amp; doing what's right isn't always the same thing. #SWAT premieres this Thursday at 10/9c on @CBS…
    Tweet 122: RT @swatcbs: Start breaking down some doors in three days with the series premiere of #SWAT. https://t.co/X8OTd8OE9y
    Tweet 123: Find out if Vincent &amp; Victoria will escape Meriwether on Michael Jackson's Halloween! Watch it now:… https://t.co/dqNk6OZ1XJ
    Tweet 124: RT @NoActivityCBS: #NoActivity is a new CBS All Access comedy from​ ​Will Ferrell, Adam McKay &amp; @funnyordie. Contains explicit language int…
    Tweet 125: Don't miss @KelseaBallerini headline #TheThanksgivingDayParade on CBS, live from New York City on Thurs, Nov. 23.… https://t.co/ig74zfxFPy
    Tweet 126: RT @startrekcbs: Get ready to experience some major déjà vu. Episode 7 of #StarTrekDiscovery is now streaming: https://t.co/dz1lwvT52d http…
    Tweet 127: #CBS is delayed 29 minutes in New York City, Philly, NOLA &amp; parts of Louisiana, Atlanta, Charlotte, Tampa, Chicago,… https://t.co/ZM9bTTgxYE
    Tweet 128: These moves are dangerous! Get groovy with Michael Jackson's Halloween and watch the full special now:… https://t.co/TrMJgeyOX4
    Tweet 129: Get ready for football! Stream NFL on CBS today w/ #CBSAllAccess (not available on mobile phones). Try 1 week FREE!… https://t.co/URKV4PPKvp
    Tweet 130: Vincent can't help but dream big on Michael Jackson's Halloween. Catch up on the full animated special:… https://t.co/fDbgzo8nrV
    Tweet 131: Stream the #3 Georgia Bulldogs @ Florida Gators LIVE today at 3:30PM ET! Try #CBSAllAccess FREE:… https://t.co/ULrmutB6Ml
    Tweet 132: Michael Jackson's Halloween will enchant you with music, magic &amp; more! Watch the full special now:… https://t.co/lgzleI955w
    Tweet 133: The Halloween fun isn’t over for @lucastill and George Eads. Tune in to a spooky episode of #MacGyver now! https://t.co/nJePYNhmUa
    Tweet 134: “Music must be the answer!” #MJHalloween https://t.co/t4UTfizfIn
    Tweet 135: There are plenty of tricks hidden in this hotel. #MJHalloween https://t.co/vQAHVXU4Ai
    Tweet 136: That pumpkin’s got some moves! #MJHalloween https://t.co/o7oaRSXzmb
    Tweet 137: Sit back, relax and get ready to dance. Michael Jackson’s Halloween starts now on CBS and CBS All Access!… https://t.co/NkswtPMtzp
    Tweet 138: Don't miss tonight's animated special with the King of Pop's most memorable hits.🎶  Watch #MJHalloween @ 8/7c on CB… https://t.co/NQGZobg2gg
    Tweet 139: Tonight, get ready for a scary good time! Watch a sneak peek from the new animated special, Michael Jackson's Hallo… https://t.co/PxILZmCl4e
    Tweet 140: RT @swatcbs: When lives hang in the balance, can you make the tough decisions? Find out with #SWAT Split-Second Decision: https://t.co/dO2V…
    Tweet 141: Find out if Vincent, played by @lucastill, will escape the villain Conformity in Michael Jackson's Halloween tonigh… https://t.co/KPaug90mCg
    Tweet 142: It's a spooktacular special you won't want to miss! Here's how you can watch Michael Jackson's Halloween tonight:… https://t.co/3sp68DgUr3
    Tweet 143: Tomorrow, the music of Michael Jackson will cast its spell! Take a sneak peek at Michael Jackson's Halloween, Frida… https://t.co/ewuRYHSICA
    Tweet 144: Get ready for Thursdays to give you more @bigbangtheory, @YoungSheldon, @LifeInPiecesCBS, @MomCBS, &amp; more Moore in… https://t.co/sdqF0Ut5Fx
    Tweet 145: Stream the Miami Dolphins @ Baltimore Ravens LIVE tonight at 8:25PM ET! Try #CBSAllAccess FREE:… https://t.co/Otdn3QkHbG
    Tweet 146: Tomorrow, meet Christine Baranski as Ms. Grau in the new animated special, Michael Jackson's Halloween. Tune in Fri… https://t.co/jmnidjSm6r
    Tweet 147: 🎶@BigBangTheory's Jim Parsons is thrilled to celebrate "the soundtrack to his life" with Michael Jackson's Hallowee… https://t.co/0Lgxyqnpxq
    Tweet 148: .@MacgyverCBS' George Eads stars in the new animated special, Michael Jackson's Halloween, this Friday at 8/7c on C… https://t.co/xo6JsH3bZB
    Tweet 149: The stakes were high when #Bull stepped in to help his college roommate. Watch the latest episode now:… https://t.co/7dAjcF4eL4
    Tweet 150: Brad Garrett, @KierseyClemons, Jim Parsons &amp; more! Meet the famous voices behind Michael Jackson's Halloween:… https://t.co/LKYCZpkBJz
    Tweet 151: In three days, @TheGoodWife_CBS' @AlanCumming stars as Meriwether in the animated special Michael Jackson's Hallowe… https://t.co/WKiPdQ6Peq
    Tweet 152: Dance the night away this Friday with the new animated special, Michael Jackson's Halloween at 8/7c on CBS.… https://t.co/VsaIxJv7Jl
    Tweet 153: This Friday, @MacgyverCBS' @LucasTill plays Vincent in the animated special Michael Jackson's Halloween. Don't miss… https://t.co/Dg6w6yWevA
    Tweet 154: RT @swatcbs: Buckle up for a S.W.A.T. mission in this 360-degree preview: https://t.co/kBadrj4rLE #SWAT https://t.co/gpXmoUgurf
    Tweet 155: Tonight the @latelateshow welcomes back @zanelowe and the latest @AppleMusic #UpNext artist -- @SabrinaClaudio! https://t.co/BSmDOayUXf
    Tweet 156: .@Elementary_CBS' @LucyLiu stars as Conformity, the villain who forbids dancing, on this Friday's Michael Jackson's… https://t.co/Lf6Y4Z0bcQ
    Tweet 157: For States of NY, parts of VT &amp; Maine  New Start Times: #60Minutes 7:36pmET #WisdomOfTheCrowd 8:36ET #NCISLA 9:36ET… https://t.co/WxzNdfzR6n
    Tweet 158: For most of East/Midwest New Start Times: #60Minutes 7:34pmET/6:34CT #WisdomOfTheCrowd 8:34ET/7:34CT #NCISLA 9:34ET… https://t.co/EJKaVsJZ2K
    Tweet 159: Get ready for football! Stream NFL on CBS today w/ #CBSAllAccess (not available on mobile phones). Try 1 week FREE:… https://t.co/Cu6sKlgjT6
    Tweet 160: Only 1 week left until you can meet @bigbangtheory's Jim Parsons as Hay Man on the new animated special Michael Jac… https://t.co/rGPlUegVjC
    Tweet 161: RT @swatcbs: Keep your phone locked and loaded with these #SWAT wallpapers: https://t.co/ff0efC5GPJ https://t.co/aRoB9005ur
    Tweet 162: RT @startrekcbs: The writers of #StarTrekDiscovery picked their favorite classic #StarTrek episodes: https://t.co/mM8V07fFdX What's your fa…
    Tweet 163: Stream pilots of the new CBS shows for free on @Apple TV, @RokuPlayer &amp; @amazonfiretv! Find out more:… https://t.co/zT0z4YMRw4
    Tweet 164: Stream the Kansas City Chiefs @ Oakland Raiders LIVE tonight at 8:25PM ET (Not available on mobile phones):… https://t.co/IxnmfZxjFi
    Tweet 165: RT @ScorpionCBS: No one should be bullied or called names simply for being who they are. Today, #TeamScorpion is going purple in honor of #…
    Tweet 166: Get ready to go on an unexpected, magical adventure in the animated special Michael Jackson's Halloween on Friday,… https://t.co/CQxmLmDvTy
    Tweet 167: An advantage changed the course of last night's tribal council. Watch the latest episode of #Survivor now:… https://t.co/zNBz4t39i6
    Tweet 168: RT @swatcbs: #SWAT is proud to wear purple &amp; stand together against bullying on #SpiritDay! https://t.co/ch5h6DHLLE
    Tweet 169: RT @LifeInPiecesCBS: Laughter is coming your way! #LifeInPieces returns in TWO WEEKS! https://t.co/kvHTQA3Vlk
    Tweet 170: RT @MomCBS: Do a little dance... #Mom returns in TWO WEEKS! https://t.co/qshl2F8ChX
    Tweet 171: .@MacgyverCBS's George Eads shares why you'll be moved by the ending of the new special Michael Jackson's Halloween… https://t.co/MDpRaWKGUI
    Tweet 172: RT @walliscw: Today is @glaad #SpiritDay, a day reminding us that EVERY day is a good day to speak out against LGBTQ bullying. @MadamSecret…
    Tweet 173: RT @marythechief: Thnx 2 my beautiful friend &amp; advocate @wcruz73 I just took @glaad ‘s #SpiritDay pledge against bullying! Join me at https…
    Tweet 174: RT @wcruz73: It’s #SpiritDay! Show your support for LGBTQ youth today by standing against bullying. @glaad @glsenofficial ✊🏽❤️🏳️‍🌈 https://…
    Tweet 175: RT @MomCBS: No one should be bullied or called names simply for being who they are. #SpiritDay #Mom https://t.co/3xuyKIXpPS
    Tweet 176: RT @CodeBlackCBS: No one should be bullied or called names simply for being who they are. #SpiritDay #CodeBlack https://t.co/JuAQvXFaVa
    Tweet 177: RT @PriceIsRight: No one should be bullied or called names simply for who they are. #SpiritDay https://t.co/P1X3VUveOL
    Tweet 178: RT @9JKLCBS: No one should be bullied or called names simply for being who they are. Today, the cast of #9JKL is wearing purple for #Spirit…
    Tweet 179: RT @SalvationCBS: #Salvation is renewed for Season 2! Congrats to the cast and crew. More thrills coming Summer 2018. ☄️#SalvationCBS https…
    Tweet 180: RT @SuperiorDonuts: What's life without a few sprinkles and a lot of love? 🍩 #SuperiorDonuts Season 2 premieres on Mon, Oct 30 at 9:30/8:30…
    Tweet 181: Check out some of the hottest hook ups in #Survivor history before tonight's all-new episode:… https://t.co/qpM4bcJZj1
    Tweet 182: RT @ManWithAPlan: The cast of #ManWithAPlan is on set and gearing up for Season 2! See what they've been up to: https://t.co/j6J2tUCIlj htt…
    Tweet 183: It was a wedding to remember on last night's #KevinCanWait. Catch up now: https://t.co/gbLTSN8UEa https://t.co/Ex0bFLgXGT
    Tweet 184: RT @CrimMinds_CBS: 17 quotes that made us fall in love with Dr. Spencer Reid: https://t.co/HveiMl7u3T #CriminalMinds #Throwback https://t.c…
    Tweet 185: RT @bigbangtheory: Let the bonding begin! Don't miss a new #BigBangTheory tonight at 8/7c on CBS and CBS All Access: https://t.co/w2qdwJRrq…
    Tweet 186: Deeks and Kensi talk about their desire to have kids on the latest #NCISLA. Catch up now: https://t.co/sY7OJD11rX https://t.co/Bhy2V5p1za
    Tweet 187: RT @startrekcbs: Choose your pain. Episode 5 of #StarTrekDiscovery is now streaming on CBS All Access: https://t.co/1pZIWRqZ3n https://t.co…
    Tweet 188: Get ready for football! Stream NFL on CBS today w/ #CBSAllAccess. Try 1 week FREE: https://t.co/2KiDxyfBfU (Not ava… https://t.co/6o85UJvyLf
    Tweet 189: Stream the #10 Auburn Tigers @ LSU Tigers LIVE today at 3:30PM ET! Try #CBSAllAccess FREE: https://t.co/FKBoknACdr https://t.co/gM5DQCN2GL
    Tweet 190: RT @NCIS_CBS: Spend your weekend with the #NCIS team. Stream the latest full episode: https://t.co/fQ3ymaBKP8 https://t.co/LJTmTOhUvB
    Tweet 191: RT @SEALTeamCBS: Congrats to the cast &amp; crew of #SEALTeam for receiving a full season order! 🙌 Wheels up! https://t.co/iYemHdb6Dh 🇺🇸 https:…
    Tweet 192: RT @NCISLA: Have you seen the latest #NCISLA? Stream it now: https://t.co/nsjhRcwy84 https://t.co/FMQ4UqLgdm
    Tweet 193: Stream the Philadelphia Eagles @ Carolina Panthers LIVE tonight at 8:25PM ET! Try #CBSAllAccess FREE:… https://t.co/vIaCChwfCv
    Tweet 194: Broadway's Biggest Night returns to CBS! The 72nd Annual Tony® Awards will air live on June 10, 2018:… https://t.co/9xNYSzea6a
    Tweet 195: RT @survivorcbs: Tonight's #Survivor will leave you speechless. Don't miss an all-new episode tonight @ 8/7c on CBS &amp; CBS All Access: https…
    Tweet 196: Josh was on a mission to have his first one-night stand on the latest episode of #9JKL. Catch up now:… https://t.co/ugKUMJRjbz
    Tweet 197: Celebrate 59 years of music memories at 'GRAMMYS® Greatest Stories: A 60th Anniversary Special' Fri, Nov. 24 on CBS… https://t.co/3oYzJq9UH0
    Tweet 198: RT @9JKLCBS: The cast is ready! Join them as they live tweet tonight’s all-new episode. https://t.co/Gu3Whd4Zwz
    Tweet 199: RT @MadamSecretary: Elizabeth is caught in the middle of a "fake news" story on the season premiere of #MadamSecretary. Stream it now: http…
    Tweet 200: RT @startrekcbs: Prepare to jump. Episode 4 of #StarTrekDiscovery is now streaming on CBS All Access: https://t.co/4H3FcqrGAi https://t.co/…
    Tweet 201: .@FLOTUS responds to Sutherland Springs shooting. https://t.co/8NQi3CZUUi https://t.co/zcc4CR534G
    Tweet 202: .@JohnCornyn responds to Sutherland Springs shooting. https://t.co/8NQi3CZUUi https://t.co/x6CQpBxHL2
    Tweet 203: Chelsea Handler Blames Republicans for Texas Massacre
    https://t.co/igmwGSQMMx
    Tweet 204: Texas Shooting Witness: We Have to Overcome Evil With Good
    
    https://t.co/aqM4cheMPk
    Tweet 205: .@DanPatrick's message in the wake of the horrific mass shooting at First Baptist Church in Sutherland Springs.… https://t.co/RkjnhftROL
    Tweet 206: .@JustinTrudeau responds to Sutherland Springs church shooting. https://t.co/8NQi3CZUUi https://t.co/Qt9ig7PRrN
    Tweet 207: Right Now: Awaiting news conference on #SutherlandSpringsShooting - For full coverage tune in to Fox News Channel.… https://t.co/K5OqYhucrF
    Tweet 208: .@BernieSanders responds to Sutherland Springs church shooting. https://t.co/8NQi3CZUUi https://t.co/zNxHqLy9Ze
    Tweet 209: .@DanPatrick: "As Christians, we stand firm on a day like today in our faith. We will not be shaken in our faith fo… https://t.co/cNzb6tBMrN
    Tweet 210: Up to 27 killed in mass shooting at Texas church https://t.co/EmySBP97Nu
    Tweet 211: .@DanPatrick: "We do not stand down when we are attacked. We stand up for the God that we love."… https://t.co/pViBpHfHEO
    Tweet 212: .@DanPatrick: "We get through these times as believers... Faith is what gets all of us through this."… https://t.co/25S3ytG9Uy
    Tweet 213: Right Now: Awaiting news conference on #SutherlandSpringsShooting - For full coverage tune in to Fox News Channel.… https://t.co/alxXxqYNHF
    Tweet 214: Pastor's 14-Year-Old Daughter Killed in #SutherlandSprings Texas Church Shooting
    https://t.co/bwLRFPOrO2
    Tweet 215: .@SenFranken responds to Sutherland Springs shooting. https://t.co/8NQi3CZUUi https://t.co/O49xnzNmLp
    Tweet 216: Texas church massacre among the deadliest US mass shootings https://t.co/igESUcx5Hp
    Tweet 217: Sutherland Springs Witness: "We just did what we do - we prayed." https://t.co/oxEOUofTV3 https://t.co/c6lJaE4udI
    Tweet 218: .@_SBTC Exec Dir Richards: "This will not stop the Gospel of Christ. This will not stop the godly people who seek t… https://t.co/EeM4jchLLL
    Tweet 219: .@RepCuellar: Pregnant woman among those killed in #SutherlandSpringsShooting. https://t.co/YAre0fZfhd https://t.co/cDegbAtkOu
    Tweet 220: Right Now: Awaiting news conference on #SutherlandSpringsShooting - For full coverage tune in to Fox News Channel.… https://t.co/QUwuTofD4d
    Tweet 221: .@RepTimRyan responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/QNPIDZcZLF
    Tweet 222: .@SpeakerRyan responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/YfR4GlsGpy
    Tweet 223: .@KenPaxtonTX: "There may be up to 25, 27 people killed, and many more injured." #SutherlandSprings… https://t.co/JL8zMZe8Ea
    Tweet 224: .@IvankaTrump responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/82wVYmZPW3
    Tweet 225: At least 20 feared dead in mass shooting at #SutherlandSpringsTexas church
    https://t.co/EmySBP97Nu
    Tweet 226: .@JohnCornyn responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/IaHwUbgznc
    Tweet 227: Pastor's 14-Year-Old Daughter Killed in Texas Church Shooting
    https://t.co/bwLRFPOrO2
    Tweet 228: .@KenPaxtonTX: "Everyone in the community is going to know someone... Who expects this on a Sunday morning in a chu… https://t.co/JcACGGIBwL
    Tweet 229: .@KenPaxtonTX: May take days or weeks to figure out gunman's motive, if ever. #SutherlandSpringsTexas https://t.co/QfHPjGO7Of
    Tweet 230: .@nancypelosi responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/k3vOSC7Ncl
    Tweet 231: .@KenPaxtonTX: "There may be up to 25, 27 people killed, and many more injured." #SutherlandSpringsTexas https://t.co/X9FawGfAt4
    Tweet 232: Moments ago, @GregAbbott_TX tweeted that he was heading to #SutherlandSprings. https://t.co/YAre0fZfhd https://t.co/Fg7wQXGzQO
    Tweet 233: .@FLOTUS responds to Sutherland Springs shooting. https://t.co/8NQi3DhvLQ https://t.co/jCFRLxCQOO
    Tweet 234: .@ArthelNeville: Daughter of Pastor Frank Pomeroy of First Baptist Church in Sutherland Springs, Texas, killed in h… https://t.co/yHOn2dUXqw
    Tweet 235: Sutherland Springs, Texas, church shooting the deadliest church shooting in almost 20 years. https://t.co/YAre0fHDSD https://t.co/U8FKkOe3e6
    Tweet 236: .@tedcruz responds to Sutherland Springs shooting. https://t.co/8NQi3CZUUi https://t.co/AEsAaiBIau
    Tweet 237: .@_SBTC Exec Dir Richards: "This will not stop the Gospel of Christ. This will not stop the godly people who seek t… https://t.co/qZ3vbCISNb
    Tweet 238: Texas Shooting Witness: We Have to Overcome Evil With Good https://t.co/oxEOUofTV3 https://t.co/sDXgGS5jDI
    Tweet 239: Moments ago, @FLOTUS tweeted about the Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/DL7H0v8R2T
    Tweet 240: Police: 20-24 people killed in church shooting in Sutherland Springs, Texas. https://t.co/YAre0fHDSD https://t.co/uPo2JiyN3I
    Tweet 241: At least 20 feared dead in mass shooting at Texas church https://t.co/YAre0fHDSD https://t.co/iNTUnjN0XV
    Tweet 242: Police: 20-24 people killed in church shooting in Sutherland Springs, Texas. https://t.co/YAre0fZfhd https://t.co/Pw7gpKHRfH
    Tweet 243: At least 20 feared dead in ‘mass shooting’ at Texas church https://t.co/YAre0fHDSD https://t.co/LP83xPnv1Y
    Tweet 244: .@IvankaTrump on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/UIgT5kT3B3
    Tweet 245: .@JohnCornyn on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/I0sa8eph0O
    Tweet 246: .@tedcruz on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/JKpKZw4zF4
    Tweet 247: At least 20 feared dead in ‘mass shooting’ at Texas church https://t.co/YAre0fHDSD https://t.co/EZUwuPsZgR
    Tweet 248: Texas church shooting: Trump, politicians react https://t.co/l44UHGruL0 #FOXNewsUS https://t.co/aeBoja1k1t
    Tweet 249: Moments ago, @nikkihaley tweeted about the Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/KiJxV46wYb
    Tweet 250: .@GregAbbott_TX's statement on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/GxbPqh15Qk
    Tweet 251: Moments ago, @VP Mike Pence tweeted about the church shooting in Sutherland Springs, Texas. https://t.co/YAre0fZfhd https://t.co/x0bokTHkiX
    Tweet 252: Moments ago, President @realDonaldTrump tweeted about the church shooting in Sutherland Springs, Texas.… https://t.co/awDwNW1pGp
    Tweet 253: Sutherland Springs Witness: "The Bible tells us that we overcome evil with good." https://t.co/YAre0fHDSD https://t.co/GQ5zgGiUiU
    Tweet 254: .@realDonaldTrump on church shooting in Sutherland Springs, Texas. https://t.co/YAre0fZfhd https://t.co/dlwtYJzPiy
    Tweet 255: Report: Man who opened fire on #Texas church now dead. #SutherlandSprings https://t.co/YAre0fHDSD https://t.co/oyDeu3zspF
    Tweet 256: .@BryanLlenas: Sutherland Springs a very small community, church has about 50 members. https://t.co/YAre0fHDSD https://t.co/zRaQ0ee5Zl
    Tweet 257: .@TXAG Ken Paxton on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/3LruH4YFhY
    Tweet 258: .@GregAbbott_TX on Sutherland Springs, Texas shooting. https://t.co/YAre0fZfhd https://t.co/ajsyfTbveK
    Tweet 259: Multiple casualty situation after man opens fire at Sutherland Springs, Texas church - Fox News has live coverage.… https://t.co/1qQhcBdQAJ
    Tweet 260: .@EricShawnTV: Reports: 2 year-old and other children among those shot, multiple deaths. #SutherlandSprings https://t.co/orVVpoOaWc
    Tweet 261: Multiple casualty situation after man opens fire at Sutherland Springs, Texas church. https://t.co/YAre0fHDSD https://t.co/oqFEXLld3S
    Tweet 262: DEVELOPING: Several people reportedly shot &amp; killed in “mass shooting” at Texas church. For continuing live coverag… https://t.co/NjxwXS2JG3
    Tweet 263: First responders on scene of church shooting in Sutherland Springs, Texas; man who opened fire reportedly dead.… https://t.co/7xvicaqju3
    Tweet 264: 'Mass shooting' reported at Sutherland Springs church in Texas
     https://t.co/YAre0fZfhd
    Tweet 265: BREAKING NEWS: Active shooter at Texas Baptist Church, several people shot. https://t.co/sqlN3HUGHl
    Tweet 266: Shalane Flanagan becomes first American woman to win NYC Marathon in 40 years https://t.co/fhHAfaqGAL https://t.co/5IU8n4VByi
    Tweet 267: On @ffweekend, @GovMikeHuckabee reflected on @POTUS's foreign policy as he travels abroad in Asia. https://t.co/QKbTTtl4Cy
    Tweet 268: Iowa mom, 18, charged after 2-year-old twins found naked outside near highway
     https://t.co/YUmB5iMWPs
    Tweet 269: Refugee Admittance to U.S. Down 87 Percent
    https://t.co/x3h7Ec7GpG
    Tweet 270: RT @EricShawnTV: What will @POTUS @realDonaldTrump tell #China? Here's @AmbJohnBolton @FoxNews Watch https://t.co/Qfu8OjYNpj I anchor 4pm E…
    Tweet 271: Happy 40th Anniversary to George W. Bush and Laura W. Bush, who got married on this date back in 1977! https://t.co/MtQ2PyRCHo
    Tweet 272: On @ffweekend, @SheriffClarke reflected on the loss of Illinois Police Officer Jaimie Cox. https://t.co/ibHcKBfzt3 https://t.co/MBgWfkvO7O
    Tweet 273: Speaker Ryan says Clinton, DNC money deal 'takes the cake'
      https://t.co/b12ZG9oIrl
    Tweet 274: .@TomiLahren: "If Bernie has any grit at all, he will tear the @DNC a new one." https://t.co/PfMOprxM2q https://t.co/ZudywtUiJ4
    Tweet 275: Staff Sgt. Alonzo Lunsford: "I think the political correctness is prohibiting us from making progress." https://t.co/6nsKzefpfa
    Tweet 276: BREAKING NEWS: @ShalaneFlanagan becomes first American woman since 1977 to win NYC Marathon. https://t.co/vaa9Mf78M9 https://t.co/EgikoATW9O
    Tweet 277: RT @FoxBusiness: Cowboys owner Jerry Jones rips Goodell's handling of Elliott suspension https://t.co/j098VTMHVP
    Tweet 278: BREAKING NEWS: @ShalaneFlanagan becomes first American woman since 1977 to win NYC Marathon. https://t.co/TJU9oZVxVx
    Tweet 279: On @ffweekend, @David_Bossie responded to news that neither of the Presidents Bush voted for @POTUS. https://t.co/MJOJzdq6TE
    Tweet 280: .@GovMikeHuckabee: "@TheDemocrats moved past Clinton. The Republicans have moved on past the Bush family." https://t.co/6oC1vQ6tBc
    Tweet 281: .@David_Bossie: "The broken status quo is what the Bushes ran." https://t.co/vtZFBEPr0p
    Tweet 282: .@jasoninthehouse: "I think the whole country was really questioning @HillaryClinton's health." https://t.co/aAH9jAtIm2
    Tweet 283: On @WattersWorld, @AnnCoulter slammed the Diversity Visa Lottery program. https://t.co/rSKyjlYOxF https://t.co/NCeh3b5Hkx
    Tweet 284: .@timclemente: "Antifa as a group is literally the definition of terrorism." https://t.co/y0avmjYEyb
    Tweet 285: .@SheriffClarke: "[Antifa] is a hate group and most of America does not side with them." https://t.co/RmfuRsM3H9
    Tweet 286: .@CLewandowski_: "It sounds like [Presidents W &amp; HW Bush] wanted @HillaryClinton to be in office to keep things the… https://t.co/FkkODnVsrt
    Tweet 287: Speaker Ryan says Clinton, DNC money deal 'takes the cake' https://t.co/C1caypRkDC
    Tweet 288: .@AnnCoulter: "Every single part of our immigration laws is insane." https://t.co/rSKyjmgppd https://t.co/9cyu2mKSQk
    Tweet 289: .@carolmswain: "We see attacks on Christianity from the @splcenter." https://t.co/jSJ34JM6Qj https://t.co/hvqcaA4tZT
    Tweet 290: It was one year ago this week since @realDonaldTrump was elected President - and on @SundayFutures, @VP reflected o… https://t.co/p15zdU8Wjf
    Tweet 291: Dr. Rebecca Grant: "Every word in that pledge is universal." https://t.co/MIXrr9yc28
    Tweet 292: #VAGov Poll: @EdWGillespie now leads @RalphNortham 40.4% to 37.4%. https://t.co/pS7RwY2zUo
    Tweet 293: Marie Harf: "I'd like for us to fairly judge the Trump Administration without always going back to what… https://t.co/xEYkYW2DU1
    Tweet 294: Refugee admissions down 87%, percent of Muslim refugees declines from 45% to 23%. https://t.co/9SgK0pVBot
    Tweet 295: .@SteveScalise: "I'm recovering. Still got a lot of rehab to go to be able to walk again on my own, but I can walk… https://t.co/3BVYoF8WcO
    Tweet 296: .@carolmswain responds to professor's op-ed slamming Pledge of Allegiance as "an instrument of white nationalism."… https://t.co/p11ghB6m5M
    Tweet 297: .@MZHemingway: "Here you have the former DNC chair accusing the former Democratic nominee of some really serious sh… https://t.co/oIPmyoU6ry
    Tweet 298: .@edhenry: "They have re-litigated, @TheDemocrats, this election for basically 12 months now." #MediaBuzz https://t.co/JDldKadTPG
    Tweet 299: Man used ice cream truck to lure, sexually assault children in North Carolina, police say https://t.co/UwiRoAmOnl
    Tweet 300: .@VP: "[@POTUS] won 30 of 50 states."
    
    WATCH: @MariaBartiromo's full interview w/ @VP - Part 4. https://t.co/d79B5eHYwb
    Tweet 301: Disney scored big with Marvel’s "Thor: Ragnarok,” which took in more than $400 million globally over the weekend https://t.co/A8p7rnVTdj
    Tweet 302: A Word With: Laurence Fishburne on the Role That Made Him Cry https://t.co/QnysIAl6jA
    Tweet 303: An army of on-the-ground operatives push the government’s policies, help purvey its propaganda and act as lookouts https://t.co/tRWBOkSPjd
    Tweet 304: A pregnant woman and children were said to be among the dead https://t.co/UyzS0yzyql
    Tweet 305: Being defined by her profession and not merely by her gender remains a work in progress https://t.co/vq87gh8LaS
    Tweet 306: Before Teen Vogue got "woke," it was an incubator for people we now call influencers https://t.co/lHUveiOglv
    Tweet 307: An NYT reader's reaction to an American woman winning the New York City Marathon for the first time in 40 years… https://t.co/7orzqiC2bK
    Tweet 308: A gunman walked into a small Baptist church in rural Texas on Sunday and opened fire, killing at least 25 people https://t.co/AfZei630bd
    Tweet 309: Google and others are looking for automated ways to deal with a shortage of artificial intelligence experts https://t.co/Ftf0bP3p3l
    Tweet 310: A few weeks after being banned in London, Uber is waging a new high-stakes regulatory fight in Brazil https://t.co/X7XyzcGrz3
    Tweet 311: Videos of the church show at least 30 people, including many children, attending Sunday service in recent weeks https://t.co/z2JQTdkVEM
    Tweet 312: The move appeared to be the most sweeping shift in governance Saudi Arabia has experienced for more than 8 decades https://t.co/Ampn9lvcLG
    Tweet 313: Documents reveal how multinational companies avoid taxes and how the superrich hide their wealth https://t.co/cCIHZV7GxY
    Tweet 314: Part of the agenda of “Uncommon Sense" is to illustrate just how broad and multicolored the autism spectrum is https://t.co/mDzqRIOAom
    Tweet 315: Carson Wentz and the Philadelphia Eagles absolutely toyed with the Denver Broncos https://t.co/xawW4nUuGl
    Tweet 316: Conan O’Brien may be taking more artistic risks than any other late-night host https://t.co/4shU1bgOCo
    Tweet 317: RT @arappeport: I.R.S. commissioner, demonized by conservatives, leaves on his terms w/ no apologies. “Survival is its own reward.” https:/…
    Tweet 318: Democrats argue that the wave of retirements will help them retake the House https://t.co/IzVkertrVt
    Tweet 319: He kept crime rates low in his first term. Now, Mayor de Blasio has a plan to make police officers nicer. https://t.co/9W1fI7EGcw
    Tweet 320: We used VR to explore what music feels like to a deaf person https://t.co/ApNIF1loo1
    Tweet 321: More than 20 people were killed after a gunman walked into a church in a rural town 30 miles east of San Antonio https://t.co/eL5QUzCWv6
    Tweet 322: When behavior goes unseen or ignored by employers, “whisper networks” can provide women with vital support systems https://t.co/4V2qikUqdq
    Tweet 323: “There’s a public perception... that Canada is a steward of the environment, but in fact the opposite is true” https://t.co/DGu2q2v0uc
    Tweet 324: Breaking News: Several people were killed, including the gunman, in a shooting at a church near San Antonio https://t.co/FXvUKLFCZh
    Tweet 325: In books like “My Secret Garden: Women’s Sexual Fantasies,” Nancy Friday helped establish “a confessional feminism” https://t.co/0Jo4hBnt22
    Tweet 326: Opinion: By fretting about food, we turn occasions for comfort and joy into sources of fear and anxiety https://t.co/E1xfBbPsoz
    Tweet 327: Many parennials give their children YouTube channels from the first sonogram and hashtags when they’re born https://t.co/SfIeFdaJkI
    Tweet 328: Michael Urie's first reaction to taking over Harvey Fierstein's part in "Torch Song"? "It was way too scary." https://t.co/5iEkuJIL3b
    Tweet 329: Behind Yuri Milner's investments in Facebook and Twitter were hundreds of millions of dollars from the Kremlin https://t.co/1nVIa0y2zf
    Tweet 330: @jeffbercovici We sent a sports alert for Shalane Flanagan's victory: https://t.co/zae1UjlCfH. Kamworor's win also received a sports alert.
    Tweet 331: Even the columnist’s daughter criticized his description of the press secretary as a “slightly chunky soccer mom” https://t.co/IDmfVEC1tJ
    Tweet 332: Commerce Secretary Wilbur Ross has profited handsomely from a shipping company with business ties to Putin’s family https://t.co/DkZO3TdANj
    Tweet 333: With tears and maybe a few colorful words, Flanagan won the race with a time of 2 hours 26 minutes 53 seconds… https://t.co/0LhSE1xlcO
    Tweet 334: “No one — no dictator, no regime and no nation — should underestimate, ever, American resolve,” Trump said https://t.co/NwU7mi9SWb
    Tweet 335: Spanish authorities are seeking to prosecute 20 politicians on rebellion for declaring Catalonia’s independence https://t.co/ynd3olMZZc
    Tweet 336: Here are the top story lines for NFL Week 9 https://t.co/IjblFapJPY
    Tweet 337: Geoffrey Kamworor of Kenya, a two-time world champion in the half-marathon, won the men’s race https://t.co/25dHU1O74x
    Tweet 338: Why was Larry David making jokes about trying to pick up women at a concentration camp? https://t.co/9hp5blyqf2
    Tweet 339: Shalane Flanagan won the New York City Marathon, the first American woman to finish first since 1977 https://t.co/Ge88TTiRRh
    Tweet 340: The 6 crew members living in isolation for a NASA-funded study exit their habitat in Hawaii after 8 months… https://t.co/SZ5TUVfAKE
    Tweet 341: Opinion: Everyone lies to the tax man, knowingly or unknowingly https://t.co/NI9jte1r0n https://t.co/5YOOU6oH0c
    Tweet 342: An act of defiance and audacity that helped propel the long, slow march to women’s suffrage https://t.co/BcDhDMU1Ur
    Tweet 343: A Catholic deacon who ran a transitional home for men with a history of addiction or crime was stabbed to death https://t.co/XiIjOU4UJw
    Tweet 344: RT @nytopinion: Will the G.O.P. try to challenge Trump in 2020? His unpopularity is stark, but not among his party’s voters. 
    https://t.co/…
    Tweet 345: Should Americans switch to year-round Daylight Saving Time? https://t.co/2truGkvPLo (This story from March is rather timely today.)
    Tweet 346: Aaaaand they’re off https://t.co/a6WDwWi4Uh
    Tweet 347: His is a family of doers in the face of adversity, whether a marathon or political oppression https://t.co/Jd4WQsTN8R
    Tweet 348: Britain now stands as one of the world’s weakest major economies, even as the world enjoys relatively robust growth https://t.co/uRtlH5ygaM
    Tweet 349: RT @dougmillsnyt: .@realDonaldTrump waves from the golf cart as @AbeShinzo drives them to the clubhouse in Tokyo Japan. #POTUSinAsia https:…
    Tweet 350: Malliotakis as Manager: Lessons From Hurricane Sandy and Albany https://t.co/TXl978tjao
    Tweet 351: Ex-Leader of Catalonia Turns Himself In to Police in Brussels https://t.co/iwAG5wzajD
    Tweet 352: 🏅 https://t.co/1Uo2dIlkKC
    Tweet 353: RT @NYTSports: The marathon great Meb Keflezighi is retiring by running the New York City Marathon on Sunday. What will you do? https://t.c…
    Tweet 354: The White House had no immediate comment on whether Trump’s call should be interpreted as an endorsement of arrests https://t.co/NQ4q09r4hH
    Tweet 355: Among Prince Alwaleed’s crown jewels: sizable stakes in Twitter, Lyft, Citigroup and 21st Century Fox https://t.co/IreBfYVeqP
    Tweet 356: Saudi Arabia’s sweeping campaign of arrests included Prince Alwaleed bin Talal, one of the world’s richest men https://t.co/EpWCYe8tky
    Tweet 357: It's the stuff of liberal fantasies: a vast, defiant territory governed by Democrats resisting Trump at every turn https://t.co/1YbErsvnr2
    Tweet 358: Life on Mars: Return to Earth https://t.co/O4xTfSV87h
    Tweet 359: Upshot/Siena Poll Gives Democrat Narrow Lead in Virginia Governor’s Race https://t.co/Ko32pgfnjf
    Tweet 360: Who gets to go on a major presidential trip? It's an exercise in internal politics. https://t.co/kyeg52T5U8
    Tweet 361: In 1972, NYC marathon organizer Fred Lebow contacted The Times. Be at the start, he said. You won't want to miss it… https://t.co/ux8tmN1nAq
    Tweet 362: Detroit is still trying to recover after the 2008 financial crisis and the 2013 bankruptcy gutted its housing market https://t.co/zkip3W6RpG
    Tweet 363: Exposures: Puerto Rico in the Dark https://t.co/NQjNp6sEbN
    Tweet 364: Tucked away in the GOP tax plan are several provisions meant to get conservative lawmakers to vote for it https://t.co/JhwFcvUnQO
    Tweet 365: More Anxiety, and More Police, Expected at New York City Marathon https://t.co/6fDeAbbarg
    Tweet 366: Joe Lockhart was in the crossfire during the Clinton impeachment. Now he's defending NFL players kneeling. https://t.co/0pvoi3r2cO
    Tweet 367: Field Notes: The Bridal Shop Just Closed. How to Rescue the Day. https://t.co/14hs5vDWmc
    Tweet 368: Youtube contains dark corners as videos that are disturbing for children slip past its filters https://t.co/C94P59X5wV
    Tweet 369: Modern Love: Recognizing What They Had, 20 Years Too Late https://t.co/v1K37ABIvw
    Tweet 370: Global Health: Deadly Plague Outbreak in Madagascar Appears to Wane https://t.co/E40FVRku1n
    Tweet 371: The 2018 Michelin Guide New York City has been released https://t.co/sN9Sv5HmCF
    Tweet 372: The week's 10 most notable new songs, including Bruce Springsteen and Rihanna https://t.co/SgbiIf7UEu
    Tweet 373: These musicians are forced to perform for high-caste Hindus. But the killing of one of their own was the last straw. https://t.co/yIm1nXUJFq
    Tweet 374: Designers have finally figured out how to dress Olympic athletes without looking like they're trying too hard https://t.co/TVfFSWB4xp
    Tweet 375: How Facebook's algorithm determines the fate of start-ups https://t.co/8kTuBBKeEH
    Tweet 376: Tens of thousands of people in Togo are demanding the nation's president resign, whose family has ruled for 50 years https://t.co/CbqY1GCLKv
    Tweet 377: ‘Saturday Night Live’: Alec Baldwin and Larry David Contribute to an Awkward Episode https://t.co/pok8aizcN8
    Tweet 378: Japanese art is more than just cliché zen gardens and cutesy Hello Kitty https://t.co/kKL3U9MxzI
    Tweet 379: The diversity visa lottery, explained https://t.co/XohR0x5V0g
    Tweet 380: Where the STEM jobs are (and where they aren't) https://t.co/byInsbrpPL https://t.co/B2BeBLnSLn
    Tweet 381: In 1979, Bob Dylan announced his embrace of Christianity. That period gets a second look on "Trouble No More." https://t.co/IjETz7sgm8
    Tweet 382: "It didn't matter there was an ocean between them and different continents, they both love fiercely" https://t.co/dlom5MXVnk
    Tweet 383: “Alias Grace” is a story about storytelling and Sarah Gadon is mesmerizing as the star, writes @poniewozik https://t.co/wOCe89dxgh
    Tweet 384: At a nightclub in Liberia, we found a stylish music scene unencumbered by the country’s past https://t.co/ry9cuWgDc2 https://t.co/4FsJ4gRn1x
    Tweet 385: What did Bernie Sanders learn about Canada's health system? Doctors like free health care as much as patients do. https://t.co/zPds0lBn6V
    Tweet 386: Wine usually takes the spotlight at Thanksgiving dinner, but beers are just as good of a complement https://t.co/WdUILym2jj
    Tweet 387: Op-Ed Contributor: How ISIS helped peace in the Philippines’s Muslim south https://t.co/ICpCuDLNax
    Tweet 388: Let the dancing begin💃🕺 https://t.co/cKAXP2Z7WO
    Tweet 389: Citigroup, 21st Century Fox, Twitter: Prince’s Arrest Touches Many https://t.co/UOsfKysdE9
    Tweet 390: Trump Arrives in Asia With Focus on Trade and North Korea https://t.co/FNmWwvYxG1
    Tweet 391: Opinion: Why the world loves New York https://t.co/bDtPbZVzFi
    Tweet 392: RT @Julseas: Thanksgiving: So many of us celebrate it, yet it’s so different for us all. Tell us your holiday story: https://t.co/3hSZd4j8G6
    Tweet 393: A 14-year-old model died while on an assignment in China. Investigators are looking into whether neglect caused it. https://t.co/TEPJe5spCy
    Tweet 394: While you can’t control your age, you can slow the decline of aging with smart choices along the way https://t.co/jhwxXfQQPg
    Tweet 395: What do colleges want in an applicant? Everything. https://t.co/eixg3GOhBb
    Tweet 396: Opinion: And then they came for Robert Mueller https://t.co/H3WRjwTKse
    Tweet 397: 2 months after Harvey, Houston still suffers from a kind of PTSD. I see it in myself and I see it in others. https://t.co/pliiN1QwVs
    Tweet 398: A pizza for fall https://t.co/R4w3jIWsrH
    Tweet 399: 5 Pieces of Inspiration, and Tips, for Travel in Turbulent Times https://t.co/Tly7P11vTX
    Tweet 400: What colleges want in an applicant (everything)
    https://t.co/pHvvgro1Yo
    Tweet 401: Suicide bombers target mosque in Kirkuk, Iraq https://t.co/76y0E66C1J https://t.co/9EEzdWbYus
    Tweet 402: The wife of First Baptist Church Pastor Frank Pomeroy says their teen daughter was killed in Texas church shooting… https://t.co/wLEuUNeEM2
    Tweet 403: British minister Damian Green denies computer pornography allegations https://t.co/cYV8znt9SG https://t.co/Iet4mk5JUE
    Tweet 404: Paul Manafort has 3 US passports and traveled to Mexico, China and Ecuador with a phone registered under a fake name https://t.co/rtthkDJ6Bk
    Tweet 405: A gunman opened fire at First Baptist Church in Sutherland Springs, Texas, killing at least 20 people… https://t.co/Oox2vRZQfI
    Tweet 406: President Trump's approval rating hits historic low, according to Washington Post-ABC poll https://t.co/6qkh8fqW20 https://t.co/jZlFVAHSYX
    Tweet 407: Reporter Ronan Farrow talks about the 'Weinstein effect' with @brianstelter on @ReliableSources… https://t.co/t6awLTF2mY
    Tweet 408: A Utah nurse who was arrested for protecting her patient gets a $500,000 settlement https://t.co/4tsJk1FxiZ https://t.co/aGnzFMdqj3
    Tweet 409: At least 20 people killed in a church shooting in Sutherland Springs, Texas, according to the Wilson County sheriff… https://t.co/tEnLYavRA5
    Tweet 410: University Hospital in San Antonio is treating 8 patients from the Sutherland Springs church shooting, says hospita… https://t.co/4LG8ZXgbhx
    Tweet 411: Texas Gov. Greg Abbot releases a statement on the shooting at First Baptist Church in Sutherland Springs… https://t.co/TiwNGu2Pht
    Tweet 412: Sutherland Springs business owner on church shooting: "It's just awful...there were emergency responders everywhere" https://t.co/TYcC5jCX9m
    Tweet 413: ISIS claims responsibility for a suicide attack in Yemen https://t.co/9ScXiQp7Sl https://t.co/cmAG9lNdTJ
    Tweet 414: Sutherland Springs resident on church shooting: "It's just awful...there were emergency responders everywhere" https://t.co/TYcC5jCX9m
    Tweet 415: Law enforcement have reported multiple victims at a Texas church, but have not said how many https://t.co/PGxqFieLyc https://t.co/pLNO4vE3sT
    Tweet 416: President Trump tweets support for people of Sutherland Springs, Texas, after church shooting… https://t.co/muJFcRBDWB
    Tweet 417: One suspect dead after reported shooting in Sutherland Springs, Texas, says Guadalupe Co. Sheriff's Office official… https://t.co/s8KvNZh8t6
    Tweet 418: Local gas station owner tells @KayleeHartung that shots fired at Texas church "sounded like a semiautomatic weapon" https://t.co/D0EChgJtJm
    Tweet 419: Catalan ex-President turns himself in to Belgian authorities https://t.co/vGBLL2A481 https://t.co/ghTN0dIGJw
    Tweet 420: House Minority Leader Nancy Pelosi: Must "exhaust" diplomatic options on North Korea
    https://t.co/LNsBvUknTQ https://t.co/gKzSAd35cb
    Tweet 421: We're live in Sutherland Springs, Texas, over the scene of a reported shooting https://t.co/49AyTQsslP… https://t.co/w8qiqXkRUA
    Tweet 422: Trump and Putin are set to meet and discuss North Korea https://t.co/h72BD4cUjd https://t.co/7yqxZK8vit
    Tweet 423: A witness at a gas station across from a Texas church said she heard 20 shots fired while a service was underway… https://t.co/vGZKfABodU
    Tweet 424: "Thor: Ragnarok" is the 17th straight number one opening for Marvel https://t.co/IZ3SPgUSnW https://t.co/XpkmIiQRXW
    Tweet 425: County Sheriff says Sutherland Springs church gunman is dead, reports CNN's @kayleehartung https://t.co/ekxguNHIsH https://t.co/ZtfHBLc4PQ
    Tweet 426: BREAKING: The FBI is responding to the scene of a shooting outside San Antonio, Texas
    https://t.co/ekxguNHIsH https://t.co/vRV1GzHgVx
    Tweet 427: Gonorrhea rates in Australia are up 63% in 5 years, data shows https://t.co/dsVnWfRKFk https://t.co/UtRgz5r04t
    Tweet 428: Billionaire Prince Alwaleed arrested in Saudi anti-corruption drive https://t.co/U6aJ7NPR7O https://t.co/pimIM00oeh
    Tweet 429: Shalane Flanagan wins NYC Marathon, becoming the first U.S. Women's champion in 40 years https://t.co/UivrO1JMUB https://t.co/i8yuNM6oY1
    Tweet 430: JUST IN: Witness says as many as 20 shots fired at a church in Sutherland Springs, Texas https://t.co/ZC919cZoUC
    Tweet 431: Sen. Dianne Feinstein urges diplomacy with North Korea: "The worst alternative is a war which could become nuclear" https://t.co/9YPIXKioLn
    Tweet 432: NYC marathon runners stay the course, despite last week's terror attack https://t.co/ORk5ykaZuV https://t.co/X6oYrUqJuX
    Tweet 433: A University of Miami art professor created Ku Klux Klan-style hoods out of American flags for a faculty art exhibi… https://t.co/jk5cNiIFSu
    Tweet 434: Double beds, swivel chairs. Here's a look at Singapore Airlines' new luxury suites https://t.co/JIvOIYU7zW https://t.co/MaRqdXRkEd
    Tweet 435: The most spectacular abandoned castles around the world https://t.co/DC14SubQJa via @cnntravel https://t.co/ExuBF2XKe8
    Tweet 436: H.W. Bush on Trump: “He’s a blowhard”
    
    George W. Bush on Trump “This guy doesn’t know what it means to be president… https://t.co/yp212uRBxT
    Tweet 437: AirlineRatings names "most excellent" airlines for 2018. For the 5th consecutive year, this carrier came out on top… https://t.co/coKs8J7Ciq
    Tweet 438: "Women are coming forward...telling the hardest stories of a lifetime," says @RonanFarrow, who wrote Weinstein story https://t.co/V6VhiZMg0R
    Tweet 439: .@brianstelter to Kellyanne Conway: "Viewers see your pivoting...when I say Russia, you say Clinton" https://t.co/lc5IdbzAP9
    Tweet 440: .@brianstelter to Kellyanne Conway: "We're not anti-Trump, Kellyanne. We're pro-truth." https://t.co/V6VhiZMg0R
    Tweet 441: Alec Baldwin's President Trump shared a shower with Paul Manafort on @nbcsnl last night https://t.co/uHcj6PRTqU https://t.co/TXxi7U9br2
    Tweet 442: What are your thoughts on polygamy? @lisaling meets open-minded couples looking for modern love on @CNNOriginals'… https://t.co/ovsONmqTzY
    Tweet 443: Saudi Arabia's newly formed anti-corruption committee has arrested at least 17 princes and top officials… https://t.co/OiiGRRGEY4
    Tweet 444: RT @CNNPolitics: Pelosi expresses disdain at the timetable for the GOP tax plan: "They're trying to move this in a matter of days" https://…
    Tweet 445: .@FareedZakaria: NY attack "an isolated incident by one troubled man that shouldn't lead to grand generalizations" https://t.co/4IR6y7eVL9
    Tweet 446: Sen. Dianne Feinstein urges diplomacy with North Korea: "The worst alternative is a war which could become nuclear" https://t.co/SehU6c2UZq
    Tweet 447: Feinstein on Sessions: "When he comes before the committee again, he has to be precise and it has to be accurate" https://t.co/kFiWDRA83w
    Tweet 448: Rep. Pelosi on tackling alleged sexual harassment in Congress: I'm "hopeful that we can do something very strong" https://t.co/p01ORHA3sY
    Tweet 449: Sen. Feinstein on AG Sessions' testimony about Russia: "I think he should come back and clarify it" #CNNSOTU https://t.co/gPiao3H9P1
    Tweet 450: Rep. Nancy Pelosi: Impeaching President Trump "is not someplace that I think we should go" #CNNSOTU https://t.co/3z5LYxTN5S
    Tweet 451: Pelosi on Brazile's allegations about Clinton and the DNC: "I would hope that there's another side to the story" https://t.co/QXp6xVCo9R
    Tweet 452: House Minority Leader Nancy Pelosi on the GOP tax plan: "This is really a gift to corporate America" #CNNSOTU https://t.co/MNygm9qM0v
    Tweet 453: House Minority Leader Nancy Pelosi: Revision of the tax code should be done in a bipartisan way #CNNSOTU https://t.co/vw8PFnGTme
    Tweet 454: House Minority Leader Pelosi: "I hope the President goes into the meeting (with Putin) really informed" https://t.co/JNBqP07Pd0 #CNNSOTU
    Tweet 455: Rep. Nancy Pelosi on North Korea: "We're poking a stick in the eye of a mad dog with some of what we're saying" https://t.co/hgvJ4yyxVL
    Tweet 456: The company that owns Corona is getting into the pot business https://t.co/HHg98jBXK7 https://t.co/eHvBjnDBic
    Tweet 457: Japanese Prime Minister Shinzo Abe gave President Trump a customized hat that read, "Make alliance even greater."… https://t.co/P73f5BrTjj
    Tweet 458: President Trump is in Japan, where he and Prime Minister Shinzo Abe are expected to talk about North Korea… https://t.co/LpmBAJUCuD
    Tweet 459: AirlineRatings names "most excellent" airlines for 2018. For the 5th consecutive year, this carrier came out on top… https://t.co/dJ16PRMPly
    Tweet 460: Long-term spaceflight "squeezes" the brain, study says https://t.co/c3D86kU0sa https://t.co/osRjvGip4G
    Tweet 461: The FDA is cracking down on claims that cannabis can cure cancer https://t.co/q1DeAGuPed https://t.co/UGTB8PNn6E
    Tweet 462: Back in 1991, Anita Hill forever changed the way we talk about sexual harassment https://t.co/til31lOEld https://t.co/yD4UsGNqA2
    Tweet 463: China will surpass the US as the world's largest air travel market in the next 5 years, according to IATA forecast… https://t.co/2Z3lWPEYcU
    Tweet 464: Court filings show Paul Manafort has three US passports. How many can you really own? Here's a closer look.… https://t.co/J8ZLwPWG4b
    Tweet 465: Taxes on cannabis could reach as high as 45% in parts of California, according to a report https://t.co/I7YHhQVyQB
    Tweet 466: 5 changes to Obamacare open enrollment for 2018 https://t.co/4YYAEeV7AY https://t.co/5EZ40NagUq
    Tweet 467: Syria was responsible for the sarin gas attack that killed more than 80 people earlier this year, a UN report finds… https://t.co/iNixmHKv3w
    Tweet 468: Tropical storms and swelling sea levels could flood NYC every five years between 2030 and 2045, a new study says… https://t.co/VgifeWmK27
    Tweet 469: The forgotten mothers and babies of Zika https://t.co/eMAtQMP2ch https://t.co/VvL589j04L
    Tweet 470: Death rates for heart disease, cancer and HIV are down in the US, but overdose death rate has risen, CDC says… https://t.co/theP2foXK8
    Tweet 471: Three surprising ways the Protestant Reformation shaped our world https://t.co/E1PkTWViEZ https://t.co/UqKvO48djs
    Tweet 472: Who's who in the Trump-Russia saga https://t.co/dgSZLFL6VV https://t.co/28OKDbT1Zz
    Tweet 473: The most spectacular abandoned castles around the world https://t.co/OxU6bpIrYP via @cnntravel https://t.co/jcPzlKPu9e
    Tweet 474: This Houston officer helped save hundreds of lives during Hurricane Harvey — while battling stage 4 colon cancer… https://t.co/jyuqfEouat
    Tweet 475: A new report concludes that an environmentalist's murder was part of a criminal plot that was months in the making https://t.co/1Tzc6wuXwz
    Tweet 476: Two Georgia teens, friends from childhood, died from lethal doses of fentanyl on the same day and half a mile apart… https://t.co/zbMZTOOZwP
    Tweet 477: A soldier deployed before he could finish painting his house. So these students jumped in to finish the job.… https://t.co/ezsh2PSzYz
    Tweet 478: A new study links pesticide residues in fruits and vegetables with women's fertility issues https://t.co/watgjAiuLD https://t.co/2KTTgXZYjT
    Tweet 479: Eleven princes arrested in Saudi Arabian anti-corruption sweep, Al-Arabiya reports. https://t.co/09rW8uGXwp
    Tweet 480: Couples are turning to a new kind of dating website to save their marriage. @lisaling learns what a “throuple” is a… https://t.co/VzaPKJQNh7
    Tweet 481: This Sports Illustrated cover from 2014 predicted the Astros' World Series win https://t.co/MU4SlGqFDk https://t.co/AJHKOQ7Jhj
    Tweet 482: US passports will identify convicted child sex offenders https://t.co/xELM7Jyspw https://t.co/2usMVZ3MEv
    Tweet 483: Beyoncé will be a part of Disney's upcoming live-action version of "The Lion King," playing the character of Nala… https://t.co/xTvf4GcxCT
    Tweet 484: President Trump touched down in Japan late Saturday ahead of a 13-day trek through Asia https://t.co/4M1t2Jp1KB
    Tweet 485: Double beds, swivel chairs. Here's a look at Singapore Airlines' new luxury suites https://t.co/0YjhV2c81O https://t.co/ulJKIq6Tus
    Tweet 486: Gender inequality actually worsened around the world in 2017, according to a report from the World Economic Forum… https://t.co/4wU497WQcO
    Tweet 487: Drone footage shows the devastation caused by Hurricane Maria in Puerto Rico's El Yunque National Rainforest… https://t.co/h2f3ceauZQ
    Tweet 488: Scientists have found evidence of a roughly 100-foot-long space hidden within the walls of the Great Pyramid of Giz… https://t.co/p3daFqOt7X
    Tweet 489: This photographer spent almost a decade taking photos of Japan's vending machines in the most remote locations… https://t.co/CgmY4oXKQD
    Tweet 490: The Las Vegas shooter had money troubles prior to the attack, but his motive is still unclear, sheriff says… https://t.co/Ju8BhpZVfD
    Tweet 491: San Juan mayor says the hurricane death toll in Puerto Rico could be 10 times higher than reported… https://t.co/0kzf6kbkFj
    Tweet 492: A University of Miami art professor created Ku Klux Klan-style hoods out of American flags for a faculty art exhibi… https://t.co/HIpnBJPkzO
    Tweet 493: Former Trump foreign policy adviser Carter Page met with Russian Deputy PM Arkady Dvorkovich while in Moscow in 201… https://t.co/b6UUpzNj1N
    Tweet 494: After terror attack, a resilient city rises up to support its runners | via @CNNopinion https://t.co/O5oGbSaZRH https://t.co/EWX8hDYNdr
    Tweet 495: Sprint and T-Mobile's have abandoned discussions about a potential merger https://t.co/80Nfe6njhZ https://t.co/B0Gzmkgpx3
    Tweet 496: Jeff Bezos just sold $1.1 billion worth of Amazon stock https://t.co/mPDNE2slyt https://t.co/hioycqq70j
    Tweet 497: The New York City terror suspect planned to return to Uzbekistan, his sister says https://t.co/1iPsUlpMc8 https://t.co/DXYMGfvI1y
    Tweet 498: This is what the GOP tax plan means for higher education https://t.co/UE8SZ1AXZY https://t.co/oy4eoVFbek
    Tweet 499: The tax bill unveiled by Republicans would eliminate a decades-old deduction for people with very high medical cost… https://t.co/3NCHAdB9Ha
    Tweet 500: Republican Sen. Rand Paul was assaulted in his Kentucky home on Friday, police say https://t.co/edfnGbL3ds https://t.co/GFd3bZLfhJ
    


```python
news_room_df = pd.DataFrame.from_dict(sentiments)
news_room_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>User</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.7430</td>
      <td>Sun Nov 05 22:27:18 +0000 2017</td>
      <td>0.701</td>
      <td>0.247</td>
      <td>0.052</td>
      <td>1</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.7351</td>
      <td>Sun Nov 05 21:32:03 +0000 2017</td>
      <td>0.733</td>
      <td>0.267</td>
      <td>0.000</td>
      <td>2</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.5574</td>
      <td>Sun Nov 05 20:49:53 +0000 2017</td>
      <td>0.825</td>
      <td>0.000</td>
      <td>0.175</td>
      <td>3</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.3818</td>
      <td>Sun Nov 05 20:47:59 +0000 2017</td>
      <td>0.714</td>
      <td>0.109</td>
      <td>0.176</td>
      <td>4</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.2732</td>
      <td>Sun Nov 05 20:46:18 +0000 2017</td>
      <td>0.826</td>
      <td>0.000</td>
      <td>0.174</td>
      <td>5</td>
      <td>@BBC</td>
    </tr>
  </tbody>
</table>
</div>




```python
news_room_df['User'] = news_room_df['User'].map({'@CBS': 'CBS', '@CNN': 'CNN', '@BBC': 'BBC', '@FoxNews': 'Fox', 
                                              '@nytimes': 'NYT'})
```


```python
news_room_df.to_csv('news_room_tweet.csv')
```


```python
fig, ax = plt.subplots()
fig.set_size_inches(10, 7)
colors = {'CNN':'red', 'BBC':'blue', 'CBS':'green', 'NYT':'white', 'Fox': 'yellow'}
ax.scatter(news_room_df['Tweets Ago'], news_room_df['Compound'], c=news_room_df['User'].apply(lambda x: colors[x]),alpha = 0.7)
ax.set_title("Sentiment Analysis of Media Tweet (11/5/2017)", weight='bold', fontsize=15)
ax.set_xlabel("Tweets Ago", weight='bold', fontsize = 12)
ax.set_ylabel('Tweet Polarity', weight ='bold', fontsize=12)
#ax.set_aspect('auto')
fig.tight_layout()
fig.savefig('CompoundScore.png')
plt.ylim(-1, 1)
plt.xlim(100,0)
plt.grid()
plt.show()
```


![png](output_7_0.png)



```python
news_room_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Date</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweets Ago</th>
      <th>User</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.7430</td>
      <td>Sun Nov 05 22:27:18 +0000 2017</td>
      <td>0.701</td>
      <td>0.247</td>
      <td>0.052</td>
      <td>1</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.7351</td>
      <td>Sun Nov 05 21:32:03 +0000 2017</td>
      <td>0.733</td>
      <td>0.267</td>
      <td>0.000</td>
      <td>2</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.5574</td>
      <td>Sun Nov 05 20:49:53 +0000 2017</td>
      <td>0.825</td>
      <td>0.000</td>
      <td>0.175</td>
      <td>3</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.3818</td>
      <td>Sun Nov 05 20:47:59 +0000 2017</td>
      <td>0.714</td>
      <td>0.109</td>
      <td>0.176</td>
      <td>4</td>
      <td>BBC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.2732</td>
      <td>Sun Nov 05 20:46:18 +0000 2017</td>
      <td>0.826</td>
      <td>0.000</td>
      <td>0.174</td>
      <td>5</td>
      <td>BBC</td>
    </tr>
  </tbody>
</table>
</div>




```python
aggregate_compound = news_room_df.groupby(['User'])['Compound'].mean()
agg_compound = pd.DataFrame(aggregate_compound)
del aggregate_compound.index.name
agg_compound
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BBC</th>
      <td>0.088186</td>
    </tr>
    <tr>
      <th>CBS</th>
      <td>0.203394</td>
    </tr>
    <tr>
      <th>CNN</th>
      <td>-0.139315</td>
    </tr>
    <tr>
      <th>Fox</th>
      <td>-0.117557</td>
    </tr>
    <tr>
      <th>NYT</th>
      <td>0.007030</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use DataFrame.plot() in order to create a bar chart of the data
agg_compound.plot(kind="bar", figsize=(10,7), legend=False)

# Set a title for the chart
plt.title("Overall Media Sentiment Based on Tweet (11/5/2017)", weight='bold', fontsize=15)

plt.ylabel('Tweet Polarity', weight ='bold', fontsize=12)
plt.ylim(-.10, .23)
plt.savefig('OverallCompoundScore.png')
plt.show()
```


![png](output_10_0.png)

