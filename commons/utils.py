from ..config.Config import Config

x = Config._json()

print(x["mongodb"]["clusters"])
# for item in x["mongodb"]["clusters"]:
#     pass