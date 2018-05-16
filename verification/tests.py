"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": '12:30 p.m.',
            "answer": '12:30'
        },
        {
            "input": '9:00 a.m.',
            "answer": '09:00'
        }
    ],
    "Extra": [
        {
            "input": '11:15 p.m.',
            "answer": '23:15'
        },
        {
            "input": '6:50 p.m.',
            "answer": '18:50'
        },
	{
            "input": '7:07 a.m.',
            "answer": '07:07'
        },
	{
            "input": '12:00 a.m.',
            "answer": '00:00'
        },
	{
            "input": '12:00 p.m.',
            "answer": '12:00'
        }
    ]
}
