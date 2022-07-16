from pyparsing import col
from pytube import YouTube

def printInfo(yt):
    title=yt.title
    streamList = yt.streams
    
    print("+-----------------------------------+")
    print("| " + title)
    print("+-----------------------------------+")
    print("Streams:")
    
    # Format stream into dictionary
    streamDictList = [{streamData[0]:streamData[1] for streamData in [
        pair.split("=") for pair in str(stream)[1:-1].replace('"','').split(" ")[1:]]} for stream in streamList]
    
    return streamDictList
    
def prettyPrintDictList(dictList, columnsToPrint):
    
    
    # Find the maximum width of the value in the column or the column header itself
    columnWidths = {column:max([len(dictList[row].get(column,"")) for row in range(len(dictList))]+[len(column)]) for column in columnsToPrint}
    columnWidths = columnWidths
    print(columnWidths)
    
    # Print the header of the table
    topHeader = "┌" + "┬".join(["─"*(columnWidths[column]+2) for column in columnsToPrint]) + "┐"
    midHeader = "│" + "│".join([column.center(columnWidths[column]+2) for column in columnsToPrint]) + "│"
    print(topHeader)
    print(midHeader)
    
    # Print the data of the table
    for row in dictList:
        topDivider = "├" + "┼".join(["─"*(columnWidths[column]+2) for column in columnsToPrint]) + "┤"
        data = "│" + "│".join(" "+[row[column].ljust(columnWidths[column]+1) for column in columnsToPrint]) + "│"
        print(topDivider)
        print(data)





print(*printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo")), sep="\n\n")
print("\n\n\n\n\n")
prettyPrintDictList(printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo")), ["itag","type","res"])