from unittest.mock import patch
import pytest

class ProductManager:

    def check_availability(self, product_id):
        # ... логика для проверки наличия продукта
        return True

    def purchase_product(self, product_id):
        if self.check_availability(product_id):
            # ... логика покупки продукта
            return 'Покупка совершена'
        else:
            return 'Продукт недоступен'

# напиши код здесь
class TestProductManager:


    @patch('product_manager.ProductManager.check_availability', return_value=True)
    def test_purchase_product_available(self, mock_check_availability, value):
        mock_check_availability.return_value = True
        product_manager = ProductManager()
        assert product_manager.purchase_product(123) == 'Покупка совершена'

    @patch('product_manager.ProductManager.check_availability', return_value=False)
    def test_purchase_product_not_available(self, mock_check_availability):
        mock_check_availability.return_value = False
        product_manager = ProductManager()
        assert product_manager.purchase_product(1) == 'Продукт недоступен'
