# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to programming
# Task: Routing protocol simulator
# Bahareh Darvishmohammadi the Material Coder, studentnr: 256276
# email: darvishm@student.tut.fi

# The program is for adding information related to the routers
# (The router name, the network that router located in, the distance
# from that network and the router's neighbours) and how the data in
# the routing tables of routers change when the devices communicate
# with each other.
# It includes a router class for an individual router( with
# attributes and methods),the function for reading the
# network file and the main function.


class Router:

    def __init__(self, name):
        '''
        three attribure has defined for this constructor including name
        of the router, routing table and connections. connection is a
        list of router's neighbour and routing table is a dictionary of
        router's networks. The key of the dictionary is the network that
        router located in and the value is the distance from that network.
        :param name: name of the router
        '''
        self.__name = name
        self.__routing_table = {}
        self.__connection = []


    def add_router(self, routers_dict):
        '''
        The method is for adding a new router.
        :param routers_dict: the dictionary of routers.
        '''
        if self.__name not in routers_dict:
            routers_dict[self.__name] = self
        else:
            print("Name is taken.")

    def print_info(self):
        '''
        The method is for printing the information related to one router.
        '''
        route_list = []

        print("  " + self.__name)
        if len(self.__connection) == 0:
            print("    N: ")
        else:
            print("    N: " + ", ".join(sorted(self.__connection)))

        if len(self.__routing_table) == 0:
            print("    R: ")
        else:
            for key in sorted(self.__routing_table):
                route_list.append(str(key) + ":" + str(self.__routing_table[key]))
            print("    R: " + ", ".join(route_list))


    def get_name(self):
        '''
        This method is only for returning the name of the router.
        :return: name of the router
        '''
        return self.__name

    def get_neighbours(self):
        '''
        This method is for returning the router's neighbour.
        :return: list of router's neighbour
        '''
        return self.__connection

    def get__routing_table(self):
        '''
        This method is for returning the router's network.
        :return: routing table
        '''
        return self.__routing_table


    def add_neighbour(self, router_obj):
        '''
        This method is for adding new neighbour to an individual router.
        :param router_obj: The router object to add a new neighbour to it
        '''
        self.__connection.append(router_obj.get_name())

    def add_network(self, network_address, distance):
        '''
        The method is for adding new network for the router.
        :param network_address: the address of the network
        :param distance: the distance of router from that network
        '''
        self.__routing_table[network_address] = distance

    def receive_routing_table(self, router_obj):
        '''
        The method is for send the content of one router's routing table
        to their neighbouring routers
        :param router_obj: the router object for adding its router's routing
                            table
        '''
        for key in router_obj.get__routing_table():
            distance = router_obj.get__routing_table()[key] + 1
            if key not in self.__routing_table:
                self.add_network(key,distance)


    def has_route(self, network_name):
        '''
        The method tells if a certain router has a connection to a certain
        network.
        :param network_name: the name of the network
        :return flag, distance:
                flag : if the router is not in that network it is false
                otherwise true
                distance: the distance of the router from that network
                if network is unknown the distance is -1
        '''
        flag = False
        distance = 0
        if network_name not in self.__routing_table:
            flag = False
            distance = -1
        elif network_name in self.__routing_table:
            flag = True
            distance = self.__routing_table[network_name]

        return flag, distance





def read_network_file(network_file):
    '''
    The function is for reading the network file
    :param network_file: the name of the network file
    :return: routers_dict: the dictionary contains all the routers's
             information.
    '''
    try:
        routers_dict = {}
        infile = open(network_file, 'r')

        for line in infile:
            line_ = line.rstrip('\n')
            router_info = line_.split('!')

            router_name = router_info[0]
            router = Router(router_name)
            if router.get_name() not in routers_dict:
                router.add_router(routers_dict)

            connections = router_info[1]
            if len(connections) > 1:
                connections = connections.split(";")
            if len(connections) != 0:
                for item in connections:
                    router2 = Router(item)
                    if router2.get_name() not in routers_dict:
                        router2.add_router(routers_dict)
                    routers_dict[router_name].add_neighbour(router2)


            network = router_info[2]
            if ";" not in network and len(network) != 0 :
                network = network.split(':')
                network_address = network[0]
                distance = network[1]
                routers_dict[router_name].add_network(network_address, int(distance))
            elif ";" in network :
                network = network.split(';')
                network1 = network[0]
                network2 = network[1]
                network_list_1 = network1.split(":")
                network_list_2 = network2.split(":")

                network_address_1 = network_list_1[0]
                distance_1 = network_list_1[1]
                routers_dict[router_name].add_network(network_address_1, int(distance_1))

                network_address_2 = network_list_2[0]
                distance_2 = network_list_2[1]
                routers_dict[router_name].add_network(network_address_2, int(distance_2))

        return routers_dict

    except ValueError:
        print("Error: the file could not be read or there is something wrong with it.")
    except IOError:
        print("Error: the file could not be read or there is something wrong with it.")
    except IndexError:
        print("Error: the file could not be read or there is something wrong with it.")




def main():
    '''
    This is the main fuction for calling the read_network_file function and
    method of the router's class.
    '''
    network_file = input("Network file: ")
    if network_file != "":
        routers_dict = read_network_file(network_file)
    elif network_file == "":
        routers_dict = {}

    while True:
        if routers_dict != None:
            command = input("> ")
            command = command.upper()

            if command == "P":
                router_name = input("Enter router name: ")
                if router_name in routers_dict:
                    routers_dict[router_name].print_info()
                else:
                    print("Router was not found.")

            elif command == "PA":
                if routers_dict != {}:
                    for key in sorted(routers_dict):
                        routers_dict[key].print_info()
                else:
                    print("Router was not found.")

            elif command == "S":
                sending_router = input("Sending router: ")
                if sending_router in routers_dict:
                    neighbours = routers_dict[sending_router].get_neighbours()
                    for item in neighbours:
                        routers_dict[item].receive_routing_table(routers_dict[sending_router])


            elif command == "C":
                router1_name = input("Enter 1st router: ")
                router2_name = input("Enter 2nd router: ")
                if router1_name in routers_dict and router2_name in routers_dict:
                    if router1_name not in routers_dict[router2_name].get_neighbours()\
                            and router2_name not in routers_dict[router1_name].get_neighbours():
                        routers_dict[router1_name].add_neighbour(routers_dict[router2_name])
                        routers_dict[router2_name].add_neighbour(routers_dict[router1_name])

            elif command == "RR":
                router_name = input("Enter router name: ")
                network_name = input("Enter network name: ")
                if router_name in routers_dict:
                    flag , distance = routers_dict[router_name].has_route(network_name)
                    if flag == False and distance == -1:
                        print("Route to the network is unknown.")
                    elif flag == True:
                        if distance == 0:
                            print("Router is an edge router for the network.")
                        else:
                            print("Network " + network_name + " is " +
                                  str(distance) +  " hops away")

            elif command == "NR":
                router_name = input("Enter a new name: ")
                router = Router(router_name)
                router.add_router(routers_dict)

            elif command == "NN":
                router_name = input("Enter router name: ")
                network_address = input("Enter network: ")
                distance = input("Enter distance: ")
                if router_name in routers_dict:
                    routers_dict[router_name].add_network(network_address, int(distance))

            elif command == "Q":
                print("Simulator closes.")
                return

            else:
                print("Erroneous command!")
                print("Enter one of these commands:")
                print("NR (new router)")
                print("P (print)")
                print("C (connect)")
                print("NN (new network)")
                print("PA (print all)")
                print("S (send routing tables)")
                print("RR (route request)")
                print("Q (quit)")

        else:
            break




main()
