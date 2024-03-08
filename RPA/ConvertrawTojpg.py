import os
import sys
import numpy as np
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QLineEdit, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt

class RawToJpgConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('RAW to JPG Converter')

        self.selectFolderBtn = QPushButton('Select Folder', self)
        self.selectFolderBtn.clicked.connect(self.selectFolder)

        self.widthLabel = QLabel('Width:', self)
        self.widthInput = QLineEdit(self)
        self.heightLabel = QLabel('Height:', self)
        self.heightInput = QLineEdit(self)

        self.convertBtn = QPushButton('Convert to JPG', self)
        self.convertBtn.clicked.connect(self.convertToJpg)
        self.convertBtn.setEnabled(False)

        self.statusLabel = QLabel(self)
        self.statusLabel.setText('')

        self.copyrightlabel = QLabel(self)
        self.copyrightlabel.setText("(C) 2024. Jiyun Moon all rights reserved")


        layout = QVBoxLayout()
        layout.addWidget(self.selectFolderBtn)
        layout.addWidget(self.widthLabel)
        layout.addWidget(self.widthInput)
        layout.addWidget(self.heightLabel)
        layout.addWidget(self.heightInput)
        layout.addWidget(self.convertBtn)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.copyrightlabel)

        self.setLayout(layout)

    def selectFolder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.folder_path:
            self.convertBtn.setEnabled(True)

    def convertToJpg(self):
        width = self.widthInput.text()
        height = self.heightInput.text()

        if not width or not height:
            QMessageBox.warning(self, 'Warning', 'Please enter both width and height.', QMessageBox.Ok)
            return

        try:
            width = int(width)
            height = int(height)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Please enter valid width and height.', QMessageBox.Ok)
            return

        raw_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith('.raw')]
        if not raw_files:
            QMessageBox.warning(self, 'Warning', 'No RAW files found in the selected folder.', QMessageBox.Ok)
            return

        output_folder = os.path.join(self.folder_path, 'Converted_JPG')
        os.makedirs(output_folder, exist_ok=True)

        progress_dialog = QProgressDialog("Converting...", "Cancel", 0, len(raw_files), self)
        progress_dialog.setWindowTitle("Conversion Progress")
        progress_dialog.setWindowModality(Qt.WindowModal)

        for j, raw_file in enumerate(raw_files):
            # print(j,"11")
            if progress_dialog.wasCanceled():
                # print(j,"22")
                response = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if response == QMessageBox.Yes:
                    QMessageBox.information(self, 'Conversion Canceled', 'Conversion to JPG was canceled.',
                                            QMessageBox.Ok)
                    break
                else:
                    # print(j,"33")
                    progress_dialog = QProgressDialog()
                    progress_dialog = QProgressDialog("Converting...", "Cancel", 0, len(raw_files), self)
                    progress_dialog.setValue(j)
                    # print("progress bar resumed")
                    continue


            # print("continue")

            raw_file_path = os.path.join(self.folder_path, raw_file)
            jpg_file_path = os.path.join(output_folder, os.path.splitext(raw_file)[0] + '.jpg')

            try:
                with open(raw_file_path, "rb") as raw:
                    raw_data = np.fromfile(raw, dtype=np.uint16)
                raw_data = raw_data >> 2
                raw_data = raw_data.astype(np.uint8)
                image = Image.frombytes("L", (width, height), raw_data)
                image.save(jpg_file_path, format='JPEG')

            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error converting {raw_file} to JPG: {str(e)}', QMessageBox.Ok)
                return

            progress_dialog.setValue(j + 1)
            QApplication.processEvents()


            # if j == len(raw_files):
        QMessageBox.information(self, 'Conversion Complete', 'Conversion to JPG completed successfully.', QMessageBox.Ok)

        progress_dialog.deleteLater()

        self.statusLabel.setText('Conversion completed.')

def main():
    app = QApplication(sys.argv)
    converter = RawToJpgConverter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
