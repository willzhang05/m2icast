from django.db import models


class Source(models.Model):
    source = models.GenericIPAddressField()
    group = models.GenericIPAddressField()
    #st = stats.split(',')
    speed = models.IntegerField()
    pps = models.IntegerField()
    packets = models.IntegerField()
    router = models.GenericIPAddressField()
    '''def __init__(self, source, group, stats, router):
        self.source = source
        self.group = group
        st = stats.split(',')
        self.speed = int(re.sub(r'[^0-9]', '', st[0]))
        self.pps = int(re.sub(r'[^0-9]', '', st[1]))
        self.packets = int(re.sub(r'[^0-9]', '', st[2]))
        self.router = router
    '''

    def __repr__(self):
        #return 'Group: {0:25s}\tSource: {1:25s}\tRouter: {2:18s}\tPackets/Second: {3:6d}'.format(self.group, self.source, self.router, self.pps)
        return ','.join([self.group, self.source, self.router, str(self.pps)])

    def __str__(self):
        #return '{0:25s}\t{1:25s}\t{2:18s}\t{3:6d}'.format(self.group, self.source, self.router, self.pps)
        #return '{0:25s}\t{1:25s}\t{2:18s}\t{3:6d}'.format(self.group, self.source, self.router, self.pps)
        return ','.join([self.group, self.source, self.router, str(self.pps)])

    def __eq__(self, other):
        return self.source == other.source and self.group == other.group and self.router == self.router

    def __lt__(self, other):
        return self.group < other.group

    def __hash__(self):
        return hash(self.__repr__())
