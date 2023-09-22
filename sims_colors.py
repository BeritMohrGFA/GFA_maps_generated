from qgis.core import QgsColorScheme
from PyQt5.QtGui import QColor


class QgsSimsColorScheme(QgsColorScheme):

    def __init__(self, parent=None):
        QgsColorScheme.__init__(self)


    def schemeName(self):
        return 'GFA Colors'


    def fetchColors(self,context='', basecolor=QColor()):
        return [[QColor('#e32219'),'Go 485C'],
                    [QColor('#1F497D'),'GFA Blue'], # Blue
                    [QColor('#F39200'),'GFA Orange'], # orange
        ]

    def flags(self):
        return QgsColorScheme.ShowInAllContexts


    def clone(self):
        return QgsSimsColorScheme()
