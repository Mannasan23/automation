import cv2
import time
import dropbox

startTime = time.time()
def takeSnapshot():
    count = 0
    captureObj = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    while(result):
        read, frame = captureObj.read()
        imageName = 'img1' + str(count) + '.png'
        cv2.imwrite(imageName, frame)
        startTime = time.time()
        count = count + 1
        result = False
    return imageName
    print('Snapshot taken')
    captureObj.release()
    captureObj.destroyAllWindows()

def uploadFiles(imageName):
    accessToken = "EASJhDAwHU0AAAAAAAAAAXFxKBdJicp2O2FaYFqmK-eM5WNh21yKUDHeDm2o5WrE"
    dbx = dropbox.Dropbox(accessToken)
    fileFrom = imageName
    fileTo = '/images/' + (imageName)
    f = open(fileFrom, 'rb')
    dbx.files_upload(f.read(), fileTo, mode = dropbox.files.WriteMode.overwrite)
    print('file uploaded')

def main():
    while(True):
        if(time.time() - startTime > 5):
            name = takeSnapshot()
            uploadFiles(name)

main()