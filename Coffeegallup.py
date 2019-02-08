# Coffee gallup.
# Task Discription:

# Finnish people drink too much coffee. The authorities are concerned 
# and decided to investigate the situation by arranging a gallup to find 
# out some accurate numbers. Gallup asks each passing person, how many 
# cups of coffee, they drink on a daily basis and writes down the response. 
# Implement a program that conducts some calculations for the responses.
# First the program prints:
# Enter one response per line. End by entering an empty row.
# and reads the integers entered by the user until the user wants to finish 
# entering the numbers and enters an empty row to mark this.First the program 
# removes the responses of non-coffee-drinkers. If there are values to be removed, 
# their number is announced to the user by printing:
# Removed X non-coffee-drinkers responses
# where X is replaced with the number of the measurement results.
# If there are responses left, the program prints interesting information related 
# to coffee drinking habits. First the program prints the text:
# Information related to coffee drinkers:
# After this, the program prints a nice graphic presentation of the distribution of 
# the responses. The graphic presentation is a bar diagram, that contains a bar for 
# each number inside the range of the response (between the smallest and the largest 
# response). The first thing at the left of each line of the graphic representation 
# is the value of the response printed in a 2-character-wide column. After this, the 
# program prints one space, and after this the character "#" as many times as there 
# are responses with this value. The presentation of the graphic visualization can be 
# seen more specifically in the example run in the end of the task description. After 
# the graphic presentation print one empty line. After this, the program prints the 
# largest response, the most common response, and the percentage of the responses that 
# differ at maximum by one from the most common response:
# The greatest response: X cups of coffee per day
# The most common response: Y cups of coffee per day
# Z% of the respondents drink A-B cups of coffee per day
# where X, Y, Z, A and B are replaced with correct values and A equals Y-1 and B equals 
# Y+1 and Z. The percentage value is printed to one decimal.
# If there are more than one most common responses, the program uses the smallest value 
# of these responses in the above specified printouts.
# The recommendation is that you should not drink more than 4 cups of coffee per day. 
# If there are responses that exceed the recommendation, the program will print 
# information related to them:
# Information related to coffee abusers:
# X% of the respondents drink more than 4 cups of coffee per day
# X respondents drink a little too much coffee (5-8 cups per day)
# X respondents drink over double the recommendation
# where X's are replaced by the correct values and the percentage value is printed to one decimal.
# If the responses include values that exeed the recommendation over twice, the program prints a 
# list of these values. First the program prints the title:
# The responses over 8 cups of coffee per day:
# and after this each response on its own row, in the order the data was entered to the program.




def main():
    '''
    This Function call other Functions and also prints information related
    to non coffee drinkers, coffee drinkers and coffee abusers.
    :return: 0 if the user press enter at the beginning and in
            this case the program will be ended.
    '''

    list_responses = input_response()
    if list_responses!=[]:
        non_coffee_drinkers = list_responses.count(0)
        list_responses=\
            remove_non_coffee_drinkers(list_responses)

        if (coffee_drinkers(non_coffee_drinkers)== False or \
                        gallup_kindergarten(list_responses)== True) :

            print("Removed " + str(non_coffee_drinkers) + " non-coffee-drinkers responses")
            print()


        if gallup_kindergarten(list_responses)== False:

            print("Information related to coffee drinkers:")

            maximum_responses, most_common_response, percent, \
            a, b, sum_response_count = coffee_drinkers_info(list_responses)

            print()

            print("The greatest response: " + str(maximum_responses) + " cups of coffee per day")
            print("The most common response: " + str(most_common_response) + \
                  " cups of coffee per day")
            print(str(percent) + "%" + " of the respondents drink " + str(a) + "-" + \
                  str(b) + " cups of coffee per day")
            print()

        if coffee_abuser(list_responses)== True:

            print("Information related to coffee abusers:")

            percentage_abuser, sum_response_count_over_five, \
            sum_response_count_double_recom, responses_over_recom = \
                calculate_coffee_abuser(sum_response_count,list_responses)

            print(str(percentage_abuser) + "%" + \
                  " of the respondents drink more than 4 cups of coffee per day")
            print( str(sum_response_count_over_five)+ \
                   " respondents drink a little too much coffee (5-8 cups per day)")
            print(str(sum_response_count_double_recom) + \
                  " respondents drink over double the recommendation")
            print("The responses over 8 cups of coffee per day:")

            for i in range(0,len(responses_over_recom)):
                print(responses_over_recom[i])
    else:
        return 0



def input_response():
    '''
    This function get the input entered by user. The input always will
    be get by user unless user enter an empty row ,in this case the program
    will be interrupted .
    :return: list_responses: input as a list
    '''
    print("Enter one response per line. End by entering an empty row.")
    list_responses = []
    while True:
        user_input = input("")
        if user_input != "":
            response = int(user_input)
            list_responses.append(response)
        elif user_input == "":
            break
    return list_responses


