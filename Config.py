import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6402487390:AAFtyJ1Im1YMd6y23gJ0m0FZuG4_P2vO2Rk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBu7069MtLetWqI13PM-vE74gQiw6gZ8OnXXttg5O8Eo3QPNhPD7QDUybYLqooNwsdCNZKMQyNnBYX5O-g2t0I8ELn-5IySajPSoGYrS1fuqyBemtrzFs0yOy6icxGgCjWGI3pdWEyLQeiRF3V67cHsgH2coPbDGpvgePqQNxw98PCQNF1aXdV9rhLI-vkcVt0nHS3ZTjVYYBfQGYdVvwgwhHCbIaA7hd46e2XMosIfV5_W7OHGWVKxQ7bXOtgYouQQn9ePSe8nIb-QCHncnXCRWa0SSH72-uXTSk1dSqRhJA34AmuZm-gQSuKS7vRbzYV_4M4yGjr49uq3XlMCBs_rAk="

)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", )
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Best_Friend_Forever_Music_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
