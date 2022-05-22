class Pet:
    def __init__(self,kind,legs_number):
        self.kind = kind
        self.legs_number = legs_number

    def start_running(self):
        print("Pet is running.")

    def stop_running(self):
        print("Pet stopped.")
        
pet1 = Pet("dog", 4)
pet2 = Pet("monkey",2)

print(pet1.legs_number)

pet1.start_running()

print(pet2.legs_number)

pet2.stop_running()
        
