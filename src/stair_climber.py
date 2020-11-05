def num_ways(n):
    """
    Calculates the number of ways to climb 'N' stairs, based on following criteria:
        - You can climb 1 step at a time
        - You can climb 2 steps at a time
    """
    if n <= 1:
        return 1
    return num_ways(n - 1) + num_ways(n - 2)

if __name__ == "__main__":
    n_stairs = 4
    print(num_ways(n=n_stairs))