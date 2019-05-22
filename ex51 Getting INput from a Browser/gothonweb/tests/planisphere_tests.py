import unittest
from gothon.planisphere import *


class TestRoom(unittest.TestCase):
    def test_room(self):
        """
        Test Room obj
        """
        name = 'GoldRoom'
        description = """This room has gold in it you can grab. There's a
                door to the north."""
        room = Room(name, description)
        self.assertEqual(room.name, name)
        self.assertEqual(room.description, description)

    def test_room_paths(self):
        """
        Test Room.add_paths and Room.go
        """
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        """
        Test Room map and Room.go
        """
        start = Room("Start", "You can go west and down a hole.")
        west = Room("Trees", "There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

    def test_load_room(self):
        """
        Test load_room
        """
        name = 'Central Corridor'
        start_room = load_room(START)
        self.assertEqual(start_room.name, name)

        self.assertEqual(start_room.go('shoot!'), scenes.get('generic_death'))
        self.assertEqual(start_room.go('dodge!'), scenes.get('generic_death'))

        room = start_room.go('tell a joke')
        self.assertEqual(room, scenes.get('laser_weapon_armory'))
    
    def test_name_room(self):
        """
        Test name_room
        """
        data = scenes.get(START)
        result = name_room(data)
        should_be = 'central_corridor'
        self.assertEqual(result, should_be)        

if __name__ == "__main__":
    unittest.main()
