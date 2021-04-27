from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name=None, diameter=float('nan'), hazardous='N'):
        """Create a new `NearEarthObject`.

        :param info: 
        required unique designation (str), 
        optional name (str), diameter (float), hazardous (bool)
        """

        self.designation = str(designation)
        self.name = str(name).title()
        self.diameter = diameter
        self.hazardous = hazardous

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""

        if self.name is None:
            return self.designation
        else:
            return self.designation + " (" + self.name + ")"

    @property
    def hazard(self):
        """Return 'is/is not' depending on boolean value of hazardous."""

        if self.hazardous == 'N':
            hazard = 'is not'
        else:
            hazard = 'is'
        return hazard

    def __str__(self):
        """Return `str(self)`."""

        formatted_string = "NEO {} has a diameter {} km and {} potentially hazardous.".format(
            self.fullname, self.diameter, self.hazard
        )

        return formatted_string

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, neo):
        return self.designation is neo.designation


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, des, time, distance=float('nan'), velocity=float('nan'), neo=None):
        """Create a new `CloseApproach`.

        :param info: 
        required unique designation (str), can be passed from the neo type'
        required date (str);
        optional: distance (float), velocity (bool), neo (neo).
        """

        self._designation = des
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""

        formatted_string = "- On {} NEO {} approaching with speed {} km/s and distance {} au.".format(
            self.time_str, self.neo.fullname, self.velocity, self.distance
        )

        return formatted_string

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""

        formatted_string = "CloseApproach(time={}, distance={}, velocity={}, neo={})".format(
            self.time_str, self.distance, self.velocity, self.neo)

        return formatted_string


# Testing -- all works well here
# n = NearEarthObject(123, 'Barsik', 21.21, True)
# cap1 = CloseApproach(123, '1900-Dec-27 12:12', 10, 0.1, n)
# cap2 = CloseApproach(123, '1910-Dec-27 12:12', 11, 1.1, n)

# print(cap1, cap2)

# n.approaches.append(cap1)
# n.approaches.append(cap2)

# print(n.approaches)
