class Ready:

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def on_ready():
        print("Ready!")
