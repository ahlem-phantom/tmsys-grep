import imaplib
import email
import os
from datetime import datetime
import mimetypes

def get_attachement() :
    mail = imaplib.IMAP4_SSL('outlook.office365.com', 993)
    mail.login("greporder@outlook.com", "MaarchMaarch")
    print("Login success..........")
    mail.select("inbox")
    result, data = mail.uid('search',None,'ALL')
    inbox_item_list = data[0].split()             
    
    counter = 0
    # iterating over UIDs
    for item in inbox_item_list:
        counter+=1
        #result2 contains confirmation in the form of "OK" and email_data contains information regarding the mail.
        result2, email_data = mail.uid('fetch',item,'(RFC822)')
        
        raw_email = email_data[0][1].decode("utf-8")   
        
        #Return a message object structure from a string.
        email_message = email.message_from_string(raw_email)

        #getting information about the mail like to, from,subject, date.
        to_ = email_message['To']         
        from_ = email_message['From']
        subject_ = email_message['Subject']
        date_ = email_message['date']
        
        # setting the format to save in text file. 
        to_ = "to: " + to_ + str("\n")
        from_ = "from: " + from_ + str("\n")
        date_ = "date: " + date_ + str("\n")
        subject__ = "subject: " + subject_ + str("\n")
        
        
        # if path length exceeds a certain limit, then changing the name of mail folder.
        lenOfSubject = len(subject_)
        if (lenOfSubject > 30):
            #Setting subject equals to exceed + counter if len of subject is more than 30.
            subject_ = "exceed"+str(counter)          
        
        # accessing the subparts of email_message
        for part in email_message.walk():
            if part.get_content_maintype == 'multipart':
                continue
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            
            filename = part.get_filename()
            # using mimetype to know the extension of attachment
            # comment below 2 lines to allow all types of format to download in all functions. 
            ext = mimetypes.guess_extension(part.get_content_type())
            # allowing pdf, jpg, png and doc format only
            if ext == '.pdf' or ext == '.jpe' or ext == '.png' or ext == '.docx':
                if filename:
                    save_path = os.path.join(os.getcwd(), ".." ,"uploads", subject_)
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    with open(os.path.join(save_path, filename), 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
                        fp.close()

        # getting the body part of the mail.
            try:
                body = part.get_payload(decode=True).decode()   
            except:
                pass
        
        # saving the required information in a file named as "textfile.txt".
            if content_type == "text/plain" and "attachment" not in content_disposition:
                save_path = os.path.join(os.getcwd(), ".." ,"uploads", subject_)
                print(save_path)

                if not os.path.exists(save_path):
                    os.makedirs(save_path)

                filename = "textfile.txt"
                with open(os.path.join(save_path, filename), 'w+', encoding='utf-8') as fp:
                    fp.writelines(to_)
                    fp.writelines(from_)
                    fp.writelines(date_)
                    fp.writelines(subject__)
                    fp.writelines(body)      #Add here if any other information you want to add in text file.
                    fp.close()
    mail.close()
    mail.logout()


