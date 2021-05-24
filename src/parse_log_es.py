import os
import re
import sys

outputDir = ""
filenamePrefix = ""

lastReqNum = 0
lastRespNum = 0
# Account for out-of-order 'resp' lines due to multiple requests sent at same time.
#   req1, req2, resp1, resp2    - req2 sent before previous resp came back
#   req1, req2, resp2, resp1    - resp1 received after a later req's resp came back
lastReqNumForThread = {}
lastRespNumForThread = {}


def writeFile(filename, str):
    filepath = f'{outputDir}/{filename}'
    with open(filepath, "w") as fp:
        fp.write(str)


def parseReq(lineNum, line, timestamp, thread, type):
    global lastReqNum, lastRespNum, lastReqNumForThread, lastRespNumForThread
    lastReqNum += 1
    lastReqNumForThread[thread] = lastReqNum
    extra = ""
    if lastReqNum >= (lastRespNum + 2):
        extra = f" - req sent before previous resp came back"

    # Get the actual request Javascript object
    filename = "## ERROR ##"
    n = line.find("SearchRequest{")
    if n != -1:
        reqJS = line[n + len("SearchRequest{") - 1 :]
        filename = f"{filenamePrefix}_{lastReqNumForThread[thread]:03d}-req.js"
        writeFile(filename, reqJS)

    print(
        f"{lineNum}: {timestamp} - {thread} - {type} \t {lastReqNumForThread[thread]} ({filename})"
        + f"{extra}"
    )


def parseResp(lineNum, line, timestamp, thread, type):
    global lastReqNum, lastRespNum, lastReqNumForThread, lastRespNumForThread
    lastRespNum += 1
    lastRespNumForThread[thread] = lastReqNumForThread[thread]
    extra = ""
    if lastRespNumForThread[thread] < lastRespNum:
        extra = f" - resp received after a later req's resp came back"

    # Get the actual response JSON object
    filename = "## ERROR ##"
    n = line.find("Elastic Search Response:")
    if n != -1:
        respJSON = line[n + len("Elastic Search Response:") + 1 :]
        filename = f"{filenamePrefix}_{lastRespNumForThread[thread]:03d}-resp.json"
        writeFile(filename, respJSON)

    print(
        f"{lineNum}: {timestamp} - {thread} - {type} \t {lastRespNumForThread[thread]} ({filename})"
        + f"{extra}"
    )


def parseLine(lineNum, line):
    lineNum = f"{lineNum:2n}"
    n1stSpace = line.find(" ")
    n2ndSPace = line.find(" ", n1stSpace + 1)
    timestamp = line[:n1stSpace]
    thread = line[n1stSpace + 1 : n2ndSPace]

    if line.find("SearchRequest{searchType=QUERY_THEN_FETCH") != -1:
        type = "req"
    elif line.find("Elastic Search Response:") != -1:
        type = "resp"
    elif (
        line.find("For tenant jama_db_pete01, query request using") != -1
        and line.find("For tenant jama_db_pete01, query request using") != -1
    ):
        type = "header"
    else:
        type = "UNKOWN"

    if type == "req":
        parseReq(lineNum, line, timestamp, thread, type)
    elif type == "resp":
        parseResp(lineNum, line, timestamp, thread, type)
    else:
        print(f"{lineNum}: {timestamp} - {thread} - {type}")


def parseFile(filePath):
    global outputDir, filenamePrefix
    outputDir = os.path.dirname(filePath)
    filenamePrefix = os.path.basename(filePath.rsplit('.', 1)[0])
    print(f"\nParsing log:")
    print(f"     Input log: {filePath}")
    print(f"     Output directory: {outputDir}")
    lineNum = 0
    with open(filePath) as fp:
        for line in fp:
            lineNum += 1
            parseLine(lineNum, line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\nERROR: Require 1 argument: path to log file to parse\n")
        sys.exit()

    filePath = sys.argv[1]
    parseFile(filePath)

    print()
