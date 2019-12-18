started=False
while True:
    command=input(">").lower()
    if command=="help":
        print("""
start:to start
stop:to stop
quit:quit
        """)
    elif command=="start":
        if started:
            print("car already started")
        else:
            print("car started")
            started=True
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            print("car stopped")
            started=False

    elif command=="quit":
        break
    else:
        print("enter proper input")

