
from functools import partial
from PySide6.QtCore import Qt

class Controller:
    def __init__(self,view,model) -> None:
        self._view = view
        self._model = model
        self._connectToggle()
        self._constantSettings()
        self._applybuttonspage()
        self._runtimerfromsp()
        
        
        
        
    def _connectToggle(self):
        self._view.ui.ToggleButton.clicked.connect(self._view.toggleMenu)
        self._view.ui.SettingsButton.clicked.connect(self._view.toggleMenu)
        self._view.ui.maximizeButton.clicked.connect(self._view.maximize_windowsize)
        self._view.ui.closeButton.clicked.connect(self._view.close)
        self._view.ui.minimizeButton.clicked.connect(self._view.showMinimized)
        
    def _constantSettings(self):
        self._view.enable_shadow_effect(self._view.ui.LeftMenuFrame,50,10,5,80)
        self._view.ui.titleframe.mouseMoveEvent = self.moveWindow
        self._view.splashscreen.sp.main_frame.mouseMoveEvent = self._view.splashscreen.moveWindow
        self._view.replaceWidgetsToCustom()
        self._view.enable_shadow_effect(self._view.ui.background,10,5,5,80)
        self._view.enable_shadow_effect(self._view.splashscreen,10,5,5,80)
        self._view.enable_shadow_effect(self._view.splashscreen.sp.progressBar,10,5,5,80)
        self._view.enable_shadow_effect(self._view.ui.select_conn_frame,10,5,5,80)
        
        
        
    def _applybuttonspage(self):
        self._model.get_all_menu_buttons(self._view.ui.buttonsframe)
        for button in self._model.all_menu_buttons:
            button.clicked.connect(partial(self._view.changePage,button))
            
    def _runtimerfromsp(self):
        self._view.splashscreen.timer.timeout.connect(self._view.splashscreen.progress)
        
        
    def moveWindow(self,event):
        if self._view.isMaximized(): self._view.maximize_restore()
        if event.buttons() == Qt.LeftButton:
            self._view.move(self._view.pos() + event.globalPos() - self._view.dragPos)
            self._view.dragPos = event.globalPos()
            event.accept()
            
    
        
    
        
    
