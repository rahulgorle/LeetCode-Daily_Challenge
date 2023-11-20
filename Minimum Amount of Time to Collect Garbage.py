class Solution(object):
    def garbageCollection(self, items, distances):
        hasG, hasP, hasM = False, False, False
        num_items = len(items)
        total_distance = 0

        for idx in range(num_items - 1):
            total_distance += 3 * distances[idx]

        for item in items:
            total_distance += len(item)

        for idx in range(num_items - 1, 0, -1):
            if "G" not in items[idx]:
                total_distance -= distances[idx - 1]
            else:
                break

        for idx in range(num_items - 1, 0, -1):
            if "P" not in items[idx]:
                total_distance -= distances[idx - 1]
            else:
                break

        for idx in range(num_items - 1, 0, -1):
            if "M" not in items[idx]:
                total_distance -= distances[idx - 1]
            else:
                break

        return total_distance
