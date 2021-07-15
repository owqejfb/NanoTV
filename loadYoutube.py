import asyncio
from time import sleep
from aiopylgtv import WebOsClient


async def runloop():
    #ex IP 192.999.0.99
    client = await WebOsClient.create("(insert your tvs IP here)")
    await client.connect()
    await client.launch_app_with_content_id(
        "youtube.leanback.v4",
        "https://www.youtube.com/watch?v=ga5Bo4YdgH4&list=PLW7FfYtQp1JjRDL11_74079-ny9CS1J4h&index=1",
    )
    #this function is here because it takes time to load youtube
    sleep(7)
    await client.button("ENTER")
    await client.disconnect()


asyncio.get_event_loop().run_until_complete(runloop())
print("DONE")
