from time import ctime as current_time

##list of help commands
HELP_COMMANDS = ['help', 'h']

##list of end program commands
QUIT_COMMANDS = ['q', 'quit']

##command to show all logs
SHOW_COMMAND = 'showlogs'

##Program state
IS_RUNNING = True

##initialize variables globally
CUSTOMER_NAME = PRODUCT_NAME = TIME_OF_PURCHASE = QTY = PRICE = TOTAL_COST = None

##the logs file path
LOGS_FILEPATH = 'logs.txt'

def trim(var):
    '''to strip newlines and spaces from a string'''
    return var.strip()

def getInput():
    '''to get valid status of input and input itself'''

    #the global variibles used
    global IS_RUNNING
    
    try:
        ##this is the input prompt to the user
        prompt = 'Type info here: '

        ##collcet info from user and assigns to respective vars
        info = input(prompt)

        #if the input is an help command
        if info.lower() in HELP_COMMANDS:
            displayHelpMessage()
            return False, None
        
        #if the input is a quit command
        if info.lower() in QUIT_COMMANDS:
            IS_RUNNING = False
            return True, None

        #if the input is a display logs command
        if info.lower() == SHOW_COMMAND:
            showLogs()
            return False, None

        #split the input to get transaction info
        info = info.split(',')
        if len(info) != 4:
            displayErrorMessage()
            return False, None
        
        return True, info

    except Exception as e:
        displayErrorMessage()
        return False, None

def displayErrorMessage():
    '''display an error message for invalid input'''
    print('Invalid Input!!!\n')
    
def displayHelpMessage():
    '''display the helper message'''
    print('Here are the working commands')
    print('-----------------------------')
    print('showLogs: to see all registered information')
    print('help [or h,]: to see the help message')
    print('Custormer Name, Product Name, Quantity, PRICE: seperated by commas to register information')
    print('quit [or q,]: to end the program')
    print()

def getUserInput():
    '''get a valid transaction input from user'''
    status = False
    while status == False:
        status, info = getInput()
    return info

def showLogs():
    '''shows trasaction logs'''
    if QTY is None:
        print('Empty Logs!\n')

    else:
        print('{:<20s} {:<15s} {:<10s} {:<10s} {:<10s} {:<10s}'.format(
                'Customer\'s Name', 'Product Name', 'QTY', 'PRICE', 'Total Cost', 'Time'
                )
            )    
        print('{:<20s} {:<15s} {:<10.2f} {:<10.2f} {:<10.2f} {:<10s}\n'.format(
                CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE, TOTAL_COST, TIME_OF_PURCHASE
                )
            )

def prepareLogs():
    '''prepare the logs file'''
    file_object = open(LOGS_FILEPATH, 'a')
    print('{}\n{:<20s} {:<15s} {:<10s} {:<10s} {:<13s} {:^25s}\n{}'.format(
          '-'*100, 'Customer\'s Name', 'Product Name', 'QTY', 'PRICE', 'Total Cost', 'Time', '-'*100),
          file=file_object)
    file_object.close()
    
def saveLog():
    '''save the log to a file'''
    file_object = open(LOGS_FILEPATH, 'a')
    print('{:<20s} {:<15s} {:<10.2f} {:<10.2f} {:<13.2f} {:^25s}'.format(
            CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE, TOTAL_COST, TIME_OF_PURCHASE),
            file=file_object)
    file_object.close()
    
def main():
    '''the main/entry point of the program'''

    #the global variables
    global CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE, TOTAL_COST, TIME_OF_PURCHASE 

    #shows how to use program
    displayHelpMessage()

    #prepare logs file
    prepareLogs()
    
    while True:
        #collects the necessary input
        info = getUserInput()
        
        if IS_RUNNING == False:
            print('Program is Shutting down...')
            print('Program Shut down Sucessfully!')
            break
        
        ##trim var spaces
        CUSTOMER_NAME, PRODUCT_NAME, QTY, PRICE = list(map(trim, info))
        
        ##cast to number
        PRICE = float(PRICE)
        QTY = float(QTY)

        ##the total cost of purchase
        TOTAL_COST = PRICE * QTY

        ##time of purchase
        TIME_OF_PURCHASE = current_time()

        #saves log of the new transaction
        saveLog();
        
if __name__ == '__main__':
    main()
