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

    def key(self):
        return 'custom'

    def instancename(self):
        return 'custom'


def oneLineTag(obj):
    return isinstance(obj, userLicense) or isinstance(obj, custom)