# command = ""
# started = False
# while command != "quit":
#     command = input(">").lower()
#     if command == "help":
#         print("""
#                 start - to start the car
#                 stop - to stop the car
#                 quit - to exit""") 
#     elif command == "start":
#         if started:
#             print("Car has been already started")
#         else:
#             print("Your car has been started")
#             started = True
#     elif command == "stop":
#         if started == False:
#             print("Your car has already been stopped")
#         else:
#             started = False
#             print("Your car has been stopped")
#     elif command == "quit":
#         break
#     else:
#         print("Enter a valid command")
# print("quitting...")

command = ""
isStarted = False
while command != "quit":
    if command == "start":
        print("Car has been started!")
        isStarted = True
    elif command == "help":
        print("""
                 start - to start the car
                 stop - to stop the car
                 quit - to exit""") 
    elif command == "stop":
        print("Car has been stopped")
        isStarted = True
    elif command == "quit":
        print("quitting the game...")
        break