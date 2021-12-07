from IDGenerator import IDGenerator
class Trainer:
    """
    Trainer entity class.
    Private Attributes:
        trainerID String
        name String
        phoneNo String
        joiningDate Date

    Public methods:
        Getters and setters
    """

    def __init__(self, name='', phoneNo='', joiningDate=''):
        self.__name = name
        self.__phoneNo = phoneNo
        self.__joiningDate = joiningDate
        self.__trainerId = IDGenerator.generateTrainerID()

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def getPhoneNo(self):
        return self.__phoneNo

    def setJoiningDate(self, joiningDate):
        self.__joiningDate = joiningDate

    def getJoiningDate(self):
        return self.__joiningDate

    def getTrainerId(self):
        return self.__trainerId

    def __str__(self):
        return self.getName()+" "+self.getPhoneNo()+" "+self.getJoiningDate()+" "+str(self.getTraniererId())