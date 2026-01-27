#!/usr/bin/env python3
"""Mixins example: SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon can swim and fly."""

    def roar(self):
        print("The dragon roars!")
