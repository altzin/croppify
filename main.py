from PIL import Image
import os

class Resizer:

    def __init__(self,pictureArray,filePath):
        self.listOfPictures = pictureArray
        self.filePath = filePath

        self.smallestPicture = self.findTemplate(self.listOfPictures)


    def findTemplate(self,pictureList):
        #returns a values for the biggest template that fits inside every picture

        current_min_x = 10000
        current_min_y = 10000

        for image in pictureList:

            currentimg = Image.open(self.filePath + "\\" + image)
            current_min_x = min(currentimg.width, current_min_x)
            current_min_y = min(currentimg.height, current_min_y)

        return (current_min_x,current_min_y)


    def resize(self,directory):

        template_x = self.smallestPicture[0]
        template_y = self.smallestPicture[1]

        #create directory to add new images to
        directory += "\\cropped"

        if not os.path.exists(directory):
            os.makedirs(directory)

        for i in range(len(self.listOfPictures)):
            currentImage = Image.open(self.filePath + "\\" + self.listOfPictures[i])

            start_x = int((currentImage.width - template_x) / 2)
            start_y = int((currentImage.height - template_y) / 2)
            # vill man flytta mallen uppåt minska detta värde^

            bbox = (start_x,start_y, (start_x + template_x), (start_y + template_y))

            cropped = currentImage.crop(bbox)
            cropped.save(directory + "\\cropped-" + self.listOfPictures[i][:-4] + ".jpg")

def main():

    while True:
        filePath = input("Give me a filepath to a set of images with varying sizes:")

        try:
            listOfPictures = [individualPic for individualPic in os.listdir(filePath)]
            break
        except Exception:
            print("Bad File")

    resizer = Resizer(listOfPictures,filePath)

    resizer.resize(filePath)

if __name__=="__main__":
    main()
