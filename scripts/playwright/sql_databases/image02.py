import subprocess
import time

import httpx
from playwright.sync_api import Playwright, sync_playwright


# Run playwright codegen to generate the code below, copy paste the sections in run()
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    # Update the viewport manually
    context = browser.new_context(viewport={"width": 960, "height": 1080})
    page = context.new_page()
    page.goto("http://localhost:8000/docs")
    page.get_by_label("post /heroes/").click()
    # Manually add the screenshot
    page.screenshot(path="docs/en/docs/img/tutorial/sql-databases/image02.png")

    # ---------------------
    context.close()
    browser.close()


process = subprocess.Popen(
    ["readyapi", "run", "docs_src/sql_databases/tutorial002.py"],
)
try:
    for _ in range(3):
        try:
            response = httpx.get("http://localhost:8000/docs")
        except httpx.ConnectError:
            time.sleep(1)
            break
    with sync_playwright() as playwright:
        run(playwright)
finally:
    process.terminate()
