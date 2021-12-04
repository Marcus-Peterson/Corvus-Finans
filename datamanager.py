import csv
import datetime
class Data:
    #Display undordered data from a csv file
    @classmethod
    def data_display(cls,filename):
        while True:
            try:
                with open(filename) as file:
                    print(file)
                    break
            except ValueError:
                print("Wrong datatype for file, try again")
            except FileNotFoundError:
                print("File couldn't be located, try again")
            except FileExistsError:
                print("File doesn't exist, try again or create a new file")
    
     
class Trades_Data():
    
    @staticmethod                       #This method is not supposed to be used outside of class
    def close_data_file(cls,file):
        try:
            with filename as csv_file:
                csv_file.close()
        except Exception:
            print("Error occured when trying to close file")
            

    @classmethod
    def amt_winnings(cls,filename):         #Enabling user to display winnings according to time periods
        try:
            with open(filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
            
                for line in csv_reader:
                    if line[1] < line[3]:
                        continue
                    else:
                        print("Your winnings:")
                        print(line)
            user_request = input("Do you want to close the file")
            if user_request == "yes":
                Trades_Data.close_data_file(csv_reader)
        except FileExistsError:
            print("File doesn't exists")
        except FileNotFoundError:
            print("Could not locate file")
        except ValueError:
            print("Wrong datatype")

    @classmethod
    def amt_losses(cls,filename):
        try:
            with open(filename,"r") as csv_file:
                csv_reader = csv.reader(csv_file)

                for line in csv_reader:
                    if line[1] > line[3]:
                        continue
                    else:
                        print("Your losses")
                        print(line) 
        except FileExistsError:
            print("File doesn't exists")
        except FileNotFoundError:
            print("Could not locate file")
        except ValueError:
            print("Wrong datatype")
        

    @classmethod
    def winnings_periods(cls,filename):
        
        try:
            with open(filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                user_request = (input("Request period: days, weeks, months, years"))
                if user_request == "days":
                    user_days = int(input("How many days? \n>>>"))
                    amt_days = datetime.timedelta(days=user_days)
                    pass #As of now, csv_reader and amt_days are unused variables
        except FileExistsError:
            print("File doesn't exists")
        except FileNotFoundError:
            print("Could not locate file")
        except ValueError:
            print("Wrong datatype")
                    
                    

Trades_Data.amt_winnings("trades.csv")