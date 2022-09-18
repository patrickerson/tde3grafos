

class EmailModel:



    
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
        
    def export_dict(self):
        return dict(date=self.date, emailFrom=self.emailFrom, emailTo=self.emailTo, content=self.content)
