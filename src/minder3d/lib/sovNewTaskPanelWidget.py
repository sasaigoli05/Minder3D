from PySide6.QtWidgets import QWidget

from .sovImageProcessPanelWidget import ImageProcessPanelWidget
from .sovIndexedOrgansPanelWidget import IndexedOrgansPanelWidget
from .sovOtsuPanelWidget import OtsuPanelWidget
from .sovTotalSegmentatorPanelWidget import TotalSegmentatorPanelWidget
from .sovUtils import time_and_log
from .ui_sovNewTaskPanelWidget import Ui_NewTaskPanelWidget


class NewTaskPanelWidget(QWidget, Ui_NewTaskPanelWidget):
    def __init__(self, gui, state, parent=None):
        """Initialize the GUI and state for the parent widget.

        Args:
            gui: The graphical user interface object.
            state: The state object.
            parent: The parent widget (default is None).
        """

        super().__init__(parent)
        self.setupUi(self)

        self.gui = gui
        self.state = state

        self.newTaskTotalSegmentatorButton.clicked.connect(
            self.add_total_segmentator_panel
        )
        self.newTaskIndexedOrgansButton.clicked.connect(
            self.add_indexed_organs_panel
        )
        self.newTaskOtsuButton.clicked.connect(self.add_otsu_panel)
        self.newTaskImageProcessButton.clicked.connect(
            self.add_image_process_panel
        )

    @time_and_log
    def add_total_segmentator_panel(self):
        if self.gui.totalSegmentatorPanel is None:
            self.gui.totalSegmentatorPanel = TotalSegmentatorPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.totalSegmentatorPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.totalSegmentatorPanel, 'Total Segmentator'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.totalSegmentatorPanel)

    def add_indexed_organs_panel(self):
        if self.gui.indexedOrgansPanel is None:
            self.gui.indexedOrgansPanel = IndexedOrgansPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.indexedOrgansPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.indexedOrgansPanel, 'Total Segmentator'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.indexedOrgansPanel)

    @time_and_log
    def add_image_process_panel(self):
        """Add an image processing panel to the GUI if it does not already exist.

        If the image processing panel does not exist, it creates a new ImageProcessPanelWidget and adds it to the tab widget.
        If the image processing panel already exists, it sets the current widget to the existing panel.

        Args:
            self (object): The current instance of the class.
        """

        if self.gui.imageProcessPanel is None:
            self.gui.imageProcessPanel = ImageProcessPanelWidget(
                self.gui, self.state
            )
        if self.gui.tabWidget.indexOf(self.gui.imageProcessPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.imageProcessPanel, 'Image Processing'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.imageProcessPanel)

    @time_and_log
    def add_otsu_panel(self):
        """Add Otsu panel to the GUI tab widget if it doesn't already exist.

        If the Otsu panel does not exist, it creates a new OtsuPanelWidget and adds it to the tab widget.
        If the Otsu panel already exists, it sets the current widget to the Otsu panel.

        Args:
            self (object): The instance of the class.
        """

        if self.gui.otsuPanel is None:
            self.gui.otsuPanel = OtsuPanelWidget(self.gui, self.state)
        if self.gui.tabWidget.indexOf(self.gui.otsuPanel) == -1:
            indx = self.gui.tabWidget.indexOf(self.gui.newTaskTab)
            self.gui.tabWidget.insertTab(
                indx, self.gui.otsuPanel, 'Otsu Threshold'
            )
            self.gui.tabWidget.setCurrentWidget(self.gui.otsuPanel)
