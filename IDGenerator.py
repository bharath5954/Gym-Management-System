class IDGenerator:
    @staticmethod
    def generateCustomerID():
        f = open("customer_id", "r+")
        id = f.readline()
        id = id.strip()
        idw = int(id)
        idw += 1
        f.seek(0)
        f.write(str(idw) + "\n")
        f.truncate()
        f.close()
        return int(id)

    @staticmethod
    def generateMembershipD():
        f = open("membership_id", "r+")
        id = f.readline()
        id = id.strip()
        idw = int(id)
        idw += 1
        f.seek(0)
        f.write(str(idw) + "\n")
        f.truncate()
        f.close()
        return int(id)

    @staticmethod
    def generateTrainerID():
        f = open("trainer_id", "r+")
        id = f.readline()
        id = id.strip()
        idw = int(id)
        idw += 1
        f.seek(0)
        f.write(str(idw) + "\n")
        f.truncate()
        f.close()
        return int(id)