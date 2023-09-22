from qgis.core import QgsColorScheme
from PyQt5.QtGui import QColor


class QgsSimsColorScheme(QgsColorScheme):

    def __init__(self, parent=None):
        QgsColorScheme.__init__(self)


    def schemeName(self):
        return 'GFA Colors'


    def fetchColors(self,context='', basecolor=QColor()):
        return [[QColor('#1F497D'),'Blue Logo'], # Blue
                    [QColor('#F39200'),'Orange Logo'], # orange
                    [QColor('#00A6D0'),'Light Blue'], #
                    [QColor('#007BC4'),'Medium Blue'],
                    [QColor('#0F265C'),'Dark Blue'],
                    [QColor('#13A538'),'Dark Green'],
                    [QColor('#86BC25'),'Light Green'],
                    [QColor('#FDC300'),'Yellow warm'],
                    [QColor('#EA5B0C'),'Dark Orange'],
                    [QColor('#E30613'),'Dark Red'],
        ]

    def flags(self):
        return QgsColorScheme.ShowInAllContexts


    def clone(self):
        return QgsSimsColorScheme()
