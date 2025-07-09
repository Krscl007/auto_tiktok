# PowerShell setup script for Windows
# Run this in the project root: ./setup.ps1

# Create virtual environment
python -m venv venv

# Activate virtual environment
& "$PWD\venv\Scripts\Activate.ps1"

# Install dependencies
pip install -r requirements.txt

Write-Host "Setup abgeschlossen. Die virtuelle Umgebung ist aktiviert und Abhängigkeiten installiert." -ForegroundColor Green
