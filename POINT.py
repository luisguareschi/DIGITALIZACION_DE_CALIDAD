class Point:
    def __init__(self, id, process_f_name, diameter, xe, ye, ze, tool_1, tool, part_1, part_2, part_3, part_4, part_5, part_6, quadrant):
        self.id = id
        self.process_f_name = process_f_name
        self.diameter = diameter
        self.xe = xe
        self.ye = ye
        self.ze = ze
        self.tool_1 = tool_1
        self.tool = tool
        self.part_1 = part_1
        self.part_2 = part_2
        self.part_3 = part_3
        self.part_4 = part_4
        self.part_5 = part_5
        self.part_6 = part_6
        self.quadrant = quadrant
        self.part_names = [self.part_1, self.part_2, self.part_3, self.part_4, self.part_5, self.part_6]