import urllib.request
import urllib.parse
import urllib
import base64
import json
import datetime

class Mpesa():
    def __init__(self, config_file: str, env: str):
        self._config_file = config_file # config_file to be a json file
        self.env = env # either prod or dev

        if self.env == "prod":
            self.API_BASE = "https://api.safaricom.co.ke"
        elif self.env == "dev":
            self.API_BASE = "https://sandbox.safaricom.co.ke"
        else:
            raise ValueError("env parameter should be 'prod' or 'dev'")

        with open(config_file, 'r') as f:
            data = json.load(f)
            self._consumerKey = data.get('consumerKey')
            self._consumerSecret = data.get('consumerSecret')
            self._passKey = data.get('passKey')
            self._shortCode = data.get('shortCode')
            self._tillNumber = data.get('tillNumber')
            self._callbackUrl = data.get('callbackUrl')
            self._transactionType = data.get('transactionType')
            self._accountRef = data.get('accountReference')
            self._transactionDesc = data.get('transactionDescription')


    async def get_auth(self):
        # Encode the consumer key and secret as base64
        base64_auth = base64.b64encode(f"{self._consumerKey}:{self._consumerSecret}".encode()).decode()

        # Create a request with Basic Authentication
        request = urllib.request.Request(f"{self.API_BASE}/oauth/v1/generate?grant_type=credentials")
        request.add_header("Authorization", f"Basic {base64_auth}")


        try:
            with urllib.request.urlopen(request) as response:
                response_data = response.read()
                data = json.loads(response_data.decode())
                print(data["access_token"])
                return data["access_token"]

        except Exception as e:
            print(e)

    @staticmethod
    async def get_time():
        utc_time = datetime.datetime.utcnow()
        ke_time = utc_time + datetime.timedelta(hours=3)
        
        return ke_time.strftime("%Y%m%d%H%M%S")

    async def _get_password(self):
        data_to_encode = f"{self._tillNumber}{self._passKey}{await self.get_time()}"
        encoded_bytes = base64.b64encode(data_to_encode.encode())
        password = encoded_bytes.decode("utf-8")

        return password

    async def stk(self, receiver: str, amount: int):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {await self.get_auth()}",
        }
        
        payload = {
            "BusinessShortCode": self._shortCode,
            "Password": await self._get_password(),
            "Timestamp": await self.get_time(),
            "TransactionType": self._transactionType,
            "Amount": amount,
            "PartyA": receiver,
            "PartyB": self._tillNumber,
            "PhoneNumber": receiver,
            "CallBackURL": self._callbackUrl,
            "AccountReference": self._accountRef,
            "TransactionDesc": self._transactionDesc,
        }

        data = urllib.parse.urlencode(payload).encode('utf-8')
        #data = json.dumps(payload).encode(
        request = urllib.request.Request(
            url="https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            headers=headers,
            method="POST",
            data=data
        )

        try:
            with urllib.request.urlopen(request) as response:
                response_data = response.read().decode("utf-8")
                response_json = json.loads(response_data)
                print("una respuesta")
                return response_json

        except Exception as e:
            print(e)
            return "An error occurred"

        
