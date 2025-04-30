import sys
import pathlib
import shutil
import datetime
from backupcfg import source,destination
import logging
import smtplib
from datetime import datetime

smtp = {"sender": "",    # elasticemail.com verified sender
        "recipient": "", # elasticemail.com verified recipient
        "server": "",      # elasticemail.com SMTP server
        "port": ,                           # elasticemail.com SMTP port
        "user": "",      # elasticemail.com user
        "password": ""}     # elasticemail.com password

# location = original file, copyplace = where you wish to move the new file.

logging.basicConfig(filename="loginfo.log", level = logging.DEBUG) 
logger=logging.getLogger()

dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")

def copyingyes(location = "", copyplace = ""):
    shutil.copy2(location,copyplace)

#sendng the email
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR in sending email: An error occurred.", e)

try:
    argCount = len(sys.argv)
    program = sys.argv[0]
    arg1 = sys.argv[1]
    # arg2 = sys.argv[2]
    
    # print("arg0=", program)
    # print("arg1 = ", arg1)
    # print(arg2)

    if (arg1.lower() == "job1") or (arg1.lower() == "job2"):
        #print("Success")
        
        print(source)
        print(destination)
        copyingyes(source, destination + dateTimeStamp)
        # copyingyes(job1list[1], backuplocation)
        # copyingyes(job1list[2], backuplocation)
        logger.info("SUCCESS. " + dateTimeStamp)
    else:
        print("job number not found.")
        logger.error("FAIL .job number not found." + dateTimeStamp)
        sendEmail("FAIL .a error has occured.job number not found")
except Exception as err:
    print("FAIL.Error has occured. ", err)
    logger.error("FAIL."+err + dateTimeStamp)
    sendEmail("FAIL." +err)
    
    

    
    

    