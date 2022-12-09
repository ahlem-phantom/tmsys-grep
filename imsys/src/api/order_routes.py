from flask import Blueprint ,jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from flask import request
from ..services.order_service import create_order, get_orders
from src.app import db
from src.models import Order
import cv2
import os
import pytesseract
from datetime import datetime

order_api = Blueprint('order', __name__)
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

@order_api.route('/add-order', methods=['POST'])
def addOrder():
    data = request.json
    return create_order(data)

@order_api.route('/save-order', methods=['GET'])
def saveOrder():
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    image_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'uploads', 'Facture_1.jpg'))
    image = cv2.imread(image_dir, cv2.IMREAD_COLOR)
    #Data After OCR Extraction
    resultat = pytesseract.image_to_string(image)
    #Ordering Data
    order_address = getTextBetween(resultat, 'www.blueprism.com/fr', 'Référence').strip()
    order_reference = getTextBetween(resultat, 'Référence: ', 'Date: ').strip()
    order_date = datetime.strptime(getTextBetween(resultat, 'Date: ', 'Client:').strip(),'%d/%m/%Y')
    order_code = getTextBetween(resultat, 'Client: ', 'Intitulé: ').strip()
    order_ht = getTextBetween(resultat, 'Total HT ', 'TVA (20%) ').strip()
    order_tva = getTextBetween(resultat, 'TVA (20%) ', 'Total TTC (en euros) ').strip()
    order_ttc = getTextBetween(resultat, 'Total TTC (en euros) ', 'En votre aimable réglement,').strip()
    data = Order(order_address, order_reference, order_date, order_code, order_ht, order_tva, order_ttc)
    db.session.add(data)
    db.session.commit()
    return jsonify({ 
            'status': True 
        })

@order_api.route('/get-order', methods=['GET'])
def getOrder():
    return get_orders()