# InstaFollowerBot

This bot comprises of a single script which does all the magic of increasing instagram followers  
all you have to do is open followup.py and configure it according to your need
Enjoy!

**please note:-due to changes in instagram login flow every time you run this bot, you will have to input otp to make it work**

# what it does?
It takes in your instagram credentials, gracefully logs you into your account,then one by one starts following all profiles provided by 
`urls` list. and if they are already followed by you then it unfollow them back so it can follow them again in next iteration.

# why follow-unfollow cycle?
hmm.. that's interesting question! actually its an instagram feature when you follow some famous personalities you start appearing in section which says `Suggested For You` just below their profile. 
now, due to this people visiting their profile are very likely to follow you.
so all this bot does is ,it increases your chances of being followed by people since you are shown in suggested list of all users you have followed.  
this saves you from tedious job of manually attempting this method.

# is it safe and secure?
about safe:-In my opinion, I tried this hundred of times and my account is still working fine, but one should not run it for very long period of time.
in short use it on your own risk.

about secure:-Hell yes! if your device is safe

# Configuration

    #for windows platform="windows"
    #for mac platform="macos"
    # by default it runs on linux but you can change according to your platform,
    # Chromedriver is updated to latest version 79.0.3945.36
    # by default otp time out is 30 seconds
    obj = webscrapper(url="", 
                      email="youremail@provider.com",
                      password="yourinstapasswordgoeshere",
                      platform="linux",
                      preview=True,
                      otp_timeout=30)
                  




