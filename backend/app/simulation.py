# A simplified electromagnetic field simulation stub.
def run_simulation(config: dict):
    # Example: simulate an electric field in a 2D space
    grid_size = config.get("grid_size", 10)
    time_steps = config.get("time_steps", 20)
    source_position = config.get("source_position", [5, 5])

    field = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    # Very basic simulation logic – placeholder for FDTD method
    for t in range(time_steps):
        x, y = source_position
        field[x][y] += 1  # Pulse the source

    return {"field": field, "message": "Simulation complete"}
