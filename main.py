import json

class SATResults:
    MAX_SAT_SCORE = 1600  # Assuming the maximum SAT score is 1600

    def __init__(self, name, address, city, country, pincode, sat_score):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.pincode = pincode
        self.sat_score = sat_score
        self.passed = "Pass" if sat_score > 0.3 * self.MAX_SAT_SCORE else "Fail"

class SATResultsManager:
    def __init__(self):
        self.results = []

    def insert_data(self):
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        country = input("Enter Country: ")
        pincode = input("Enter Pincode: ")
        sat_score = int(input("Enter SAT Score: "))

        result = SATResults(name, address, city, country, pincode, sat_score)
        self.results.append(result)
        print("Data inserted successfully.")

    def view_all_data(self):
        for result in self.results:
            print(json.dumps(result.__dict__, indent=2))

    def get_rank(self):
        name = input("Enter Name to get rank: ")
        sorted_results = sorted(self.results, key=lambda x: x.sat_score, reverse=True)
        rank = [i+1 for i, result in enumerate(sorted_results) if result.name == name]
        if rank:
            print(f"{name} has rank {rank[0]}")
        else:
            print(f"{name} not found in the data.")

    def update_score(self):
        name = input("Enter Name to update SAT Score: ")
        for result in self.results:
            if result.name == name:
                new_score = int(input(f"Enter new SAT Score for {name}: "))
                result.sat_score = new_score
                result.passed = "Pass" if new_score > 0.3 * SATResults.MAX_SAT_SCORE else "Fail"
                print("SAT Score updated successfully.")
                return
        print(f"{name} not found in the data.")

    def delete_record(self):
        name = input("Enter Name to delete record: ")
        for result in self.results:
            if result.name == name:
                self.results.remove(result)
                print(f"Record for {name} deleted successfully.")
                return
        print(f"{name} not found in the data.")

    def save_to_file(self, filename="sat_results.json"):
        with open(filename, 'w') as file:
            json.dump([result.__dict__ for result in self.results], file, indent=2)
        print(f"Data saved to {filename}.")

def main():
    manager = SATResultsManager()

    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Save to file")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.insert_data()
        elif choice == "2":
            manager.view_all_data()
        elif choice == "3":
            manager.get_rank()
        elif choice == "4":
            manager.update_score()
        elif choice == "5":
            manager.delete_record()
        elif choice == "6":
            manager.save_to_file()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
