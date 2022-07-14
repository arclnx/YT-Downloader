from pytube import YouTube

def printInfo(yt):
    title=yt.title
    streamList = yt.streams
    
    print("+-----------------------------------+")
    print("| " + title)
    print("+-----------------------------------+")
    print("Streams:")
    
    # Format stream into dictionary
    streamDict = [{streamData[0]:streamData[1] for streamData in [
        pair.split("=") for pair in str(stream)[1:-1].replace('"','').split(" ")[1:]]} for stream in streamList]
    
    print(*streamDict, sep="\n\n")
    
def prettyPrintDict(dict, columnsToPrint):
    
    # Find the maximum width of the value in the column or the column header itself
    max(
        [len(dict.get(column,"")) for column in columnsToPrint]
        + column for column in columnsToPrint)
    
    pass
    
printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo"))