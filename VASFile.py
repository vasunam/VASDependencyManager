import re

class VASFile:

    def __init__(self, path):
        self.path = path
        self.filename = path.split('\\')[-1]
        # self.raw_contents = get_content(path)
        # self.dependencies = get_dependencies(self.raw_contents)
        
    def get_content(self):
        f = open(self.path, "r")
        self.raw_content = f.read()

    def get_dependencies(self):
        dependencies = []
        dependencies_in_angular_quotes = []
        dependencies_in_angular_braces = re.findall('\<(.*?)\>', self.raw_content)
        print(self.raw_content)
        for line in self.raw_content.split("\n"):
            if line[0]=='#':
                dependencies_in_angular_quotes.append = re.find(r'"([^"]*)"', line)
        self.dependencies = dependencies_in_angular_braces+dependencies_in_angular_quotes