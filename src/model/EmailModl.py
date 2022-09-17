

class EmailModel:

    def __init__(self, email):
        self.email = email

    
    def set_schema(
        self,
        id=None,
        date=None,
        emailFrom=None,
        emailTo=None,
        content=None
        ):
        self.id = id
        self.date = date
        self.emailFrom = emailFrom
        self.emailTo = emailTo
        self.content= content
        
