"""
One Press - Coding Practice Solution Helper
============================================
A study aid for working through coding-practice problems. It runs in the
background and listens for a single hotkey press. When activated on a practice
problem from an open coding site (LeetCode, HackerRank, Codewars, Project Euler,
etc.), it extracts the prompt, asks OpenAI for a reference solution, and copies
the result to your clipboard so you can compare it against your own attempt.

Intended for self-study on open practice platforms. Don't use it on graded
coursework, quizzes, or exams.

How to use:
1. Launch Chrome with debugging: run launch_chrome.bat (or .sh on Mac)
2. Run this script: python onepress.py
3. Browse to a practice problem you're working on
4. Press the hotkey to get a reference solution (copied to clipboard)
5. Press Ctrl+V (or Cmd+V on Mac) to paste it for comparison
"""

import time
import pyperclip
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openai import OpenAI

# ============================================================================
# CONFIGURATION - Customize these variables for your needs
# ============================================================================

# Hotkey to trigger the automation (press this key to get a solution)
HOTKEY = "p"

# CSS Selector - AUTO-DETECTED!
# The script automatically tries multiple common webpage selectors.
# No manual configuration needed - just press the hotkey and it works!

# OpenAI model to use for generating solutions
OPENAI_MODEL = "gpt-4o"

# Path to the file containing your OpenAI API key
API_KEY_FILE = "apikey.txt"

# Chrome remote debugging port (must match the port in launch_chrome.bat)
CHROME_DEBUGGER_PORT = 9222

# Maximum time to wait for page elements to load (in seconds)
PAGE_LOAD_TIMEOUT = 10

# Maximum characters to extract from a page (prevents excessive token usage)
MAX_EXTRACT_LENGTH = 8000

# ============================================================================
# END CONFIGURATION
# ============================================================================


def load_api_key():
    """Load OpenAI API key from file."""
    try:
        with open(API_KEY_FILE, 'r') as f:
            api_key = f.read().strip()
        return api_key
    except FileNotFoundError:
        print(f"Error: API key file '{API_KEY_FILE}' not found.")
        return None
    except Exception as e:
        print(f"Error reading API key: {e}")
        return None


def connect_to_chrome():
    """
    Connect to an existing Chrome browser instance that was launched with
    remote debugging enabled on port 9222.

    Returns:
        WebDriver instance connected to existing Chrome, or None if connection fails
    """
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", f"localhost:{CHROME_DEBUGGER_PORT}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

        return driver

    except Exception as e:
        print(f"\n❌ Error connecting to Chrome: {e}")
        print("\nMake sure you:")
        print("1. Launched Chrome using the provided launcher script")
        print("2. Chrome is running with remote debugging on port 9222")
        return None


def extract_problem_description(driver):
    """
    Extract the problem description from the current webpage.
    Automatically tries multiple common CSS selectors until one works,
    then falls back to full page text extraction.

    Args:
        driver: Selenium WebDriver instance

    Returns:
        str: The problem description text, or None if extraction fails
    """
    try:
        # CSS selectors for open coding-practice platforms, ordered by specificity
        selectors_to_try = [
            # LeetCode
            "[data-track-load='description_content']",
            ".elfjS",
            # HackerRank
            ".challenge-body-html",
            # Codewars
            "#description",
            # Project Euler / general problem statements
            ".problem_content",
            ".problem-statement",
            ".problem",
            # Generic semantic fallbacks common to practice sites
            "article",
            "main",
            "[role='main']",
            ".question-content",
            ".content",
            ".prompt",
            ".task-description",
            "#content",
            "#main-content",
        ]

        print("🔍 Scanning page for the practice problem...")

        for selector in selectors_to_try:
            try:
                element = driver.find_element(By.CSS_SELECTOR, selector)
                problem_text = element.text.strip()

                if problem_text and len(problem_text) > 50:
                    print(f"✓ Found content using selector: {selector}")
                    print(f"✓ Extracted {len(problem_text)} characters")
                    return problem_text[:MAX_EXTRACT_LENGTH]

            except:
                continue

        # Fallback: extract entire page body text
        try:
            body_text = driver.execute_script("return document.body.innerText;")
            if body_text and len(body_text.strip()) > 100:
                print("✓ Using full page text (no specific selector matched)")
                truncated = body_text.strip()[:MAX_EXTRACT_LENGTH]
                print(f"✓ Extracted {len(truncated)} characters")
                return truncated
        except:
            pass

        print("❌ Could not find problem text on this page")
        print("   The page may not contain extractable text content.")
        return None

    except Exception as e:
        print(f"❌ Error extracting problem: {e}")
        return None


