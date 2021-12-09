#!/usr/bin/env python
class person:
    def __init__ (self, name, birthday):
        self.name = name
        self.birthday = birthday

    def toString(self):
        print(self.name + "'s birthday is on " + self.birthday)

#p1 = person("Ng Shien Ming", "02/06/2002")
#p1.toString()
print(__name__)