from imaplib import _Authenticator
from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel
import pickle
from starlette.middleware.cors import CORSMiddleware
import numpy as np

#from io import StringIO




app = FastAPI()

app.add_middleware(

     CORSMiddleware,
     allow_origins=['*'],
     allow_methods=['*'],
     allow_headers=['*'],

)
#la methode get 
      
    
@app.get("/predict")
async def predict_(CASH_IN:Optional[float]=0.0,CASH_OUT:Optional[float]=0.0,DEBIT:Optional[float]=0.0,PAYMENT:Optional[float]=0.0,TRANSFER:Optional[float]=0.0,amount:Optional[float]=0.0,oldbalanceOrg:Optional[float]=0.0,newbalanceOrig:Optional[float]=0.0,oldbalanceDest:Optional[float]=0.0,newbalanceDest:Optional[float]=0.0):

 
     

   
    # u = np.array(u).reshape((1,-1))
    # res = loaded_model.predict(u)
    # return res

    
    fil = open("RLClassifier.sav",'rb')
    loaded_model = pickle.load(fil)
    fil.close()
    #uhugfjtyr
    u = np.array([CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER, amount , oldbalanceOrg, newbalanceOrig,oldbalanceDest,newbalanceDest])
    u = np.array(u).reshape((1,-1))
    prd =loaded_model.predict(u)
    prediction = prd[0]
    if TRANSFER==1.0:
      if amount>oldbalanceOrg:
              prediction= "la balance est insuffisant"
      if amount==0.0:
              prediction="la montant ne peut pas etre nulle"/n
      else:
            if amount< oldbalanceOrg:
                  if(newbalanceOrig!= oldbalanceOrg-amount):
                        prediction= "frauduleuse "
                  elif (newbalanceDest != oldbalanceDest+amount) :
                        prediction= " frauduleuse "
                  else:
                        prediction= "n'est pas frauduleuse "      

#     if prediction==0.0:
#           prediction = "n'est pas fraudulante" 
    
    
    
            
    if CASH_IN==1.0:
      if amount==0.0:
            prediction="la montant ne peut pas etre nulle"
      else:
            if(newbalanceOrig != amount+oldbalanceOrg):
                  prediction= "frauduleuse "
            else :
                  prediction= "n'est pas frauduleuse "

    if CASH_OUT==1.0:
      
      if amount==0.0:
              prediction="la montant ne peut etre nulle"
      else:
            if amount>oldbalanceOrg:
                  prediction= "la balance est insuffisant"
            else:
                  if (newbalanceOrig != oldbalanceOrg-amount):
                        prediction= "frauduleuse "
                  else:
                        prediction= "n'est pas frauduleuse "




      
    if PAYMENT==1:
        if(newbalanceOrig != oldbalanceOrg-amount):
               prediction= "frauduleuse "
        else :
               prediction= "n'est pas frauduleuse "
    if DEBIT==1:
         if (newbalanceOrig != oldbalanceOrg+amount):
               prediction= "frauduleuse "
         else:
             prediction= "n'est pas frauduleuse "


#     else:
#            prediction = " fraudulante" 
    a  = {}

    a["result"] = str(prediction)

    return a







    #data_in = [data['amount'],data['New_Balance_Orig'], data['Oldbalance_inacc'], data['OrigBalance_inacc'], data['DestBalance_inacc'],data['type_otheres'],data['type_transfer']]
    # prediction = loaded_model.predict([[TRANSFER,CACH_IN,CACH_OUT,DEBIT,PAYMENT,amount,oldBalanceOrig,newBalanceOrig,OldbalanceDest,newbalanceDest]])
    
    # #probability = loaded_model.predict_proba(data_in).max()
#     if amount==0:
#         return "amount can't be a null"
#     if TRANSFER:
#         if amount>oldBalanceOrig:
#             return "la balance est insuffisant"
#         elif amount<= oldBalanceOrig:
#             newBalanceOrig= oldBalanceOrig-amount
#             newbalanceDest=OldbalanceDest+amount
#             return 'Not a Fraude '
#         elif newbalanceDest!=OldbalanceDest+amount:
#             return 'exists a fraude'
    # if CACH_IN:
    #     newBalanceOrig=amount+oldBalanceOrig
    # if CACH_OUT:
    #     if amount>oldBalanceOrig:
    #         return "amount est insuffisant"
    #     else:
    #         newBalanceOrig=oldBalanceOrig-amount
    # if PAYMENT:
    #     if amount>oldBalanceOrig:
    #         return "amount est insuffisant"
    #     else:
    #         newBalanceOrig=oldBalanceOrig-amount
    #         newbalanceDest=OldbalanceDest+amount

    # if DEBIT:
    #     if amount>oldBalanceOrig:
    #         return "amount insuffisant"
    #     else:
    #         newBalanceOrig=oldBalanceOrig-amount

    

        
        
       
   