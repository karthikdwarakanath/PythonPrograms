#Messaging System mock design

class Message(object):
    def __init__(self, message):
        self.message = message
        self.timestamp = 0

    def generateTimeStp(self):
        pass
        
class Server(object):
    def __init__(self):
        pass

    def generateTimeStamp(self):
        pass

    def addUser(self, user):
        #check if the user exists in the local db and add if it doesn't
        #broadcast the user to other servers
        pass

    def removeUser(self):
        #check if the user exists and delete if it doesn
        #broadcast the remove request to other servers
        pass

    def lookupUser(self):
        pass

    def lookupMessage(self, startTime, endTime, toUser):
        #Given start and end time stamp and to user name
        #find if there are any new messages stored locally in that time range
        #that are addressed to the toUser
        #return the message to the caller
        pass

    def sendMessage(self, toUser, message, fromUser):
        #Once a message is received from fromUser, stored it with timestamp with
        #key as the toUser
        #Also send this message over to the other servers so that they can update their
        #cache
        pass

    def requestHandler(self):
        pass

class Client(object):
    def __init__(self):
        pass

    def getMessage(self):
        #This executes in a loop
        #checks for message every 30 seconds and time can be configured
        #Provide a timestamp interval for the server to check for new messages
        #last message timestamp and current timestamp
        #the received messages are sorted based on the timestamp
        pass

    def sendMessage(self):
        #Client gets a prompt to enter the user to whom the message is addressed
        #enters the message and sends it to the server.
        pass
