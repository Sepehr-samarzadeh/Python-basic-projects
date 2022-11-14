#this is one of the easiest way to convert currencies 
#be careful its not that accurate 
#always check for the latest updates form the authentic websites

def main():
    print("this program converts US Dollars to Swidish Krona")
    print()


    dollars = eval(input("Enter the amount of Dollars: "))
    kronas= convert_to_krona(dollars)

    print("That is", kronas, "Kronas.")

convert_to_krona= lambda dollars: dollars * 10.80
main()