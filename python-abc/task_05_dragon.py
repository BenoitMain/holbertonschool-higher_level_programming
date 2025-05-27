#!/usr/bin/python3
"""
Module defining mixins (SwimMixin, FlyMixin) and the Dragon class
that demonstrates multiple inheritance via mixins.
"""

class SwimMixin:
    """Mixin class providing swimming ability.

    Methods:
        swim(): Print a message indicating that the creature can swim.
    """

    def swim(self):
        """Print a message indicating that the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying ability.

    Methods:
        fly(): Print a message indicating that the creature can fly.
    """

    def fly(self):
        """Print a message indicating that the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon class that can both swim and fly.

    Inherits:
        SwimMixin: Provides swimming ability.
        FlyMixin: Provides flying ability.

    Methods:
        roar(): Print a message indicating that the dragon is roaring.
    """

    def roar(self):
        """Print a message indicating that the dragon is roaring."""
        print("The dragon roars!")
