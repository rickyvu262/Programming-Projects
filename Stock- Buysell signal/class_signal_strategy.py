
class simple_moving_strategy():

    def execute(self,signal_list,day_interval,price_list):
        result_list=[]
        for i in range(day_interval):
             result_list.append('')
        for i in range(day_interval-1,len(signal_list)-1):
            # start_date_price_cal = (day_interval - 1) + i
            if signal_list[i] > price_list[i+1] and signal_list[i+1]< price_list[i+1]:

                result_list.append('BUY')
            elif signal_list[i]< price_list[i] and signal_list[i+1]> price_list[i+1]:

                result_list.append('SELL')
            else:
                result_list.append('')

        return result_list


class directional_indicator_strategy:

    def __init__(self, buy_threshold , sell_threshold):
        self._pair_buy_sell_threshold = (buy_threshold,sell_threshold)

    def execute(self,signal_list,day_interval,price_list):

        result_list=['']
        for i in range(len(signal_list)-1):
            if signal_list[i]<= self._pair_buy_sell_threshold[0] and signal_list[i+1]> self._pair_buy_sell_threshold[0]:

                result_list.append("BUY")
            elif signal_list[i]>= self._pair_buy_sell_threshold[1] and signal_list[i+1]< self._pair_buy_sell_threshold[1]:

                result_list.append("SELL")
            else:
                result_list.append('')

        return result_list

a = simple_moving_strategy()


