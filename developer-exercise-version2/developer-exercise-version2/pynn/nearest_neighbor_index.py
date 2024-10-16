import math


class NearestNeighborIndex:
    """
    TODO give me a decent comment

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points


    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        """
        A slow method for finding the nearest neighbor by checking all points.

        :param query_point: The point (x, y) for which the nearest neighbor is searched.
        :param haystack: A list of 2D points to search from.

        :return: The point from `haystack` that is closest to `query_point`.
        """

        min_dist = None
        min_point = None

        # Loop through each 2D points to find the nearest points
        for point in haystack:

            # (x 2 − x 1 ) - ( y 2 − y 1 )
            x = point[0] - query_point[0]
            y = point[1] - query_point[1]

            # No need to use Euclidean formula by squaring
            # Instead: (x^2 ) * 2 + ( y^2 ) * 2
            dis_sq = x ** 2 + y ** 2

            if min_dist is None or dis_sq < min_dist:
                min_dist = dis_sq
                min_point = point

        return min_point

    def find_nearest_fast(self, query_point):
        """
        returns the point that is closest to query_point.
        If there are no indexed points, None is returned.
        """

        """  
        A faster method for finding the nearest neighbor by reducing unnecessary computations.
        The current implementation is still brute-force, but it avoids calculating the square root
        for each distance check, improving performance.
        
        :param query_point: The point (x, y) for which the nearest neighbor is searched.
        :return: The closest point from the index.
        """

        min_dist_sq = float('inf')
        min_point = None

        for point in self.points:
            x = point[0] - query_point[0]
            y = point[1] - query_point[1]
            dist_sq = (x * x + y * y)

            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                min_point = point

        return min_point

    def find_nearest(self, query_point):
        """
        TODO comment me.
        """

        # TODO implement me so this class runs much faster.
        return self.find_nearest_fast(query_point)
