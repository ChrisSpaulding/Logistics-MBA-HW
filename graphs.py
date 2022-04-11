import csv

import networkx as nx

Graph = nx.DiGraph()


LA = 'Los Angeles, CA'
FoCo = 'Fort Collins, CO'
Helm = 'Helmetta, NJ'
SanAntonio = 'San Antonio, TX'
Dayton = 'Dayton, OH'
Weight = 'Price'
pairs = ((LA, Helm), (Helm, LA), (LA, FoCo), (FoCo, LA), (LA, SanAntonio), (SanAntonio, LA), (LA, Dayton), (Dayton, LA))

def add_nodes(nodes: list()):
    for node in nodes:
        Graph.add_node(node)


def add_edge(edges: dict):
    for value in edges.keys():
        Graph.add_edge()


def add_csv_content(file_name: str):
    with open(file_name, mode='r') as csv_file:
        file_content = list()
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            file_content.append(line)
    for node in file_content:
        Graph.add_node(node['Origin'])

    for edge in file_content:
        Graph.add_edge(edge['Origin'], edge['Destination']
                       , Price=float(edge['Price'].replace('$', '').replace(',', ''))
                       , Days=float(edge['Days'])
                       , RR=edge['RR']
                       )
    print('hi')


def get_cheapest_path():
    if len(Graph) == 0:
        add_csv_content(f'C:\\Users\\chris\\PycharmProjects\\Logistics\\venv\\data.csv')
    for origin, dest in pairs:
        cheapPath = nx.shortest_path(Graph, origin, dest, Weight)
        weight = nx.path_weight(Graph, cheapPath, 'Price')
        days = nx.path_weight(Graph, cheapPath, 'Days')
        day_cheap_path = nx.shortest_path(Graph, origin, dest, care_about_time_function)
        day_weight = nx.path_weight(Graph, day_cheap_path, 'Price')
        day_days = nx.path_weight(Graph, day_cheap_path, 'Days')
        myDict =nx.all_pairs_dijkstra(Graph, 7, 'Days')
        if(days <=7.0):
            print("Cheapest wins")
            print('Path"' + str(cheapPath))
            print('cost:' + str(weight))
            print(days)
        elif(day_days <= 7.0):
            print("Cheapest too long:")
            print(day_cheap_path)
            print(day_weight)
            print(day_days)
        else:
            print('cannot complete route in time:' + day_days)
    print('done')


def care_about_time_function(node1: nx, node2, values: dict):
    return values['Days']


def try_all_LA_Port():
    pathDict = {(str, str): (str)}
    costDict = {(str, str): float}
    if len(Graph) == 0:
        add_csv_content(f'C:\\Users\\chris\\PycharmProjects\\Logistics\\venv\\data.csv')
    for origin, dest in pairs:
        pathDict[(origin, dest)] = ''
        costDict[(origin, dest)] = 100000
        paths = nx.all_simple_paths(Graph, origin, dest)
        for path in paths:
            time = nx.path_weight(Graph, path, 'Days')
            if time <= 6.5: # I need to build in time to change trains in chicago so I can't just do 7
                cost = nx.path_weight(Graph, path, 'Price')
                if cost < costDict[(origin,dest)]:
                    costDict[(origin, dest)] = cost
                    pathDict[(origin, dest)] = path
    for pair in pairs:
        print('---------------\n\n ______________________')
        print(pair)
        print('cost:')
        print(costDict[pair])
        print('path:')
        print(pathDict[pair])
        print('days:')
        print(nx.path_weight(Graph, pathDict[pair], 'Days'))


