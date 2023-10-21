import unittest
import asyncio
import datetime
from daraja import mpesa


class TestMpesaClass(unittest.TestCase):
    def setUp(self): # initialize the class instance
        self.instance = mpesa.Mpesa(config_file="test_config.json", env="dev")

    def tearDown(self):
        del self.instance # clean up the instance

    def test_init(self):
        self.assertEqual(self.instance.env, "dev")

    def test_get_time(self):
        async def run_test():
            test_ke_time = datetime.datetime.utcnow() + \
                datetime.timedelta(hours=3)
            
            test_ke_fmt_time = test_ke_time.strftime("%Y%m%d%H%M%S")
            
            ke_time = await self.instance.get_time()
            self.assertEqual(test_ke_fmt_time, ke_time)

        asyncio.run(run_test())


    def test_get_password(self):
        async def run_test():
            psswd = await self.instance._get_password()
            self.assertTrue(psswd)

        asyncio.run(run_test())

    def test_stk(self):
        async def run_test():
            billing_receiver = "254791500264"
            amount = 50
            
            response = await self.instance.stk(billing_receiver, amount)
            #self.assertIn("ResponseCode", response)
            self.assertTrue(response)

        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
