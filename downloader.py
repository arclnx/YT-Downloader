from pytube import YouTube

def printInfo(yt):
    title=yt.title
    streamList = yt.streams
    
    print("+-----------------------------------+")
    print("| " + title)
    print("+-----------------------------------+")
    print("Streams:")
    print(yt.streams[0] , sep="\n")
    
printInfo(YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo"))