import pickle as cPickle
class GymManager:
    def __init__(self):
        self.customers = dict()
        self.membership = dict()
        self.trainer =dict()
        self.subscriptions = dict()
        self.payments = dict()

    def addCustomer(self, customer) :
        self.customers[customer.getCustomerId()] = customer
        self.subscriptions[customer.getCustomerId()] = dict()
        self.payments[customer.getCustomerId()] = dict()

    def addMembership(self, membership):
        self.membership[membership.getMembershipId()] = membership

    def addTrainer(self, trainer) :
        self.trainer[trainer.getTrainerId()] = trainer
        self.subscriptions[trainer.getTrainerId()] = dict()
        self.payments[trainer.getTrainerId()] = dict()

    def addSubscription(self, customer,membership, months):
        membershipId = membership.getMembershipId()
        customerId = customer.getCustomerId()
        self.subscriptions[customerId][membershipId] = months

    def addPayment(self, customer, membership, amount):
        membershipId = membership.getMembershipId()
        customerId = customer.getCustomerId()
        self.payments[customerId][membershipId] += amount
        self.subscriptions[customerId][membershipId] -= 1

    def save(self):
        cPickle.dump(self, open("gym_manager.bin", "wb"))
