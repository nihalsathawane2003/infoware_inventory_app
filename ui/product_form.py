from PySide6.QtWidgets import (
    QWidget, QFormLayout, QLineEdit, QComboBox,
    QPushButton, QLabel, QFileDialog
)
from models.product_model import add_product

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master")
        layout = QFormLayout()

        self.barcode = QLineEdit(); layout.addRow("Barcode:", self.barcode)
        self.sku = QLineEdit(); layout.addRow("SKU ID:", self.sku)
        self.name = QLineEdit(); layout.addRow("Name:", self.name)
        self.category = QLineEdit(); layout.addRow("Category:", self.category)
        self.subcat = QLineEdit(); layout.addRow("SubCategory:", self.subcat)
        self.gst = QLineEdit(); layout.addRow("GST %:", self.gst)
        self.price = QLineEdit(); layout.addRow("Price:", self.price)
        self.unit = QComboBox(); self.unit.addItems(["pcs", "kg", "ltr"]); layout.addRow("Unit:", self.unit)
        self.conv = QLineEdit(); layout.addRow("Conv Fact.:", self.conv)
        self.supplier = QLineEdit(); layout.addRow("Supplier ID:", self.supplier)

        self.image_path = ""
        img_btn = QPushButton("Choose Image")
        img_btn.clicked.connect(self.choose_image)
        layout.addRow("Image:", img_btn)

        save_btn = QPushButton("Save Product")
        save_btn.clicked.connect(self.save_product)
        layout.addRow(save_btn)

        self.feedback = QLabel("")
        layout.addRow(self.feedback)

        self.setLayout(layout)

    def choose_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.image_path = path
            self.feedback.setText(f"Image: {path}")

    def save_product(self):
        try:
            data = {
                'barcode': self.barcode.text(),
                'sku_id': self.sku.text(),
                'name': self.name.text(),
                'category': self.category.text(),
                'subcategory': self.subcat.text(),
                'gst_tax': float(self.gst.text() or 0),
                'price': float(self.price.text() or 0),
                'default_unit': self.unit.currentText(),
                'conversion_factor': float(self.conv.text() or 1),
                'supplier_id': int(self.supplier.text() or 0),
                'image_path': self.image_path,
                'description': "",
                'gst': float(self.gst.text() or 0)
            }
            pid = add_product(data)
            self.feedback.setText(f"✅ Saved product with ID: {pid}")
        except Exception as e:
            self.feedback.setText(f"❌ Error: {str(e)}")
