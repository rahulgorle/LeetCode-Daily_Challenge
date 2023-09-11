class Solution:
    def groupThePeople(self, groupSizes):
        # Initialize a dictionary to store groups
        groups_dict = {}
        result = []

        # Iterate through groupSizes
        for i, size in enumerate(groupSizes):
            # Check if the group size is already in the dictionary
            if size in groups_dict:
                groups_dict[size].append(i)
            else:
                groups_dict[size] = [i]

            # If the group size list has reached its desired size, add it to the result
            if len(groups_dict[size]) == size:
                result.append(groups_dict[size])
                del groups_dict[size]  # Remove the used group size key

        return result
