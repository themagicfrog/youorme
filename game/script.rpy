define m = Character('me', color="#c8ffc8")
define f = Character('Felix', color="#c8c8ff")
define d = Character('Dog', color="#c8c8ff")
define o = Character('Mom', color="#c8c8ff")
define h = Character('Dad', color="#c8c8ff")

label start:

    with fade

    scene bg park at smaller

    show felix chappy at fit_screen

    "Evelyn was out for a walk in the park when she ran into Felix, who was walking his Balulu."

    transform fit_screen:
        zoom 0.4     
        xalign 0.5
        yalign 1.0  

    transform bigger:
        zoom 0.6     
        xalign 0.5
        yalign 1.0  

    transform smaller:
        zoom 0.7    
        xalign 0.5
        yalign 1.0   
    
    transform right_side:
        zoom 0.4         
        xalign 0.99    
        yalign 1.0    

    transform left_side:
        zoom 0.4         
        xalign 0.01    
        yalign 1.0   

    m "Hi, Felix. Isn't the weather so nice today?"

    show felix ohappy at fit_screen

    f "Hi, Evelyn. Yeah, it's wonderful! After I finish walking my balulu, I'm going to get some matcha and read feminist literature! Wanna come?"

    show felix cworried at fit_screen

    m "I'd love to, but I have to feed my dog Fluffy..."

    show felix chappy at fit_screen
    
    m "but I could also go get matcha with you."

    show felix ohappy at fit_screen

    f "You should come with me! I'd love to spend time with you."

    menu:

        "Sure! I'll come with you. Fluffy can wait.":
            jump matcha

        "I'd love to, but I need to go feed Fluffy.":
            jump dog

    label dog: 

        hide felix ohappy
        scene bowl full at smaller
        show fluffy ohappy at fit_screen
        d "Ruff ruff! I'm so excited to eat."

        show fluffy chappy at fit_screen

        m "Fluffy, here's your dinner."

        show fluffy ohappy at fit_screen

        d "Thanks!"

        m "Aw, I'm so lonely without Felix."

        "Time to start over..."

        return
    
    label matcha: 
        
        f "Great! Let's go."

        hide felix chappy
        scene bowl empty at smaller
        show fluffy hungry at fit_screen
        d "(at home) Woof... I'm so hungry."

        m "I hope Fluffy is okay."

        show fluffy dead at bigger

        d "*dies from starvation*"

        hide fluffy dead
        show felix ohappy at fit_screen

        f "I know a great matcha place not far from here, come with me."

        m "Okay! Let's go..."

        show felix chappy at fit_screen
        scene bg cafe at smaller

        m "Look! We've arrived. Wow, I'm so thirsty."

        scene bg cafe at smaller
        show felix oworried at fit_screen

        m "Wow, this is great!"

        f "Right? Oh no! I forgot my wallet at home..."

        menu :
            "It's okay. I can pay for yours!":
                show felix chappy at fit_screen
                jump pay

            "Aw, well, maybe a different time then...":
                show felix cworried at fit_screen
                jump nope

        
        label pay :
            show felix chappy at fit_screen
            f "Great! Thank you so much."

            show felix ohappy at fit_screen
            m "Yeah... no problem...  (getting fatigued...) I only have enough money for 1 drink though,"

            hide felix ohappy
            show felix ohappy at right_side
            show money at left_side
            "You can have it."

            hide money
            show felix ohappy at left_side
            show matcha at right_side
            f "What tasty matcha!"

            jump choice

        label nope:
            f "Could you pay for mine? I'm really dehydrated."

            menu :

                "Okay, I guess... (getting fatigued)":
                    jump drink

                "No... sorry.":
                    jump end

        label drink:
            show felix chappy at fit_screen
            m "I only have enough money for 1 drink, here"

            show felix ohappy at left_side
            show matcha at right_side

            f "What tasty matcha!"

            jump choice

        menu : 
            "Okay, I guess":
                jump dehydrate

            "No":
                jump end

        label dehydrate:
            show felix cworried at fit_screen
            m "I'm so thirsty..."
            
            jump choice
        
        label end: 
            show felix oangry at fit_screen
            f "You're such a bad person."

            m "Time to try again..."

            return

        label choice:

            show felix chappy at left_side
            m "I'm getting a call from someone."

            m "It's my mom!"

            hide felix oangry
            hide matcha
            show phone at fit_screen

            o "Honey, your father got into a car crash. He's in the hospital, and he's in a serious condition."

            o "The doctors don't know if he will make it. Come to the hospital now!"

            hide phone
            show felix ohappy at fit_screen

            f "Stay with me! Don't you want to hang out with me?"

            show felix cworried at fit_screen

            m "Uhhh... I don't know..."

            menu :
                "Okay, I guess I can stay with you. My dad can wait.":
                    jump dying

                "No, I need to go see my dad." :
                    jump dad

            label dying: 

                hide felix ohappy
                show phone at fit_screen

                o "Where were you, Evelyn?"

                o "I have some sad news..."

                scene bg dying at smaller
                hide phone

                o "your father died."

                m "..."

                return

            label dad:
                show felix oangry at fit_screen
                f "You are such a bad person."

                m "Time to try again..."

            
            