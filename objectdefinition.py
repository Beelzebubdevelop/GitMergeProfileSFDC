class applicationVisibilities:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '1'

    def key(self):
        return 'application'

    def instancename(self):
        return 'applicationVisibilities'


class recordTypeVisibilities:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '9'

    def key(self):
        return 'recordType'

    def instancename(self):
        return 'recordTypeVisibilities'


class fieldPermissions:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '4'

    def key(self):
        return 'field'

    def instancename(self):
        return 'fieldPermissions'


class classAccesses:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '2'

    def key(self):
        return 'apexClass'

    def instancename(self):
        return 'classAccesses'


class userPermissions:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '12'

    def key(self):
        return 'name'

    def instancename(self):
        return 'userPermissions'


class customPermissions:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '13'

    def key(self):
        return 'name'

    def instancename(self):
        return 'customPermissions'


class tabVisibilities:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '10'

    def key(self):
        return 'tab'

    def instancename(self):
        return 'tabVisibilities'


class pageAccesses:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '8'

    def key(self):
        return 'apexPage'

    def instancename(self):
        return 'pageAccesses'


class loginIpRanges:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '6'

    def key(self):
        return 'endAddress'

    def instancename(self):
        return 'loginIpRanges'    


class layoutAssignments:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '5'

    def key(self):
        return 'recordType'

    def instancename(self):
        return 'layoutAssignments'


class objectPermissions:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '7'

    def key(self):
        return 'object'

    def instancename(self):
        return 'objectPermissions'


class userLicense:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '11'

    def key(self):
        return 'userLicense'

    def instancename(self):
        return 'userLicense'

        
class custom:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '3'

    def key(self):
        return 'custom'

    def instancename(self):
        return 'custom'

class fullName:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '3'

    def key(self):
        return 'fullName'

    def instancename(self):
        return 'fullName'

class externalDataSourceAccesses:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '3'

    def key(self):
        return 'externalDataSource'

    def instancename(self):
        return 'externalDataSourceAccesses'

class flowAccesses:
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)
    
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __lt__(self, other):
        return self.outputvalue() > other.outputvalue()

    def outputvalue(self):
        return '3'

    def key(self):
        return 'flow'

    def instancename(self):
        return 'flowAccesses'


def oneLineTag(obj):
    return isinstance(obj, userLicense) or isinstance(obj, custom) or isinstance(obj, fullName)