import pandas
import os

CSV_HEADER = ["path", "name", "gnome"]


class Data:
    def __init__(self):
        """Check if the csv file is present, if not create on"""
        if not os.path.exists("cmd_path.csv"):
            terminal = input("Are you on a Gnome environment(Ubuntu, PopOS)? If not, you need to have xterm installed!"
                             "\nType 'y' or 'n' ").lower()
            if terminal == "y":
                dataframe = pandas.DataFrame(columns=["path", "name", "gnome"])
            else:
                dataframe = pandas.DataFrame(columns=["path", "name", "xterm"])
            dataframe.to_csv("cmd_path.csv")
        self.script_data = pandas.read_csv("cmd_path.csv")  # TODO Remove this?
        self.read_csv()

    def read_csv(self):
        """Read the CSV file and print the content"""
        self.script_data = pandas.read_csv("cmd_path.csv")
        for (index, row) in self.script_data.iterrows():
            print(f"{index + 1}. {row['name']}")
        self.number_of_row = len(self.script_data["name"])

    def add_to_csv(self):
        """Add a command to the CSV file"""
        # TODO Check that it's functioning well
        path = input("Enter script path or command: ")
        name = input("Enter the name of the application: ")
        new_row = {f"path": path, "name": name}
        self.script_data = self.script_data.append(new_row, ignore_index=True)
        self.update_csv_file()

    def remove_to_csv(self):
        """Remove a command to the CSV file"""
        # TODO Check that it's functioning well
        row = int(input(f"Which application would you like to remove? Type 1 to {len(self.script_data['name'])}: "))
        self.script_data = self.script_data.drop([row - 1])
        # self.script_data.to_csv("cmd_path.csv", header=True, index=False)
        # print(self.script_data)
        self.update_csv_file()

    def update_csv_file(self):
        """Write the CSV  with the new value"""
        self.script_data.to_csv("cmd_path.csv", header=True, index=False)