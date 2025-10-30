import os
import sys
from Email_SMTP.Email_SMTP import Email #this imports Email function from Email_SMTP
from JSON_to_EXCEL.JSON_to_EXCEL import Convert_JSON_to_EXCEL

def main(): #This is wehere we need to call all 
    Convert_JSON_to_EXCEL()
    Email()
    
    


if __name__=="__main___":
    main()





