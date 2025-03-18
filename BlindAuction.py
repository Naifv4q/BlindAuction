from os import system
import Art
system("cls")
Art.Intro()
bidderName=input("Name of the bidder: ")
bidderBid=int(input("How much would you bid ?: $"))
#This is a test!
isTrue=True
Bidders={bidderName:bidderBid}
while isTrue:
    decision=input("Are there anymore bidders admin? 'Yes' or  'No': ").lower()
    if decision=="yes":
        system("cls")
        Art.Intro()
        bidderName=input("Name of the bidder: ")
        bidderBid=int(input("How much would you bid ?: $"))
        Bidders[bidderName]=bidderBid
    elif decision=="no":
        highestBid=0
        for key in Bidders:
            if Bidders[key] >highestBid:
                highestBid=Bidders[key]
                highestBidderName=key
        Art.Money()
        print(f"The highest bidder is {highestBidderName} with a bid of ${highestBid}")
        isTrue=False
    else:
        print("Invalid Input !")
#I added this comment to test if I edit what happens
    
