

class EmailModel:



    
    def set_schema(
        self,
        id=None,
        date=None,
        emailFrom=None,
        emailTo=None,
        ):
        self.id = id
        self.date = date
        self.emailFrom = emailFrom
        self.emailTo = emailTo
        
    def export_dict(self):
        return dict(id=self.id,date=self.date, emailFrom=self.emailFrom, emailTo=self.emailTo)
