
import urllib.request
from datetime import date

def ticker_symbol():
    ticker_input= input('Please enter the ticker symbol:').strip().upper()
    return ticker_input

def start_date_analysis():
    start_year=0
    start_month=0
    start_day=0
    while True:
        try:
            start_date_input= input('Please enter the start date to analyze:').strip() # format input='YYYY-MM-DD'

            start_year,start_month,start_day = start_date_input.split('-')


            # if start_date_input <= today's date
            today= date.today()
            day_input= date(int(start_year),int(start_month),int(start_day))

            if day_input <= today:
                return (start_year,start_month,start_day,day_input)
        except:
            print("date format is not correct.Please try again")

def end_date_analysis(startdate):
    end_year=0
    end_month=0
    end_day=0
    while True:
        try:
            end_date_input= input('Please enter end date to analyze:').strip()
            end_year,end_month,end_day= end_date_input.split('-')
            today= date.today()
            end_day_input = date(int(end_year),int(end_month),int(end_day))
            if end_day_input <= today and end_day_input > startdate:
                return (end_year,end_month,end_day)

        except:
            print('end date format is not correct. Please try again')



def open_url(url_test: str):
    #download date from URL
    url_response = urllib.request.urlopen(url_test)
    data= url_response.read()
    url_response.close()

    string_data = data.decode( encoding = 'utf-8')

    line_list= string_data.splitlines()

    date_list=[]
    close_price_list=[]

    for element in line_list:

        each_in_element= element.split(',')
        date_list.append(each_in_element[0])    #list of all dates
        close_price_list.append((each_in_element[4])) #list of all close price

    date_list.pop(0) #pop the title 'Date' in list
    close_price_list.pop(0) #pop the title 'close price' in list

    date_list.reverse()
    close_price_list.reverse()

    float_close_price = []
    for each_price in close_price_list:
        float_price= float(each_price)
        float_close_price.append(float_price)



    return (date_list,float_close_price)



