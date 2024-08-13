import unittest
from challenges import add_chocolate, lou_bega, assemble_guest_list, is_prime
from unittest.mock import patch, Mock

class TestCase(unittest.TestCase):

    def test_add_chocolate(self):
        for case, expected_result in (
            (
                ["apples", "oranges", "cheese"],
                ["apples", "oranges", "cheese", "chocolate"]
            ),
            (
                [],
                ["chocolate"]
            ),
            (
                ["cheese", "bread", "dip", "onions", "asparagus"],
                ["cheese", "bread", "dip", "onions", "asparagus", "chocolate"]
            )
        ):
            actual_result = add_chocolate(case)

            if type(actual_result) != list:
                self.fail(msg=f"Your function was supposed to return a list, but instead it returned {type(actual_result)}!")
            
            self.assertEqual(
                expected_result, 
                actual_result, 
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"    
            )

    def test_lou_bega(self):
        for case, expected_result in (
            (
                [
                    "Monica in my life", 
                    "Erica by my side", 
                    "Rita's all I need"
                ],
                [
                    "A little bit of Monica in my life", 
                    "A little bit of Erica by my side", 
                    "A little bit of Rita's all I need"
                ]
            ),
            (
                ["cheese", "bread", "dip", "onions", "asparagus"],
                [
                    "A little bit of cheese", 
                    "A little bit of bread", 
                    "A little bit of dip", 
                    "A little bit of onions", 
                    "A little bit of asparagus"
                ]
            ),
            (
                [],
                []
            )
        ):
            actual_result = lou_bega(case)

            if type(actual_result) != list:
                self.fail(msg=f"Your function was supposed to return a list, but instead it returned {type(actual_result)}!")
            
            self.assertEqual(
                expected_result, 
                actual_result, 
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"    
            )
    


    input_mock = Mock()
    input_mock.side_effect = [
        "Monica", "Erica", "Rita", "",
        "Monica", "Chandler", "Phoebe", "Ross", "Rachel", "Joey", "",
        ""    
    ]

    @patch('builtins.input', input_mock)
    def test_assemble_guest_list(self):
        for case, expected_result in (
            (
                ["Monica", "Erica", "Rita", ""],
                ["Monica", "Erica", "Rita"]
            ),
            (
                ["Monica", "Chandler", "Phoebe", "Ross", "Rachel", "Joey", ""],
                ["Monica", "Chandler", "Phoebe", "Ross", "Rachel", "Joey"]
            ),
            (
                ["", ],
                []
            )
        ): 
            actual_result = assemble_guest_list()
            
            if type(actual_result) != list:
                self.fail(msg=f"Your function was supposed to return a list, but instead it returned {type(actual_result)}!")
            
            self.assertEqual(
                expected_result, 
                actual_result, 
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"    
            )

    def test_is_prime(self):
        for case, expected_result in (
            (
                1,
                False
            ),
            (
                2,
                True
            ),
            (
                104729,
                True
            ),
            (
                831,
                False
            ),
            (
                0, 
                False
            )
        ): 
            actual_result = is_prime(case)
            
            if type(actual_result) != bool:
                self.fail(msg=f"Your function was supposed to return a boolean, but instead it returned {type(actual_result)}!")
            
            self.assertEqual(
                expected_result, 
                actual_result, 
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"    
            )

runner = unittest.TextTestRunner(verbosity=2)

runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(TestCase))))