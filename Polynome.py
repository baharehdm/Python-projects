# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: Polynome Task
# Bahareh Darvishmohammadi the Material Coder, 256276

# This program is for performing calculation on two Polynomials.The
# calculation include addition, decuction and multiplication.

class Polynome:

    def __init__(self):
        '''
        two attribure has defined for this constructor including poly_dict
        and result_dict. poly_dict is dictionary of polynome exponents and
        factor. result_dict is the dictionary of calculation results.In
        both dictionaries the key is polynome exponent and the value is
        the polynome factor.
        '''
        self.__poly_dict = {}
        self.__result_dict = {}


    def create_poly_sentence(self, dict):
        '''
        :param dict: the dictionary of polynome factor and exponent
        :return: polynome sentence

        The method create a polynome sentence in the string format. It
        also prevents from returning two or more zero polynome in the sentence
        with already one non-zero polynome.
        '''
        poly_created_list = []
        removed_zero_list = []
        for exponent in sorted(dict, reverse=True):
            if dict[exponent] != 0:
                poly_item = str(dict[exponent]) + "x" + "^" + str(exponent)
            else:
                poly_item = '0'
            poly_created_list.append(poly_item)

        for x in poly_created_list:
            if x not in removed_zero_list:
                removed_zero_list.append(x)
        if len(removed_zero_list) > 1:
            if '0' in poly_created_list:
                removed_zero_list.remove('0')

        return " + ".join(removed_zero_list)


    def add_term(self, exponent, factor):
        '''
        :param exponent: exponent of an element of polynome
        :param factor: factor of an element of polynome
        This method is for seting the polynome dictionary in the
        class.
        '''
        self.__poly_dict[exponent] = factor


    def add_polynomes(self, polynome_obj):
        '''
        This method is for adding two polynomes together.
        :param polynome_obj: the second polynome for adding
        :return: addition object
        '''
        temp_dict = {}
        for exp_1 in self.__poly_dict:
            for exp_2 in polynome_obj.__poly_dict:
                if exp_1 == exp_2:
                    temp_dict[exp_1] = self.__poly_dict[exp_1] + \
                                       polynome_obj.__poly_dict[exp_2]

        for exp in self.__poly_dict:
            if exp not in temp_dict:
                temp_dict[exp] = self.__poly_dict[exp]

        for exp_2 in polynome_obj.__poly_dict:
            if exp_2 not in temp_dict:
                temp_dict[exp_2] = polynome_obj.__poly_dict[exp_2]
        addition_obj = Polynome()
        addition_obj.__result_dict = temp_dict

        return addition_obj

    def get_poly_dict(self):
        '''
        This method is only for returning the polynome dictionary.
        :return: poly_dict: polynome dictionary of the class
        '''
        return self.__poly_dict

    def get_result_dict(self):
        '''
        This method is only for returning the result of calculation dictionary.
        :return: result_dict: result of calculation dictionary
        '''
        return self.__result_dict


    def deduct_polynomes(self, polynome_obj):
        '''
        This method is for deducting two polynomes from each other.
        it first mutiply the factors with -1 and it uses the
        add_polynomes method
        :param polynome_obj: the second polynome for deducting
        :return: deduct object
        '''
        self.__result_dict.clear()
        polynome_obj.__result_dict.clear()
        poly_dict = polynome_obj.__poly_dict
        temp_dict = {}
        for exp in poly_dict:
            temp_dict[exp] = poly_dict[exp] * -1
        add_obj = Polynome()
        add_obj.__poly_dict = temp_dict
        deduct_obj = self.add_polynomes(add_obj)

        return deduct_obj

    def set_result_dict(self, result_dict):
        self.__result_dict = result_dict


    def multiply_polynomes(self, polynome_obj):
        '''
        This method is for multiplying two polynomes.
        :param polynome_obj: the second polynome for multiplying
        :return: multiplied object
        '''
        self.__result_dict.clear()
        polynome_obj.__result_dict.clear()
        poly_dict_2 = polynome_obj.get_poly_dict()
        for exp_1 in self.__poly_dict:
            for exp_2 in poly_dict_2:
                factor_total = self.__poly_dict[exp_1] * poly_dict_2[exp_2]
                exponent_total = exp_1 + exp_2
                if exponent_total in self.__result_dict:
                    exponent = exponent_total
                    factor = self.__result_dict[exponent_total] + \
                             factor_total
                    self.__result_dict[exponent] = factor
                else:
                    self.__result_dict[exponent_total] = factor_total
        return self


