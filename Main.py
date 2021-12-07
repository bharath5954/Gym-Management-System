from GymManager import GymManager
from Customer import Customer
from Membership import Membership
from Trainer import Trainer

gymManager = GymManager()
print ("\n")
print (" ----- Uni Fitness Center ----- ")
print ("Hello, Admin welcome. ")


def menu():
    print ("1. Add Customer")
    print ("2. Add Membership")
    print ("3. Add Trainer")
    print ("4. Show all Membership")
    print ("5. Show all Customers")
    print ("6. Show all Trainer")
    print ("7. Find customer by name")
    print ("8. Add Subscription")
    print ("9. Add Payment")
    print ("10. Show this menu again")
    print ("\nEnter You Choice: ")

menu()

while(True):
    inp = int(input())
    if inp == 1:
        name = str(input("Enter Customer name - "))
        phoneNo = str(input("Enter Customer phone no. - "))
        joinDate = str(input("Enter joining date - "))
        customer = Customer(name, phoneNo, joinDate)
        gymManager.addCustomer(customer)

    elif inp == 2:
        type = str(input("Enter membership type - "))
        facilities = str(input("Enter facilities - "))
        cost = int(input("Enter membership cost - "))
        Membership = Membership(type, facilities, cost)
        gymManager.addMembership(Membership)

    elif inp == 3:
        name = str(input("Enter trainer's name - "))
        phoneNo = str(input("Enter trainers phone no. - "))
        joinDate = str(input("Enter joining date - "))
        trainer = Trainer(name, phoneNo, joinDate)
        gymManager.addTrainer(trainer)


    elif inp == 4:
        print ("MembershipID\tType\tFacilities\tCost")
        for memId in gymManager.membership.keys():
            membership = gymManager.membership[memId]
            membershipId = memId
            type = membership.getType()
            facilities = membership.getFacilities()
            cost = membership.getCost()
            print (str(membershipId) + "\t"   +  type   + "\t" + facilities  + "\t" + str(cost))

    elif inp == 5:
        print ("CustomerID\tName\tPhone\tJoining Date")
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            customerId = cusId
            name = customer.getName()
            phoneNo = customer.getPhoneNo()
            joinDate = customer.getJoiningDate()
            print (str(customerId) + "\t" + name   + "\t" + phoneNo  + "\t" + joinDate)

    elif inp == 6:
        print ("TrainerID\tName\tPhone\tJoining Date")
        for traId in gymManager.trainer.keys():
            customer = gymManager.trainer[traId]
            TrainerId = traId
            name = trainer.getName()
            phoneNo = trainer.getPhoneNo()
            joinDate = trainer.getJoiningDate()
            print (str(TrainerId) + "\t"   + name +  "\t" + phoneNo + "\t" + joinDate)

    elif inp == 7:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found".format(name))
        else:
            membershipDict = gymManager.subscriptions.get(customerId)
            print ("Customer found", gymManager.customers[customerId])
            if membershipDict != {}:
                print ("Subscribed to")
                for memId in membershipDict.keys():
                    print (gymManager.membership[memId], "for {0} months".format(gymManager.subscriptions[customerId][membershipId]))
            else:
                print ("No subscription found for this customer")

    elif inp == 8:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break;
        if customerId == -1:
            print ("Customer with name - {0} not found.".format(name))
            print ("Try adding a new customer.")
        else:
            print ("Customer found", gymManager.customers[customerId])
            if gymManager.membership.keys():
                for memId in gymManager.membership.keys():
                    print (memId, gymManager.membership[memId])
                membershipId = int(input("Select a membership: "))
                if membershipId > max(gymManager.membership.keys()):
                    print ("Please select a valid membership.")
                else:
                    months = int(input("Enter no. of months"))
                    gymManager.addSubscription(gymManager.customers[customerId], gymManager.membership[membershipId], months)
                    print ("Subscription added.")
            else:
                print ("No membership exists. Try adding a membership first.")

    elif inp == 9:
        name = str(input("Enter customer name - "))
        customerId = -1
        for cusId in gymManager.customers.keys():
            customer = gymManager.customers[cusId]
            if customer.getName() == name:
                print (customer)
                customerId = cusId
                break ;
        if customerId == -1:
            print ("Customer with name - {0} not found.".format(name))
            print ("Try adding a new customer.")
        else:
            print ("Customer found", gymManager.customers[customerId])
            if gymManager.membership.keys():
                for memId in gymManager.membership.keys():
                    print (memId, gymManager.membership[memId])
                membershipId = int(input("Select a membership :"))
                if membershipId > max(gymManager.membership.keys()):
                    print ("Please select a valid membership.")
                else:
                    if gymManager.subscriptions[customerId][membershipId] > 0:
                        customer = gymManager.customers[customerId]
                        membership = gymManager.membershipS[membershipId]
                        gymManager.addPayment(customer, membership,membershipId)
                        print ("Payment added. Subscription expires in {0} months.".format(gymManager.subscriptions[customerId][membershipId]))
    elif inp == 10:
        menu()
    elif inp == 11:
        gymManager.save()
        exit(0)
    else:
        print ("Please enter a valid number")
    menu()
