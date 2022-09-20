

class EmailModel:



    
    def set_schema(
        self,
        emailFrom=None,
        emailTo=None,
        ):
        self.emailFrom = emailFrom
        self.emailTo = emailTo
        
    def export_dict(self):
        return dict(emailFrom=self.emailFrom, emailTo=self.emailTo)
