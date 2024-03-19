import pandas as pd


class Database:
    database = pd.DataFrame({'User_name':["Aryan"],
                            'Health_Notes':["Diabetes"]})
    
    def addUser(self, argument:dict):
        self.database.loc[-1] = argument
        self.database.index = self.database.index + 1
    
    def deleteUser(self, index):
        self.database = self.database.drop(index=index, axis = 0, inplace=False)

data = Database()
data.deleteUser(0)
print(data.database.info)
print("then here")
data.addUser({"User_name":"Aryan", "Health_Notes":"Dmksd"})
print(data.database.info)