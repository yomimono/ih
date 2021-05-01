from click.testing import CliRunner
from pathlib import Path
from PIL import Image, ImageDraw

from ih import chart
import json

from test_cli import runner, TEST_OUTPUT
test_image = "test/images/smile.png"

def test_json():
    json_chart = chart.chart(image=test_image,
            palette_name="floss-dmc",
            fileformat="json")
    readback_chart = json.loads(json_chart)
    assert len(readback_chart) == 7 # 7 colors in the test image
