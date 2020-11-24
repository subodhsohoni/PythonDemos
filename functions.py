def hellouser(username):
    print ("Hello " + username)

class functionsdemo:

    @classmethod
    def splconcat(cls, str1, str2):
        retval = str1 + ' ' + str2
        return retval

    def validatepassword(self, strpass):
        if (len(strpass) >= self.MinLen):
            print ("Password minimum legth condition passed")
        else:
            print ("Password minimum legth condition did not passed")
        if (len(strpass) <= self.MaxLen):
            print ("Password maximum legth condition passed")
        else:
            print ("Password maximum legth condition did not passed")

    MinLen = 6
    MaxLen = 10


mydemo = functionsdemo()
print (mydemo.splconcat("Subodh", "Sohoni"))
mydemo.validatepassword("P2ssw0rd12345")

hellouser(input("Enter your name:"))

