import os
import subprocess
from pathlib import Path

def compile_translations():
    """Компилирует файлы перевода .ts в .qm"""
    translations_dir = Path(__file__).parent
    lrelease_path = "lrelease"  # Путь к lrelease (должен быть в PATH)
    
    for ts_file in translations_dir.glob("*.ts"):
        qm_file = ts_file.with_suffix(".qm")
        cmd = [lrelease_path, str(ts_file), "-qm", str(qm_file)]
        subprocess.run(cmd)

if __name__ == "__main__":
    compile_translations() 