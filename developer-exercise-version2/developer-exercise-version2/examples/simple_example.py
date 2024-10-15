import sys
import os

# Get the current script's directory (which is the 'examples' directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of 'examples' (which should contain 'pynn') to the system path
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

# Now we can import from 'pynn'
from pynn.nearest_neighbor_index import NearestNeighborIndex

def main():
    # Define a set of points
    points = [
        (1, 2),
        (5, 5),
        (10, 12),
        (-1, -3),
        (3, 7),
    ]

    # Create the nearest neighbor index using the provided points
    nn_index = NearestNeighborIndex(points)

    # Define the query point for which you want to find the nearest neighbor
    query_point = (2, 3)

    # Use the find_nearest method to find the closest point
    nearest_point = nn_index.find_nearest(query_point)

    # Output the nearest point
    print(f"The nearest point to {query_point} is {nearest_point}")

# Ensure the script runs only when executed
if __name__ == "__main__":
    main()
