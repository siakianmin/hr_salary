"""Application entry point for HR Salary."""
from __future__ import annotations

import sys

from PyQt6.QtWidgets import QApplication

from hr_salary.ui.main_window import MainWindow
from hr_salary.ui.theme import apply_approved_theme


def main() -> int:
    """Start the HR Salary desktop application."""
    app = QApplication(sys.argv)
    app.setApplicationName("HR Salary")
    app.setOrganizationName("HR Salary")
    apply_approved_theme()
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
