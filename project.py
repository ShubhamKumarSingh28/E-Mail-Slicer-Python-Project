print("Welcome to E-mail slicer")
print("******************************************************************************************************************************************************************************************************************************************************************************************************")
print("We check for E-mail validation and allow user to change there domain if they want")
def email_check(a):
    i=0
    l=0
    m=""
    if a == "0":
        print("Thank you using this program")
        exit()
    else:
        f=a.split("@")
        f=f[0:-1]
        print(f)
        for i in range(len(f)):
            m+=f[i]
        if "?" in m:
            print("Entered email is invalid")
        elif "!" in m:
            print("Entered email is invalid")
        elif "@" in m:
            print("Entered email is invalid")
        elif "#" in m:
            print("Entered email is invalid")
        elif "%" in m:
            print("Entered email is invalid")
        elif "$" in m:
            print("Entered email is invalid")
        elif "^" in m:
            print("Entered email is invalid")
        elif "&" in m:
            print("Entered email is invalid")
        elif "*" in m:
            print("Entered email is invalid")
        elif "/" in m:
            print("Entered email is invalid")
        elif "," in m:
            print("Entered email is invalid")
        else:
            k=0
            while i < len(a):
                if a[i] == "@":
                    k = i
                i += 1
            if len(a[0:k])>2:
                l1=["gmail.com","yahoo.com","hotmail.com","facebook.com","amazon.com","reddit.com","apple.com","wikipedia.org","twitter.com","paypal.com","outlook.com","microsoftonline.com","bing.com","weather.com","quora.com","ebay.com","cnn.com","espn.com","imdb.com","reddit.it","microsoft.com","office.com","hulu.com","netflix.com","pintrest.com","discord.com","spotify.com","shein.com","github.com","msn.com","adobe.com","blogspot.com","accuweather.com","patreon.com","uber.com","ign.com","yahoo.co.in","ymail.com","live.com","hotmail.it","googlemail.com","yahoo.it","sky.com","virgillio.it","gmx.net","mac.com","comcast.net","rediffmail.com","free.fr","web.de","verizon.net","live.co.uk","live.nl","ig.com.br","yahoo.it","rocketmail.com","yahoo.ca","earthlink.net","optonline.net","qq.com","mail.com","windstream.net","aim.com","rambler.ru","bellsouth.net","yahoo.co.jp","me.com","ntlworld.com","okta.com","nih.gov","steam.com","ticketmaster.com","evergage.com","fedex.com","chaturbate.com","bestbuy.com","zoom.in","samsung.com","mcdonalds.com","indeed.com","duckduckgo.com","tiktok.com","arcor.de","yahoo.co.id","tiscali.it","charter.net","aol.com","optusnet.com.au","juno.com","windstream.net","centurytel.net","instagram.com","twitch.tv","linkedin.com","instructure.com","wikimedia.org","foxnews.com","chase.com","gfg.com","tumblr.com"]
                while i < len(a):
                    if a[i] == "@":
                        k = i
                    i += 1
                if a[k+1:] in l1:
                    print("Entered email is Valid")
                elif "." in a[k+1:]:
                    print("New domain found.........","\n","Do you want to add this domain in the domain list?")
                    j=str(input("Enter your choice -> "))
                    if j=="Y" or j=="y":
                        l1.append(a[k+1:])
                        print("The new domain is successfully added")
                else:
                    print("Entered email is invalid")
            else:
                print("Entered email is invalid")
def add_changer(a):
    x=str(input("Do you want to change the address of the email (Example: .aus .uk etc) {Y/N}: "))
    if x=="Y" or x=="y":
        i=0
        while i < len(a):
            if a[i] == "@":
                k = i
            i += 1
        g=a[0:k+1]
        y=str(input("What do you want to change your mail address to? "))
        g+=y
        print("Your new email is:","\n",g)
    elif x=="0":
        print("Thank you using this program")
        exit()
    else:
        print("Email without changes:","\n",a)
def email_domain_slice(a):
    x=0
    i=0
    b=len(a)
    if a == "0":
        print("Thank you using this program")
        exit()

    else:
        while i<b:
            if a[i]=="@":
                x=i
            i+=1
    print("\n","Username for the entered email is:","\n",a[0:x])
    print("Domain for the entered email is:","\n",a[x+1:])

a=str(input("Please enter your email ID ->"))
print()
if a=="0":
    print("Thank you using this program")
    exit()
else:
    email_check(a)
    i=0
    k=0
    while i < len(a):
        if a[i] == "@":
            k = i
        i += 1
    if len(a[0:k]) > 2:

        email_domain_slice(a)
        add_changer(a)

    while True:
        s1=str(input("Do you want to continue?"))
        if s1=='Y'or s1=="y":
            b = str(input("Please enter your email ID ->"))
            email_check(b)
            while i < len(b):
                if b[i] == "@":
                    k = i
                i += 1
            if len(a[0:k]) > 2:

                email_domain_slice(b)
                add_changer(b)

        else:
            print()
            print("Thank you using this program")
            break
