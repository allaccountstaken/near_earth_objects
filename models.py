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

    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False):
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

        if self.hazardous:
            hazard = 'is'
        else:
            hazard = 'is not'
        return hazard

    def __str__(self):
        """Return `str(self)`."""

        return f"NEO {self.fullname} has a diameter {self.diameter} km and {self.hazard} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""

        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


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

    def __init__(self, neo, time, distance=float('nan'), velocity=float('nan')):
        """Create a new `CloseApproach`.

        :param info: 
        required unique designation (str), can be passed from the neo type'
        required date (str);
        optional: distance (float), velocity (bool), neo (neo).
        """

        self.neo = neo
        self._designation = neo.designation
        self.time = cd_to_datetime(time)

        self.distance = distance
        self.velocity = velocity

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
        return (f"At {self.time_str} {self.neo.fullname}, "
                f"approaching with speed {self.velocity} and distance {self.distance}")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
