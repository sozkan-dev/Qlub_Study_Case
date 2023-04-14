from Pages.PaymentPage import PaymentPage
from Tests.test_base import BaseTest
import time


class Test_Payment(BaseTest):

    def test_click_to_pay_button(self):
        self.paymentPage = PaymentPage(self.driver)
        self.paymentPage.clickToPayTheBillButton()
        self.paymentPage.clickToDivideTheBillButton()
        self.paymentPage.clickToSetAmountButton()
        self.paymentPage.sendAmountToInput()
        self.paymentPage.clickToConfirmButton()
        self.paymentPage.clickToTipButton()
        self.paymentPage.fillCreditCardField()
        self.paymentPage.clickToPayButton()
        assert self.paymentPage.isSuccessfull()
