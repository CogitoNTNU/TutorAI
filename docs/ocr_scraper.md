OCR, or Optical Character Recognition, is a technology that converts different types of documents, such as scanned paper documents, PDF files, or images captured by a digital camera, into editable and searchable data. When applied to PDF scraping, OCR plays a crucial role, especially when dealing with PDFs that contain images of text rather than selectable text layers.

Workflow

PIL (Pillow) => open an image

OpenCV => Change an image / preprossess

Tesseract (PyTesseract) => OCR an image

Convert pdf to images, pipeline to remove noice and water marks and stuff, and then pass to pytesseract
