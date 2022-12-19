import sys
from app import App
from PyQt5 import QtWidgets
        
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()