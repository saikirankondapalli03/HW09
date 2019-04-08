class Major: 
    def __init__(self, major):
        '''
        constructor for setting values
        '''
        self.major= major
        self.electives= list()
        self.required = list()
    
    def __str__(self):
        return (f"Major name: {self.major}  electives: {self.electives}  Required: {self.required}")


    def details(self):
        return [self.major,sorted(self.required), sorted(self.electives)]
            
    def add_course(self,required,course_name):
        if(required == 'R'):
            if course_name not in self.required:
                self.required.append(course_name)
        else:
            if course_name not in self.electives:
                self.electives.append(course_name)
