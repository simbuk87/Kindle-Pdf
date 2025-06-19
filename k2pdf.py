import time
import pyautogui
import shutil
import os
from PIL import ImageGrab
from fpdf import FPDF
from PyPDF2 import PdfMerger
from PIL import Image
finalBookname = input('Enter name of book: ')

bookname = 'bookscreenshots'
try:
    shutil.rmtree(bookname)
except FileNotFoundError:
    print("folder not present")
os.mkdir(bookname)
path = os.path.dirname(__file__)+'/'+bookname+'/'
print('start taking screenshots in 15 sec')
time.sleep(7)
i = 1
print('\a')
while (1):
    #myScreenshot = pyautogui.screenshot()
    myScreenshot = ImageGrab.grab()
    myScreenshot.save(path+"screenshot_"+str(format(i, '05d'))+'.png')

    if i > 1:
        if open(path+"screenshot_"+str(format(i, '05d'))+'.png', "rb").read() == open(path+"screenshot_"+str(format(i-1, '05d'))+'.png', "rb").read():
            print('\a')
            stop = input('enter 0 if book finished or just press enter: ')
            if stop == '0':
                os.remove(path+"screenshot_"+str(format(i, '05d'))+'.png')
                print('\a')
                print('reached to the end of book')
                break
            else:
                print('resuming taking screenshots in 5 sec')
                pyautogui.press('alt'+'tab')
                time.sleep(3)
                continue
    pyautogui.press('right')
    time.sleep(1)  # Adjust the delay as needed
    i = i+1
totalpages = i+0
print('\a')
print(f'{"Total Number Pages Captured was :"}{totalpages-1}')

##### Converting images for pdf creation

path = os.path.dirname(__file__)

screenshotpath = path+'/bookscreenshots/'
screenshotpdfpath = path+'/screenshot_pdfs/'

try:
    shutil.rmtree('screenshot_pdfs')
except FileNotFoundError:
    print("folder not present")
os.mkdir('screenshot_pdfs')
onlyfiles = next(os.walk(screenshotpath))[2]

pdf = FPDF()
pdf.add_page('L')

for i in range(1, len(onlyfiles)+1):

# Opens a image in RGB mode
    image1 = Image.open(screenshotpath+"screenshot_"+str(format(i, '05d'))+'.png')
    im = image1.convert('RGB')
    
# Size of the image in pixels (size of original image)
# (This is not mandatory)

    width, height = im.size

# Setting the points for cropped image
    left = 480
    top = 0
    right = 1440
    bottom = 1080
    
# Cropped image of above dimension
# (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    
    im1.save(path+'/screenshot_pdfs/'+"screenshot_"+str(format(i, '05d'))+'.png')
    
    pdf.image(screenshotpdfpath+"screenshot_"+str(format(i, '05d'))+'.png')
#    pdf.image(screenshotpdfpath+"screenshot_"+str(format(i, '05d'))+'.png', x=-40, y=0, w=375)
    pdf.add_page('L')

pdf.output(finalBookname+".pdf")
    # im1 = image1.convert('RGB')
    # im1.save(path+'/screenshot_pdfs/'+str(format(i, '05d'))+'.pdf')

# merging pdf
# pdfs = []
# for i in range(1, len(onlyfiles)+1):
    # pdfs.append(str(format(i, '05d'))+'.pdf')
# merger = PdfMerger()
# for pdf in pdfs:
    # merger.append(path+'/screenshot_pdfs/'+pdf)
# merger.write(finalBookname+".pdf")
# merger.close()
print('\a')
print('pdf of book created with name '+finalBookname+'.pdf')

# Remove the created Directories 
# try:
    # shutil.rmtree(screenshotpath)
    # print("Directory '% s' has been removed successfully" % screenshotpath)
# except OSError as error:
    # print(error)
    # print("Directory '% s' can not be removed" % screenshotpath)

# try:
    # shutil.rmtree(screenshotpdfpath)
    # print("Directory '% s' has been removed successfully" % screenshotpdfpath)
# except OSError as error:
    # print(error)
    # print("Directory '% s' can not be removed" % screenshotpdfpath)
    
# if the specified path
# is not an empty directory
# then permission error will
# be raised
