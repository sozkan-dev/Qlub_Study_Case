from Config.config import TestData
from Pages.Base import Base
from selenium.webdriver.common.by import By


class PaymentPage(Base):
    PAY_THE_BILL = (By.CLASS_NAME, "Vendor_billAmount__CUTO1")
    DIVIDE_BILL = (By.XPATH, "//button[contains(text(),'Hesabı bölüş')]")
    SET_AMOUNT_BUTTON = (By.ID, "select-custom")
    AMOUNT_INPUT_PLACE = (By.ID, "fullWidth")
    AMOUNT = "100"
    CONFIRM_BUTTON = (By.ID, "confirm-split")
    TIP_OPTION = (By.XPATH, "//div[normalize-space()='10%']")
    CREDIT_CARD_NUMBER = (By.XPATH, "//input[@id='checkout-frames-card-number']")
    CREDIT_CARD_EXP = (By.XPATH, "//input[@id='checkout-frames-expiry-date']")
    CREDIT_CARD_CVV = (By.XPATH, "//input[@id='checkout-frames-cvv']")
    PAY_BUTTON = (By.XPATH, "//button[@id='checkout-action-btn']")
    SUCCESS = (
        By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 Confirm_paymentMessage__ajLGv css-1ot7q6p']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.URL)

    def clickToPayTheBillButton(self):
        self.clickToElement(self.PAY_THE_BILL)

    def clickToDivideTheBillButton(self):
        self.clickToElement(self.DIVIDE_BILL)

    def clickToSetAmountButton(self):
        self.clickToElement(self.SET_AMOUNT_BUTTON)

    def sendAmountToInput(self):
        self.sendTextToElement(self.AMOUNT_INPUT_PLACE, TestData.AMOUNT)

    def clickToConfirmButton(self):
        self.clickToElement(self.CONFIRM_BUTTON)

    def clickToTipButton(self):
        self.clickToElement(self.TIP_OPTION)

    def fillCreditCardField(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "cardNumber"))
        self.sendTextToElement(self.CREDIT_CARD_NUMBER, TestData.CREDIT_CARD)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "expiryDate"))
        self.sendTextToElement(self.CREDIT_CARD_EXP, TestData.CARD_EXP)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "cvv"))
        self.sendTextToElement(self.CREDIT_CARD_CVV, TestData.CARD_CVV)
        self.driver.switch_to.default_content()

    def clickToPayButton(self):
        self.clickToElement(self.PAY_BUTTON)

    def isSuccessfull(self):
        self.visibilityOfElement(self.SUCCESS)
