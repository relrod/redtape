from securitas.representation import Representation

class Group(Representation):
    @property
    def name(self):
        return self._attr('cn')

    @property
    def description(self):
        return self._attr('description')

    @property
    def members(self):
        '''
        NOTE:
        This won't exist (will throw!) if we call group_find with all=False
        '''
        return self._attrlist('member_user')

    @property
    def sponsors(self):
        '''
        NOTE:
        This won't exist (will throw!) if we call group_find with all=False
        '''
        return self._attrlist('membermanager_user')

    @property
    def dn(self):
        if 'dn' in self.raw:
            return self.raw['dn']
        return None
