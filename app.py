from pathlib import Path
import sys

import uvicorn

backend_path = str(Path(__file__).resolve().parent / "backend")
sys.path.insert(0, backend_path)

from back.main import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
