
import csv
class excel99:
    def latestvalues(self):
        results = []
        with open('C:\\Users\\1023816\\Downloads\\modified-code-master\\csvfile\\new.csv') as File:
            reader = csv.DictReader('consessionnum')
            for row in reader:
                results.append(row)
        print(results)
    def writingdata(self,carddata):
        myData = [carddata]

        myFile = open('C:\\Users\\murali\\PycharmProjects\\untitled\\utilites2\\tracking.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            for wr in writer:
              writer.writerows(myData)


        print("Writing complete")


