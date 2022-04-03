import python.build.database
from python.build.database import Database


m = Database("localhost", "erick", "1234", "passwords")

m.SetTable("erick")

password = m.GetPassword("twitch", "ham")
print(password)



