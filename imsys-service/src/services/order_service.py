from src.app import db
from src.models import Order
from flask import jsonify
import cv2
import os
import pytesseract
import os 
from datetime import datetime
import imaplib
import email
import mimetypes


def RemoveEmptyLines(entree):
    tab = entree.strip()
    tableausansvide = [ x for x in tab.splitlines() if x!='' ]
    res = ''
    for i in range(0, len(tableausansvide)):
        res = res + tableausansvide[i] + '\n'
    return res

def getTextBetween(mainString, startWord, endWord):
    start = mainString.find(startWord) + len(startWord)
    end = mainString.find(endWord)
    return RemoveEmptyLines(mainString[start:end])

def getPosElement(po):
    element = {}
    element['product_qte'] = po[0:po.find (' ')].strip()
    po = po[po.find (' '):len(po)]
    element['product_tot'] = po[po.rfind (' '):len(po)].strip()
    po = po[0:po.rfind (' ')]
    element['product_price'] = po[po.rfind (' '):len(po)].strip()
    po = po[0:po.rfind (' ')]
    element['product_decription'] = po.strip()
    return element

#Create order postman
def create_order(body):
    order_address =  body['order_address'];
    order_reference =  body['order_reference'];
    order_date = datetime.strptime(body['order_date'],'%Y-%m-%d')
    order_code = body['order_code'];
    order_ht = body['order_ht'];
    order_tva = body['order_tva'];
    order_ttc = body['order_ttc'];
    data = Order( order_address, order_reference, order_date, order_code, order_ht, order_tva, order_ttc)
    db.session.add(data)
    db.session.commit()
    return jsonify({ 
            'status': True 
        })

# create order from mail
def order_save():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'uploads', 'Facture_3.jpg'))
    image = cv2.imread(image_dir, cv2.IMREAD_COLOR)
    #Data After OCR Extraction
    resultat = pytesseract.image_to_string(image)
    #Ordering Data
    order_address = getTextBetween(resultat, 'www.blueprism.com/fr', 'R??f??rence').strip()
    order_reference = getTextBetween(resultat, 'R??f??rence: ', 'Date: ').strip()
    order_date = datetime.strptime(getTextBetween(resultat, 'Date: ', 'Client:').strip(),'%d/%m/%Y')
    order_code = getTextBetween(resultat, 'Client: ', 'Intitul??: ').strip()
    order_ht = getTextBetween(resultat, 'Total HT ', 'TVA (20%) ').strip()
    order_tva = getTextBetween(resultat, 'TVA (20%) ', 'Total TTC (en euros) ').strip()
    order_ttc = getTextBetween(resultat, 'Total TTC (en euros) ', 'En votre aimable r??glement,').strip()
    data = Order(order_address, order_reference, order_date, order_code, order_ht, order_tva, order_ttc)
    db.session.add(data)
    db.session.commit()
    return jsonify({ 
            'status': True 
        })


def get_orders() :
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
    return jsonify({ 
            'status': True 
        })






