import networkx as nx


def find_evacuation_route():
    graph = nx.Graph()

    graph.add_edge("Village_A", "Road_1", weight=5)
    graph.add_edge("Road_1", "Road_2", weight=3)
    graph.add_edge("Road_2", "Shelter_A", weight=4)

    graph.add_edge("Village_A", "Road_3", weight=8)
    graph.add_edge("Road_3", "Shelter_A", weight=6)

    route = nx.shortest_path(
        graph,
        source="Village_A",
        target="Shelter_A",
        weight="weight"
    )

    distance = nx.shortest_path_length(
        graph,
        source="Village_A",
        target="Shelter_A",
        weight="weight"
    )

    return route, distance


if __name__ == "__main__":
    route, distance = find_evacuation_route()

    print("Recommended Evacuation Route:")
    print(" → ".join(route))

    print("Estimated Distance:", distance, "km")
