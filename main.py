import BFS
import UCS
import GBFS
import astar
if __name__ == '__main__':


    print("Choose an Algorithm:)")
    print("1. A Star")
    print("2. Breadth First Search (BFS)")
    print("3. Depth First Search (DFS)")
    print("4. Uniform-Cost Search (UCS)")
    print("5. Greedy Best First Search (GBFS)")
    print()
    choice = int(input("Your Choice: "))
    start = input("Enter Your Starting City\n")
    goal = input("Enter Your Destination City\n")

    if choice == 1:
        print("*--------------------------------------A* IMPLEMENTATION--------------------------------------*\n")
        astar.result(start,goal)
    elif choice == 2:
        print("*--------------------------------------BFS IMPLEMENTATION--------------------------------------*\n")
        BFS.result(start, goal)
    elif choice == 3:
        print("*--------------------------------------DFS IMPLEMENTATION--------------------------------------*\n")

    elif choice == 4:
        print("*--------------------------------------UCS IMPLEMENTATION--------------------------------------*\n")
        UCS.result(start, goal)
    elif choice == 5:
        print("*--------------------------------------GBFS IMPLEMENTATION--------------------------------------*\n")
        GBFS.result(start, goal)

