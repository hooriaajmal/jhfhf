nameT=();
nameD={};
size=int(input("Enter the size of dictionary : "));
for i in range(size):
    firstName=input("Enter First Name : ");
    lastName=input("Enter Last Name : ");
    name = firstName + lastName;
    pNo= int(input("Enter the Phone Number : "));
    nameD.update({name:pNo});
nameT=nameD;
x=input("Enter the First Name whose pNo you want to see : ");
y=input("Enter the Last Name whose pNo you want to see : ");
m=x+y;
if m in name:
        print(name,pNo);
else:
        print("not found");
