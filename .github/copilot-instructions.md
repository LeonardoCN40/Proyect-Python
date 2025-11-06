# AI Coding Agent Instructions for Selenium Test Automation Project

## Project Overview
This is a Python-based web automation testing project using **Selenium WebDriver** with a **Page Object Model (POM)** architecture. The project targets the Free Range Testers sandbox website for UI testing scenarios.

## Architecture & Structure

### Page Object Model Implementation
- **Base class**: `pages/base_page.py` contains common WebDriver utilities (wait strategies, clicks, hover actions)
- **Page classes**: Inherit from `BasePage` and define page-specific locators and methods
- **Locator pattern**: Use XPath with text-based selectors: `(By.XPATH, "//button[contains(text(), 'Enviar')]")`

### Test Organization
- **Test files**: Located in `tests/` directory, prefixed with `test_`
- **Fixtures**: `conftest.py` provides shared fixtures (browser session, page objects)
- **Markers**: Use `@pytest.mark.sandbox` for categorizing tests per pytest.ini configuration
- **Test data**: CSV files in `tests/TestData/` for parameterized tests

## Environment Setup

### Virtual Environment
- **Location**: `TestEnv/` directory (included in repo)
- **Activation**: Use full path commands: `"C:/Users/56979/OneDrive/Documentos/proyect Python/TestEnv/Scripts/python.exe"`
- **Dependencies**: Selenium 4.21.0, pytest 8.2.1, webdriver-manager 4.0.1

### Browser Driver Management
- Uses `webdriver-manager` for automatic ChromeDriver installation
- Standard pattern in fixtures:
```python
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
```

## Key Development Patterns

### Test Fixture Architecture
- **Session-scoped browser**: Single browser instance across all tests in a session
- **Function-scoped page objects**: Fresh page object per test
- **Parameterized tests**: Use `@pytest.fixture(params=read_search_terms())` with CSV data

### Exception Handling
- Handle `ElementClickInterceptedException` with explicit waits
- Use `WebDriverWait` with `expected_conditions` for dynamic elements
- Default timeout: 350 seconds (unusually high - verify if intentional)

### Spanish Language Context
- Test descriptions and assertions in Spanish
- Element text validation includes Spanish phrases
- Error messages in Spanish locale

## Testing Workflows

### Running Tests
```powershell
# From project root
& "C:/Users/56979/OneDrive/Documentos/proyect Python/TestEnv/Scripts/python.exe" -m pytest tests/test_sandbox.py -v

# Run specific markers
& "C:/Users/56979/OneDrive/Documentos/proyect Python/TestEnv/Scripts/python.exe" -m pytest -m sandbox
```

### Test Categories
- **Sandbox tests**: Interactive UI elements (dynamic IDs, hover effects, form submissions)
- **Google search tests**: Parameterized testing with CSV data
- **Basic smoke tests**: Simple navigation and title verification

## Common Patterns to Follow

1. **Page Object Methods**: Combine navigation + action in single method (e.g., `navigate_sandbox()`)
2. **Locator definitions**: Use descriptive UPPERCASE constants for element locators
3. **Wait strategies**: Always use explicit waits, avoid implicit waits or sleep()
4. **Test assertions**: Include descriptive failure messages in Spanish
5. **CSV test data**: First row as headers, subsequent rows as test parameters

## Known Issues
- ChromeDriver compatibility issues with current webdriver-manager version
- Inconsistent driver initialization patterns between test files (`test_pruebainicial.py` vs fixtures)
- High timeout values (350s) may indicate flaky test conditions

## File Templates
When creating new page objects, follow the pattern in `pages/sandbox_page.py`:
- Import `BasePage` and inherit from it
- Define locators as class constants
- Implement navigation and interaction methods
- Handle exceptions appropriately