"""
-> Made by Krypton#6788.
-> Please give credit :)
"""
import os, sys, aiohttp, asyncio, time

class WebhookSpammer:

    def __init__(self, webhook: str, msg: str, tasks: int):
        self.clear = lambda: os.system("cls; clear")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"}
        self.webhook = webhook
        self.payload = {"content": msg}
        self.tasks = tasks

    async def webhook_spammer(self, session, webhook, amount):
       while True:
           async with session.post(webhook, json=self.payload) as s:
              if s.status in (200, 201, 204):
                  sys.stdout.write(f"-> Sent webhook to channel with {amount} tasks in its payload.\n\n")
              else:
                  json = await s.json()
                  sys.stdout.write(f"-> Error sending webhook with {amount} tasks in its payload.\n-> Message: {json['message']}\n-> Retry After: {json['retry_after']}\n\n")
  
    async def start(self):
        self.clear()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for amount in range(self.tasks):
                tasks.append(asyncio.create_task(self.webhook_spammer(session, self.webhook, amount)))
            await asyncio.gather(*tasks)
            tasks.clear()

if __name__ == "__main__":
    try:
        client = WebhookSpammer(
        webhook = input("-> Webhook URL?: "),
        msg = input("-> Message Content?: "),
        tasks = int(input("-> Tasks?: "))
        )
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(client.start())
        finish_time = round((time.time() - start_time), 4)
        sys.stdout.write(f"-> Finished executing webhook.\n-> Finished in {finish_time}s.")
    except Exception as error:
        sys.stdout.write(f"-> Event loop has ended or you are being ratelimited or was given invalid roles.\n-> Exception: {error}.\n-> Press enter to exit.\n")
        input("-> ")
        os._exit(0)
