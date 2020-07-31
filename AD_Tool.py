import os
from PyQt5 import QtWidgets
from AD_Tool_UI import Ui_AD_Tool

class AdTool(QtWidgets.QWidget, Ui_AD_Tool):
    def  __init__ (self):
        super(AdTool, self).__init__()
        self.setupUi(self)
        self.le_inputUsername.returnPressed.connect(self.Inquiry)
        self.le_inputPassword.returnPressed.connect(self.ResetPassword)
        self.bt_inquiry.clicked.connect(self.Inquiry)
        self.bt_resetPassword.clicked.connect(self.ResetPassword)

    def Inquiry(self):
        username = self.le_inputUsername.text()
        if username != '':
            cmd = 'net user ' + username + ' /domain'
            buf = os.popen(cmd)
            print(cmd)
            result = buf.read()
            if len(result) > 50:
                self.te_showDetails.setText(result)
            else:
                self.te_showDetails.setText('用户名不存在！')
        else:
            self.te_showDetails.setText('请输入用户名！')

    def ResetPassword(self):
        pass

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    ui = AdTool()    
    ui.show()
    sys.exit(app.exec_())