def coffee_drinkers_count(list_responses):
    '''
    This function has one parameters which is a list of responses.
    This function count the number of coffee drinkers and return it as a list.
    :param list_responses: list_responses: list of responses without non coffee drinkers(zero input)
    :return: responses: the list of responses without repetition
             count_list: the list for number of times each response repeated
             maximum_response: the largest response
    '''
    count_list=[]
    responses=[]
    maximum_response = max(list_responses)
    # a loop from 1 until the maximum of responses
    for i in range(1,maximum_response+1):
        count=list_responses.count(i)
        # the program check if i in the for loop exist on the list, in the other
        # word if the numbers of times i repeated is not zero.
        if count!=0:
            count_list.append(count)
            responses.append(i)
    return responses,count_list,maximum_response


#
def remove_non_coffee_drinkers(list_responses):
    '''
    This function remove the input which is equivalent to zero(zero cup of coffee).
    :param list_responses: list_responses list of input responses
    :return: list_responses: list of responses with removed zero
    '''
    length_of_list = len(list_responses) - 1
    i = 0
    while i <= length_of_list:
        if list_responses[i] == 0:
            list_responses.remove(list_responses[i])
            length_of_list -= 1
            i -= 1
        i += 1
    return list_responses




def coffee_drinkers_info(list_responses):
    '''
    This Function calculate the largest response, most common response and the sum
    of the number of responses based on the cup of coffee consumed.
    :param list_responses: list_responses: list of responses with removed zero
    :return: maximum_responses, most_common_response, percent, a, b, sum_response_count
    '''
    sum_response_count = 0
    most_common_response = 0
    response, count_of_response, maximum_responses = \
        coffee_drinkers_count(list_responses)

    most_common_response_count = max(count_of_response)

    for i in range(0, len(response)):
        if count_of_response[i] == most_common_response_count:
            if most_common_response == 0:
                most_common_response = response[i]

    minimum=min(list_responses)

    for i in range(minimum,maximum_responses+1):
        print(format(i, '2d'),end=' ')
        if i in response:
            j=response.index(i)
            print('#' * count_of_response[j])
        else:
            print(" ")

    a = most_common_response - 1
    b = most_common_response + 1
    c = most_common_response
    sum_most_common_response = 0

    for i in range(0, len(response)):
        sum_response_count += count_of_response[i]
        if response[i] == a:
            sum_most_common_response += count_of_response[i]
        if response[i] == b:
            sum_most_common_response += count_of_response[i]
        if response[i] == c:
            sum_most_common_response += count_of_response[i]

    percent = calculate_percentage(sum_most_common_response, sum_response_count)

    return maximum_responses, most_common_response, percent, a, b, sum_response_count





def calculate_percentage(sum_most_common_response,sum_response_count):
    '''
    This function calculate the percentage of the responses that differ
    at maximum by one from the most common response
    :param sum_most_common_response: sum_most_common_response
            sum of the the responses that differ at maximum
            by one from the most common response
    :param sum_response_count: sum_response_count:
            sum of the number of times each response repeated
    :return: percent
    '''
    percent = format(sum_most_common_response / sum_response_count * 100, '.1f')
    return percent


#
def calculate_coffee_abuser(sum_response_count,list_responses):
    '''
    This function calculate the percentage and the amount of responses that
    exceed the recommendation.
    :param sum_response_count: sum_response_count: sum of the number of times
            each response repeated.
    :param list_responses: list_responses: list of responses with removed zero.
    :return: percentage, sum_response_count_over_five,
             sum_response_count_double_recom, responses_over_recom
    '''
    sum_response_count_over_four=0
    sum_response_count_over_five=0
    sum_response_count_double_recom=0
    responses_over_recom=[]
    for i in range(0, len(list_responses)):
        if list_responses[i]>4:
            sum_response_count_over_four+=1
        if list_responses[i]>=5 and list_responses[i]<=8:
            sum_response_count_over_five+=1
        if list_responses[i]>8:
            sum_response_count_double_recom+=1
            responses_over_recom.append(list_responses[i])

    percentage=format(sum_response_count_over_four/sum_response_count*100,'.1f')

    return percentage, sum_response_count_over_five, \
           sum_response_count_double_recom, responses_over_recom


#
#
def gallup_kindergarten(response_list):
    '''
    This function checks if there are only non coffee drinkers and then
    return True if there are only non coffee drnkers
    :param response_list: list_responses: list of responses with removed zero
    :return: flag
    '''
    flag=False
    # The parameter of the function is the list with removed zero,
    # so if the list is empty it means that all the inpput were zero
    if response_list==[]:
        flag = True
    return flag


def coffee_drinkers(non_coffee_drinkers_count):
    '''
    This Function checks if there are only coffee drinkers
    (there is no zero in the list) and return True if there
    are otherwise it return False.
    :param non_coffee_drinkers_count: non_coffee_drinkers :
            the numbers of responses with zero cup of coffee
    :return: flag
    '''
    flag=False
    if non_coffee_drinkers_count==0:
        flag=True
    return flag


def coffee_abuser(respose_list):
    '''
    This function checks if there are coffee drinkers who exceed the recomdation
    and return True if there are otherwise it return False.
    :param respose_list: list_responses : list of responses with removed zero
    :return: flag
    '''
    flag=False
    for i in range(0,len(respose_list)):
        if respose_list[i]>4:
            flag=True
    return flag


main()

