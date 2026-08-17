"""Main HR Salary desktop window.

Stage 1 builds the approved navigation shell and screen structure only. Business
logic will be connected behind these screens in later approved stages.
"""
from __future__ import annotations

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class MetricCard(QFrame):
    def __init__(self, title: str, value: str = "—", parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("metricCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        title_label = QLabel(title)
        title_label.setObjectName("metricTitle")
        value_label = QLabel(value)
        value_label.setObjectName("metricValue")
        layout.addWidget(title_label)
        layout.addWidget(value_label)


class MainWindow(QMainWindow):
    """HR Salary application shell using the approved HR_SQL_EN theme."""

    NAV_ITEMS = (
        ("home", "Dashboard"),
        ("master", "Master Data"),
        ("import", "HR_SQL_EN Import"),
        ("setup", "Payroll Setup"),
        ("processing", "Payroll Processing"),
        ("review", "Payroll Review"),
        ("payslip", "Payslip"),
        ("reports", "Reports"),
        ("payment", "Payment"),
        ("database", "Database Tools"),
        ("system", "System"),
    )

    PAGE_DETAILS = {
        "master": (
            "Master Data",
            "Maintain employee salary profiles, salary components, departments, designations and payment information.",
            ("Employee Salary Profile", "Salary Components", "Departments & Designations", "Bank / Payment Information"),
        ),
        "import": (
            "HR_SQL_EN Data Import",
            "Receive controlled employee, attendance, overtime and leave data while keeping both programs stand-alone.",
            ("Employee Master Import", "Attendance Summary Import", "Overtime Import", "Leave Summary Import", "Validation & Import History"),
        ),
        "setup": (
            "Payroll Setup",
            "Configure payroll periods, salary rules and statutory calculation settings.",
            ("Payroll Period", "Salary Calculation Rules", "Overtime Rates", "Allowance & Deduction Rules", "EPF / SOCSO / EIS / PCB Settings"),
        ),
        "processing": (
            "Payroll Processing",
            "Run the controlled payroll workflow from imported data through calculation and finalisation.",
            ("1. Import Data", "2. Verify", "3. Adjust", "4. Calculate", "5. Review", "6. Finalise", "7. Payslip / Payment"),
        ),
        "review": (
            "Payroll Review",
            "Review each employee's salary calculation before payroll is finalised.",
            ("Basic Salary", "Overtime", "Allowances", "Deductions", "EPF / SOCSO / EIS / PCB", "Net Salary"),
        ),
        "payslip": (
            "Payslip",
            "Preview and prepare individual or batch employee payslips.",
            ("Payslip Preview", "Individual Payslip", "Batch Payslip", "PDF Output"),
        ),
        "reports": (
            "Reports",
            "Access payroll, statutory, employee and management reporting from one workspace.",
            ("Payroll Summary", "Employee Salary Detail", "Allowance & Deduction", "Overtime", "Statutory Reports", "Department Payroll Cost"),
        ),
        "payment": (
            "Payment",
            "Prepare salary payment listings and retain payment status and history.",
            ("Bank Payment Listing", "Payment Export", "Payment Status", "Payment History"),
        ),
        "database": (
            "Database Tools",
            "Maintain the independent HR Salary database with controlled backup, restore and audit functions.",
            ("Database Backup", "Database Restore", "Import / Export", "Audit Log", "Database Maintenance"),
        ),
        "system": (
            "System",
            "Configure company information, access controls and application settings.",
            ("User Access", "Company Information", "Payroll Settings", "About / Version"),
        ),
    }

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("HR Salary")
        self.resize(1440, 900)
        self.setMinimumSize(1180, 720)
        self.nav_buttons: dict[str, QPushButton] = {}
        self.subject_tabs: dict[str, int] = {}
        self._build_ui()

    def _build_ui(self) -> None:
        root = QWidget()
        root.setObjectName("appRoot")
        shell = QHBoxLayout(root)
        shell.setContentsMargins(0, 0, 0, 0)
        shell.setSpacing(0)

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(238)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(14, 18, 14, 18)
        sidebar_layout.setSpacing(8)

        brand = QLabel("HR Salary")
        brand.setObjectName("sidebarBrand")
        version = QLabel("Version 0.1.0")
        version.setObjectName("sidebarVersion")
        sidebar_layout.addWidget(brand)
        sidebar_layout.addWidget(version)
        sidebar_layout.addSpacing(12)

        for key, label in self.NAV_ITEMS:
            button = QPushButton(label)
            button.setObjectName("sidebarNav")
            button.setCheckable(True)
            button.setMinimumHeight(42)
            button.clicked.connect(lambda checked=False, k=key: self.open_subject(k))
            sidebar_layout.addWidget(button)
            self.nav_buttons[key] = button

        sidebar_layout.addStretch(1)
        info_card = QFrame()
        info_card.setObjectName("sidebarInfoCard")
        info_layout = QVBoxLayout(info_card)
        info_layout.setContentsMargins(12, 10, 12, 10)
        info_layout.addWidget(QLabel("HR Salary"))
        info_layout.addWidget(QLabel("Stand-alone Payroll System"))
        sidebar_layout.addWidget(info_card)

        content = QWidget()
        content.setObjectName("contentArea")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(26, 18, 26, 18)
        content_layout.setSpacing(12)

        topbar = QHBoxLayout()
        self.context_label = QLabel("HR Salary Workspace")
        self.context_label.setObjectName("topbarTitle")
        self.home_button = QPushButton("Home")
        self.home_button.setObjectName("homeButton")
        self.home_button.setMinimumWidth(96)
        self.home_button.clicked.connect(lambda: self.open_subject("home"))
        topbar.addWidget(self.context_label)
        topbar.addStretch(1)
        topbar.addWidget(self.home_button)
        content_layout.addLayout(topbar)

        self.tabs = QTabWidget()
        self.tabs.setObjectName("contentTabs")
        self.tabs.setUsesScrollButtons(True)
        self.tabs.tabBar().hide()

        self.subject_tabs["home"] = self.tabs.addTab(self._home_page(), "Dashboard")
        for key, _label in self.NAV_ITEMS[1:]:
            title, subtitle, sections = self.PAGE_DETAILS[key]
            self.subject_tabs[key] = self.tabs.addTab(
                self._standard_page(title, subtitle, sections), title
            )

        content_layout.addWidget(self.tabs, 1)
        shell.addWidget(sidebar)
        shell.addWidget(content, 1)
        self.setCentralWidget(root)

        self.setStatusBar(QStatusBar())
        self.operation_status = QLabel("HR Salary ready")
        self.statusBar().addPermanentWidget(self.operation_status)
        self.open_subject("home")

    def _home_page(self) -> QWidget:
        page = QWidget()
        page.setObjectName("dashboardPage")
        layout = QVBoxLayout(page)
        layout.setContentsMargins(8, 4, 8, 8)
        layout.setSpacing(16)

        heading = QLabel("Welcome to HR Salary")
        heading.setObjectName("pageTitle")
        subtitle = QLabel("Prepare, review and finalise payroll from one consistent workspace.")
        subtitle.setObjectName("pageSubtitle")
        layout.addWidget(heading)
        layout.addWidget(subtitle)

        quick = QGridLayout()
        quick.setHorizontalSpacing(14)
        quick.setVerticalSpacing(14)
        actions = (
            ("import", "Import HR Data", "Bring approved employee, attendance, overtime and leave summaries into payroll."),
            ("setup", "Payroll Setup", "Maintain salary structures, calculation rules and statutory settings."),
            ("processing", "Process Payroll", "Prepare the selected payroll period and run salary calculations."),
            ("review", "Review Payroll", "Check employee-by-employee calculations before finalisation."),
            ("reports", "Reports", "Open payroll, statutory and management reports."),
        )
        for i, (key, title, description) in enumerate(actions):
            card = QFrame()
            card.setObjectName("workAreaCard")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(18, 16, 18, 16)
            card_layout.setSpacing(8)
            card_title = QLabel(title)
            card_title.setObjectName("workAreaTitle")
            card_desc = QLabel(description)
            card_desc.setObjectName("workAreaDescription")
            card_desc.setWordWrap(True)
            open_button = QPushButton(f"Open {title}")
            open_button.setObjectName("cardActionButton")
            open_button.clicked.connect(lambda checked=False, k=key: self.open_subject(k))
            card_layout.addWidget(card_title)
            card_layout.addWidget(card_desc)
            card_layout.addStretch(1)
            card_layout.addWidget(open_button)
            quick.addWidget(card, 0, i)
        layout.addLayout(quick)

        summary = QGroupBox("Current Payroll Summary")
        summary.setObjectName("summaryCard")
        summary_layout = QGridLayout(summary)
        summary_layout.setHorizontalSpacing(14)
        summary_layout.setVerticalSpacing(12)
        for i, card in enumerate((
            MetricCard("Payroll Period"),
            MetricCard("Employees"),
            MetricCard("Gross Payroll"),
            MetricCard("Net Payroll"),
        )):
            summary_layout.addWidget(card, 0, i)
        layout.addWidget(summary)

        system = QFrame()
        system.setObjectName("systemInfoCard")
        system_layout = QHBoxLayout(system)
        system_layout.setContentsMargins(18, 14, 18, 14)
        system_layout.setSpacing(18)
        database_title = QLabel("Database")
        database_title.setObjectName("systemInfoLabel")
        database_value = QLabel("hr_salary.db (SQLite)")
        database_value.setObjectName("databasePath")
        version = QLabel("Version 0.1.0")
        version.setObjectName("systemInfoValue")
        status = QLabel("UI foundation ready")
        status.setObjectName("systemReady")
        system_layout.addWidget(database_title)
        system_layout.addWidget(database_value, 1)
        system_layout.addWidget(version)
        system_layout.addWidget(status)
        layout.addWidget(system)
        layout.addStretch(1)
        return page

    def _standard_page(self, title: str, subtitle: str, sections: tuple[str, ...]) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(8, 4, 8, 8)
        layout.setSpacing(16)

        title_label = QLabel(title)
        title_label.setObjectName("pageTitle")
        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("pageSubtitle")
        subtitle_label.setWordWrap(True)
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)

        grid = QGridLayout()
        grid.setHorizontalSpacing(14)
        grid.setVerticalSpacing(14)
        for index, section in enumerate(sections):
            card = QFrame()
            card.setObjectName("workAreaCard")
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(18, 16, 18, 16)
            label = QLabel(section)
            label.setObjectName("workAreaTitle")
            label.setWordWrap(True)
            description = QLabel("UI module reserved for the next approved implementation stage.")
            description.setObjectName("workAreaDescription")
            description.setWordWrap(True)
            card_layout.addWidget(label)
            card_layout.addWidget(description)
            card_layout.addStretch(1)
            row, column = divmod(index, 3)
            grid.addWidget(card, row, column)
        layout.addLayout(grid)
        layout.addStretch(1)
        return page

    def open_subject(self, key: str) -> None:
        if key not in self.subject_tabs:
            return
        self.tabs.setCurrentIndex(self.subject_tabs[key])
        self.home_button.setEnabled(key != "home")
        label = dict(self.NAV_ITEMS).get(key, "Dashboard")
        self.context_label.setText(f"HR Salary Workspace / {label}")
        for nav_key, button in self.nav_buttons.items():
            button.setChecked(nav_key == key)
