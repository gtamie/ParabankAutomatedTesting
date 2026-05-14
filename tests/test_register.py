from pages.home_page import HomePage


class TestCadastro:

    def test_navegar_para_tela_de_cadastro(self, driver):
        home = HomePage(driver)
        home.open()
        home.go_to_register()

        assert "cadastro" in driver.current_url.lower()