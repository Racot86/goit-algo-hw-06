import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime,timedelta

port_list = {
    'Ningbo':(0,2),
    'Shanghai':(0,3),
    'Los Angeles':(6,2),
    'Oakland':(6,3),
    'Honolulu':(3,1),
    'Dutch Harbor':(5,5),
    'Kwangyang':(2,5),
    'Pusan':(3,6),
    'Incheon':(1,6)
}

EXX = nx.DiGraph()
for port in port_list.keys():
    color = ''
    if port == 'Ningbo' or port == 'Shanghai':
        color = 'red'
    EXX.add_node(port, pos=port_list[port], color=color)

EXX.add_edge("Ningbo", "Shanghai",weight=234)
EXX.add_edge("Shanghai", "Los Angeles",weight=5720)
EXX.add_edge("Los Angeles", "Oakland",weight=420)
EXX.add_edge("Oakland", "Honolulu",weight=2106)
EXX.add_edge("Honolulu", "Dutch Harbor",weight=2200)
EXX.add_edge("Dutch Harbor", "Pusan",weight=3060)
EXX.add_edge("Pusan", "Kwangyang",weight=105)
EXX.add_edge("Kwangyang", "Incheon",weight=406)
EXX.add_edge("Incheon", "Ningbo",weight=682)
EXX.add_edge("Kwangyang", "Ningbo",weight=497)
EXX.add_edge("Honolulu", "Pusan",weight=4005)
EXX.add_edge("Oakland", "Dutch Harbor",weight=2073)
EXX.add_edge("Oakland", "Kwangyang",weight=5083)


labels = nx.get_edge_attributes(EXX,'weight')




ningbo = nx.dfs_tree(EXX, source='Ningbo')
#nx.draw(ningbo,pos, with_labels=True,node_color='red')
#plt.show()

ningbo = nx.bfs_tree(EXX, source='Ningbo')
#nx.draw(ningbo,pos, with_labels=True)
#plt.show()
while True:
    print('Welcome to Eagle Express X Container Shipping Calculator')
    print('')
    print('  1. Draw Eagle Express Port Rotation Map                                     (Full graph view)')
    print('  2. Search possible destinations by Port Of loading                          (using BFS & DFS methods)')
    print("  3. Calculate shrtest distance between Port Of Loading and Port Of Discharge (using Dijkstra's algorithm)")
    print("  0. Exit porgram")
    print('')
    menu  = input("Make your choise> ")

    if int(menu) == 0:
        break
    
    if int(menu) == 1:
        pos = nx.get_node_attributes(EXX,'pos')
        plt.title("Eagle Express X Port Rotation")
        nx.draw(EXX,pos, with_labels=True, node_color = 'grey')
        nx.draw_networkx_edge_labels(EXX,pos, edge_labels=labels)
        no_nods  = len(EXX)
        no_edges = len(EXX.edges)
        plt.text(1,0,f"This line contains {no_nods} ports and {no_edges} connections between them.")
        
        plt.show()
    if int(menu) == 2:
        while True:
            index = 1
            print("Choose your port of loading: ")
            print('')
            for port in port_list.keys():
                print(f'  {index}. {port}')
                index += 1
            print('  0. Return to main menu')
            print('')
            menu2 = input("Make your choise> ")
            ports = list(port_list.keys())
            if int(menu2) != 0 and int(menu2) <= len(port_list):

                bfs_port = nx.bfs_tree(EXX, source=ports[int(menu2)-1])
                dfs_port = nx.dfs_tree(EXX, source=ports[int(menu2)-1])
                pos = nx.get_node_attributes(EXX,'pos')
                pos2 = nx.get_node_attributes(EXX,'pos')
                
                for key, val in pos2.items():
                    x = val[0]
                    y = val[1] + 9
                    pos2[key] = (x,y)
                
                color_map = []
                

                for node in bfs_port:
                    #print(node)
                    if node == ports[int(menu2)-1]:
                        color_map.append('blue')
                    else:
                        color_map.append('green')
                        

                color_map2 = []
                for node in dfs_port:
                    #print(node)
                    if node == ports[int(menu2)-1]:
                        color_map2.append('blue')
                    else:
                        color_map2.append('red')

                nx.draw(bfs_port,pos, with_labels=True,node_color=color_map)
                nx.draw(dfs_port,pos2, with_labels=True,node_color=color_map2)
                plt.text(1,0,"Possible Ports Of Discharge using BFS method")
                plt.text(1,9,"Possible Ports Of Discharge using DFS method")
                plt.show()
            if int(menu2) == 0:
                break
    if int(menu) == 3:
        pol = ''
        pod = ''
        while True:
            index = 1
            print("Choose your Port of loading: ")
            print('')
            for port in port_list.keys():
                print(f'  {index}. {port}')
                index += 1
            print('  0. Return to main menu')
            print('')
            menu_pol = input('Choose Port of Loading: ')
            
            if int(menu_pol) == 0:
                break
            
            if int(menu_pol) <= len(port_list):
                pol = list(port_list)[int(menu_pol)-1]
                print('')
                print("Your Port Of Loading:",pol)
            else:
                continue
            
            pod_list = []
            for port in port_list.keys():
                if port != pol:
                    pod_list.append(port)
            
            index = 1
            print('')
            print("Choose your Port of Discharge: ")
            print('')
            for port in pod_list:
                print(f'  {index}. {port}')
                index += 1
            
            print('  0. Return to main menu')
            print('')
            menu_pod = input('Choose Port of Discharge: ')
            if int(menu_pod) == 0:
                break
            if int(menu_pod) <= len(pod_list):
                pod = pod_list[int(menu_pod)-1]
                print('')
                print("Your Port Of Discharge:",pod)
                print('')
            else:
                continue
            path = nx.dijkstra_path(EXX,pol,pod)
            length = nx.dijkstra_path_length(EXX,pol,pod)
            print('')
            print(f'{pol} - {pod}')
            print('Your shipment path: ')
            for port in path:
                print(f'  {port}')
            hours = length/19.7
            date_now = datetime.now()
            total_hours = timedelta(hours=hours)
            delivery_date = date_now + total_hours
            delivery_date_str = delivery_date.strftime("%d/%m/%Y")
            print(f'Total distance {length} nautical miles')
            print('Your shipment will be delivered on', delivery_date_str)
            pos = nx.get_node_attributes(EXX,'pos')
            color_map_ship = []
            for node in EXX:
                if node in path:
                    if node == pol:
                        color_map_ship.append('red')
                    elif node == pod:
                        color_map_ship.append('green')
                    else:
                        color_map_ship.append('red')
                else:
                    color_map_ship.append('grey')
            path_edges = []
            for i in range(0,len(path)-1):
                path_edges.append((path[i],path[i+1]))

            color_edges = []
            for edge in EXX.edges:
                if edge in path_edges:
                    color_edges.append('red')
                else:
                    color_edges.append('black')
            plt.title(f"Your Shipment Map: {pol} - {pod}")
            nx.draw(EXX,pos, with_labels=True, edge_color = color_edges, node_color = color_map_ship)
            nx.draw_networkx_edge_labels(EXX,pos, edge_labels=labels)
            plt.text(1,0,"Your shimpent will be delivered on " + delivery_date_str)
            plt.show()