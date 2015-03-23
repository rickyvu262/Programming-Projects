
class simple_moving:

    def execute(self, day_interval:int, close_price_list:list):
        result_list=[]

        for i in range(day_interval-1):
            result_list.append(0)
        for i in range(0,len(close_price_list)- day_interval):
            total= sum(close_price_list[i:day_interval+i])
            average= total/day_interval
            result_list.append(average)


        return result_list

class directional:

    def execute(self, day_interval:int, close_price_list:list):
        result_list=[]
        movement_list=[0]
        # movement_list list all the +1,1,0 when compare price with previous (Note:1st price on the movement is always 0)
        for i in range(0,len(close_price_list)-1):
            if close_price_list[i+1] > close_price_list[i]:
                movement_list.append(1)
            elif close_price_list[i+1] < close_price_list[i]:
                movement_list.append(-1)
            elif close_price_list[i+1] == close_price_list[i]:
                movement_list.append(0)


        total_movement=0
        for i in range (0,day_interval-1): # for index of list that is less than the day_interval, append it to the list first

            total_movement = total_movement + (movement_list[i])# append the rest of the list based on the day-interval specify
            result_list.append(total_movement)

        for i in range(0,len(movement_list)-day_interval+1):
            total_of_movement= sum(movement_list[i:day_interval+i])
            result_list.append(total_of_movement)

        return result_list


x= directional()
y= simple_moving()





