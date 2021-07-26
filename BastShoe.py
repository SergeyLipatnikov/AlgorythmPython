class BastSHoes:
    __count = 0
    __Final_Operations = ['']
    __lastOperation = 0
    __tempString = ''

    def check_command(self, command):

        if (command[0] != '[1-5]'):

            return BastSHoes.__tempString

        elif (int(command[0]) == 1 or int(command[0]) == 2) and (BastSHoes.__lastOperation == 4 or BastSHoes.__lastOperation == 5):

            temp = BastSHoes.__tempString

            BastSHoes.__count = 0

            BastSHoes.__Final_Operations.clear()

            BastSHoes.__Final_Operations.append(temp)

        if int(command[0]) == 1:

            return self.append_string(command[2:])

        elif int(command[0]) == 2:

            return self.remove_symbols(command[2:])

        elif int(command[0]) == 3:

            return self.index_symbol(command[2:])
        
        elif int(command[0]) == 4:

            return self.Undo()

        elif int(command[0]) == 5:

            return self.Redo()


    def append_string(self,S):

        BastSHoes.__tempString = BastSHoes.__tempString + S

        self.__Final_Operations.append(self.__tempString)

        BastSHoes.__count += 1

        BastSHoes.__lastOperation = 1

        return self.__Final_Operations[len(BastSHoes.__Final_Operations)-1]

    def remove_symbols(self,Symbols):

        N = int(Symbols)

        lenght = len(BastSHoes.__tempString)

        if N < lenght:

            self.__Final_Operations.append(BastSHoes.__tempString[0:lenght - N])

        else:

            self.__Final_Operations.append('')

        BastSHoes.__count += 1

        BastSHoes.__lastOperation = 2

        BastSHoes.__tempString = self.__Final_Operations[len(BastSHoes.__Final_Operations)-1]

        return self.__Final_Operations[len(BastSHoes.__Final_Operations)-1]
    
    def index_symbol(self,i):

        if int(i) < len(BastSHoes.__tempString):

            return BastSHoes.__tempString[int(i)]

        else:

            return ''

    def Undo(self):

        BastSHoes.__count -= 1

        if BastSHoes.__count < 0:

            BastSHoes.__count = 0

        BastSHoes.__lastOperation = 4

        BastSHoes.__tempString = self.__Final_Operations[BastSHoes.__count]

        return self.__Final_Operations[BastSHoes.__count]

    def Redo(self):

        BastSHoes.__count += 1

        if BastSHoes.__count > len(BastSHoes.__Final_Operations)-1:

            BastSHoes.__count = len(BastSHoes.__Final_Operations) - 1

        BastSHoes.__lastOperation = 5

        BastSHoes.__tempString = self.__Final_Operations[BastSHoes.__count]

        return self.__Final_Operations[BastSHoes.__count]


def BastShoe(command):

    String = BastSHoes()

    return String.check_command(command)