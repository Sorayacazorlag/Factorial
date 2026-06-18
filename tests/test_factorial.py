from playwright.sync_api import Page, expect
import pytest

def test_calcular_factorial_numero_entero_positivo(page: Page):

    print("Given el usuario abre la página de Factorial")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce el número entero positivo 3")
    page.get_by_role("textbox", name="Enter an integer").fill("3")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver el resultado del factorial 6")
    expect(page.locator("#resultDiv")).to_contain_text("6")
    
def test_calcular_factorial_valor_no_numerico(page: Page):

    print("Given el usuario abre la página de Factorial ")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce el valor de texto text")
    page.get_by_role("textbox", name="Enter an integer").fill("text")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver un mensaje de error")
    expect(page.locator("#resultDiv")).to_contain_text("Please enter an integer")

@pytest.mark.skip(reason="test desactivado porque existe un error conocido https://adalab-equipo2.atlassian.net/browse/FC-2")
def test_calcular_factorial_numero_negativo(page: Page):
    
    print("Given el usuario abre la página de Factorial")
    page.goto("https://qainterview.pythonanywhere.com/")

    print("When introduce el número negativo -2")
    page.get_by_role("textbox", name="Enter an integer").fill("-2")

    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()

    print("Then debe ver un mensaje de error")
    expect(page.locator("#resultDiv")).to_contain_text("Please enter an integer")

