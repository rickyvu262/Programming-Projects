import url_open
import class_indicator
import class_signal_strategy

from datetime import date


def user_interface():

    while True:
        try:
            # user_input for symbol,start date, end date & signal_indicator
            SYMBOL = url_open.ticker_symbol()

            START_YEAR,START_MONTH,START_DAY,start_date = url_open.start_date_analysis()

            END_YEAR,END_MONTH,END_DAY = url_open.end_date_analysis(start_date)
            # extract the data from Yahoo site, stored them in the lists: date, price
            date , close_price = download_url(SYMBOL,START_MONTH,START_DAY,START_YEAR,END_MONTH,END_DAY,END_YEAR)

            # get the indicator list & signal_strategy list
            indicator_list,signal_strategy_list,strategy_print = signal_strategy_method(close_price)

            # formating to print out these 4 lists: date,close_price,indicator_list, signal_strategy_list
            print("SYMBOL: ",SYMBOL)
            print(strategy_print)
            print_report_format(date,close_price,indicator_list,signal_strategy_list)
            break

        except:
        # can't download the URL or sth wrong might happen in between
            print("Please enter another URL that is valid.")
    quit()

def print_report_format(date_list,close_price_list,indicate_list, signal_list):
    print("{:^8}   {:>7}   {:>7}     {:^7} ".format("DATE","CLOSE","INDICATOR","SIGNAL"))
    for i in range(len(indicate_list)):
        print("{:8}  {:7.2f}   {:7.2f}     {:7} ".format (date_list[i],close_price_list[i],indicate_list[i],signal_list[i]))


def download_url(SYMBOL,START_MONTH,START_DAY,START_YEAR,END_MONTH,END_DAY,END_YEAR):
    url_test ='http://ichart.yahoo.com/table.csv?s='+SYMBOL+'&a='+START_MONTH+'&b='+START_DAY+'&c='+START_YEAR+'&d='+ END_MONTH +'&e='+END_DAY+'&f='+END_YEAR+'&g=d'
    date, close_price = url_open.open_url(url_test)

    return (date,close_price)

def signal_strategy_method(list_price):
    # asked user for signal_strategy, return the indicator, signal list according to the user's input
    signal_input= input(
'''
Please select  A: simple moving average
               B: directional indicator
''').strip().upper()

    if signal_input == 'A':
        #access the simple moving average, use the class_indicator object (simple moving)
        simple_moving_list, day_interval = indicator(class_indicator.y,list_price)

        #signal list generated using class_signal object (simple moving)
        simple_signal = signal_strategy(class_signal_strategy.a,simple_moving_list,list_price,day_interval)
        #print format of strategy
        x= 'STRATEGY: Simple movement average ('+ str(day_interval) + ' -day)'

        return (simple_moving_list,simple_signal,x)

    elif signal_input == 'B':
        #access the directional indicator, use the class_indicator object (directional)
        directional_list,day_range = indicator(class_indicator.x,list_price)

        buy_threshold = int(input("Please enter the buy threshold:"))
        sell_threshold= int(input("Please enter the sell threshold:"))

        #signal list generated using class_signal object (directional)
        directional_signal = signal_strategy(class_signal_strategy.directional_indicator_strategy(buy_threshold,sell_threshold),directional_list,list_price,day_range)

        # print format strategy
        y= 'STRATEGY: Directional (' + str(day_range) + '-day), buy above +' + str(buy_threshold) + ',sell below' + str(sell_threshold)

        return (directional_list,directional_signal,y)

def indicator(indicator_signal:'class',close_price_list:list):
    # return indicator list from indicator object
    day_interval= int(input("please enter the number of days to generate:"))
    indicator_list = indicator_signal.execute(day_interval,close_price_list) #execute method from class_indicator module (applied for both simple and directional(same parameter,same output)
    return (indicator_list,day_interval)

def signal_strategy(indicated_signal_strategy:'object',signal_indicator_list , close_price_list, day):
    # return signal list from strategy object
    signal_list= indicated_signal_strategy.execute(signal_indicator_list,day,close_price_list) #execute method from class_signal_strategy module(applied for both simple & directional(same parameter,same output))
    return (signal_list)

if __name__ == '__main__':
    user_interface()