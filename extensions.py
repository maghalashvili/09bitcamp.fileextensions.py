

# #Informs user about the extension of their file

# fileformat = input("Fila name: ").lower()
# filetype = fileformat[fileformat.find("."):]
# match filetype:
#     case ".gif":
#         print("image/gif")
#     case ".jpg" | ".jpeg":
#         print("image/jpeg")
#     case ".png":
#         print("image/png")
#     case ".pdf":
#         print("application/pdf")
#     case ".txt":
#         print("text/plain")
#     case ".zip":
#         print("application/zip")
        
        #//      
        
extensions = {
    "gif" : "image",
    "jpg" : "image",
    "jpeg" : "image",
    "png" : "image",
    "pdf" : "application",
    "txt" : "text",
    "zip" : "file"
}

file = input("File name:").replace(" ", "").split("-")

if len(file) == 1:
    print(f"application/{file[0]}")
else:
    print(f"{extensions[file[1]]}/{file[1]}")