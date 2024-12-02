class FileReading:

    def __init__(self):
        print("only Constructor !!!")
    def fileReading(self):

        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731635215.695829.txt","r") as file:
            c = file.read()
            # print(c)
        
    def fileReadingLineByLine(self):
        count = 0
        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731635215.695829.txt","r") as file:
            for line in file:
                print(line.strip)
                if(line.__contains__("server")):
                    count = count +1
        # print(count)

    def readingSpecificLine(self):
        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731635215.695829.txt","r") as file:
            line = file.readlines()
            # print(line[0])
        
    def writeToFile(self):
        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731635215.695829.txt","w") as file:
            line = file.write("Writing to a file from python")
            # print(line) 
    
    def appendLinesToList(self):
        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731674948.9562578.txt","r") as file:
            lines = [line.strip() for line in file]
        
        print(lines)
    
    def retunLineNumberWhereStringAppear(self):
        line_numbers = []
        with open ("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731674948.9562578.txt","r") as file:
            for line_number, line in enumerate(file, start=1):
                if  "server" in line:
                    line_numbers.append(line_number)
        return line_numbers

    def lineNumberofString(self):
        with open("C:\\Users\\SanjeevaKumarGeejula\\Downloads\\Teams1\\Teams\\Sikuli_java_stdout_1731674948.9562578.txt","r") as file:
            l_list = []
            for line in file:
                if line.__contains__("server"):
                    l_list.append(line)
        print(l_list)



   


fr = FileReading()
# print(fr.fileReading())

# print(fr.fileReadingLineByLine())
# print(fr.readingSpecificLine())
# print(fr.writeToFile())
# print(fr.appendLinesToList())
# print(fr.retunLineNumberWhereStringAppear())
# print(fr.lineNumberofString())