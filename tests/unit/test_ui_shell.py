"""Regression checks for the Stage 1 HR Salary UI shell."""
from __future__ import annotations

import os

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PyQt6.QtWidgets import QApplication

from hr_salary.ui.main_window import MainWindow
from hr_salary.ui.theme import apply_approved_theme


def test_main_window_contains_all_approved_work_areas() -> None:
    app = QApplication.instance() or QApplication([])
    apply_approved_theme()
    window = MainWindow()

    expected = {
        "home",
        "master",
        "import",
        "setup",
        "processing",
        "review",
        "payslip",
        "reports",
        "payment",
        "database",
        "system",
    }
    assert set(window.subject_tabs) == expected
    assert set(window.nav_buttons) == expected
    assert window.width() >= 1180
    window.close()
