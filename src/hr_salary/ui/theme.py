"""HR Salary application theme matched to the approved HR_SQL_EN visual system.

This module intentionally reproduces the approved light-cyan/white visual language
without importing or modifying HR_SQL_EN.
"""
from __future__ import annotations

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication


def apply_approved_theme() -> None:
    """Apply the HR_SQL_EN-approved visual theme to HR Salary."""
    app = QApplication.instance()
    if app is None:
        return
    app.setFont(QFont("Segoe UI", 10))
    app.setStyleSheet(
        """
        QMainWindow, QDialog, QWidget { background: #F3FCFE; color: #17324D; }
        QWidget#appRoot, QWidget#contentArea { background: #F6FCFD; }
        QFrame#sidebar { background: #EAF8FB; border-right: 1px solid #B7DEE5; }
        QLabel#sidebarBrand { color: #075985; font-size: 20px; font-weight: 700; }
        QLabel#sidebarVersion { color: #5D7885; font-size: 11px; }
        QPushButton#sidebarNav { background: transparent; border: 0; border-radius: 6px; color: #173B56; text-align: left; padding: 9px 12px; font-weight: 500; }
        QPushButton#sidebarNav:hover { background: #D7F2F6; }
        QPushButton#sidebarNav:checked { background: #0E7490; color: white; font-weight: 700; }
        QFrame#sidebarInfoCard { background: #F8FEFF; border: 1px solid #9FD4DE; border-radius: 7px; }
        QLabel#topbarTitle { color: #52717E; font-size: 12px; font-weight: 600; }
        QPushButton#homeButton { background: #F7FDFE; border: 1px solid #79C2CE; border-radius: 6px; padding: 8px 18px; }
        QPushButton#homeButton:hover { background: #E0F5F8; }

        QMenuBar, QMenu { background: #F3FCFE; color: #17324D; border: 0; }
        QMenuBar { border-bottom: 1px solid #C7E6EB; }
        QMenuBar::item { padding: 8px 12px; }
        QMenuBar::item:selected, QMenu::item:selected { background: #D8F2F6; }

        QTabWidget::pane { background: transparent; border: 0; }
        QTabBar::tab { background: #E3F5F8; border: 1px solid #B6DCE3; padding: 8px 14px; }
        QTabBar::tab:selected { background: #0E7490; color: white; font-weight: 700; }

        QLabel#pageTitle, QLabel#homeTitle { color: #075985; font-size: 24px; font-weight: 700; }
        QLabel#pageSubtitle { color: #557684; font-size: 12px; }
        QLabel#databasePath { color: #4D6F7C; }

        QFrame#workAreaCard, QFrame#systemInfoCard, QFrame#metricCard,
        QGroupBox, QFrame#contentCard {
            background: #FFFFFF; border: 1px solid #B7DEE5; border-radius: 8px;
        }
        QFrame#workAreaCard:hover { border: 1px solid #69BCC9; background: #FBFEFF; }
        QLabel#workAreaTitle { color: #075985; font-size: 14px; font-weight: 700; }
        QLabel#workAreaDescription { color: #425F6B; }
        QLabel#systemInfoLabel { color: #075985; font-weight: 700; }
        QLabel#systemInfoValue { color: #17324D; font-weight: 600; }
        QLabel#systemReady { color: #138A5B; font-weight: 700; }

        QGroupBox { margin-top: 12px; padding: 14px; font-weight: 700; }
        QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 6px; color: #075985; }
        QLabel#metricTitle { color: #587783; font-size: 11px; font-weight: 700; }
        QLabel#metricValue { color: #0B3D52; font-size: 20px; font-weight: 700; }
        QFrame#metricCard { padding: 4px; }

        QLineEdit, QComboBox, QDateEdit, QTimeEdit, QDoubleSpinBox, QSpinBox {
            background: #FFFFFF; color: #17324D; border: 1px solid #9BCFD8; border-radius: 4px; padding: 6px 8px;
        }
        QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus,
        QDoubleSpinBox:focus, QSpinBox:focus { border: 1px solid #0E7490; }
        QComboBox::drop-down { border: 0; width: 26px; }

        QPushButton { background: #EFF9FB; color: #173B49; border: 1px solid #79C2CE; border-radius: 5px; padding: 8px 14px; }
        QPushButton:hover { background: #DDF4F7; border-color: #4BA8B8; }
        QPushButton:pressed { background: #CDECF1; }
        QPushButton#cardActionButton { background: #F0FAFC; color: #075985; font-weight: 600; }
        QPushButton#primaryButton { background: #0E7490; color: white; border-color: #0E7490; font-weight: 700; }
        QPushButton#primaryButton:hover { background: #0B647A; }

        QTableWidget, QTableView, QTextBrowser { background: #FFFFFF; alternate-background-color: #F0FAFC; border: 1px solid #B7DEE5; border-radius: 5px; gridline-color: #D6EDF1; }
        QHeaderView::section { background: #DDF3F6; color: #17475A; border: 0; border-right: 1px solid #B7DEE5; border-bottom: 1px solid #B7DEE5; padding: 7px; font-weight: 700; }
        QTableWidget::item:selected { background: #CDECF1; color: #12384A; }

        QStatusBar { background: #F6FCFD; color: #52717E; border-top: 1px solid #D2E9ED; }
        QToolTip { background: #173B49; color: white; border: 0; padding: 5px; }
        """
    )
