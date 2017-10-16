from PIL import Image
import os
import filehandler

#C:\Users\altzi\Desktop\testmapp\profilbilder

class Resizer:

    def __init__(self,pictureArray):
        self.listOfPictures = pictureArray
        self.smallestPicture = self.findTemplate(self.listOfPictures)
        self.filepath = ""

    def findTemplate(self,pictureList):
        #returns a values for the biggest template that fits inside every picture

        current_min_x = 10000
        current_min_y = 10000

        for image in pictureList:
            currentimg = Image.open(image)
            current_min_x = min(currentimg.width, current_min_x)
            current_min_y = min(currentimg.height, current_min_y)

        return (current_min_x,current_min_y)


    def resize(self,directory):

        template_x = self.smallestPicture[0]
        template_y = self.smallestPicture[1]

        #create directory to add new images to
        directory += "\\cropped"

        lengthOfPath = len(directory)

        if not os.path.exists(directory):
            os.makedirs(directory)

        for i in range(len(self.listOfPictures)):
            currentImage = Image.open(self.listOfPictures[i])

            start_x = int((currentImage.width - template_x) / 2)
            start_y = int((currentImage.height - template_y) / 2)

            cropped = currentImage.crop((start_x,start_y,start_x + template_x,start_y + template_y))
            print(start_x, start_y, template_x, template_y)
            cropped.save(directory+"\\" + str(i) +".jpg")

def main():
    #ANVÄNDA THUMBNAIL FRÅN IMAGE.PIL?

    while True:
        print("Give me a filepath to a set of images with varying sizes:")
        try:
            filePath = input()

            imagesFromFile = [filePath + "\\" + individualPic for individualPic in os.listdir(filePath)]
            break
        except Exception:
            print("Bad File")

    listOfPictures = imagesFromFile

    resizer = Resizer(listOfPictures)


    resizer.resize(filePath)





if __name__=="__main__":
    main()
