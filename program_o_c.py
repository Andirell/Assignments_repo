class Election:
    def __init__(self, name, age, position, party):
        self.name = name 
        self.age = age
        self.position = position 
        self.party = party

    def __str__(self):
        return "Election Candidate"
    
class Candidate:
    def __init__(self):
        self.list_of_candidates = []

    def add_candidates(self):
        # getting data from inputs
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        position = input("Enter your position: ")
        party = input("Enter your party: ")

        # creating an instance of election
        election_candidates = Election(name, age, position, party)


        self.list_of_candidates.append(election_candidates)


        print(f"{"~~" * 32}\n{name} added to Candidate list.\n{"~~" * 32}")
    

    def view_candidates(self):
        # if not self.list_of_candidates:
        if len(self.list_of_candidates) == 0:
            print(f"{"~~" * 32}\nThere are no Candidate.\n{"~~" * 32}")
            return
        
        print(
            "~~" * 44
        )

        for index, election_candidates in enumerate (self.list_of_candidates):
            print(f"{index + 1}. Name:{election_candidates.name}, Age: {election_candidates.age}years, Position: Aspiring {election_candidates.position}, Party: {election_candidates.party}")

        print(
            "~~" * 44
        )
    

    def disqualify_candidates(self):
        if len(self.list_of_candidates) == 0:
            print(f"{"~~" * 32}\nThere are no Candidate to be disqualified in the list.\n{"~~" * 32}")
            return
        
        print(
            "~~" * 44
        )

        for candidate in self.list_of_candidates:
            if int(candidate.age) < 35:
                print(f"{candidate.name} is not up to 50years old and is disqualified.")


    def run(self):
        while True:
            menu = input("1. Add Candidate: \n2. View Candidates\n3. Disqualify Candidates. \n4. Exit. \nChoose an option(1|2|3|4) ")

            match menu:
                case "1":
                    self.add_candidates()
                case "2":
                    self.view_candidates()
                case "3":
                    self.disqualify_candidates()
                case "4":
                    break


candidate = Candidate()
candidate.run()