import wx
import GUI
import sqlite3

dbconn = sqlite3.connect("E:/data kuliah/semester 4/PBO 2/Project/DB/db_test.db")


app = wx.App()

class LoginFrame(GUI.LoginFrame):
    def __init__(self, parent):
        super().__init__(parent)

    def goLogin(self, event):
        uname = self.uname_text.GetValue()
        pwd = self.pwd_text.GetValue()

        getUserDB = 'SELECT * FROM User WHERE username="%s" AND password="%s"' % (uname, pwd)
        getAdminDB = 'SELECT * FROM Admin WHERE username = "%s" AND password = "%s"' % (uname, pwd)

        cur = dbconn.cursor()
        cur.execute(getUserDB)
        if (len(list(cur)) < 1):
            curs = dbconn.cursor()
            curs.execute(getAdminDB)
            if (len(list(curs)) > 0):
                print('admin ada')
                FrameMainAdmin.Show()
                FrameLogin.Hide()
                for row in dbconn.execute(getAdminDB):
                    FrameMainAdmin.adminName_placeholder.SetLabel(row[3])
            else:
                wx.MessageBox('Username / password salah!')

        else:
           FrameMainUser.Show()
           FrameLogin.Hide()
           for row in dbconn.execute(getUserDB):
               FrameMainUser.nama_placeholder.SetLabel(row[3])
               FrameMainUser.username_placeholder.SetLabel(row[1])
           
           print('user ada')

    def aboutBtn(self, event):
        wx.MessageBox(' --- CHANDRAEL --- ')

class MainFrameAdmin(GUI.MainFrameAdmin):
    def __init__(self, parent):
        super().__init__(parent)

    def goLogOut(self, event):
        FrameLogin.Show()
        FrameMainAdmin.Hide()
    
class MainFrameUser(GUI.MainFrameUser):
    def __init__(self, parent):
        super().__init__(parent)



#daftar Frame
FrameLogin = LoginFrame(None)
FrameMainAdmin = MainFrameAdmin(None)
FrameMainUser = MainFrameUser(None)

#mainLoop frame utama
FrameLogin.Show()
app.MainLoop()
    