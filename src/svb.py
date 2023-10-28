import asyncio
from daraja import Mpesa

pay = Mpesa(config_file="test_config.json", env="prod")


async def runp():
    res = await pay.stk("254748467252", 20)

    print(res)

asyncio.run(runp())
