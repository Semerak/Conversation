from nltk.parse.corenlp import CoreNLPServer
import os

STANFORD = "stanford-corenlp-4.2.0"

# Create the server
try:
    server = CoreNLPServer(
        path_to_jar=os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"),
    )
    server.start()

except:
    server = CoreNLPServer(
        path_to_jar=os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"),
        path_to_models_jar=os.path.join(STANFORD, "stanford-corenlp-4.2.0-models.jar")

    )
    server.start()


while True:
    resp = input("Press q to exit \n")
    if resp == "q":
        break
server.stop()
