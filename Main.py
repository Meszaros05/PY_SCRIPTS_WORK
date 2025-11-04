import os
import sys
import time
from Email_SMTP.Email_SMTP import Email #this imports Email function from Email_SMTP
from JSON_to_EXCEL.JSON_to_EXCEL import Convert_JSON_to_EXCEL
from API_Handler.API_Handler import *
from JSON_to_EXCEL.helper import wait_for_file



def main():
    main_API_Handler()
    Convert_JSON_to_EXCEL()
    #Email()

if __name__ == "__main__":
    main()




