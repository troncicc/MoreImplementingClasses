"""
A   Baby   class and methods that use the Baby class.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Catianne Troncin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    After you have made the Baby class, run this module. If your Baby
    class is correct, the output of the code below should be:

        Hello baby McKinley!
        Hello baby Keegan!
        - - - - -
        Baby Keegan is sleeping.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        - - - - -
        Baby Keegan is awake.  Time for food.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
    """
    mckinley = Baby('McKinley')
    keegan = Baby('Keegan')
    for k in range(2):
        print('- - - - -')
        keegan.hour_passes()
        mckinley.feed_baby()
        for j in range(4):
            mckinley.hour_passes()


# ----------------------------------------------------------------------
# DONE: 2. Implement a class called   Baby   that has a constructor and
#   two methods, as described below.  Your finished Baby class should
#   cause the code above to display the expected output.  Hint: Your
#   class will need instance variables that you must figure out.
#
# Constructor
#     What comes in:
#        -- self
#        -- a string for the name of the baby
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Sets instance variables as needed
#        -- Prints 'Hello baby <your baby's name>!'
#
# feed_baby
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Prints 'Thank you for feeding baby <your baby's name>.'
#        -- Modifies instance variables if needed
#
# hour_passes
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#      -- If it is the first time this function has been called since Baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is sleeping.'
#      -- If it is the second time this function has been called since baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is awake.  Time for food.'
#      -- If it is the third (or more) time this function has been called since baby was created or fed
# 	       -- Prints 'Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!'
#
# After implementing this class run this module and compare your output
#   to the expected output of main.
#
# Notice that the baby is never printed, so you are not required to make
#     a __repr__ method.  Each method call above simply does a print as
#     a side effect.
# ----------------------------------------------------------------------

########################################################################
# The   Baby   class (and its methods) should begins here.
# Here is a reminder for the syntax to create a new class.
#
#      class NameOfClass(object):
#          """ Brief description of what objects of the class 'are'. """
#
########################################################################
class Baby(object):
    """These are thing the babies can do..."""

    def __init__(self, baby_name):
        self.hour = 0
        self.baby_name = baby_name
        print('Hello baby ' + baby_name + '!')

    def feed_baby(self):
        self.hour = 0
        print("Thank you for feeding baby " + self.baby_name + "!")

    def hour_passes(self):
        """-- If it is the first time this function has been called since Baby was created or fed
        -- Prints 'Baby <your baby's name> is sleeping.'
        -- If it is the second time this function has been called since baby was created or fed
        -- Prints 'Baby <your baby's name> is awake.  Time for food.'
        -- If it is the third (or more) time this function has been called since baby was created or fed
        -- Prints 'Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!'"""
        self.hour = self.hour + 1

        if self.hour == 1:
            print("Baby " + self.baby_name + " is sleeping.")
        if self.hour == 2:
            print("Baby " + self.baby_name + " is awake.  Time for food.")
        if self.hour >= 3:
            print("Baby " + self.baby_name + " is CRYING uncontrollably!  Feed the Baby!")

        return self.hour


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
