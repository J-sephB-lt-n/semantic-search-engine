import pytest
from chunking_functions import chunk_by_paragraph


def test_chunk_by_paragraph():
    # Test case 1: Regular input with multiple paragraphs
    input_text = """
‘Hola! Gorbag! What are you doing up here? Had enough of war
already?’
‘Orders, you lubber. And what are you doing, Shagrat? Tired of
lurking up there? Thinking of coming down to fight?’

So Gandalf and Peregrin rode to the Great Gate of the Men of
Gondor at the rising of the sun, and its iron doors rolled back before
them.
‘Mithrandir! Mithrandir!’ men cried. ‘Now we know that the storm
is indeed nigh!’
‘It is upon you,’ said Gandalf. ‘I have ridden on its wings. Let me
pass! I must come to your Lord Denethor, while his stewardship
lasts. Whatever betide, you have come to the end of the Gondor that
you have known. Let me pass!’
Then men fell back before the command of his voice and ques-
tioned him no further, though they gazed in wonder at the hobbit
that sat before him and at the horse that bore him. For the people
of the City used horses very little and they were seldom seen in their
streets, save only those ridden by the errand-riders of their lord. And
they said: ‘Surely that is one of the great steeds of the King of Rohan?
Maybe the Rohirrim will come soon to strengthen us.’ But Shadowfax
walked proudly up the long winding road.


For the fashion of Minas Tirith was such that it was
    """
    expected_output = [
        """‘Hola! Gorbag! What are you doing up here? Had enough of war
already?’
‘Orders, you lubber. And what are you doing, Shagrat? Tired of
lurking up there? Thinking of coming down to fight?’""",
        """So Gandalf and Peregrin rode to the Great Gate of the Men of
Gondor at the rising of the sun, and its iron doors rolled back before
them.
‘Mithrandir! Mithrandir!’ men cried. ‘Now we know that the storm
is indeed nigh!’
‘It is upon you,’ said Gandalf. ‘I have ridden on its wings. Let me
pass! I must come to your Lord Denethor, while his stewardship
lasts. Whatever betide, you have come to the end of the Gondor that
you have known. Let me pass!’
Then men fell back before the command of his voice and ques-
tioned him no further, though they gazed in wonder at the hobbit
that sat before him and at the horse that bore him. For the people
of the City used horses very little and they were seldom seen in their
streets, save only those ridden by the errand-riders of their lord. And
they said: ‘Surely that is one of the great steeds of the King of Rohan?
Maybe the Rohirrim will come soon to strengthen us.’ But Shadowfax
walked proudly up the long winding road.""",
        """For the fashion of Minas Tirith was such that it was""",
    ]
    assert chunk_by_paragraph(input_text, min_nchar=10) == expected_output


if __name__ == "__main__":
    pytest.main()
