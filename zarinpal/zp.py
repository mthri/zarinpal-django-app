from zeep import Client 

class Zarinpal():
    

    WSDL = 'https://www.zarinpal.com/pg/services/WebGate/wsdl'
    WEB_GATE = 'https://www.zarinpal.com/pg/StartPay/'
    MERCHANT_ID: str
    CALLBACK_URL: str
    
    __zarinpal_client: Client 

    def __init__(self, merchant_id:str, callback_url: str, wsdl_address: str = None, sandbox = False):

        # if you want to use a diffrent WSDL address
        if wsdl_address is not None:
            self.WSDL = wsdl_address

        # if you want to test your payment gate | fake paid 
        if sandbox:
            self.WSDL = 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl'
            self.WEB_GATE = 'https://sandbox.zarinpal.com/pg/StartPay/'

        self.MERCHANT_ID = merchant_id
        self.CALLBACK_URL = callback_url
        self.__zarinpal_client = Client(self.WSDL)

    def payment_request(self, amount: int, description: str, 
                        email: str = None, mobile: str = None ) -> str :

        # try to get a Reference ID
        result = self.__zarinpal_client.service.PaymentRequest(self.MERCHANT_ID,
                                                               amount,
                                                               description,
                                                               email,
                                                               mobile,
                                                               self.CALLBACK_URL)
        # 100 means success
        if result.Status == 100:
            # convert to int and save value to self.authority
            self.authority = int(result.Authority)
            return self.WEB_GATE + str(self.authority) 
        else:
            self.__error_generator(result.Status)

    def payment_verification(self, amount: int, authority: str) -> tuple:
        result = self.__zarinpal_client.service.PaymentVerification(self.MERCHANT_ID,
                                                                    authority,
                                                                    amount)
        
        if result.Status == 100:
            return 100, 'Transaction success', result.RefID
        elif result.Status == 101:
            return 101, 'Transaction submitted', None
        else:
            self.__error_generator(result.Status)

    def __error_generator(self, status_number:int):
        if status_number == -1:
            raise ZarinpalError('Information submitted is incomplete.')
        elif status_number == -2:
            raise ZarinpalError('Merchant ID or Acceptor IP is not correct.')
        elif status_number == -3:
            raise ZarinpalError('Amount should be above 100 Toman.')
        elif status_number == -4:
            raise ZarinpalError('Approved level of Acceptor is Lower than the silver.')
        elif status_number == -11:
            raise ZarinpalError('Request Not found.')
        elif status_number == -21:
            raise ZarinpalError('Financial operations for this transaction was not found.')
        elif status_number == -22:
            raise ZarinpalError('Transaction is unsuccessful.')
        elif status_number == -33:
            raise ZarinpalError('Transaction amount does not match the amount paid.')
        elif status_number == -34:
           raise ZarinpalError('Limit the number of transactions or number has crossed the divide')
        elif status_number == -40:
           raise ZarinpalError('There is no access to the method.')
        elif status_number == -41:
           raise ZarinpalError('Additional Data related to information submitted is invalid.')
        elif status_number == -54:
           raise ZarinpalError('Request archived.')
        # elif status_number == -101:
        #    raise ZarinpalError('Operation was successful but PaymentVerification \
        #         operation on this transaction have already been done')
        else:
            raise ZarinpalError(f'Un Handled error {status_number}')

# generate specific error for zarinpal
class ZarinpalError(Exception):
    pass