from utils.num import removeText
from utils.Date import  custom_date_formatter



def main():
    print('main function')
    output = removeText()
    print(f'ouput ={output}')
    

    print()
    userDate = custom_date_formatter ()
    print(f'convertDate={userDate}')


if __name__ == '__main__':
        main()