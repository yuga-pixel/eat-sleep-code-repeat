# An application which tells the horoscope of every zodiac sign.

next = True
while next == True :
    





    print(''' ZODIAC SIGNS:
    1) Aries
    2) Taurus
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    s = int(input("Pick the number assigned to the zodiac sign whose horoscope you want to see and then press Enter.\n"))
    print(s)

    if s==1 :
        print("They say everything happens at the right time and in the right place, and you are beginning to see proof of your own manifesting power in your outer reality. Become aware of the opportunities you are attracting, dear Aries. There is a good chance your higher self has pulled a few strings on your behalf. Remember, fortune favours the brave. So, don't be afraid to take a risk or to step out of your comfort zone. Realising your highest potential is going to a big theme for you in the months to come.")







    elif s==2 :
        print("You look exhausted, Taurus, and that weariness isn't going to go anywhere until you do something about it. Revitalising on a mind, body, and soul level is an important theme for you right now. In moments of deep contemplation, you will find your answers. Remember, nature is the best healer. Give yourself the permission to venture into the wild and the unknown, knowing that you will return feeling more optimistic about your surroundings.")

    

              

    elif s==3 :
        print("The Universe works in mysterious ways, providing us with the help, assistance, and guidance we need at the precise moment that we are in need of it. Become aware of the signs and symbols around you. They are revealing to you your soul's purpose. Consciously connecting with Source energy is also going to be a big theme. Remember, we all have our own ways of experiencing transcendence. What works for one person, may not work for the other. Word for the wise: find your own unique method to raise your vibrations.")

    



        

    elif s==4 :
        print("The past few months have been a time of deep inner contemplation. A time of letting go of the old and meeting your true self. Releasing yourself from past trauma has been anything but easy. You found the courage required to integrate your shadows anyway. What the days ahead will bring forth: clarity on your mission and your purpose. The more you connect with your deep inner knowing, the more clarity you will receive from your ancestors and your guides.")

    




    elif s==5 :
        print("The past few months have been anything but easy. You may have felt like everything is being taken away from you. Has it really, though? Trust your inner guidance that's saying you are making space for a new dawn. On the cards for you this week: a sudden turn of fortune. Trust that the abundance you have been working towards will find its way into your life unexpectedly, along with fulfilling opportunities. While there's a part of you that believes you can have anything you desire, there's another part that fears the change. This is the part of you that must be put to rest, Leo. Overheard at the cosmic conference: the time to step into bigger shoe")






    elif s==6 :
        print("You're on the right track, Virgo, one that's helping you fulfil your mission and purpose. Channel your warrior spirit and continue walking the path armed with courage. You will receive the fruits of your labour in due course of time. For now, focus on strengthening the foundation. Those on a yogic journey will find that grounding practices and asanas are especially beneficial at this time. Not a fan of movement meditation? Consider walking barefoot in the park in order to connect with the element of Earth.")






    elif s==7 :
        print("Tranquility promises to be a constant in your world, Libra, along with the wisdom required to make peace where there has been war. The compassion to be receptive to the other side will make all the difference. So listen with an open heart and vow to leave your judgements at the doorstep. Connecting with the element of water will also invoke a sense of calm in the midst of this storm. Consider a ritualistic bath (if you don't live near a natural body of water) or meditating with a blue-hued crystal such as aquamarine, Larimar or turquoise")


    elif s==8 :
        print("The cards are urging you to reconsider your relationship with your body. Do you believe that a workout has to be punishing in order to be effective, or that you need to count every calorie to a level that's borderline obsessive? Consider the art of moderation, Scorpio. Resist nothing. Be mindful of everything. Oh, and while you're at it, allow yourself a simple treat! PS: a warm cup of cocoa with a bit of sea salt and honey sounds like just the indulgence you need today.")


    elif s==9 :
        print("There are things that have helped you reach the epitome of success, and then there are things that made you realise what rock bottom is made of. However, no experience is inherently good or bad. Each of them played a significant role in making you the person you are today. So, instead of looking outside for answers, look within and assimilate the learnings. This will help you tap into your own reservoir of wisdom and make decisions that are in alignment with your greatest good.")





    elif s==10 :
        print("There are choices that helped you emerge victorious, and then there are choices that made you question your abilities endlessly. But, if you look at your life from a higher perspective, you will realise, no decision is good or bad. Each of them played a significant role in making you the person you are now. Today, instead of looking outside for answers, turn inwards and review your life story. This will give you clarity on your mission and purpose. Given that you are at an important juncture, making the right decisions will help pave the way for success.")


    elif s==11 :
        print("It's true that movement is essential for the circulation of chi through the energy pathways of the body, but who says workouts have to be punishing in order to be effective? The cards are urging you to examine your relationship with both, your vessel and physical activity. If you've been pushing yourself to your limits, bring gentleness into the equation. Just for today, consider engaging in an activity that your body enjoys—swimming or dance movement therapy, for instance. When it comes to your diet, practice moderation. Resist nothing. Be mindful of everything. Over a period of time, your body will start to reject what isn't improving your health in any way.")



    elif s==12 :
        print("Take a moment to examine your dreams—your wildest and most outrageous dreams. Do you believe you are capable of manifesting them in your reality, or fear the outcome of creating your best life? It's time to break past the mental prison and align yourself with the life you were always meant to live. Spirit is pulling more than a few strings on your behalf. Work with, rather than against, the energy of miracles.")


    else :
        print("Hey, you sure about the number?")

    next = True if input("Shall we do it again? (Y/N) ")=="Y" else False



        
