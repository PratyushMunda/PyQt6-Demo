import sys
from pathlib import Path

from PyQt6.QtCore import QDate, QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStyle,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class PartyDetailsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Party Details")
        self.setMinimumSize(1280, 540)
        self.resize(1360, 600)

        self.party_code_input = QLineEdit()
        self.date_input = QDateEdit()
        self.party_name_input = QLineEdit()
        self.mobile_input = QLineEdit()
        self.email_input = QLineEdit()
        self.gst_input = QLineEdit()
        self.price_list_input = QComboBox()
        self.address_input = QTextEdit()

        self.price_list_input.addItems(
            ["Select Price List", "Retail", "Wholesale", "Distributor"]
        )

        self.date_input.setCalendarPopup(True)
        self.date_input.setDisplayFormat("yyyy-MM-dd")
        self.date_input.setSpecialValueText("")
        self.date_input.setMinimumDate(QDate(1900, 1, 1))
        self.date_input.setDate(self.date_input.minimumDate())
        self.address_input.setFixedSize(795, 110)
        self.address_input.document().setDocumentMargin(4)
        self._align_field_text_left()

        self._build_ui()
        self._connect_signals()
        self._apply_styles()

    def _align_field_text_left(self):
        for field in (
            self.party_code_input,
            self.party_name_input,
            self.mobile_input,
            self.email_input,
            self.gst_input,
        ):
            field.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.date_input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.address_input.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def _label(self, text):
        label = QLabel(text)
        label.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        return label

    def _icon_text_button(self, text, icon=None, width=150, height=70):
        button = QPushButton()
        button.setObjectName("actionButton")
        button.setFixedHeight(height)
        button.setMinimumWidth(width)
        button.setText("")

        button_layout = QVBoxLayout(button)
        button_layout.setContentsMargins(4, 5, 4, 5)
        button_layout.setSpacing(2)

        text_label = QLabel(text)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        if icon is None:
            button_layout.addStretch(1)
            button_layout.addWidget(text_label)
            button_layout.addStretch(1)
        else:
            icon_label = QLabel()
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            icon_label.setFixedHeight(20)
            icon_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            icon_label.setPixmap(self.style().standardIcon(icon).pixmap(QSize(18, 18)))
            button_layout.addWidget(icon_label)
            button_layout.addWidget(text_label)
        return button

    def _build_ui(self):
        root = QWidget()
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(0, 10, 0, 0)
        root_layout.setSpacing(28)

        root_layout.addLayout(self._create_top_bar())
        root_layout.addLayout(self._create_form())
        root_layout.addLayout(self._create_bottom_buttons())
        root_layout.addItem(
            QSpacerItem(1, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )

        self.setCentralWidget(root)

    def _create_top_bar(self):
        top_bar = QHBoxLayout()
        top_bar.setSpacing(0)
        top_bar.setContentsMargins(2, 0, 0, 0)

        button_specs = [
            ("New-Ctrl+N", QStyle.StandardPixmap.SP_FileIcon),
            ("Modify-Ctrl+O", QStyle.StandardPixmap.SP_FileDialogDetailedView),
            ("Delete-Ctrl+D", QStyle.StandardPixmap.SP_TrashIcon),
            ("Search-Ctrl+F", QStyle.StandardPixmap.SP_FileDialogContentsView),
            ("Print-Ctrl+P", QStyle.StandardPixmap.SP_DialogSaveButton),
            ("Top", QStyle.StandardPixmap.SP_ArrowUp),
            ("Back", QStyle.StandardPixmap.SP_ArrowLeft),
            ("Next", QStyle.StandardPixmap.SP_ArrowRight),
            ("Last", QStyle.StandardPixmap.SP_ArrowDown),
            ("Exit-Alt+F4", QStyle.StandardPixmap.SP_DialogCloseButton),
        ]

        for index, (text, icon) in enumerate(button_specs):
            button = self._icon_text_button(
                text,
                icon,
                width=78 if 5 <= index <= 8 else 150,
            )
            top_bar.addWidget(button)

            if index in (4, 8):
                top_bar.addSpacing(20)

        top_bar.addStretch(1)
        return top_bar

    def _create_form(self):
        form = QVBoxLayout()
        form.setContentsMargins(13, 0, 0, 0)
        form.setSpacing(17)

        self.party_code_input.setFixedWidth(150)
        self.date_input.setFixedWidth(150)
        self.party_name_input.setFixedWidth(400)
        self.mobile_input.setFixedWidth(150)
        self.email_input.setFixedWidth(300)
        self.gst_input.setFixedWidth(300)
        self.price_list_input.setFixedWidth(200)

        first_row = QHBoxLayout()
        first_row.setSpacing(10)
        first_row.addWidget(self._label("Party Code:"))
        first_row.addWidget(self.party_code_input)
        first_row.addWidget(self._label("Date:"))
        first_row.addWidget(self.date_input)
        first_row.addStretch(1)
        form.addLayout(first_row)

        party_name_row = QHBoxLayout()
        party_name_row.setSpacing(10)
        party_name_row.addWidget(self._label("Party Name:"))
        party_name_row.addWidget(self.party_name_input)
        party_name_row.addStretch(1)
        form.addLayout(party_name_row)

        contact_row = QHBoxLayout()
        contact_row.setSpacing(10)
        contact_row.addWidget(self._label("Mobile:"))
        contact_row.addWidget(self.mobile_input)
        contact_row.addWidget(self._label("Email:"))
        contact_row.addWidget(self.email_input)
        contact_row.addStretch(1)
        form.addLayout(contact_row)

        gst_row = QHBoxLayout()
        gst_row.setSpacing(10)
        gst_row.addWidget(self._label("GST No:"))
        gst_row.addWidget(self.gst_input)
        gst_row.addWidget(self._label("Price List:"))
        gst_row.addWidget(self.price_list_input)

        add_price_button = QPushButton("+")
        add_price_button.setObjectName("smallActionButton")
        add_price_button.setFixedSize(34, 32)
        gst_row.addWidget(add_price_button)
        gst_row.addStretch(1)
        form.addLayout(gst_row)

        address_row = QHBoxLayout()
        address_row.setSpacing(10)
        address_row.addWidget(self._label("Address:"))
        address_row.addWidget(self.address_input)
        address_row.addStretch(1)
        form.addLayout(address_row)

        return form

    def _create_bottom_buttons(self):
        bottom_bar = QHBoxLayout()
        bottom_bar.setContentsMargins(2, 8, 0, 0)
        bottom_bar.setSpacing(0)

        self.save_button = self._icon_text_button(
            "Save",
            QStyle.StandardPixmap.SP_DriveFDIcon,
            width=80,
        )
        self.undo_button = self._icon_text_button(
            "Undo",
            QStyle.StandardPixmap.SP_ArrowBack,
            width=80,
        )
        self.cancel_button = self._icon_text_button(
            "Cancel",
            None,
            width=80,
        )

        for button in (self.save_button, self.undo_button, self.cancel_button):
            button.setObjectName("bottomButton")
            button.setFixedSize(80, 70)
            bottom_bar.addWidget(button)

        bottom_bar.addStretch(1)
        return bottom_bar

    def _connect_signals(self):
        self.save_button.clicked.connect(self.save_data)
        self.cancel_button.clicked.connect(self.clear_fields)

    def _apply_styles(self):
        down_arrow_path = Path(__file__).with_name("down_arrow.svg").as_posix()

        style = """
            QMainWindow, QWidget {
                background: #FFF5B8;
                color: black;
                font-family: Arial;
                font-size: 18px;
            }

            QLabel {
                background: transparent;
                color: black;
            }

            QPushButton#actionButton,
            QPushButton#bottomButton,
            QPushButton#smallActionButton {
                background: #FFb16E;
                border: 1px solid #805f3c;
                color: black;
                font-weight: bold;
            }

            QPushButton#actionButton:hover,
            QPushButton#bottomButton:hover,
            QPushButton#smallActionButton:hover {
                background: #ffc18a;
            }

            QLineEdit,
            QDateEdit,
            QComboBox,
            QTextEdit {
                background: #CBBD93;
                border: 1px solid #8f8468;
                color: black;
                padding: 3px 6px;
                selection-background-color: #FFb16E;
                min-height: 24px;
            }

            QLineEdit:focus,
            QDateEdit:focus,
            QComboBox:focus,
            QTextEdit:focus {
                background: white;
            }

            QComboBox::drop-down,
            QDateEdit::drop-down {
                border-left: 1px solid #8f8468;
                background: #CBBD93;
                width: 20px;
            }

            QComboBox::down-arrow,
            QDateEdit::down-arrow {
                image: url(__DOWN_ARROW__);
                width: 10px;
                height: 10px;
            }
            """
        self.setStyleSheet(style.replace("__DOWN_ARROW__", down_arrow_path))

    def save_data(self):
        data = {
            "party_code": self.party_code_input.text(),
            "date": self.date_input.date().toString("yyyy-MM-dd"),
            "party_name": self.party_name_input.text(),
            "mobile": self.mobile_input.text(),
            "email": self.email_input.text(),
            "gst_no": self.gst_input.text(),
            "price_list": self.price_list_input.currentText(),
            "address": self.address_input.toPlainText(),
        }

        print("Party Details:")
        for field, value in data.items():
            print(f"{field}: {value}")

    def clear_fields(self):
        for field in (
            self.party_code_input,
            self.party_name_input,
            self.mobile_input,
            self.email_input,
            self.gst_input,
            self.address_input,
        ):
            field.clear()

        self.date_input.setDate(QDate.currentDate())
        self.price_list_input.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PartyDetailsWindow()
    window.show()
    sys.exit(app.exec())
