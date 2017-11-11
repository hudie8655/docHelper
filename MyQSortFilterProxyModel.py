from PyQt5.QtCore import QSortFilterProxyModel, QDate


class MyQSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self,typeset,banset,sd,ed):
        super().__init__()
        self.bans = set(banset)
        self.types = set(typeset)
        self.sd = sd
        self.ed = ed
    def filterAcceptsRow(self, sourceRow, sourceParent):
        index_ban = self.sourceModel().index(sourceRow,4,sourceParent)
        index_date = self.sourceModel().index(sourceRow, 3, sourceParent)
        index_type = self.sourceModel().index(sourceRow, 2, sourceParent)

        return self.sourceModel().data(index_ban) in self.bans and self.sourceModel().data(index_type) in self.types \
               and QDate.fromString(self.sourceModel().data(index_date),'yyyy-MM-dd') >=self.sd <= self.ed

