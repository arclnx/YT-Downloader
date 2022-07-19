from pyparsing import col
from pytube import YouTube

def getInfo(url):
    yt = YouTube(url)
    title=yt.title
    streamList = yt.streams
    
    print("+-----------------------------------+")
    print("| " + title)
    print("+-----------------------------------+")
    
    # Format stream into dictionary
    streamDictList = [{streamData[0]:streamData[1] for streamData in [
        pair.split("=") for pair in str(stream)[1:-1].replace('"','').split(" ")[1:]]} for stream in streamList]
    
    return streamDictList
    
def prettyPrintStreams(url, columnsToPrint):
    
    # Get YouTube video information
    yt = YouTube(url)

    streamList = yt.streams

    # Create a list of streams, each one a dict
    dictList = [{streamData[0]:streamData[1] for streamData in [
        pair.split("=") for pair in str(stream)[1:-1].replace('"','').split(" ")[1:]]} for stream in streamList]
    
    
    # Find the maximum width of the value in the column or the column header itself
    columnWidths = {column:max([len(dictList[row].get(column,"")) for row in range(len(dictList))]+[len(column)]) for column in columnsToPrint}
    
    # Print the video details
    title = yt.title
    author = yt.author
    length = str(yt.seconds//3600).zfill(2) + ":" + str(yt.seconds%3600//60).zfill(2) + ":" + str(yt.seconds%3600%60)
    
    # Print the header of the table
    topHeader = "┌" + "┬".join(["─"*(columnWidths[column]+2) for column in columnsToPrint]) + "┐"
    midHeader = "│" + "│".join([column.center(columnWidths[column]+2) for column in columnsToPrint]) + "│"
    print(topHeader)
    print(midHeader)
    
    # Print the data of the table
    for row in dictList:
        topDivider = "├" + "┼".join(["─"*(columnWidths[column]+2) for column in columnsToPrint]) + "┤"
        data = "│" + "│".join([" "+row.get(column,"").ljust(columnWidths[column]+1) for column in columnsToPrint]) + "│"
        print(topDivider)
        print(data)

    # Print the bottom of the table
    bottom = "└" + "┴".join(["─"*(columnWidths[column]+2) for column in columnsToPrint]) + "┘"
    print(bottom)


prettyPrintStreams("https://www.youtube.com/watch?v=2lAe1cqCOXo", ["itag","type","res","fps","abr","vcodec","acodec"])