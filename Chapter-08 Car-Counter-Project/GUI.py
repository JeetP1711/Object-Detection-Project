import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QGridLayout,
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

class TrafficManagementApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Traffic Management System")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Traffic Management System")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Camera Selection
        self.camera_label = QLabel("Selected Camera: 1")
        layout.addWidget(self.camera_label)
        camera_layout = QHBoxLayout()
        for i in range(1, 5):
            btn = QPushButton(f"Camera {i}")
            btn.clicked.connect(lambda _, cam=i: self.change_camera(cam))
            camera_layout.addWidget(btn)
        layout.addLayout(camera_layout)

        # Traffic Signal Status
        layout.addWidget(QLabel("Traffic Signal Status"))
        self.traffic_data = {
            "North": {"count": 12, "signal": "red"},
            "South": {"count": 8, "signal": "green"},
            "East": {"count": 5, "signal": "red"},
            "West": {"count": 3, "signal": "red"},
        }
        grid_layout = QGridLayout()
        self.signal_labels = {}
        for i, (direction, data) in enumerate(self.traffic_data.items()):
            label = QLabel(f"{direction}: {data['count']} vehicles")
            label.setStyleSheet(f"color: {data['signal']}")
            self.signal_labels[direction] = label
            grid_layout.addWidget(label, i // 2, i % 2)
        layout.addLayout(grid_layout)

        # Traffic Violations Table
        layout.addWidget(QLabel("Traffic Violations"))
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Vehicle Number", "Violation", "Time", "Status"])
        self.populate_table()
        layout.addWidget(self.table)

        self.setLayout(layout)

    def change_camera(self, cam):
        self.camera_label.setText(f"Selected Camera: {cam}")

    def populate_table(self):
        violations = [
            ("ABC-123", "Red Light Violation", "14:30", "Pending"),
            ("XYZ-789", "Speed Limit Exceeded", "14:45", "Generated"),
        ]
        self.table.setRowCount(len(violations))
        for row, (vehicle, violation, time, status) in enumerate(violations):
            self.table.setItem(row, 0, QTableWidgetItem(vehicle))
            self.table.setItem(row, 1, QTableWidgetItem(violation))
            self.table.setItem(row, 2, QTableWidgetItem(time))
            status_item = QTableWidgetItem(status)
            if status == "Generated":
                status_item.setBackground(QColor("green"))
            else:
                status_item.setBackground(QColor("yellow"))
            self.table.setItem(row, 3, status_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrafficManagementApp()
    window.show()
    sys.exit(app.exec())