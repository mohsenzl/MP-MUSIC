import  os
import  threading
import  time
import PyQt5 as qt

from PyQt5.QtWidgets import QFileDialog , QAction
from PyQt5 import QtWidgets,QtGui,QtCore
from mutagen.mp3 import MP3
from pygame import mixer
from PIL import Image
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from stagger import read_tag
from io import BytesIO

class MUSIC_PLAYER:
    def __init__(self, QtWnd):
        self.AddressList = list()
        self.NameList = list()
        self.playLists = {}
        self.paused = False
        self.QtWindow = QtWnd
        self.albumPicSize = (256, 256)
        self.baseElemRow = 0
        self.artist = {
            'unknown':[]
        }
        self.album = {
            'unknown':[]
        }
        self.genre = {
            'unknown':[]
        }

        self.QtWindow.setWindowTitle("MP MUSIC")

        #initializing the mixer
        mixer.init()

        self.QtWindow.QtWidgets.setFixedSize(640, 480)

        # making the menu
        ExitBtn = QAction('&Close', self)
        ExitBtn.setShortcut('esc')
        ExitBtn.setStatusTip('Exit')
        ExitBtn.triggered.connect(QtWidgets.qApp.quit)

        ########### important     :      connect to playlists later
        OpenBtn = QAction('&Open', self)
        OpenBtn.setStatusTip('Open File')
        OpenBtn.triggered.connect(self.music_getter)

        makePlayLitsBtn = QAction('&New PlayList', self)
        makePlayLitsBtn.setStatusTip('Make a new playlist')
        makePlayLitsBtn.triggered.connect(self.new_playlist)

    def music_getter(self):
        files_getter = QFileDialog.getOpenFileNames()
        for address in files_getter:
            if file[len(file) - 4:] == '.mp3' or file[len(file) - 4:] == '.wav':
                self.AddressList.append(address)
                tags = read_tag(address)
                self.NameList.append(tags.title)
                if tags.genre != '':
                    if tags.genre in self.genres.keys():
                        self.genres[tags.genre].append(file)
                    else:
                        self.genres[tags.genre] = []
                        self.genres[tags.genre].append(file)
                else:
                    self.genres['unknown'].append(file)
                if tags.artist != '':
                    if tags.artist in self.artists:
                        self.artists[tags.artist].append(file)
                    else:
                        self.artists[tags.artist] = []
                        self.artists[tags.artist].append(file)
                else:
                    self.artists['unknown'].append(file)
                if tags.album != '':
                    if tags.album in self.albums:
                        self.albums[tags.album].append(file)
                    else:
                        self.albums[tags.album] = []
                        self.albums[tags.album].append(file)
                else:
                    self.albums['unknown'].append(file)
            else:
                pass

    def new_playlist(self):
        







