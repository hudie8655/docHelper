from PyQt5.QtCore import QSortFilterProxyModel


class MyQSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self,typeset,banset):
        super().__init__()
        self.bans = set(banset)
        self.types = set(typeset)
    def filterAcceptsRow(self, sourceRow, sourceParent):
        index_ban = self.sourceModel().index(sourceRow,4,sourceParent)
        index_type = self.sourceModel().index(sourceRow, 2, sourceParent)

        return self.sourceModel().data(index_ban) in self.bans and self.sourceModel().data(index_type) in self.types