def read_polynome_file(polynome_file):
    '''
    This fuction read the polynome file and it will add the polynome objects
    to memory locations list.
    :param polynome_file: the name of the file containing polynomes.
    :return: polynome_memory_list: list of polynome objects
    '''
    try:
        infile = open(polynome_file, 'r')
        polynome_memory_list = []
        for lines in infile:
            line = lines.rstrip('\n')
            if ";" in line:
                polynome_component_list = line.split(';')
            else:
                polynome_component_list = []
                polynome_component_list.append(line)
            polynome = Polynome()
            for item in polynome_component_list[::-1]:
                component = item.split(" ")
                factor = int(component[0])
                exponent = int(component[1])
                polynome.add_term(exponent, factor)

            polynome_memory_list.append(polynome)

        return polynome_memory_list
    except ValueError:
        print("Error in reading the file.")
    except IOError:
        print("Error in reading the file.")



def check_user_input(input_str):
    '''
    This method check if the user enters the right input otherwise
    it will set the flag to False and assign the right string to error message.
    :param input_str: the line entered by the user
    :return: error_msg, flag : error message and error flag
    '''
    error_msg = ""
    flag = True
    line_list = input_str.split()
    operator_list = {"+", "*", "-"}

    if len(line_list)== 3:
        operator = line_list[1]
        if operator in operator_list and  line_list[0].isdigit() is False \
                or line_list[2].isdigit() is False:
            error_msg = "Error: entry format is memory_location operation memory_location."
            flag = False
        elif operator not in operator_list:
            error_msg = "Error: unknown operator."
            flag = False
        elif int(line_list[0])> 6 or int(line_list[0])< 0 \
                or int(line_list[2])> 6 or int(line_list[2])< 0:
            error_msg = "Error: the given memory location does not exist."
            flag = False
    else:
        error_msg = "Error: entry format is memory_location operation memory_location."
        flag = False

    return error_msg, flag




def main():
    '''
    This is the main fuction for calling the check_user_input and
    read_polynome_file function and method of the Polynome class and priting.
    the polynome sentences and the calculation results.
    '''

    polynome_file = input("Enter file name: ")
    memory_location_list = read_polynome_file(polynome_file)

    while True:
        if memory_location_list!= None:
            line = input("> ")
            if line == "quit":
                print("Bye bye!")
                return
            else:
                error_msg, flag = check_user_input(line)
                if flag == False:
                    print(error_msg)

            if len(line) == 5 and flag == True :
                command = line[2]
                first_location = int(line[0])
                second_location = int(line[4])
                dict_1 = memory_location_list[first_location].get_poly_dict()
                dict_2 = memory_location_list[second_location].get_poly_dict()
                if command == "+":
                    print("Memory location " + line[0] + ": " +
                          memory_location_list[first_location].create_poly_sentence(dict_1))
                    print("Memory location " + line[4] + ": " +
                          memory_location_list[second_location].create_poly_sentence(dict_2))
                    addition_obj = memory_location_list[first_location].\
                        add_polynomes(memory_location_list[second_location])
                    print("The simplified result:")
                    print(addition_obj.create_poly_sentence(addition_obj.get_result_dict()))

                elif command == "-":
                    print("Memory location " + line[0] + ": " +
                          memory_location_list[first_location].create_poly_sentence(dict_1))
                    print("Memory location " + line[4] + ": " +
                          memory_location_list[second_location].create_poly_sentence(dict_2))
                    deduct_obj = memory_location_list[first_location]. \
                        deduct_polynomes(memory_location_list[second_location])
                    print("The simplified result:")
                    print(deduct_obj.create_poly_sentence(deduct_obj.get_result_dict()))

                elif command == "*":
                    print("Memory location " + line[0] + ": " +
                          memory_location_list[first_location].create_poly_sentence(dict_1))
                    print("Memory location " + line[4] + ": " +
                          memory_location_list[second_location].create_poly_sentence(dict_2))
                    multi_obj = memory_location_list[first_location]. \
                        multiply_polynomes(memory_location_list[second_location])
                    print("The simplified result:")
                    print(multi_obj.create_poly_sentence(multi_obj.get_result_dict()))

                elif command != "+" or command != "-" or command != "*":
                    print("Error: unknown operator.")
        else:
            break

main()