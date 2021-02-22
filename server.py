from nltk.parse.corenlp import CoreNLPServer
import os

STANFORD = "stanford-corenlp-4.2.0"

# Create the server
server = CoreNLPServer(
    path_to_jar= os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"),
    #os.path.join(STANFORD, "stanford-corenlp-4.2.0-models.jar"),
    port=9000
)

# Start the server in the background
server.start()
while True:
    resp = input("Press q to exit \n")
    if resp == "q":
        break
server.stop()
