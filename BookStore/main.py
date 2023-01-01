import xml.etree.ElementTree as ET

#parse the XML file
xtree = ET.parse(r"BookStore\info.xml")

#get root element
root = xtree.getroot()

#getting all book details
def dispdetails(child):
        print("-------------------------------------")
        print("Book: {}".format(child.get('name')))
        print("Title: {}".format(child[0].text))
        print("Author: {}".format(child[1].text))
        print("Published: {}".format(child[2].text))
        print("-------------------------------------")
flag = 1
while(flag!=0):
    print("------------------------------------")
    print("| Welcome to MyBookStore!          |")
    print("| Enter 1 to Display all Books     |")
    print("| Enter 2 to Search books by Year  |")
    print("| Enter 0 to Exit                  |")
    print("------------------------------------")
    choice = input("Your input here: ")
    if(int(choice) == 1):
        for child in root:
            dispdetails(child)
    elif(int(choice)==2):
        it = 0
        year = input("Enter the Year")
        #get book by publishing year
        for child in root:
            if(child[2].text==year):
                it = it + 1
                print("Found a match in Book: {}".format(child.get('name')))
                print("Displaying Details...................")
                dispdetails(child)
                break
        if(it==0):
            print("No books found for this year")
    elif(int(choice)==0):
        break
    else:
        print("Enter a valid choice!")
    