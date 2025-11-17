import unittest
from src.tools import get_order_status, initiate_return, faq_lookup

class TestTools(unittest.TestCase):

    def test_get_order_status_success(self):
        response = get_order_status("ORD123456")
        self.assertTrue(response["success"])
        self.assertEqual(response["order"]["status"], "shipped")

    def test_get_order_status_not_found(self):
        response = get_order_status("ORD999999")
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "Order not found")

    def test_initiate_return_success(self):
        response = initiate_return("ORD789012", "Item was defective")
        self.assertTrue(response["success"])
        self.assertEqual(response["return_id"], "RET789012")

    def test_initiate_return_not_found(self):
        response = initiate_return("ORD999999", "No longer needed")
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "Order not found")

    def test_initiate_return_not_delivered(self):
        response = initiate_return("ORD345678", "Changed my mind")
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "Only delivered orders can be returned")

    def test_faq_lookup_success(self):
        response = faq_lookup("return policy")
        self.assertTrue(response["success"])
        self.assertIn("return policy", response["matches"])

    def test_faq_lookup_no_match(self):
        response = faq_lookup("unknown question")
        self.assertFalse(response["success"])
        self.assertEqual(response["error"], "No matching FAQs found")

if __name__ == "__main__":
    unittest.main()