import cv2
import time
import random
import dropbox

startTime = time.time()

def take_snapshot():
    rand = random.randint(1, 1000000)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        print(ret)
        img_name = "img"+str(rand)+".png"
        cv2.imwrite(img_name, frame)
        startTime = time.time()
        result = False
    return(img_name)
    print("Snapshot Taken. File name is " + img_name)
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'OgTQw6cs2QcAAAAAAAAAAQzJXCPbcAV6gnWbO-83_A_4hb-ANP53LhNAkKWevbOP'
    file_from = img_name
    file_to = "/DontLookAtMyPCImWatchingU/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded to dropbox.")

def main():
    while(True):
        if(time.time()-startTime>=300):
            name = take_snapshot()
            upload_file(name)

main()