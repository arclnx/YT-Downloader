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
    
    return streamDict
    
def prettyPrintDict(dict, columnsToPrint):
    
    # Find the maximum width of the value in the column or the column header itself
    columnWidths = 
    
    return columnWidths
    
print(*printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo")), sep="\n\n")
print("\n\n\n\n\n")
print(prettyPrintDict(printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo")), "itag"))