import unittest
from gothonweb.planisphere import *


class TestRoom(unittest.TestCase):
    def test_room(self):
        """
        Test Room
        """
        gold = Room("GoldRoom",
                    """This room has gold in it you can grab. There's a
                    door to the north.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

    def test_room_paths(self):
        """
        Test Room.paths
        """
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        """
        Test Room.go and Room map
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

    def test_gothon_game_map(self):
        """
        Test load_room
        """
        start_room = load_room(START)

        result1 = start_room.go('shoot!')
        result2 = start_room.go('dodge!')
        result3 = start_room.go('tell a joke')
        self.assertEqual(result1.name, generic_death.die().name)
        self.assertEqual(result2.name, generic_death.die().name)
        self.assertEqual(result3.name, laser_weapon_armory.name)

    def test_name_room(self):
        """
        Test name_room
        """
        data = central_corridor
        result = name_room(data)
        should_be = 'central_corridor'
        self.assertEqual(result, should_be)


class TestScenes(unittest.TestCase):
    def test_scenes(self):
        """
        Test scenes
        """
        pass

if __name__ == '__main__':
    unittest.main()
