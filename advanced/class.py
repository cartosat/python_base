db = { }

class AddUser:
    def add(self, uId, uName, uAge):
        self.uId = uId
        self.uName = uName
        self.uAge = uAge
        try:
            db[uId] = {self.uName, self.uAge}
            print(f"User {self.uName} added successfully")
        except Exception as e:
            print(e)

class DelUser:
    def remove(self, uId):
        try:
            db.pop(uId)
        except Exception as e:
            print("user not found with id:-",e)

class UpdateUser:
    def __init__(self):
        pass

u1 = AddUser()
u1.add(1, 'Vaibhav', 24)
print(db)
d1 = DelUser()
d1.remove(2)
print(db)