def get_solution_from_openai(problem_text, api_key):
    """
    Send the problem to OpenAI and get a solution.

    Args:
        problem_text: The problem description
        api_key: OpenAI API key

    Returns:
        str: The generated solution, or None if request fails
    """
    print("🤖 Sending to OpenAI GPT-4o...")

    try:
        client = OpenAI(api_key=api_key)

        prompt = f"""You are an expert coding tutor. I will provide a coding-practice
problem extracted from a webpage. Analyze it and provide a clear, correct
reference solution that I can compare against my own attempt.

For a coding problem, provide the code solution.
For a math or logic problem, provide a concise worked answer.
Always prioritize accuracy and clarity.

Problem:
{problem_text}

Solution:"""

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert problem solver. You provide clean, accurate solutions to any type of problem - coding, math, science, or otherwise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4000
        )

        solution = response.choices[0].message.content.strip()

        # Remove markdown code blocks if present
        if solution.startswith("```"):
            lines = solution.split('\n')
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].strip() == "```":
                lines = lines[:-1]
            solution = '\n'.join(lines)

        print("✓ Solution received!")
        return solution

    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return None


def copy_to_clipboard(text):
    """
    Copy text to the system clipboard.

    Args:
        text: The text to copy

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        pyperclip.copy(text)
        print("📋 Copied to clipboard!")
        return True
    except Exception as e:
        print(f"❌ Clipboard error: {e}")
        return False


def process_problem(driver, api_key):
    """
    Process the current webpage: extract problem, get solution, copy to clipboard.

    Args:
        driver: Selenium WebDriver instance
        api_key: OpenAI API key

    Returns:
        bool: True if successful, False otherwise
    """
    print("\n" + "=" * 70)
    print("⚡ One Press - Processing problem...")
    print("=" * 70)

    # Step 1: Extract problem description
    problem_text = extract_problem_description(driver)
    if not problem_text:
        print("❌ Failed to extract problem\n")
        return False

    # Step 2: Get solution from OpenAI
    solution = get_solution_from_openai(problem_text, api_key)
    if not solution:
        print("❌ Failed to get solution\n")
        return False

    # Step 3: Copy solution to clipboard
    if copy_to_clipboard(solution):
        print("\n✅ Done! Solution copied to clipboard - press Ctrl+V to paste")
        print(f"   Solution length: {len(solution)} characters")
        print("=" * 70 + "\n")
        return True
    else:
        print("❌ Failed to copy to clipboard\n")
        print("Solution:")
        print(solution)
        return False


def main():
    """Main function - runs as a background service listening for hotkey."""
    print("=" * 70)
    print("⚡ One Press - Coding Practice Solution Helper")
    print("   Get a reference solution for a practice problem with one keypress")
    print("=" * 70)
    print()

    # Load API key
    print("Loading API key...")
    api_key = load_api_key()
    if not api_key:
        print("❌ Cannot proceed without API key. Exiting.")
        return
    print("✓ API key loaded")
    print()

    # Connect to Chrome
    print("Connecting to Chrome...")
    driver = connect_to_chrome()
    if not driver:
        print("\n❌ Failed to connect to Chrome. Run the launcher script first.")
        return
    print("✓ Connected to Chrome")
    print()

    print("=" * 70)
    print(f"✨ Ready! Open a practice problem and press '{HOTKEY.upper()}' for a reference solution")
    print("   The solution will be copied to your clipboard automatically")
    print("   Press Ctrl+C to exit")
    print("=" * 70)
    print()

    try:
        def on_hotkey():
            """Called when hotkey is pressed."""
            try:
                process_problem(driver, api_key)
            except Exception as e:
                print(f"❌ Error processing problem: {e}\n")

        keyboard.add_hotkey(HOTKEY, on_hotkey)

        print("Listening for hotkey... (running in background)")
        keyboard.wait()

    except KeyboardInterrupt:
        print("\n\n👋 Exiting One Press...")

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

    finally:
        try:
            keyboard.unhook_all()
            print("Done!\n")
        except:
            pass


if __name__ == "__main__":
    main()
